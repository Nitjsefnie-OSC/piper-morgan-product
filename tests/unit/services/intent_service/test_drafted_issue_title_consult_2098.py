"""#2098 — "change the title to X" on a pending issue draft (Arch's shape, 2026-10-19).

Web's #1386 scenario B3 on alpha e801b1a309: with a draft pending, "Actually, change the
title to '<new>'" was appended to the body and the title stayed. The first fix (a marker
list) was a binder and retitled on body prose ("we should call it out in the release
notes" → "out in the release notes"); reverted at f260d8ed5b. This is the replacement: the
carrier consults the router on the held turn through ``classify_armed_reply`` with
``update_issue`` as its answering operation. Only a BIND naming ``update_issue`` with a
non-empty ``title`` retitles; ``none``, CONFIRM, RELEASE, a title-less bind and a consult
failure all continue down today's path (the #1627 body bind).

LAYER: ``handle_drafted_issue_turn`` with the real offer store and the consult stubbed.
DENOMINATOR: the five consult outcomes, the no-LLM failure path, Arch's three misfire
strings, the filing path's title read, the binder's absence.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service import drafted_issue as mod
from services.intent_service.armed_turn_consult import ArmedReplyDecision, ArmedReplyOutcome
from services.intent_service.classifier import IntentClassifier
from services.intent_service.drafted_issue import DRAFTED_ISSUE_KIND, handle_drafted_issue_turn
from services.intent_service.workflow_entries import register_default_workflows
from services.shared_types import IntentCategory

CONSULT = "services.intent_service.armed_turn_consult.classify_armed_reply"
_USER = "3f7b8a52-2098-4b00-9e00-000000002098"
OLD_TITLE = "Add search functionality to navigation bar"
NEW_TITLE = "Implement full-text search across nav and global search bar"
BODY = "Users can't find pages from the nav; search should cover nav items and content."
TITLE_TURN = f"Actually, change the title to '{NEW_TITLE}'"
PROSE_TURN = "Also we should call it out in the release notes"
# A body answer long enough to read as prose at the seam (the #1627 length floor), so the
# "every other outcome binds to the body" pins exercise the bind rather than the fall-through.
PROSE_LONG = (
    "Also we should call it out in the release notes and mention the keyboard shortcut that "
    "opens search, since support keeps getting asked about it every week."
)
ARCH_MISFIRES = [
    PROSE_TURN,
    "Add that users name it as their top pain",
    "Please make the title shorter",
]


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


@pytest.fixture
def svc():
    register_default_workflows()
    return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


def _offer():
    intent = Intent(
        category=IntentCategory.EXECUTION,
        action="create_issue",
        confidence=0.95,
        original_message=f"draft an issue about {OLD_TITLE}",
        context={"title": OLD_TITLE, "description": BODY, "repository": "octo/repo"},
    )
    return {
        "kind": DRAFTED_ISSUE_KIND,
        "question": mod._POST_BIND_ASK,
        "pending_action": {
            "action": "create_issue",
            "intent": intent,
            "draft": {"title": OLD_TITLE, "body": BODY, "repository": "octo/repo"},
            "summary": f"Issue in octo/repo: {OLD_TITLE}",
        },
    }


def _walk_offers(store):
    """The offer store's shape is the service's own; find every offer dict in it."""
    if isinstance(store, dict):
        if "pending_action" in store:
            yield store
        else:
            for v in store.values():
                yield from _walk_offers(v)
    elif isinstance(store, (list, tuple)):
        for v in store:
            yield from _walk_offers(v)


def _decision(outcome, operation=None, **args):
    return ArmedReplyDecision(outcome=outcome, operation=operation, confidence=0.9, args=args)


async def _turn(svc, message, decision=None, sid="s-2098"):
    offer = _offer()
    if decision is None:
        return offer, await handle_drafted_issue_turn(
            offer, message, session_id=sid, user_id=_USER, intent_service=svc
        )
    stub = AsyncMock(return_value=decision)
    with patch(CONSULT, new=stub):
        result = await handle_drafted_issue_turn(
            offer, message, session_id=sid, user_id=_USER, intent_service=svc
        )
    return offer, result, stub


class TestBindRetitles:
    @pytest.mark.asyncio
    async def test_update_issue_bind_with_title_retitles_keeps_body_and_rearms(self, svc):
        offer, result, stub = await _turn(
            svc, TITLE_TURN, _decision(ArmedReplyOutcome.BIND, "update_issue", title=NEW_TITLE)
        )
        assert result["message"].startswith(
            "Updated the title. Nothing is filed yet. Here's the draft:"
        )
        assert f"**Title**: {NEW_TITLE}" in result["message"]
        assert BODY in result["message"]
        assert result["intent_data"]["drafted_issue_retitled"] is True
        assert result["requires_clarification"] is True
        draft = offer["pending_action"]["draft"]
        assert draft["title"] == NEW_TITLE and draft["body"] == BODY
        # the create rail reads intent.context["title"] first: "file it as is" files the new one
        assert offer["pending_action"]["intent"].context["title"] == NEW_TITLE
        assert offer["pending_action"]["intent"].context["description"] == BODY
        # re-armed in the store with the retitled draft
        store = svc.workflow_offer_service._pending_offers
        stored = [
            o
            for o in _walk_offers(store)
            if (o.get("pending_action") or {}).get("draft", {}).get("title") == NEW_TITLE
        ]
        assert stored, f"retitled draft not re-armed in the store: {list(store)}"
        # the consult saw the message with update_issue as this carrier's answering operation
        kwargs = stub.await_args.kwargs
        assert stub.await_args.args[0] == TITLE_TURN
        assert kwargs["answering_operations"] == frozenset({"update_issue"})

    @pytest.mark.asyncio
    async def test_title_value_is_stripped(self, svc):
        offer, result, _ = await _turn(
            svc,
            TITLE_TURN,
            _decision(ArmedReplyOutcome.BIND, "update_issue", title=f"  {NEW_TITLE}  "),
        )
        assert offer["pending_action"]["draft"]["title"] == NEW_TITLE


class TestEverythingElseIsTodaysPath:
    @pytest.mark.parametrize(
        "decision",
        [
            _decision(ArmedReplyOutcome.BIND, None),  # router none → body prose
            _decision(ArmedReplyOutcome.CONFIRM, None),  # uncertain → never a silent retitle
            _decision(ArmedReplyOutcome.RELEASE, "list_projects"),  # the #1627 hold stays
            _decision(ArmedReplyOutcome.BIND, "update_issue"),  # named, but no title value
            _decision(ArmedReplyOutcome.BIND, "update_issue", title="   "),
        ],
        ids=["none", "confirm", "release", "no-title-arg", "blank-title"],
    )
    @pytest.mark.asyncio
    async def test_non_title_outcomes_bind_prose_to_the_body(self, svc, decision):
        offer, result, _ = await _turn(svc, PROSE_LONG, decision)
        assert result["message"].startswith("Added to the draft — nothing is filed yet.")
        draft = offer["pending_action"]["draft"]
        assert draft["title"] == OLD_TITLE
        assert draft["body"].endswith(PROSE_LONG)
        assert "drafted_issue_retitled" not in result["intent_data"]

    @pytest.mark.parametrize(
        "decision",
        [
            _decision(ArmedReplyOutcome.BIND, None),
            _decision(ArmedReplyOutcome.CONFIRM, None),
            _decision(ArmedReplyOutcome.BIND, "update_issue"),
        ],
        ids=["none", "confirm", "no-title-arg"],
    )
    @pytest.mark.asyncio
    async def test_command_shaped_title_turn_without_a_title_falls_through_never_retitles(
        self, svc, decision
    ):
        """Arch's shape, point 3: with no router value there is nothing to confirm, so the
        turn takes today's path. "Actually, change the title to …" is command-shaped (the
        execute framing reads through the lead-in since this row), and a command-shaped
        turn on a held draft falls through to the generic flow, as it did before #2098.
        The one thing that must never happen is a retitle on a guess."""
        offer, result, _ = await _turn(svc, TITLE_TURN, decision)
        assert result is None
        assert offer["pending_action"]["draft"]["title"] == OLD_TITLE

    @pytest.mark.parametrize("prose", ARCH_MISFIRES)
    @pytest.mark.asyncio
    async def test_arch_misfire_strings_on_a_none_verdict_go_to_the_body(self, svc, prose):
        offer, result, _ = await _turn(svc, prose, _decision(ArmedReplyOutcome.BIND, None))
        # The title never moves on a none verdict. Where the turn goes next is today's
        # path (a long answer binds to the body; a short one re-asks or falls through).
        assert offer["pending_action"]["draft"]["title"] == OLD_TITLE
        assert "Updated the title" not in ((result or {}).get("message") or "")
        if result is not None and result.get("intent_data", {}).get("drafted_issue_body_bound"):
            assert offer["pending_action"]["draft"]["body"].endswith(prose)

    @pytest.mark.asyncio
    async def test_consult_without_an_llm_is_todays_path_not_a_crash(self, svc):
        """The real consult against the explosive LLM: its failure path is CONFIRM, so
        prose binds to the body and the command-shaped title turn falls through."""
        offer, result = await _turn(svc, PROSE_LONG)
        assert result["message"].startswith("Added to the draft — nothing is filed yet.")
        assert offer["pending_action"]["draft"]["title"] == OLD_TITLE
        offer, result = await _turn(svc, TITLE_TURN)
        assert result is None
        assert offer["pending_action"]["draft"]["title"] == OLD_TITLE

    @pytest.mark.asyncio
    async def test_accept_and_decline_never_reach_the_consult(self, svc):
        stub = AsyncMock(side_effect=AssertionError("consulted"))
        with patch(CONSULT, new=stub):
            offer = _offer()
            assert (
                await handle_drafted_issue_turn(
                    offer, "no, drop it", session_id="s-d", user_id=_USER, intent_service=svc
                )
                is None
            )
        assert stub.await_count == 0


class TestNoBinderCameBack:
    def test_marker_list_and_extractor_are_gone(self):
        assert not hasattr(mod, "_TITLE_CHANGE_MARKERS")
        assert not hasattr(mod, "extract_title_change")

    def test_corpus_carries_both_rows(self):
        import yaml

        rows = yaml.safe_load(open("tests/fixtures/inversion_corpus_phase0.yaml"))["corpus"]
        by_phrase = {r["phrase"]: r for r in rows}
        assert by_phrase[TITLE_TURN]["expected"] == "action:update_issue"
        assert by_phrase[TITLE_TURN]["expected_args"] == {"title": NEW_TITLE}
        assert by_phrase[PROSE_TURN]["expected"] == "floor"
