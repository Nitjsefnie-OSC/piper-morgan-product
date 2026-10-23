"""The promote job refuses while ops/alpha-hold.md exists on origin/main (CIO/Arch 10-23).

Runs the step's own bash against a throwaway git repo with an ``origin``:
(a) the hold on main → refused, the file printed;
(b) the hold on main, the checkout on another branch → still refused (read from origin/main);
(c) no hold → proceeds; (d) origin/main unresolvable → refused (fail closed).
"""

import subprocess
from pathlib import Path

import yaml

WORKFLOW = Path(__file__).resolve().parents[2] / ".github" / "workflows" / "fly-deploy.yml"
STEP = "No hold may be on (ops/alpha-hold.md on origin/main)"


def _step():
    jobs = yaml.safe_load(WORKFLOW.read_text())["jobs"]
    steps = jobs["promote-alpha"]["steps"]
    names = [s.get("name") for s in steps]
    return steps, names.index(STEP)


def test_the_hold_step_runs_before_any_other_gate():
    steps, i = _step()
    assert i == 1 and "actions/checkout" in steps[0]["uses"]  # first gate, right after checkout
    later = [s.get("name", "") for s in steps[i + 1 :]]
    assert any("Tests must have concluded success" in n for n in later)
    assert "${{" not in steps[i]["run"]  # no expression substitution in the run block


def _git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _run_step(tmp_path, *, hold_on_main, checkout_branch="main", break_origin=False):
    origin = tmp_path / "origin"
    origin.mkdir()
    _git(origin, "init", "-q", "-b", "main")
    _git(origin, "config", "user.email", "t@example.com")
    _git(origin, "config", "user.name", "t")
    (origin / "README").write_text("x\n")
    _git(origin, "add", "README")
    _git(origin, "commit", "-q", "-m", "init")
    _git(origin, "branch", "other")
    if hold_on_main:
        (origin / "ops").mkdir()
        (origin / "ops" / "alpha-hold.md").write_text("held by: PA\nwhy: test 2\n")
        _git(origin, "add", "ops/alpha-hold.md")
        _git(origin, "commit", "-q", "-m", "hold")
    work = tmp_path / "work"
    _git(tmp_path, "clone", "-q", "-b", checkout_branch, str(origin), str(work))
    if break_origin:
        _git(work, "remote", "set-url", "origin", str(tmp_path / "nowhere"))
        _git(work, "update-ref", "-d", "refs/remotes/origin/main")
    steps, i = _step()
    return subprocess.run(
        ["bash", "-e", "-c", steps[i]["run"]], cwd=work, capture_output=True, text=True
    )


def test_a_hold_on_main_refuses_and_prints_the_holder(tmp_path):
    r = _run_step(tmp_path, hold_on_main=True)
    assert r.returncode == 1
    assert "A hold is on" in r.stdout and "held by: PA" in r.stdout


def test_a_dispatch_from_another_branch_still_sees_the_hold(tmp_path):
    r = _run_step(tmp_path, hold_on_main=True, checkout_branch="other")
    assert r.returncode == 1
    assert "held by: PA" in r.stdout


def test_no_hold_proceeds(tmp_path):
    r = _run_step(tmp_path, hold_on_main=False)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "No hold" in r.stdout


def test_an_unresolvable_origin_main_refuses(tmp_path):
    r = _run_step(tmp_path, hold_on_main=False, break_origin=True)
    assert r.returncode == 1
    assert "fail closed" in r.stdout
