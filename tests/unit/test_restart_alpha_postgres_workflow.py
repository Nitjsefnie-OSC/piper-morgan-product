"""#2085 track 1: the external Postgres restarter (xian 2026-10-21 15:11, "build (a) after
main is protected").

A workflow-file pin with the guards read in order: dispatch-only, behind the alpha-db
environment with a db-scoped secret; Arch's three guards (the fault is the database's,
one restart per thirty minutes, capture before restart) all come BEFORE the one restart
command; the capture filters credential-looking lines; the post-restart check fails the
job when the database does not come back; permissions stay minimal.
"""

from pathlib import Path

import yaml

WORKFLOW = (
    Path(__file__).resolve().parents[2] / ".github" / "workflows" / "restart-alpha-postgres.yml"
)


def _text() -> str:
    return WORKFLOW.read_text()


def test_dispatch_only_behind_the_alpha_db_environment_with_a_db_scoped_secret():
    doc = yaml.safe_load(_text())
    on = doc.get("on") or doc.get(True)  # PyYAML reads a bare `on:` key as True
    assert list(on.keys()) == ["workflow_dispatch"]
    assert on["workflow_dispatch"]["inputs"]["reason"]["required"] is True
    job = doc["jobs"]["restart"]
    assert job["environment"] == "alpha-db"
    text = _text()
    assert "FLY_API_TOKEN_ALPHA_DB" in text
    assert "FLY_API_TOKEN_ALPHA }}" not in text  # never the app deploy token
    assert "FLY_API_TOKEN_STAGING" not in text
    assert doc["permissions"] == {"contents": "read", "actions": "read", "issues": "write"}
    assert doc["concurrency"]["cancel-in-progress"] is False


def test_the_three_guards_come_before_the_one_restart_in_order():
    text = _text()
    g1a = text.index("Guard 1a")
    g1b = text.index("Guard 1b")
    g2 = text.index("Guard 2")
    g3 = text.index("Guard 3")
    restart = text.index("flyctl machine restart")
    assert g1a < g1b < g2 < g3 < restart
    assert text.count("flyctl machine restart") == 1
    # Guard 1: the fault must be the database's, read from both sides
    assert 'if [ "$db" = "healthy" ]' in text[g1a:g1b]
    assert "critical) ;;" in text[g1b:g2]  # Arch 15:29: only critical restarts
    patterns = [ln.strip() for ln in text[g1b:g2].splitlines() if ln.strip().endswith(") ;;")]
    assert patterns == ["critical) ;;"]  # no warning|failing|failed pattern
    # Guard 2: thirty minutes, read from this workflow's own successful runs
    assert "--status success" not in text[g2:g3]  # an uncured restart fails its run
    assert "--json jobs" in text[g2:g3]
    assert 'startswith("Restart the Postgres machine")' in text[g2:g3]
    assert "age<1800" in text[g2:g3]
    # Guard 3: evidence first
    assert "flyctl machine status" in text[g3:restart]
    assert "flyctl logs" in text[g3:restart]
    assert "dmesg" in text[g3:restart]


def test_the_capture_filters_credential_looking_lines_and_echoes_no_environment():
    text = _text()
    g3 = text.index("Guard 3")
    restart = text.index("flyctl machine restart")
    capture = text[g3:restart]
    assert "filter()" in capture
    start = capture.index("filter()")
    filter_line = capture[start : capture.index("}", start) + 1]
    for word in ("password", "secret", "token", "DATABASE_URL", "postgres://"):
        assert word in filter_line
    assert "printenv" not in text and "env |" not in text and "echo $FLY" not in text


def test_a_restart_that_does_not_cure_fails_the_job_and_still_comments():
    text = _text()
    verify = text[text.index("Verify alpha reads the database healthy") :]
    assert "Database still not healthy after the restart" in verify
    assert "exit 1" in verify[: verify.index("Comment on the open alert issue")]
    comment = verify[verify.index("Comment on the open alert issue") :]
    assert "if: always() && steps.restart.outcome == 'success'" in comment
    assert "a person is needed" in comment


def _guard2_program() -> str:
    doc = yaml.safe_load(_text())
    steps = doc["jobs"]["restart"]["steps"]
    run = next(s["run"] for s in steps if s.get("name", "").startswith("Guard 2"))
    start = run.index("python3 -c '") + len("python3 -c '")
    end = run.index("')\"", start)
    return run[start:end]


def _guard2(runs) -> str:
    import json
    import subprocess
    import sys

    out = subprocess.run(
        [sys.executable, "-c", _guard2_program()],
        input=json.dumps(runs),
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def _run(minutes_ago: int, restart_conclusion):
    from datetime import datetime, timedelta, timezone

    at = (datetime.now(timezone.utc) - timedelta(minutes=minutes_ago)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    steps = [
        {
            "name": "Guard 1a, alpha's own verdict says the database is not healthy",
            "conclusion": "success",
        },
        {"name": "Restart the Postgres machine (once)", "conclusion": restart_conclusion},
        {
            "name": "Verify alpha reads the database healthy within three minutes",
            "conclusion": "failure",
        },
    ]
    return {"updatedAt": at, "jobs": [{"name": "restart", "conclusion": "failure", "steps": steps}]}


def test_guard_2_blocks_on_a_restart_whose_run_failed_afterwards():
    """Arch 15:29: the run that restarted and did not cure concludes `failure`; the
    guard must still see its restart step and refuse a second restart."""
    assert _guard2([_run(10, "success")]).startswith("block ")
    # a refused run (restart skipped) does not count
    assert _guard2([_run(10, "skipped")]) == "clear"
    # an old restart does not count
    assert _guard2([_run(40, "success")]) == "clear"
    assert _guard2([]) == "clear"  # an empty history is a readable answer
    # Arch 15:45: unreadable must refuse; "clear" licenses a write
    assert _guard2([{"updatedAt": "garbage", "jobs": []}]) == "block unreadable"
    assert _guard2_raw("not json") == "block unreadable"
    # a restart step that ran at all counts, success or not
    assert _guard2([_run(10, "failure")]).startswith("block ")
    assert _guard2([_run(10, "cancelled")]).startswith("block ")


def _guard2_raw(stdin_text: str) -> str:
    import subprocess
    import sys

    out = subprocess.run(
        [sys.executable, "-c", _guard2_program()],
        input=stdin_text,
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def test_guard_2_refuses_when_a_run_cannot_be_read():
    text = _text()
    g2 = text.index("Guard 2")
    g3 = text.index("Guard 3")
    loop = text[g2:g3]
    assert "|| echo '[]'" not in loop
    assert "Cannot read run" in loop
    view = loop.index('gh run view "$id"')
    assert "exit 1" in loop[view : loop.index("done <<<")]
    assert '"block unreadable")' in loop


def test_the_capture_is_best_effort_and_cannot_block_the_restart():
    text = _text()
    g3 = text.index("Guard 3")
    restart = text.index("flyctl machine restart")
    capture = text[g3:restart]
    assert "set +o pipefail" in capture
    assert "(not captured:" in capture
    assert "cap()" in capture
    for cmd in ("flyctl machine status", "flyctl logs", "flyctl ssh console"):
        line = next(
            ln for ln in capture.splitlines() if cmd in ln and not ln.strip().startswith("#")
        )
        assert line.strip().startswith('cap "'), line


def _guard1b_program() -> str:
    doc = yaml.safe_load(_text())
    steps = doc["jobs"]["restart"]["steps"]
    run = next(s["run"] for s in steps if s.get("name", "").startswith("Guard 1b"))
    start = run.index("python3 -c '") + len("python3 -c '")
    end = run.index("')\"", start)
    return run[start:end]


def _guard1b(stdin_text: str) -> str:
    import subprocess
    import sys

    out = subprocess.run(
        [sys.executable, "-c", _guard1b_program()],
        input=stdin_text,
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def test_guard_1b_reads_flyctls_real_shape_a_dict_keyed_by_machine_id():
    """PA 15:48 ran the guard's own parser on `flyctl checks list --json` from the live
    app: the top level is {"<machine id>": [{"name", "status", "output", "updated_at"}, ...]}.
    The first draft read only lists and printed "absent" for every run."""
    import json

    def live(pg_status: str) -> str:
        return json.dumps(
            {
                "865105fe247158": [
                    {"name": "pg", "status": pg_status, "output": "...", "updated_at": "t"},
                    {"name": "role", "status": "passing", "output": "...", "updated_at": "t"},
                    {"name": "vm", "status": "passing", "output": "...", "updated_at": "t"},
                ]
            }
        )

    assert _guard1b(live("passing")) == "passing"
    assert _guard1b(live("critical")) == "critical"
    assert _guard1b(live("warning")) == "warning"
    # the two list shapes still read
    assert _guard1b(json.dumps([{"name": "pg", "status": "critical"}])) == "critical"
    assert _guard1b(json.dumps([{"checks": [{"name": "pg", "status": "critical"}]}])) == "critical"
    # anything unreadable reads absent (and the step refuses on absent)
    assert _guard1b("not json") == "absent"
    assert _guard1b(json.dumps({"865105fe247158": "zero"})) == "absent"
    assert _guard1b(json.dumps({})) == "absent"


def test_guard_1b_reads_the_one_machine_not_the_app_wide_listing():
    """xian's token block (10-22 13:38): `checks list` lists every machine (ListActive),
    which the one-machine caveat refuses. Guard 1b reads the single machine's GET."""
    text = _text()
    g1b = text[text.index("Guard 1b") : text.index("Guard 2")]
    commands = "\n".join(ln for ln in g1b.splitlines() if not ln.strip().startswith("#"))
    assert "flyctl checks list" not in commands
    assert "https://api.machines.dev/v1/apps/$DB_APP/machines/$DB_MACHINE" in g1b
    assert '"FlyV1 "*) auth="$FLY_API_TOKEN"' in g1b
    assert "unset auth" in g1b
    assert 'echo "$auth' not in g1b and "echo $auth" not in g1b


def test_guard_1b_parser_reads_the_machine_get_shape():
    """The Machines API's single-machine GET (fly-go Machine: `checks` is a list of
    {name, status, output, updated_at}); other list fields (events, host_features)
    must not confuse it."""
    import json

    def machine(pg_status):
        return json.dumps(
            {
                "id": "865105fe247158",
                "state": "started",
                "host_features": ["x"],
                "events": [{"type": "launch", "status": "started"}],
                "checks": [
                    {"name": "pg", "status": pg_status, "output": "...", "updated_at": "t"},
                    {"name": "role", "status": "passing"},
                    {"name": "vm", "status": "passing"},
                ],
            }
        )

    assert _guard1b(machine("critical")) == "critical"
    assert _guard1b(machine("passing")) == "passing"
    assert _guard1b("{}") == "absent"  # an unread or refused machine reads absent and refuses
