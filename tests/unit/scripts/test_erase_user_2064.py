"""#2064: scripts/erase_user.py, the planner and the census, without a database.

Pins: the argv shape refuses everything but one safe identifier (plus the
two-step ``--erase --confirm <uuid>``); the plan's order is the FK dependency
order (a child is erased before any parent it references without CASCADE);
every column a predicate names exists on its table; the census walk counts
owner columns, FKs to users, and children of user data; the file step erases
only the user's own directory; nothing printed carries the email.

The scratch-Postgres round trip is tests/integration/test_erase_user_roundtrip_2064.py.
"""

from __future__ import annotations

import importlib
import re
import uuid

import pytest
import sqlalchemy as sa

mod = importlib.import_module("scripts.erase_user")

UID = "11111111-2222-4333-8444-555555555555"


def _metadata():
    import services.database.models  # noqa: F401  (registers every model table)
    from services.database.models import Base

    return Base.metadata


# --- argv ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "argv",
    [
        [],
        ["a;b"],
        ["-x"],
        ["--erase"],
        ["$(id)"],
        ["user", "extra"],
        ["user", "--erase"],  # no --confirm
        ["user", "--confirm", UID],  # --confirm without --erase
        ["user", "--erase", "--confirm", "not-a-uuid"],
    ],
)
def test_parse_args_refuses(argv):
    with pytest.raises(SystemExit) as exc:
        mod.parse_args(argv)
    assert exc.value.code not in (0, None)


@pytest.mark.parametrize(
    "argv,erase",
    [
        (["someone@example.com"], False),
        (["someone"], False),
        ([UID], False),
        (["someone", "--erase", "--confirm", UID], True),
    ],
)
def test_parse_args_accepts(argv, erase):
    args = mod.parse_args(argv)
    assert args.erase is erase


def test_count_is_the_default():
    assert mod.parse_args(["someone"]).erase is False


# --- the plan -------------------------------------------------------------------


def test_plan_tables_are_unique_and_users_is_last():
    tables = mod.plan_tables()
    assert len(tables) == len(set(tables))
    assert tables[-1] == "users"


def test_every_planned_table_exists_in_the_model():
    md = _metadata()
    missing = [t for t in mod.plan_tables() if t not in md.tables]
    assert not missing


def test_plan_order_is_fk_dependency_order():
    """For every FK between two planned tables that does not cascade or null
    itself, the referencing table is erased first. Otherwise the transaction
    fails on that FK in production."""
    md = _metadata()
    pos = {t: i for i, t in enumerate(mod.plan_tables())}
    wrong = []
    checked = 0
    for t in md.tables.values():
        for fk in t.foreign_keys:
            parent = fk.column.table.name
            if parent == t.name or t.name not in pos or parent not in pos:
                continue
            checked += 1
            if (fk.ondelete or "").upper() in ("CASCADE", "SET NULL"):
                continue
            if pos[t.name] > pos[parent]:
                wrong.append(f"{t.name}.{fk.parent.name} -> {parent}")
    assert checked >= 30, f"only {checked} FKs between planned tables; the walk broke"
    assert not wrong, f"erased after the parent it references: {wrong}"


_COL = re.compile(r"\b([a-z_]+)::text\b")
_PARAM = re.compile(r":([a-z_]+)\b")


@pytest.mark.parametrize("step", mod.PLAN, ids=lambda s: s.table)
def test_predicate_columns_exist(step):
    table = _metadata().tables[step.table]
    cols = set(_COL.findall(step.where))
    if step.table == "secure_credentials":
        cols.add("name")
    assert cols, f"{step.table}: predicate names no column"
    assert cols <= set(table.columns.keys()), cols - set(table.columns.keys())
    params = set(_PARAM.findall(step.where.replace("::text", ""))) - {"text"}
    assert params <= {"uid"} | set(mod.SCOPE_QUERIES), params
    if step.action == "detach":
        assert step.detach_column in table.columns
        assert table.columns[step.detach_column].nullable


def test_scope_queries_name_planned_tables():
    for key, sql in mod.SCOPE_QUERIES.items():
        table = sql.split(" FROM ", 1)[1].split()[0]
        assert table in mod.plan_tables(), key


# --- the census walk ---------------------------------------------------------------


def test_user_owned_tables_on_a_synthetic_schema():
    md = sa.MetaData()
    sa.Table("users", md, sa.Column("id", sa.String, primary_key=True))
    sa.Table(
        "by_fk",
        md,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("u", sa.ForeignKey("users.id")),
    )
    sa.Table(
        "by_name",
        md,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.String),
    )
    sa.Table(
        "by_suffix",
        md,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("x_user_id", sa.String),
    )
    sa.Table(
        "child",
        md,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("p", sa.ForeignKey("by_name.id")),
    )
    sa.Table(
        "grandchild",
        md,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("c", sa.ForeignKey("child.id")),
    )
    sa.Table(
        "unrelated", md, sa.Column("id", sa.Integer, primary_key=True), sa.Column("name", sa.String)
    )
    owned = mod.user_owned_tables(md)
    assert set(owned) == {"users", "by_fk", "by_name", "by_suffix", "child", "grandchild"}
    census = mod.fk_census(md)
    assert census == {"fk_cascade": 0, "fk_no_ondelete": 1, "owner_cols_without_fk": 2}


def test_unplanned_reports_tables_outside_plan_and_allow_list():
    assert mod.unplanned(["users", "conversations"]) == []
    assert mod.unplanned(["users", "brand_new_user_table"]) == ["brand_new_user_table"]


# --- outside Postgres -----------------------------------------------------------


def test_user_upload_dir_refuses_a_non_uuid(tmp_path):
    with pytest.raises(SystemExit):
        mod.user_upload_dir("../etc", tmp_path)
    assert mod.user_upload_dir(UID, tmp_path) == tmp_path / UID


def test_count_files_writes_nothing_and_erase_files_stays_in_the_users_dir(tmp_path):
    base = tmp_path / "uploads"
    mine = base / UID
    mine.mkdir(parents=True)
    known = mine / "known.pdf"
    known.write_bytes(b"k")
    (mine / "sub").mkdir()
    stray = mine / "sub" / "stray.txt"
    stray.write_bytes(b"s")
    legacy = base / "20260101_legacy.txt"  # a pre-#1401 root-level upload of this user
    legacy.write_bytes(b"l")
    other = base / str(uuid.uuid4())
    other.mkdir()
    (other / "theirs.txt").write_bytes(b"t")
    gone = str(mine / "gone.pdf")

    paths = [str(known), str(legacy), gone]
    counts = mod.count_files(paths, mine)
    assert counts == {
        "db_known_on_disk": 2,
        "db_known_missing": 1,
        "untracked_in_user_dir": 1,
        "user_dir_exists": 1,
    }
    assert known.exists() and stray.exists() and legacy.exists()

    result = mod.erase_files(paths, mine)
    assert result == {"removed_via_seam": 2, "swept_from_user_dir": 1}
    assert not mine.exists() and not legacy.exists()
    assert (other / "theirs.txt").exists()
    # Idempotent: a second run finds nothing and does not raise.
    assert mod.erase_files(paths, mine) == {"removed_via_seam": 0, "swept_from_user_dir": 0}


def test_revoke_grants_is_best_effort():
    calls = []

    async def disconnect(uid, connector):
        calls.append(connector)
        if connector == "slack":
            raise RuntimeError("provider down")

    out = mod.revoke_grants(UID, ["github", "slack", "notion"], disconnect)
    assert calls == ["github", "slack", "notion"]
    assert out == {
        "github": "disconnected",
        "slack": "FAILED (RuntimeError)",
        "notion": "disconnected",
    }


def test_chroma_chunk_ids_match_by_base_id():
    class Coll:
        def get(self, include):
            return {"ids": ["pdf_a_chunk_0", "pdf_a_chunk_1", "pdf_b_chunk_0", "pdf_ab_chunk_0"]}

    assert mod.chroma_chunk_ids(Coll(), ["pdf_a"]) == ["pdf_a_chunk_0", "pdf_a_chunk_1"]
    assert mod.chroma_chunk_ids(None, ["pdf_a"]) == []


# --- what gets printed -------------------------------------------------------------


def test_fingerprint_never_carries_the_value():
    fp = mod.fingerprint("Someone@Example.com")
    assert re.fullmatch(r"[0-9a-f]{16}", fp)
    assert fp == mod.fingerprint("someone@example.com")  # normalized
    assert "example" not in fp
    assert mod.fingerprint(None) == "(none)"


def test_format_census_shape():
    c = mod.Census(
        rows={s.table: 0 for s in mod.PLAN},
        files={
            "db_known_on_disk": 0,
            "db_known_missing": 0,
            "untracked_in_user_dir": 0,
            "user_dir_exists": 0,
        },
        chroma=None,
        redis=0,
        connectors=[],
        unplanned_live=["x"],
    )
    text = mod.format_census(c, "COUNT ONLY, nothing written")
    assert f"database rows ({len(mod.PLAN)} planned tables" in text
    assert "  users: 0" in text and "  total: 0" in text
    assert "chromadb chunks: store absent" in text
    assert "UNPLANNED user tables ['x']" in text


# --- the pre-flight (Arch's 10-16 condition) ---------------------------------------


class _Diag:
    constraint_name = "todo_items_project_id_fkey"
    table_name = "todo_items"


class ForeignKeyViolation(Exception):
    diag = _Diag()


class _FakeConn:
    """Records every statement; raises an IntegrityError on ``DELETE FROM <fail_on>``."""

    def __init__(self, fail_on=None):
        self.fail_on = fail_on
        self.statements: list = []
        self.rollbacks = 0
        self.commits = 0

    def execute(self, clause, params=None):
        sql = str(clause)
        self.statements.append(sql)
        if self.fail_on and sql.startswith(f"DELETE FROM {self.fail_on} "):
            raise sa.exc.IntegrityError(sql, params, ForeignKeyViolation("fk"))
        return None

    def rollback(self):
        self.rollbacks += 1

    def commit(self):  # pragma: no cover - must never be called
        self.commits += 1

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_preflight_runs_every_planned_statement_and_rolls_back():
    conn = _FakeConn()
    verdict = mod.preflight(conn, {"uid": UID}, set(mod.plan_tables()))
    assert verdict.ok and verdict.line().startswith("pre-flight: would erase cleanly")
    writes = [s for s in conn.statements if s.startswith(("DELETE", "UPDATE"))]
    assert len(writes) == len(mod.PLAN)
    assert writes[-1].startswith("DELETE FROM users ")
    assert "SET CONSTRAINTS ALL IMMEDIATE" in conn.statements
    assert conn.commits == 0 and conn.rollbacks >= 1


def test_preflight_names_the_table_and_error_class_and_stops():
    conn = _FakeConn(fail_on="projects")
    verdict = mod.preflight(conn, {"uid": UID}, set(mod.plan_tables()))
    assert not verdict.ok
    assert verdict.table == "projects"
    assert verdict.error == "IntegrityError/ForeignKeyViolation"
    assert verdict.detail == "constraint todo_items_project_id_fkey on table todo_items"
    assert verdict.line() == (
        "pre-flight: would refuse at projects (IntegrityError/ForeignKeyViolation; "
        "constraint todo_items_project_id_fkey on table todo_items)"
    )
    # Stopped at the failing step; nothing after it ran; rolled back, never committed.
    assert not any(s.startswith("DELETE FROM users ") for s in conn.statements)
    assert conn.commits == 0 and conn.rollbacks >= 1


def test_preflight_rolls_back_even_when_something_unexpected_escapes():
    class Boom(_FakeConn):
        def execute(self, clause, params=None):
            if str(clause).startswith("SET CONSTRAINTS"):
                raise KeyboardInterrupt
            return super().execute(clause, params)

    conn = Boom()
    with pytest.raises(KeyboardInterrupt):
        mod.preflight(conn, {"uid": UID}, set(mod.plan_tables()))
    assert conn.rollbacks >= 2 and conn.commits == 0  # the opening one and the finally


def _empty_census():
    return mod.Census(
        rows={s.table: 1 for s in mod.PLAN},
        files={
            "db_known_on_disk": 1,
            "db_known_missing": 0,
            "untracked_in_user_dir": 0,
            "user_dir_exists": 1,
        },
        chroma=1,
        redis=0,
        connectors=["github"],
        unplanned_live=[],
    )


@pytest.fixture
def run_with_cross_user_reference(monkeypatch):
    """run() with resolution and census stubbed, the REAL pre-flight on a fake
    connection whose DELETE FROM projects raises (another user's todo is in this
    user's project), and every outside-store step recording calls."""
    conn = _FakeConn(fail_on="projects")
    calls: list = []

    class Engine:
        def connect(self):
            calls.append("connect")
            return conn

        def begin(self):  # the step-4 transaction
            calls.append("begin")
            return conn

    present = set(mod.plan_tables())
    monkeypatch.setattr(mod, "resolve_user", lambda c, i: (UID, "u", "e@x"))
    monkeypatch.setattr(
        mod,
        "take_census",
        lambda c, uid, ub, ch, rc: (
            _empty_census(),
            {"present": present, "params": {"uid": UID}, "paths": []},
        ),
    )
    monkeypatch.setattr(mod, "erase_files", lambda *a: calls.append("erase_files"))
    monkeypatch.setattr(mod, "upload_paths", lambda *a: calls.append("upload_paths") or [])

    class Chroma:
        def get(self, include):
            calls.append("chroma.get")
            return {"ids": []}

        def delete(self, ids):
            calls.append("chroma.delete")

    async def disconnect(uid, connector):
        calls.append(("disconnect", connector))

    return conn, calls, Engine(), Chroma(), disconnect


def test_erase_refuses_on_failed_preflight_before_any_outside_store(run_with_cross_user_reference):
    conn, calls, engine, chroma, disconnect = run_with_cross_user_reference
    lines: list = []
    with pytest.raises(SystemExit) as exc:
        mod.run(
            UID,
            erase=True,
            confirm=UID,
            engine=engine,
            chroma=chroma,
            disconnect=disconnect,
            out=lines.append,
        )
    msg = str(exc.value.code)
    assert msg.startswith(
        "refusing: pre-flight failed at projects (IntegrityError/ForeignKeyViolation"
    )
    assert "nothing erased anywhere" in msg
    # Never reached step 1, 2, 3 or 4.
    assert not [c for c in calls if isinstance(c, tuple)], calls
    assert "erase_files" not in calls and "upload_paths" not in calls
    assert "chroma.get" not in calls and "chroma.delete" not in calls
    assert "begin" not in calls
    assert conn.commits == 0
    assert "pre-flight: would refuse at projects" in "\n".join(lines)


def test_main_exits_non_zero_on_failed_preflight(run_with_cross_user_reference, monkeypatch):
    _, calls, engine, _, _ = run_with_cross_user_reference
    monkeypatch.setattr(mod, "_engine", lambda: engine)
    monkeypatch.setattr(mod, "_redis_client", lambda: None)
    monkeypatch.setattr(mod, "_chroma_collection", lambda: None)
    with pytest.raises(SystemExit) as exc:
        mod.main(["someone", "--erase", "--confirm", UID])
    assert exc.value.code not in (0, None)
    assert "begin" not in calls


def test_count_mode_prints_the_verdict_and_touches_nothing(run_with_cross_user_reference):
    conn, calls, engine, chroma, disconnect = run_with_cross_user_reference
    lines: list = []
    mod.run(
        UID,
        erase=False,
        confirm=None,
        engine=engine,
        chroma=chroma,
        disconnect=disconnect,
        out=lines.append,
    )
    text_out = "\n".join(lines)
    assert "pre-flight: would refuse at projects (IntegrityError/ForeignKeyViolation" in text_out
    assert calls == ["connect"] and conn.commits == 0
