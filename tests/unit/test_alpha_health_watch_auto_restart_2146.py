"""#2146: the health watch dispatches the restarter only on a database failure, never under a hold.

Arch B (database-only), C (the hold respected, a failed read does not act), HOST's
condition 3 (narrow: `--ref ops/restarter`, `actions: write` on that one job). The
hold step's own bash runs here against a fake `gh`.
"""

import os
import stat
import subprocess
from pathlib import Path

import yaml

WF = Path(__file__).resolve().parents[2] / ".github" / "workflows" / "alpha-health-watch.yml"


def _doc():
    return yaml.safe_load(WF.read_text())


def test_only_the_restart_job_can_dispatch_and_only_on_ops_restarter():
    doc = _doc()
    assert "actions" not in doc["permissions"]
    assert "permissions" not in doc["jobs"]["probe"]
    assert doc["jobs"]["restart"]["permissions"] == {
        "actions": "write",
        "contents": "read",
        "issues": "write",
    }
    run = doc["jobs"]["restart"]["steps"][0]["run"]
    assert "gh workflow run restart-alpha-postgres.yml --ref ops/restarter" in run
    assert run.count("gh workflow run") == 1
    assert "${{" not in run


def test_it_runs_only_on_a_declared_stall_with_a_database_miss():
    cond = _doc()["jobs"]["restart"]["if"]
    assert "failure()" in cond
    assert "needs.probe.outputs.kind == 'stall'" in cond  # not a blip, not a forced test
    assert "needs.probe.outputs.db_misses != '0'" in cond


def _db_predicate():
    run = _doc()["jobs"]["probe"]["steps"][0]["run"]
    start = run.index("python3 -c '") + len("python3 -c '")
    return run[start : run.index("' 2>/dev/null", start)]


def _db(body: str) -> str:
    import sys

    out = subprocess.run(
        [sys.executable, "-c", _db_predicate()], input=body, capture_output=True, text=True
    )
    return out.stdout.strip()


def test_the_probe_reads_the_database_field_the_way_guard_1a_does():
    assert _db('{"status":"degraded","services":{"database":"unreachable"}}') == "unreachable"
    assert _db('{"status":"degraded","services":{"database":"healthy"}}') == "healthy"
    assert _db('{"status":"degraded","services":{}}') == "absent"
    assert _db("not json") == "unreadable"
    probe = _doc()["jobs"]["probe"]["steps"][0]["run"]
    assert "healthy|absent|unreadable) ;;" in probe  # only a named failure counts


def _run_hold_step(tmp_path, gh_behaviour: str):
    log = tmp_path / "gh.log"
    fake = tmp_path / "bin" / "gh"
    fake.parent.mkdir()
    fake.write_text(
        f"""#!/bin/bash
echo "$@" >> {log}
case "$1 $2" in
  "api repos/"*)
    case "{gh_behaviour}" in
      hold) echo "$(printf 'held by: PA\\nwhy: test' | base64)"; exit 0 ;;
      hold_md) echo "$(printf '# Alpha promotion hold\\n\\n- **Held by:** PA, from 15:13.\\n- **Why:** test' | base64)"; exit 0 ;;
      none) echo "gh: Not Found (HTTP 404)" >&2; exit 1 ;;
      error) echo "gh: Server Error (HTTP 500)" >&2; exit 1 ;;
    esac ;;
  "issue list") echo 2144 ;;
  *) exit 0 ;;
esac
"""
    )
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    run = _doc()["jobs"]["restart"]["steps"][0]["run"]
    env = {
        **os.environ,
        "PATH": f"{fake.parent}:{os.environ['PATH']}",
        "GH_REPO": "o/r",
        "TITLE": "Alpha health watch: failing",
        "RUN_URL": "https://x/run/1",
    }
    r = subprocess.run(["bash", "-c", run], env=env, capture_output=True, text=True)
    return r, (log.read_text() if log.exists() else "")


def test_a_hold_on_main_means_no_dispatch_and_a_comment_naming_the_holder(tmp_path):
    r, calls = _run_hold_step(tmp_path, "hold")
    assert r.returncode == 0
    assert "workflow run" not in calls
    assert "Hold on, not restarting: held by: PA" in calls


def test_the_comment_names_the_held_by_line_not_the_heading(tmp_path):
    r, calls = _run_hold_step(tmp_path, "hold_md")
    assert r.returncode == 0
    assert "workflow run" not in calls
    assert "Hold on, not restarting: Held by: PA, from 15:13." in calls
    assert "Alpha promotion hold" not in calls


def test_no_hold_dispatches_the_restarter_once(tmp_path):
    r, calls = _run_hold_step(tmp_path, "none")
    assert r.returncode == 0, r.stderr
    assert calls.count("workflow run restart-alpha-postgres.yml --ref ops/restarter") == 1
    assert "automatic restart dispatched" in calls


def test_an_unreadable_hold_does_not_act(tmp_path):
    r, calls = _run_hold_step(tmp_path, "error")
    assert r.returncode == 1
    assert "workflow run" not in calls
    assert "Couldn't read ops/alpha-hold.md" in calls
