"""#2151 step 1 -- the read-claim inventory covers exactly the live surface set.

The row set comes from code (scripts/read_claim_inventory.py). This test pins:
the live set is nonzero (refuse to report on zero, the #1423 lesson); the YAML
covers it exactly, with no missing and no stale rows; every row is well formed;
every red and exempt row says why; and nothing is left at an unknown verdict.
"""

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts"))
import read_claim_inventory as rci  # noqa: E402

_STATE_VALUES = {"distinct", "n/a", "unknown"} | {f"conflated:{s}" for s in rci.STATES}


@pytest.fixture(scope="module")
def live():
    return rci.live_surfaces()


@pytest.fixture(scope="module")
def rows():
    return rci.load_inventory()


def test_live_surface_set_is_nonzero_for_every_kind(live):
    assert len(live) > 0
    kinds = {v["kind"] for v in live.values()}
    assert kinds == set(rci.KINDS), f"a source produced no surfaces: {set(rci.KINDS) - kinds}"


def test_rail_walk_matches_wired_chat_actions_part_one(live):
    from services.intent_service.workflow_dispatcher import wired_chat_actions

    rail = {k for k, v in live.items() if v["kind"] == "rail"}
    legacy = {k.split(":", 1)[1] for k, v in live.items() if v["kind"] == "legacy"}
    assert rail | legacy == set(wired_chat_actions())


def test_yaml_covers_the_live_set_exactly(live, rows):
    missing, stale = rci.join(live, rows)
    assert not missing, f"live surfaces with no inventory row: {missing}"
    assert not stale, f"inventory rows with no live surface: {stale}"


def test_ids_are_unique(rows):
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids))


def test_rows_are_well_formed(live, rows):
    for r in rows:
        assert r.get("kind") == live[r["id"]]["kind"], r["id"]
        assert r.get("reads"), r["id"]
        assert ":" in str(r.get("handler", "")), r["id"]
        assert r.get("verdict") in ("green", "red", "exempt"), r["id"]
        states = r.get("states") or {}
        assert set(states) == set(rci.STATES), r["id"]
        for state, value in states.items():
            assert value in _STATE_VALUES, (r["id"], state, value)


def test_red_rows_carry_notes(rows):
    bare = [r["id"] for r in rows if r["verdict"] == "red" and not str(r.get("notes", "")).strip()]
    assert not bare, f"red rows without notes: {bare}"


def test_red_rows_name_a_conflation(rows):
    bare = [r["id"] for r in rows if r["verdict"] == "red" and not rci.conflations(r)]
    assert not bare, f"red rows with no conflated state: {bare}"


def test_exempt_rows_carry_a_reason(rows):
    bare = [
        r["id"] for r in rows if r["verdict"] == "exempt" and not str(r.get("reason", "")).strip()
    ]
    assert not bare, f"exempt rows without a reason: {bare}"


def test_no_unknown_verdicts(rows):
    assert not [r["id"] for r in rows if r.get("verdict") == "unknown"]


def test_script_refuses_zero(monkeypatch):
    monkeypatch.setattr(rci, "live_surfaces", lambda: {})
    assert rci.main([]) == 2


def test_script_fails_on_a_stale_row(monkeypatch, live, rows):
    monkeypatch.setattr(rci, "load_inventory", lambda: rows + [{"id": "route:GET /nowhere"}])
    monkeypatch.setattr(rci, "live_surfaces", lambda: live)
    assert rci.main([]) == 1


def test_script_fails_on_a_missing_row(monkeypatch, live, rows):
    monkeypatch.setattr(rci, "load_inventory", lambda: rows[1:])
    monkeypatch.setattr(rci, "live_surfaces", lambda: live)
    assert rci.main([]) == 1
