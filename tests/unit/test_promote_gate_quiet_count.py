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
    reader = [line for line in gate.splitlines() if 'verdict="$(printf' in line][0]
    assert "accounts" not in reader  # the count is not read; the verdict is
