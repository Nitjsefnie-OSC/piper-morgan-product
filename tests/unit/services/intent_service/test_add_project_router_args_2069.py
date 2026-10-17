"""#2069: add_project consumes the router's name / description / repo args,
and the reply is built from the created row.

Web on alpha, 2026-10-16:

    > Add a project called Baz with description testing the description
    < Added Baz with description testing the description to your portfolio.
      If you want a GitHub repo on it, say: link [owner/repo] to Baz with
      description testing the description.

and the stored row: name "Baz with description testing the description",
description "". The #1856 extractor splits off only a repo clause, so the
whole tail became the name.

Arch's ruling (2026-10-16 18:56, the #1943 shape, ADR-080 D1):
  1. The router names the slots: the add_project rail entry's description
     names ``name``, ``description`` and ``repo`` args; the handler consumes
     them. The #1856 extractor stays only as the fallback when the router
     sends no args, and is NOT widened (no "with description" regex; the
     phrasing is a corpus row).
  2. A description is written only from the router's ``description`` arg.
  3. The reply describes the row as stored: its name, a description only if
     one was saved, a repo only if one was linked; the repo how-to uses the
     stored name.
CXO (2026-10-16 18:56): a description asked for but not stored reads
"Added Baz. I can't set a description yet."

Layer: the rail adapter ``run_add_project_workflow`` and the REAL
``CanonicalHandlers._handle_add_project`` / ``_create_or_report_project``
with the DB session and repositories faked (the created row echoes what was
written, as the ORM does). No LLM: the router's args are supplied as the
``inversion_args`` the live consult writes onto the Intent.
"""

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from services.intent_service import workflow_entries as we
from services.intent_service.canonical_handlers import CanonicalHandlers

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"

BAZ = "Add a project called Baz with description testing the description"


class _FakeScope:
    async def __aenter__(self):
        return SimpleNamespace()

    async def __aexit__(self, *exc):
        return False


class _Store:
    """A ProjectRepository double whose ``create`` returns a row holding
    exactly what was written (name, description), like the ORM refresh."""

    def __init__(self, row_override=None):
        self.rows = []
        self.linked = []
        self.row_override = row_override

    def patches(self):
        from services.database.repositories import ProjectRepository
        from services.database.session_factory import AsyncSessionFactory

        async def _create(_self, **kwargs):
            row = SimpleNamespace(
                id="proj-2069",
                name=kwargs.get("name"),
                description=kwargs.get("description"),
            )
            if self.row_override:
                for k, v in self.row_override.items():
                    setattr(row, k, v)
            self.rows.append(row)
            return row

        async def _find_by_name(_self, **kwargs):
            return None

        async def _link(_self, repo_repo, repo_name, project_id, user_id):
            self.linked.append(repo_name)
            return True, ""

        return [
            patch.object(AsyncSessionFactory, "session_scope", staticmethod(lambda: _FakeScope())),
            patch.object(ProjectRepository, "create", _create),
            patch.object(ProjectRepository, "find_by_name", _find_by_name),
            patch.object(CanonicalHandlers, "_link_repo_to_new_project", _link),
        ]


async def _run_rail(message, router_args=None, store=None):
    """Drive the add_project rail adapter the way the live consult does:
    the Intent carries ``original_message`` and the router's
    ``inversion_args``."""
    import contextlib

    store = store or _Store()
    svc = SimpleNamespace(
        canonical_handlers=CanonicalHandlers(),
        _is_generic_canonical_response=lambda *a, **k: False,
        _arm_write_offer=lambda *a, **k: None,
        _track_offer_hint=lambda *a, **k: None,
    )
    ctx = {"original_message": message}
    if router_args is not None:
        ctx["inversion_args"] = router_args
    intent = SimpleNamespace(action="add_project", context=ctx)
    with contextlib.ExitStack() as stack:
        for p in store.patches():
            stack.enter_context(p)
        out = await we.run_add_project_workflow(
            "s-2069", "u-2069", {"intent": intent, "intent_service": svc}
        )
    return out.message, store


# ---------------------------------------------------------------------------
# (a) router args name / description / repo → the row, and a reply naming both
# ---------------------------------------------------------------------------


class TestRouterArgsConsumed:
    @pytest.mark.asyncio
    async def test_name_and_description_stored_apart_and_reply_names_both(self):
        msg, store = await _run_rail(BAZ, {"name": "Baz", "description": "testing the description"})
        (row,) = store.rows
        assert row.name == "Baz"
        assert row.description == "testing the description"
        assert msg == (
            'Added Baz to your portfolio with the description "testing the description". '
            "If you want a GitHub repo on it, say: link [owner/repo] to Baz."
        )

    @pytest.mark.asyncio
    async def test_router_repo_is_linked_under_the_stored_name(self):
        msg, store = await _run_rail(
            "add project Baz with repo octo/baz described as testing the description",
            {"name": "Baz", "description": "testing the description", "repo": "octo/baz"},
        )
        (row,) = store.rows
        assert (row.name, row.description) == ("Baz", "testing the description")
        assert store.linked == ["octo/baz"]
        assert msg == (
            'Added Baz to your portfolio with the description "testing the description" '
            "and linked octo/baz to it."
        )

    @pytest.mark.asyncio
    async def test_router_name_only_stores_no_description(self):
        msg, store = await _run_rail("Add a project called Bar", {"name": "Bar"})
        (row,) = store.rows
        assert (row.name, row.description) == ("Bar", "")
        assert msg == (
            "Added Bar to your portfolio. If you want a GitHub repo on it, "
            "say: link [owner/repo] to Bar."
        )


# ---------------------------------------------------------------------------
# Honesty guard (the #1976 word-set check): an LLM-written arg never stores
# words the user did not say; a description asked for but not stored gets
# CXO's interim line, verbatim.
# ---------------------------------------------------------------------------


class TestHonestyGuard:
    @pytest.mark.asyncio
    async def test_paraphrased_description_is_not_stored_and_reply_says_so(self):
        msg, store = await _run_rail(BAZ, {"name": "Baz", "description": "a test of descriptions"})
        (row,) = store.rows
        assert (row.name, row.description) == ("Baz", "")
        assert msg == (
            "Added Baz. I can't set a description yet. If you want a GitHub repo "
            "on it, say: link [owner/repo] to Baz."
        )

    @pytest.mark.asyncio
    async def test_invented_name_falls_back_to_the_extractor(self):
        msg, store = await _run_rail("Add a project called Bar", {"name": "Quux"})
        (row,) = store.rows
        assert row.name == "Bar"
        assert "Quux" not in msg

    @pytest.mark.asyncio
    async def test_repo_not_in_the_message_is_not_linked(self):
        _msg, store = await _run_rail(
            "Add a project called Bar", {"name": "Bar", "repo": "octo/bar"}
        )
        assert store.linked == []

    @pytest.mark.parametrize("args", [None, {}, "Baz", {"name": ""}, {"name": 7}])
    def test_unusable_args_name_nothing(self, args):
        routed = CanonicalHandlers._router_add_project_args(args, BAZ)
        assert routed["name"] is None and routed["description"] is None


# ---------------------------------------------------------------------------
# (b) no router args: the fallback's row is what the reply says
# ---------------------------------------------------------------------------


class TestFallbackReportsTheRow:
    @pytest.mark.asyncio
    async def test_with_description_phrase_without_args_reply_matches_the_row(self):
        msg, store = await _run_rail(BAZ)
        (row,) = store.rows
        # The fallback is not widened: no description is parsed out of the
        # utterance by code (Arch ruling point 2).
        assert row.description == ""
        assert msg == (
            f"Added {row.name} to your portfolio. If you want a GitHub repo on it, "
            f"say: link [owner/repo] to {row.name}."
        )
        assert "with the description" not in msg

    @pytest.mark.asyncio
    async def test_reply_is_built_from_the_created_row_not_the_request(self):
        # The row as stored differs from what was asked (e.g. a DB-side
        # normalisation): the reply follows the row.
        store = _Store(row_override={"name": "Baz (2)", "description": None})
        msg, _ = await _run_rail("Add a project called Baz", None, store)
        assert msg == (
            "Added Baz (2) to your portfolio. If you want a GitHub repo on it, "
            "say: link [owner/repo] to Baz (2)."
        )


# ---------------------------------------------------------------------------
# (c) the plain path is unchanged
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_plain_add_project_reply_unchanged():
    msg, store = await _run_rail("Add a project called Bar")
    (row,) = store.rows
    assert (row.name, row.description) == ("Bar", "")
    assert msg == (
        "Added Bar to your portfolio. If you want a GitHub repo on it, "
        "say: link [owner/repo] to Bar."
    )


# ---------------------------------------------------------------------------
# (d) the corpus row, the scorer's args keys, and the rail description
# ---------------------------------------------------------------------------


def test_corpus_row_carries_name_and_description_args():
    # The scorer's own loader (the corpus file is parsed by it, not plain
    # yaml.safe_load).
    sys.path.insert(0, str(_SCRIPTS))
    import inversion_phase0_baseline as p0

    (row,) = [r for r in p0.load_corpus() if r.get("phrase") == BAZ]
    assert row["expected"] == "action:add_project"
    assert row["expected_args"] == {"name": "Baz", "description": "testing the description"}


def test_scorer_compares_name_description_repo():
    path = _SCRIPTS / "inversion_phase1_shadow_score.py"
    sys.path.insert(0, str(_SCRIPTS))
    spec = importlib.util.spec_from_file_location("_score_2069", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    want = {"name": "Baz", "description": "testing the description"}
    assert mod.args_match(want, {"name": "baz", "description": "Testing the description."})[0]
    ok, note = mod.args_match(want, {"name": "Baz with description testing the description"})
    assert not ok and note.startswith("name:")
    assert not mod.args_match({"repo": "octo/baz"}, {"repo": "octo/bar"})[0]


# Rule 7 (2026-10-17): the args sentence ("Put the parts in args: name = …;
# description = …; repo = …") was screened ×6 in three wordings and DROPPED —
# each put 'add octocat/hello-world to the project' link_repo ×6 → CLARIFY ×6
# (dev/2026/10/17/controls/rule7-attribution-2051-2069-wordings-2026-10-17.md).
# Under main's wording the served router already names name/description on
# the Baz row (action AND args right 3/3) — the #1976 shape: the description
# is unchanged and the handler consumes the router's args anyway.
MAIN_ADD_PROJECT_DESCRIPTION = (
    "Create a new project in the user's portfolio, optionally linking a "
    "named GitHub repo in the same utterance; asks once for a name if "
    "the utterance didn't carry one (#1595 Phase 3)"
)


def test_rail_description_is_unchanged_from_main():
    desc = we.add_project_entry.description
    assert desc == MAIN_ADD_PROJECT_DESCRIPTION
    assert "args" not in desc


@pytest.mark.asyncio
async def test_handler_consumes_router_args_without_the_description_sentence():
    msg, store = await _run_rail(
        "add project Baz with repo octo/baz described as testing the description",
        {"name": "Baz", "description": "testing the description", "repo": "octo/baz"},
    )
    (row,) = store.rows
    assert (row.name, row.description) == ("Baz", "testing the description")
    assert store.linked == ["octo/baz"]
