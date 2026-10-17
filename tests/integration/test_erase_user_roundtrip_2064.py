"""#2064: erase_user.py round trip on a REAL, migrated, SCRATCH Postgres.

Seeds two synthetic users with one row in EVERY planned table (a generic
seeder over ``Base.metadata``, so a new planned table gets seeded without
editing this file), plus an upload file on disk for each. Then:

- count mode reports exactly one row per planned table for user A (two for
  conversation_turns, one per user parent chain) and writes nothing;
- ``--erase`` leaves every count at 0, removes A's upload file and upload dir;
- user B's counts and file are byte-for-byte unchanged.

DESTRUCTIVE against the database it runs on, so it runs ONLY when
``ERASE_USER_2064_DB`` names a scratch database (never ``piper_morgan``):

    createdb piper_2064 && POSTGRES_DB=piper_2064 alembic upgrade head
    ERASE_USER_2064_DB=piper_2064 pytest tests/integration/test_erase_user_roundtrip_2064.py
"""

from __future__ import annotations

import datetime as dt
import importlib
import os
import uuid

import pytest
import sqlalchemy as sa

mod = importlib.import_module("scripts.erase_user")

_DB = os.getenv("ERASE_USER_2064_DB", "")

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
        not _DB or _DB == "piper_morgan",
        reason="needs ERASE_USER_2064_DB naming a scratch database (never piper_morgan)",
    ),
]


def _engine():
    user = os.getenv("POSTGRES_USER", "piper")
    pw = os.getenv("POSTGRES_PASSWORD", "dev_changeme_in_production")
    host = os.getenv("POSTGRES_HOST", "127.0.0.1")
    port = os.getenv("POSTGRES_PORT", "5433")
    return sa.create_engine(f"postgresql+psycopg2://{user}:{pw}@{host}:{port}/{_DB}")


def _value_for(col, uid: str, slack_id: str):
    """A synthetic value a NOT NULL column accepts, by name first, then type."""
    name = col.name
    if mod.is_owner_column(name) and name != "slack_user_id":
        return uid
    if name == "slack_user_id":
        return slack_id
    t = col.type
    py = None
    try:
        py = t.python_type
    except (NotImplementedError, AttributeError):
        pass
    if isinstance(t, sa.Enum):
        return t.enums[0]
    if isinstance(t, sa.Boolean) or py is bool:
        return False
    if isinstance(t, (sa.Integer, sa.Numeric, sa.Float)) or py in (int, float):
        return 1
    if isinstance(t, (sa.DateTime, sa.Date)) or py in (dt.datetime, dt.date):
        return dt.datetime.now(dt.timezone.utc)
    if isinstance(t, sa.JSON) or py in (dict, list):
        return {}
    if isinstance(t, sa.ARRAY):
        return []
    if py is uuid.UUID or "UUID" in type(t).__name__.upper():
        return str(uuid.uuid4())
    if isinstance(t, sa.LargeBinary):
        return b"x"
    length = getattr(t, "length", None) or 32
    return f"s{uuid.uuid4().hex}"[:length]


# Postgres CHECK constraints the model doesn't carry: valid values by column.
_OVERRIDES = {
    ("conversations", "lifecycle_state"): "active",
    ("todo_items", "lifecycle_state"): "emergent",
    ("todo_items", "status"): "pending",
    ("todo_items", "priority"): "medium",
    ("projects", "lifecycle_state"): "emergent",
    ("artifacts", "lifecycle_state"): "emergent",
    ("items", "item_type"): "todo",
    ("lists", "item_type"): "todo",
}


def _seed_user(conn, tag: str, upload_base) -> dict:
    """One user and one row in every planned table, FK-consistent."""
    md = mod_metadata()
    uid = str(uuid.uuid4())
    slack_id = f"U{uuid.uuid4().hex[:10].upper()}"
    seeded: dict = {}
    planned = set(mod.plan_tables())
    for table in md.sorted_tables:
        if table.name not in planned:
            continue
        row = {}
        for col in table.columns:
            fk = next(iter(col.foreign_keys), None)
            if fk is not None:
                target = fk.column.table.name
                if target == "users":
                    row[col.name] = uid
                elif target == table.name:
                    row[col.name] = None  # self-parent: leave the root a root
                elif target in seeded:
                    row[col.name] = seeded[target][fk.column.name]
                elif col.nullable:
                    row[col.name] = None
                continue
            if (table.name, col.name) in _OVERRIDES:
                row[col.name] = _OVERRIDES[(table.name, col.name)]
            elif table.name == "users" and col.name == "id":
                row[col.name] = uid
            elif table.name == "users" and col.name in ("username", "email"):
                row[col.name] = f"erase2064-{tag}-{uid[:8]}" + (
                    "@example.com" if col.name == "email" else ""
                )
            elif table.name == "secure_credentials" and col.name == "name":
                row[col.name] = f"{uid}_github_api_key"
            elif table.name == "uploaded_files" and col.name == "storage_path":
                user_dir = upload_base / uid
                user_dir.mkdir(parents=True, exist_ok=True)
                f = user_dir / "note.txt"
                f.write_bytes(b"synthetic upload " + tag.encode())
                row[col.name] = str(f)
            elif mod.is_owner_column(col.name) or col.name == "slack_user_id":
                row[col.name] = _value_for(col, uid, slack_id)
            elif col.primary_key and isinstance(col.type, sa.Integer):
                continue  # serial
            elif col.primary_key or not col.nullable:
                if col.server_default is not None and not col.primary_key:
                    continue
                if col.default is not None and not col.primary_key:
                    continue
                row[col.name] = _value_for(col, uid, slack_id)
        if table.name == "todo_items":
            row["id"] = seeded["items"]["id"]
        if table.name == "conversation_links":
            # chk_conversation_links_no_self_link: link the first turn to a second one.
            turns = md.tables["conversation_turns"]
            second = {
                **seeded["conversation_turns"],
                "id": f"t{uuid.uuid4().hex}",
                "turn_number": 2,
            }
            conn.execute(turns.insert().values(**second))
            row["target_id"] = second["id"]
        result = conn.execute(table.insert().values(**row).returning(*table.primary_key.columns))
        pk = result.mappings().one()
        seeded[table.name] = {**row, **dict(pk)}
    return {"uid": uid, "rows": seeded, "file": upload_base / uid / "note.txt"}


def mod_metadata():
    import services.database.models  # noqa: F401  (registers every model table)
    from services.database.models import Base

    return Base.metadata


def _counts(engine, uid, upload_base):
    with engine.connect() as conn:
        census, _ = mod.take_census(conn, uid, upload_base, None, None)
        conn.rollback()
    return census


@pytest.fixture
def seeded(tmp_path):
    engine = _engine()
    upload_base = tmp_path / "uploads"
    with engine.begin() as conn:
        a = _seed_user(conn, "a", upload_base)
        b = _seed_user(conn, "b", upload_base)
    yield engine, upload_base, a, b
    # Leave the scratch DB as we found it, whatever the test did.
    with engine.begin() as conn:
        for who in (a, b):
            present = mod.existing_tables(conn)
            mod.erase_rows(conn, mod.resolve_scope(conn, who["uid"], present), present)
    engine.dispose()


def test_count_then_erase_round_trip(seeded):
    engine, upload_base, a, b = seeded
    b_before = _counts(engine, b["uid"], upload_base)

    lines: list = []
    before = mod.run(
        a["uid"],
        erase=False,
        confirm=None,
        engine=engine,
        upload_base=upload_base,
        out=lines.append,
    )
    # Every planned table is present in the migrated schema and holds A's row.
    assert all(n is not None for n in before.rows.values()), before.rows
    zero = sorted(t for t, n in before.rows.items() if n == 0)
    assert not zero, f"seeded but counted 0 (the plan's predicate misses the seed): {zero}"
    assert before.files["db_known_on_disk"] == 1
    assert before.unplanned_live == []
    assert "github" in before.connectors
    # Count mode wrote nothing.
    assert _counts(engine, a["uid"], upload_base).rows == before.rows
    assert a["file"].exists()
    # Nothing the user typed or their email reached the output.
    text_out = "\n".join(lines)
    assert "@example.com" not in text_out and "erase2064-a" not in text_out

    revoked: list = []

    async def fake_disconnect(uid, connector):
        revoked.append((uid, connector))

    after = mod.run(
        a["uid"],
        erase=True,
        confirm=a["uid"],
        engine=engine,
        upload_base=upload_base,
        disconnect=fake_disconnect,
        out=lines.append,
    )
    assert after.total_rows() == 0, {t: n for t, n in after.rows.items() if n}
    assert all(n == 0 for n in after.rows.values())
    assert not a["file"].exists()
    assert not (upload_base / a["uid"]).exists()
    assert (a["uid"], "github") in revoked

    # B is untouched: same counts, file still there.
    assert _counts(engine, b["uid"], upload_base).rows == b_before.rows
    assert b["file"].exists()

    # Idempotent: a rerun by id after the account is gone finds nothing and erases nothing.
    again = mod.run(
        a["uid"],
        erase=True,
        confirm=a["uid"],
        engine=engine,
        upload_base=upload_base,
        disconnect=fake_disconnect,
        out=lines.append,
    )
    assert again.total_rows() == 0


def test_cross_user_reference_refuses_before_any_outside_store(seeded):
    """Arch's 10-16 pre-flight condition on a real schema: user B's todo sits in
    user A's project (todo_items.project_id -> projects, no ondelete), so the
    erase transaction would roll back at ``projects``. The pre-flight must refuse
    BEFORE the grants, files or Chroma are touched: A's file stays on disk and
    every one of A's rows still counts."""
    engine, upload_base, a, b = seeded
    todo = mod_metadata().tables["todo_items"]
    with engine.begin() as conn:
        conn.execute(
            todo.update()
            .where(todo.c.id == b["rows"]["todo_items"]["id"])
            .values(project_id=a["rows"]["projects"]["id"])
        )
    try:
        a_before = _counts(engine, a["uid"], upload_base)
        lines: list = []
        mod.run(
            a["uid"],
            erase=False,
            confirm=None,
            engine=engine,
            upload_base=upload_base,
            out=lines.append,
        )
        verdict = [ln for ln in lines if ln.startswith("pre-flight:")]
        assert verdict and verdict[0].startswith(
            "pre-flight: would refuse at projects (IntegrityError/ForeignKeyViolation"
        ), verdict

        revoked: list = []

        async def fake_disconnect(uid, connector):
            revoked.append((uid, connector))

        class Chroma:
            calls: list = []

            def get(self, include):
                self.calls.append("get")
                return {"ids": []}

            def delete(self, ids):
                self.calls.append("delete")

        chroma = Chroma()
        with pytest.raises(SystemExit) as exc:
            mod.run(
                a["uid"],
                erase=True,
                confirm=a["uid"],
                engine=engine,
                upload_base=upload_base,
                chroma=chroma,
                disconnect=fake_disconnect,
                out=lines.append,
            )
        msg = str(exc.value.code)
        assert msg.startswith(
            "refusing: pre-flight failed at projects (IntegrityError/ForeignKeyViolation"
        ), msg
        assert "todo_items" in msg and "nothing erased anywhere" in msg
        assert revoked == []  # step 1 never ran
        assert a["file"].exists() and (upload_base / a["uid"]).is_dir()  # step 2 never ran
        assert "delete" not in Chroma.calls  # step 3 never ran
        assert _counts(engine, a["uid"], upload_base).rows == a_before.rows  # step 4 never ran
        assert a_before.total_rows() > 0
    finally:
        # Put B's todo back in B's own project so the fixture teardown can erase both.
        with engine.begin() as conn:
            conn.execute(
                todo.update()
                .where(todo.c.id == b["rows"]["todo_items"]["id"])
                .values(project_id=b["rows"]["projects"]["id"])
            )
