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
