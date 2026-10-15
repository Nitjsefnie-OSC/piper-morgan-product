"""#2030: the multi-intent path carries a canonical builder's ``offer_hint``,
arms exactly one, and asks that one question last.

Arch's ruling (issue comment issuecomment-6203827433):

1. ``IntentExecutionResult`` carries ``offer_hint``; the orchestrator does no
   store writes.
2. The FIRST successful sub-result (plan order) with a hint is the armed one.
3. Every hinted sub-result's ``offer_text`` is removed from its response by
   EXACT match; a failed match arms nothing and renders no question.
4. The armed ``offer_text`` is appended LAST to the composed reply, once.
5. IntentService arms it through ``_track_offer_hint`` BEFORE
   ``_apply_soft_offer``, so the #1770 guard adds no second, soft ask.

Before the fix, ``_execute_single`` kept only ``result["message"]``: the
builder's question rendered mid-reply and a "yes" next turn bound to nothing.
The source-level reach pin is check (d) of
``test_2010_offer_hint_reach_tripwire`` in tests/test_architecture_enforcement.py.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.consciousness.files_consciousness import (
    empty_projects_message,
    empty_projects_offer_hint,
)
from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.canonical_handlers import CanonicalHandlers
from services.intent_service.conversation_context import get_or_create_context
from services.intent_service.orchestrator import (
    IntentExecutionResult,
    IntentOrchestrator,
    OrchestratedResponse,
    _remove_offer_text,
)
from services.intent_service.pre_classifier import MultiIntentResult
from services.shared_types import IntentCategory

MESSAGE = "what time is it and list my projects"

# The real #2010 empty-projects reply and hint (one source).
EMPTY_MSG = empty_projects_message()
EMPTY_HINT = empty_projects_offer_hint()
EMPTY_Q = EMPTY_HINT["offer_text"]

# The real _format_project_setup_guidance reply and hint (#2024 copy).
_SETUP = CanonicalHandlers()._format_project_setup_guidance()
SETUP_MSG = _SETUP["message"]
SETUP_HINT = _SETUP["offer_hint"]
SETUP_Q = SETUP_HINT["offer_text"]


def _intent(category: IntentCategory, action: str) -> Intent:
    return Intent(
        category=category,
        action=action,
        confidence=1.0,
        original_message=MESSAGE,
        context={"original_message": MESSAGE},
    )


TIME = _intent(IntentCategory.TEMPORAL, "get_current_time")
PORTFOLIO = _intent(IntentCategory.PORTFOLIO, "manage_portfolio")


def _reply(message, hint=None, action="x"):
    out = {"message": message, "intent": {"category": "c", "action": action}}
    if hint is not None:
        out["offer_hint"] = dict(hint)
    return out


def _by_category(replies):
    async def handle(intent, session_id, user_id=None):
        return replies[intent.category]

    return handle


def _orchestrator(replies) -> IntentOrchestrator:
    handlers = CanonicalHandlers()
    handlers.handle = AsyncMock(side_effect=_by_category(replies))
    return IntentOrchestrator(canonical_handlers=handlers)


def _plan(*intents):
    return MultiIntentResult(intents=list(intents), original_message=MESSAGE, is_multi_intent=True)


# ---------------------------------------------------------------------------
# Orchestrator: carry, pick one, compose (no store writes)
# ---------------------------------------------------------------------------


class TestOrchestratorCarriesAndPicksOne:
    @pytest.mark.asyncio
    async def test_one_hinted_sibling_asks_once_and_last(self):
        orch = _orchestrator(
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, EMPTY_HINT),
            }
        )
        out = await orch.execute_plan(orch.create_plan(_plan(TIME, PORTFOLIO)), "s", None)

        assert out.armed_offer_hint == EMPTY_HINT
        assert out.results[1].offer_hint == EMPTY_HINT  # carried
        # the sibling's own text no longer carries the question
        assert out.results[1].response == "You don't have any active projects yet."
        assert EMPTY_Q not in out.results[1].response
        # the question renders once, as the last paragraph
        assert out.aggregated_message.count(EMPTY_Q) == 1
        assert out.aggregated_message.endswith(f"\n\n{EMPTY_Q}")
        assert out.aggregated_message == (
            "It's 3:15 PM. Regarding your portfolio, you don't have any active projects yet."
            f"\n\n{EMPTY_Q}"
        )

    @pytest.mark.asyncio
    async def test_two_hinted_siblings_only_the_first_arms(self):
        orch = _orchestrator(
            {
                IntentCategory.TEMPORAL: _reply(SETUP_MSG, SETUP_HINT),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, EMPTY_HINT),
            }
        )
        out = await orch.execute_plan(orch.create_plan(_plan(TIME, PORTFOLIO)), "s", None)

        assert out.armed_offer_hint == SETUP_HINT
        msg = out.aggregated_message
        assert msg.count(SETUP_Q) == 1 and msg.endswith(f"\n\n{SETUP_Q}")
        # the second sibling renders no question at all
        assert EMPTY_Q not in msg
        assert msg.count("?") == 1

    def test_a_failed_hinted_sibling_arms_nothing(self):
        orch = IntentOrchestrator(canonical_handlers=MagicMock())
        failed = IntentExecutionResult(
            intent=PORTFOLIO, response=EMPTY_MSG, success=False, offer_hint=dict(EMPTY_HINT)
        )
        ok = IntentExecutionResult(intent=TIME, response="It's 3:15 PM.", success=True)
        response = OrchestratedResponse(results=[ok, failed], has_partial_failure=True)
        response.armed_offer_hint = orch._pick_armed_offer(response.results)
        assert response.armed_offer_hint is None
        msg = orch._aggregate_messages(response)
        assert "?" not in msg

    def test_a_failed_first_hint_lets_the_first_successful_one_arm(self):
        orch = IntentOrchestrator(canonical_handlers=MagicMock())
        failed = IntentExecutionResult(
            intent=TIME, response=SETUP_MSG, success=False, offer_hint=dict(SETUP_HINT)
        )
        ok = IntentExecutionResult(
            intent=PORTFOLIO, response=EMPTY_MSG, success=True, offer_hint=dict(EMPTY_HINT)
        )
        assert orch._pick_armed_offer([failed, ok]) == EMPTY_HINT

    @pytest.mark.asyncio
    async def test_drift_arms_nothing_and_appends_no_question(self):
        """offer_text not verbatim in the reply: no arm, nothing appended, and
        the sibling's text is left exactly as the handler rendered it (the
        ruling strips nothing else)."""
        drifted = {"continuation_hint": "add a new project", "offer_text": "Want to add one?"}
        orch = _orchestrator(
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, drifted),
            }
        )
        out = await orch.execute_plan(orch.create_plan(_plan(TIME, PORTFOLIO)), "s", None)

        assert out.armed_offer_hint is None
        assert out.results[1].response == EMPTY_MSG
        assert "Want to add one?" not in out.aggregated_message

    @pytest.mark.asyncio
    async def test_no_hint_turn_is_unchanged(self):
        orch = _orchestrator(
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply("Three active projects."),
            }
        )
        out = await orch.execute_plan(orch.create_plan(_plan(TIME, PORTFOLIO)), "s", None)
        assert out.armed_offer_hint is None
        assert out.aggregated_message == (
            "It's 3:15 PM. Regarding your portfolio, three active projects."
        )


class TestRemoveOfferTextExactMatch:
    def test_end_of_line(self):
        assert _remove_offer_text(EMPTY_MSG, EMPTY_Q) == "You don't have any active projects yet."

    def test_real_setup_guidance_keeps_its_statement(self):
        out = _remove_offer_text(SETUP_MSG, SETUP_Q)
        assert SETUP_Q not in out
        assert out.endswith("Ask me how project context works any time.")
        assert out == SETUP_MSG[: SETUP_MSG.index(SETUP_Q)].rstrip()

    def test_mid_paragraph_rejoins_with_the_existing_break(self):
        text = "Each has a setup. Would you like guidance?\n\nOnce connected, tell me."
        assert (
            _remove_offer_text(text, "Would you like guidance?")
            == "Each has a setup.\n\nOnce connected, tell me."
        )

    def test_mid_line_rejoins_with_one_space(self):
        assert _remove_offer_text("A. Q? B.", "Q?") == "A. B."

    def test_no_verbatim_match_is_none(self):
        assert _remove_offer_text(EMPTY_MSG, "Want to add one?") is None
        assert _remove_offer_text(EMPTY_MSG, "") is None


# ---------------------------------------------------------------------------
# IntentService seam: arm through _track_offer_hint, before _apply_soft_offer
# ---------------------------------------------------------------------------


@pytest.fixture
def classifier():
    c = MagicMock()
    c.classify_multiple = AsyncMock()
    c.classify = AsyncMock()
    return c


def _service(classifier, replies) -> IntentService:
    service = IntentService(intent_classifier=classifier)
    handlers = CanonicalHandlers()
    handlers.handle = AsyncMock(side_effect=_by_category(replies))
    service.canonical_handlers = handlers
    service.intent_orchestrator = IntentOrchestrator(canonical_handlers=handlers)
    return service


class TestServiceArmsThePickedHint:
    @pytest.mark.asyncio
    async def test_one_hinted_sibling_arms_through_track_offer_hint(self, classifier):
        service = _service(
            classifier,
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, EMPTY_HINT),
            },
        )
        assert service._is_orchestratable_sibling(TIME)
        assert service._is_orchestratable_sibling(PORTFOLIO)
        classifier.classify_multiple.return_value = _plan(TIME, PORTFOLIO)
        session_id = str(uuid4())

        with patch.object(service, "_track_offer_hint", wraps=service._track_offer_hint) as track:
            result = await service.process_intent(
                message=MESSAGE, session_id=session_id, user_id=None
            )

        assert result.multi_intent_orchestrated
        track.assert_called_once_with({"offer_hint": EMPTY_HINT}, session_id, None)
        offer = get_or_create_context(session_id).last_offer
        assert offer is not None
        assert offer.continuation_hint == EMPTY_HINT["continuation_hint"]
        assert offer.offer_text == EMPTY_Q
        assert result.message.count(EMPTY_Q) == 1
        assert result.message.endswith(EMPTY_Q)

    @pytest.mark.asyncio
    async def test_yes_next_turn_binds_the_armed_question(self, classifier):
        service = _service(
            classifier,
            {
                IntentCategory.TEMPORAL: _reply(SETUP_MSG, SETUP_HINT),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, EMPTY_HINT),
            },
        )
        classifier.classify_multiple.return_value = _plan(TIME, PORTFOLIO)
        session_id = str(uuid4())
        first = await service.process_intent(message=MESSAGE, session_id=session_id, user_id=None)
        assert first.message.endswith(SETUP_Q) and EMPTY_Q not in first.message
        assert (
            get_or_create_context(session_id).last_offer.continuation_hint
            == (SETUP_HINT["continuation_hint"])
        )

        classifier.classify_multiple.reset_mock()
        classifier.classify_multiple.return_value = MultiIntentResult(
            intents=[TIME],  # any canonical intent: only the classifier's context is read
            original_message="yes",
            is_multi_intent=False,
        )
        await service.process_intent(message="yes", session_id=session_id, user_id=None)
        context = classifier.classify_multiple.call_args.kwargs.get("context")
        assert context["contextual_continuation_hint"] == SETUP_HINT["continuation_hint"]

    @pytest.mark.asyncio
    async def test_a_failed_hinted_sibling_arms_nothing(self, classifier):
        service = _service(classifier, {})
        classifier.classify_multiple.return_value = _plan(TIME, PORTFOLIO)
        session_id = str(uuid4())

        async def fake_single(intent, sid, uid=None):
            if intent.category == IntentCategory.PORTFOLIO:
                return IntentExecutionResult(
                    intent=intent, response=EMPTY_MSG, success=False, offer_hint=dict(EMPTY_HINT)
                )
            return IntentExecutionResult(intent=intent, response="It's 3:15 PM.", success=True)

        with patch.object(service.intent_orchestrator, "_execute_single", side_effect=fake_single):
            result = await service.process_intent(
                message=MESSAGE, session_id=session_id, user_id=None
            )

        assert get_or_create_context(session_id).last_offer is None
        assert EMPTY_Q not in result.message

    @staticmethod
    def _soft_offer_live(service):
        """A soft-offer candidate that WOULD append (detector + throttle say yes)."""
        offer = MagicMock(
            workflow_type="soft_wf",
            offer_message="SOFT ASK?",
            decline_message="ok",
        )
        detection = MagicMock(has_offer=True, offer=offer)
        return [
            patch.object(service.soft_invocation_detector, "detect", return_value=detection),
            patch.object(service.workflow_offer_service, "should_offer", return_value=(True, "ok")),
            patch.object(
                service.workflow_offer_service,
                "format_offer",
                side_effect=lambda o, m: f"{m}\n\n{o.offer_message}",
            ),
        ]

    @pytest.mark.asyncio
    async def test_hint_plus_soft_offer_candidate_asks_once(self, classifier):
        """#1770: the armed hint is live before _apply_soft_offer, so the
        soft candidate is skipped (control: without the hint it appends)."""
        for hinted in (True, False):
            service = _service(
                classifier,
                {
                    IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                    IntentCategory.PORTFOLIO: (
                        _reply(EMPTY_MSG, EMPTY_HINT) if hinted else _reply("Three projects.")
                    ),
                },
            )
            classifier.classify_multiple.return_value = _plan(TIME, PORTFOLIO)
            patches = self._soft_offer_live(service)
            for p in patches:
                p.start()
            try:
                result = await service.process_intent(
                    message=MESSAGE, session_id=str(uuid4()), user_id=None
                )
            finally:
                for p in patches:
                    p.stop()
            if hinted:
                assert "SOFT ASK?" not in result.message
                assert result.message.count("?") == 1
                assert result.message.endswith(EMPTY_Q)
            else:
                assert result.message.endswith("SOFT ASK?")  # the candidate was live


class TestSingleIntentPathUnchanged:
    @pytest.mark.asyncio
    async def test_single_intent_reply_keeps_the_question_in_place(self, classifier):
        """The single path renders the handler's message as-is and arms its
        hint (no stripping, no reordering)."""
        service = _service(classifier, {IntentCategory.PORTFOLIO: _reply(SETUP_MSG, SETUP_HINT)})
        classifier.classify_multiple.return_value = MultiIntentResult(
            intents=[PORTFOLIO], original_message="set up projects", is_multi_intent=False
        )
        session_id = str(uuid4())
        result = await service.process_intent(
            message="set up projects", session_id=session_id, user_id=None
        )
        assert result.message == SETUP_MSG
        assert get_or_create_context(session_id).last_offer.offer_text == SETUP_Q


class TestMultiIntentArmIsPrincipalKeyed:
    """#1533 authenticated sibling: two real user_ids, one session_id. The
    multi-intent arm lands under the acting user's composite key only."""

    @pytest.mark.asyncio
    async def test_the_arm_lands_under_the_acting_user(self, classifier):
        service = _service(
            classifier,
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, EMPTY_HINT),
            },
        )
        classifier.classify_multiple.return_value = _plan(TIME, PORTFOLIO)
        session_id = str(uuid4())
        user_a, user_b = str(uuid4()), str(uuid4())

        with patch.object(service, "_track_offer_hint", wraps=service._track_offer_hint) as track:
            result = await service.process_intent(
                message=MESSAGE, session_id=session_id, user_id=user_a
            )
        track.assert_called_once_with({"offer_hint": EMPTY_HINT}, session_id, user_a)
        assert result.message.endswith(EMPTY_Q)

        offer_a = get_or_create_context(session_id, user_id=user_a).last_offer
        assert offer_a is not None and offer_a.offer_text == EMPTY_Q
        assert get_or_create_context(session_id, user_id=user_b).last_offer is None
