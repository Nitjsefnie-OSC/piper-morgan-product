"""The promote job reads alpha's quiet count before promoting (grant condition 3).

A workflow-file pin: the step exists, reads the served field, refuses on a non-zero
count unless `quiet_override` is set, and does not refuse when the field is absent.
"""

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[2] / ".github" / "workflows" / "fly-deploy.yml"


def test_the_promote_job_carries_the_quiet_gate():
    text = WORKFLOW.read_text()
    promote = text[text.index("  promote-alpha:") :]
    gate = promote[promote.index("Alpha must be quiet") : promote.index("Content-parity gate")]
    assert "services" in gate and "chat_turns_last_30m" in gate
    assert "accounts" in gate
    assert "exit 1" in gate
    assert "quiet_override" in text[: text.index("concurrency:")]  # the dispatch input exists
    assert "QUIET_OVERRIDE" in gate
    assert "Quiet count not served" in gate  # absent field: noted, not refused
    # CIO 10-21: a down alpha is its own branch; the override reaches it (a forward fix)
    assert "Alpha did not answer /health" in gate
    assert gate.index("|| true") < gate.index("Alpha did not answer")
    # CIO 10-21: the step also holds the 30-minute uptime wait, always on, override reaches it
    assert "uptime_seconds" in gate and "1800" in gate
    assert "Alpha restarted less than 30 minutes ago" in gate
    assert "Uptime not served" in gate  # absent field: noted, not refused
    # Arch 10-21: a served-but-broken count refuses (not "not served"); override reaches it
    assert "Quiet count broken" in gate
    assert "record_failed_in_window" in gate
    assert gate.index('"broken"') < gate.index("Quiet count broken")
    # CIO 10-21 11:37: a not-healthy alpha refuses before the quiet read; override reaches it
    assert "Alpha is not healthy" in gate
    assert gate.index("Alpha is not healthy") < gate.index("Quiet count not served")
    assert "Alpha is not healthy, overridden" in gate
    # 10-21 11:25: the older count shape is "legacy" (noted), never "broken" (refused)
    assert "Quiet verdict not served" in gate
    assert gate.index('"legacy"') < gate.index("Quiet verdict not served")


def _reader_program(marker: str = 'verdict="$(printf') -> str:
    text = WORKFLOW.read_text()
    promote = text[text.index("  promote-alpha:") :]
    gate = promote[promote.index("Alpha must be quiet") : promote.index("Content-parity gate")]
    line = [ln for ln in gate.splitlines() if marker in ln][0]
    start = line.index("python3 -c '") + len("python3 -c '")
    end = line.rindex("')\"")
    return line[start:end]


def _verdict(body, marker: str = 'verdict="$(printf') -> str:
    import json
    import subprocess
    import sys

    out = subprocess.run(
        [sys.executable, "-c", _reader_program(marker)],
        input=json.dumps(body),
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def test_the_reader_runs_the_served_shapes_the_way_the_step_documents():
    """The reader is shell-embedded Python; run it on the bodies alpha has served
    or could serve. The 11:25 refusal was the second row reading "broken"."""
    svc = lambda v: {"services": {"chat_turns_last_30m": v}}  # noqa: E731
    assert _verdict({"services": {"web": "healthy"}}) == "absent"
    # the older build (b28d46a97f): counts, no verdict -> noted, not refused
    assert _verdict(svc({"accounts": 0, "turns": 0, "record_failed_in_window": False})) == "legacy"
    assert _verdict(svc({"accounts": 2, "turns": 5, "record_failed_in_window": False})) == "legacy"
    # the verdict shape (d09b7e0d86)
    assert _verdict(svc({"quiet": True, "record_failed_in_window": False})) == "quiet"
    assert _verdict(svc({"quiet": False, "record_failed_in_window": False})) == "busy"
    # broken: a record failure in the window, an error marker, or no usable field
    assert _verdict(svc({"quiet": True, "record_failed_in_window": True})) == "broken"
    assert _verdict(svc({"accounts": 0, "turns": 0, "record_failed_in_window": True})) == "broken"
    assert _verdict(svc({"error": "unavailable"})) == "broken"
    assert _verdict(svc("zero")) == "broken"
    assert _verdict(svc({})) == "broken"
    assert _verdict(svc({"accounts": True})) == "broken"  # a bool is not a count


def test_the_health_reader_names_the_status_and_the_database():
    """CIO 10-21 11:37: the 11:25 body (degraded, database unreachable) must refuse;
    a missing status reads "missing" and refuses like an unreachable alpha."""
    h = lambda body: _verdict(body, marker='health="$(printf')  # noqa: E731
    assert h({"status": "healthy", "services": {"database": "healthy"}}) == "healthy healthy"
    assert (
        h({"status": "degraded", "services": {"database": "unreachable"}}) == "degraded unreachable"
    )
    assert h({"services": {"database": "healthy"}}) == "missing healthy"
    assert h({"status": "", "services": {}}) == "missing unknown"
    assert h({"status": "healthy"}) == "healthy unknown"
