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
    assert "critical|warning|failing|failed" in text[g1b:g2]
    # Guard 2: thirty minutes, read from this workflow's own successful runs
    assert "--workflow restart-alpha-postgres.yml --status success" in text[g2:g3]
    assert '"$age" -lt 1800' in text[g2:g3]
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
