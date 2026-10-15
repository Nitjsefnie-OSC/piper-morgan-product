"""#2033 (folds #2032) — a cancel / skip / decline with NOTHING running.

Web's served run on 6f2916d10f (2026-10-15): with no standup active or
suspended, a bare ``cancel`` returned "Got it — standup cancelled. Quick
heads-up on a few overdue reminders …", and ``skip the standup`` / ``no, not
now`` returned "Got it, standup skipped. Heads up — …". Neither string is in
``services/``: the conversational floor NARRATED an action code never took
(Arch: an ADR-080 breach; meaning is the LLM's, actions and their reports are
code's).

Measured (Arch's ask): no deterministic surface claims any of these turns
(``PreClassifier.pre_classify`` → None for all of them), so their category is
the LLM's, and the #2004 floor gate (CONVERSATION/UNKNOWN only, and
``is_bare_decline`` only) could not see ``cancel``/``stop`` or ``skip the
standup`` at all. The fix answers them BEFORE classification
(``IntentService._nothing_running_reply``), after every arm that could consume
the turn. CXO's two lines, nothing appended.

Layer: the real ``process_intent`` over the real ``ProcessRegistry`` +
``StandupProcessAdapter`` on the in-memory manager double. The nothing-running
turns run against an EXPLOSIVE LLM: they are answered with no classification
and no floor. Not a served run; Web's re-run after promotion is the acceptance.
"""

from __future__ import annotations

import inspect
import json
from unittest.mock import MagicMock, patch
from uuid import uuid4

import pytest

from services.intent.intent_service import IntentService
from services.intent_service import conversational_floor as cf
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.intent_service.pre_classifier import PreClassifier
from services.process.adapters import StandupProcessAdapter
from services.process.registry import ProcessRegistry
from services.process.standup_copy import (
    STANDUP_DROP_PAUSED_REPLY,
    STANDUP_DROP_REPLY,
    STANDUP_ESCAPE_PAUSE_REPLY,
    STANDUP_NOT_RUNNING_REPLY,
)
from services.shared_types import StandupConversationState
from services.ui_messages.keyless_pleasantry import (
    BARE_DECLINE_NOTHING_OPEN,
    NOTHING_RUNNING_TO_CANCEL,
)
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

_USER = "3f7b8a52-2033-4b00-9e00-000000002033"

# CXO's ruled lines (#2033 comment, 2026-10-15), quoted so drift fails loudly.
CXO_NOTHING_TO_CANCEL = "There's nothing running to cancel."
CXO_NO_STANDUP = "There's no standup running right now. Say 'do a standup' whenever you want one."
STANDUP_SESSION_EXISTS_ASK = (
    "You have a standup conversation in progress. "
    "Would you like to continue where you left off, or start fresh?\n"
    "Reply 'continue' or 'restart'."
)

# Shape → line. The phrasings Web quoted plus the acceptance's.
TO_CANCEL = [
    "cancel",
    "stop",
    "never mind",
    "please cancel",
    "cancel please",
    "Cancel",
    "quit",
    "forget it",  # generic #1529 exit, fits every process
    "nevermind",  # same
]
NO_STANDUP = [
    "skip the standup",
    "cancel the standup",
    "please skip the standup",
    "end standup",
    "stop the standup",
    "no, not now",
    "not now",
    "not right now",
]

# The served phantom claims and the reminder tail.
_PHANTOM = ("cancelled", "canceled", "skipped", "heads up", "heads-up", "remind", "overdue")


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name}); this turn is deterministic")


class _ChitchatLLM:
    """For turns that DO classify (controls): a CONVERSATION verdict."""

    async def complete(self, **kwargs):
        return json.dumps(
            {"category": "conversation", "action": "chitchat", "confidence": 0.95, "reasoning": "x"}
        )


@pytest.fixture
def floor_calls(monkeypatch):
    calls = []

    async def fake_respond(self, ctx):
        calls.append(ctx)
        return cf.FloorResponse(message="(stubbed floor answer)")

    monkeypatch.setattr(cf.ConversationalFloor, "respond", fake_respond)
    return calls


def _service(llm):
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService(intent_classifier=IntentClassifier(llm_service=llm))


class _World:
    """The in-memory manager, the real registry with the real standup adapter,
    and the patches that make every seam see them (the #1771 harness)."""

    def __init__(self):
        self.manager = FakeStandupConversationManager()
        self.registry = ProcessRegistry()
        adapter = StandupProcessAdapter()
        adapter._manager = self.manager
        self.registry.register(adapter)
        self._patches = [
            patch(
                "services.conversation.conversation_handler._get_standup_components",
                return_value=(self.manager, MagicMock()),
            ),
            patch(
                "services.intent.intent_service.get_process_registry",
                return_value=self.registry,
            ),
        ]

    def __enter__(self):
        for p in self._patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in reversed(self._patches):
            p.stop()
        return False

    async def mid_interview(self, session_id):
        conv = await self.manager.create_conversation(session_id, _USER)
        await self.manager.transition_state(conv.id, StandupConversationState.GATHERING_YESTERDAY)
        return conv

    async def suspended(self, session_id):
        conv = await self.mid_interview(session_id)
        await self.manager.transition_state(conv.id, StandupConversationState.SUSPENDED)
        return conv

    async def state(self, conv):
        return (await self.manager.get_conversation(conv.id)).state


def _clean(text):
    lowered = text.lower()
    return not any(p in lowered for p in _PHANTOM)


class TestRuledStrings:
    def test_constants_are_cxos_lines(self):
        assert NOTHING_RUNNING_TO_CANCEL == CXO_NOTHING_TO_CANCEL
        assert STANDUP_NOT_RUNNING_REPLY == CXO_NO_STANDUP

    def test_statements_not_asks(self):
        """The unarmed-ask census is unchanged: neither line asks."""
        assert "?" not in NOTHING_RUNNING_TO_CANCEL
        assert "?" not in STANDUP_NOT_RUNNING_REPLY


class TestMeasurement:
    """Arch's ask: does anything deterministic claim these turns? No — so the
    category the #2004 gate keys on is the LLM's, and the turn must be answered
    before classification."""

    @pytest.mark.parametrize("text", TO_CANCEL + NO_STANDUP)
    def test_no_deterministic_surface_claims_it(self, text):
        assert PreClassifier.pre_classify(text) is None


class TestNothingRunningThroughProcessIntent:
    pytestmark = pytest.mark.asyncio

    @pytest.mark.parametrize("text", TO_CANCEL)
    async def test_cancel_words_get_nothing_to_cancel(self, text, floor_calls):
        service = _service(_ExplosiveLLM())
        with _World() as w:
            result = await service.process_intent(
                message=text, session_id=str(uuid4()), user_id=_USER
            )
            assert w.manager._conversations == {}
        assert result.message == CXO_NOTHING_TO_CANCEL  # byte-for-byte, no tail
        assert _clean(result.message)
        assert result.intent_data["nothing_running"] is True
        assert floor_calls == []

    @pytest.mark.parametrize("text", NO_STANDUP)
    async def test_standup_leaves_get_no_standup_line(self, text, floor_calls):
        service = _service(_ExplosiveLLM())
        with _World() as w:
            result = await service.process_intent(
                message=text, session_id=str(uuid4()), user_id=_USER
            )
            assert w.manager._conversations == {}
        assert result.message == CXO_NO_STANDUP
        assert _clean(result.message)
        assert floor_calls == []

    async def test_anonymous_turn_too(self, floor_calls):
        service = _service(_ExplosiveLLM())
        with _World():
            result = await service.process_intent(
                message="cancel", session_id=str(uuid4()), user_id=None
            )
        assert result.message == CXO_NOTHING_TO_CANCEL

    @pytest.mark.parametrize("text", ["no thanks", "skip", "nope", "no"])
    async def test_plain_bare_decline_keeps_the_2004_ack(self, text, floor_calls):
        """#2004 unchanged: a plain no (no deferral, no exit) classifies and the
        floor gate answers "Okay."."""
        service = _service(_ChitchatLLM())
        with _World():
            result = await service.process_intent(
                message=text, session_id=str(uuid4()), user_id=_USER
            )
        assert result.message == BARE_DECLINE_NOTHING_OPEN
        assert floor_calls == []

    @pytest.mark.parametrize(
        "text",
        [
            "cancel my 3pm meeting",
            "never mind, show my todos",
            "no, maybe later",  # a non-bare part: not whole-message
            "skip the standup and the retro",
        ],
    )
    async def test_compound_turns_are_not_claimed(self, text, floor_calls):
        service = _service(_ChitchatLLM())
        with _World():
            result = await service.process_intent(
                message=text, session_id=str(uuid4()), user_id=_USER
            )
        assert result.message not in (CXO_NOTHING_TO_CANCEL, CXO_NO_STANDUP)


class TestStandupActiveOrSuspendedUnchanged:
    """#888 / #1771 behaviour with a standup on the session is unchanged: the
    registry or the resume seam answers first, and the nothing-running step
    never claims a turn while a standup is suspended anywhere for the user."""

    pytestmark = pytest.mark.asyncio

    async def test_active_cancel_drops_it(self, floor_calls):
        service = _service(_ExplosiveLLM())
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            result = await service.process_intent(message="cancel", session_id=sid, user_id=_USER)
            assert await w.state(conv) == StandupConversationState.ABANDONED
        assert result.message == STANDUP_DROP_REPLY

    async def test_active_stop_pauses_it(self, floor_calls):
        service = _service(_ExplosiveLLM())
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            result = await service.process_intent(message="stop", session_id=sid, user_id=_USER)
            assert await w.state(conv) == StandupConversationState.SUSPENDED
        assert result.message == STANDUP_ESCAPE_PAUSE_REPLY

    async def test_suspended_skip_the_standup_drops_the_paused_one(self, floor_calls):
        service = _service(_ExplosiveLLM())
        sid = str(uuid4())
        with _World() as w:
            conv = await w.suspended(sid)
            result = await service.process_intent(
                message="skip the standup", session_id=sid, user_id=_USER
            )
            assert await w.state(conv) == StandupConversationState.ABANDONED
        assert result.message == STANDUP_DROP_PAUSED_REPLY

    @pytest.mark.parametrize("text", ["not now", "never mind", "no, not now"])
    async def test_suspended_elsewhere_is_not_nothing_running(self, text, floor_calls):
        """A standup paused in ANOTHER chat is the user's: no nothing-running
        line; the pre-#2033 path answers and the standup stays SUSPENDED."""
        service = _service(_ChitchatLLM())
        with _World() as w:
            conv = await w.suspended(str(uuid4()))
            result = await service.process_intent(
                message=text, session_id=str(uuid4()), user_id=_USER
            )
            assert await w.state(conv) == StandupConversationState.SUSPENDED
        assert result.message not in (CXO_NOTHING_TO_CANCEL, CXO_NO_STANDUP)


class TestSeamUnit:
    pytestmark = pytest.mark.asyncio

    async def test_armed_rail_wins(self):
        service = _service(_ExplosiveLLM())
        sid = str(uuid4())
        with _World():
            with patch.object(IntentService, "_armed_offer_signal", return_value="workflow_offer"):
                out = await service._nothing_running_reply("cancel", session_id=sid, user_id=_USER)
        assert out is None

    async def test_lookup_failure_never_claims_nothing_running(self):
        service = _service(_ExplosiveLLM())
        with patch(
            "services.intent.intent_service.get_process_registry",
            side_effect=RuntimeError("boom"),
        ):
            out = await service._nothing_running_reply(
                "cancel", session_id=str(uuid4()), user_id=_USER
            )
        assert out is None

    def test_runs_before_classification_after_the_arms(self):
        import services.intent.intent_service as mod

        src = inspect.getsource(mod.IntentService._process_intent_internal)
        step = src.index("await self._nothing_running_reply(")
        assert src.index("await self._check_pending_resume_offer(") < step
        assert src.index("self._check_pending_list_remainder(") < step
        assert step < src.index("await self.intent_classifier.classify_multiple(")


class TestCrossChatStandupAsk:
    """Arch's pin (same lane): a standup SUSPENDED in chat A; a standup ask in
    chat B offers continue/restart and creates NO new conversation row."""

    pytestmark = pytest.mark.asyncio

    async def test_slash_standup_in_chat_b_through_process_intent(self, floor_calls):
        service = _service(_ExplosiveLLM())
        chat_a, chat_b = str(uuid4()), str(uuid4())
        with _World() as w:
            conv = await w.suspended(chat_a)
            before = len(w.manager._conversations)
            result = await service.process_intent(
                message="/standup", session_id=chat_b, user_id=_USER
            )
            assert len(w.manager._conversations) == before == 1
            assert await w.state(conv) == StandupConversationState.SUSPENDED
        assert result.message == STANDUP_SESSION_EXISTS_ASK
        assert result.intent_data["action"] == "standup_session_exists"
        offer = get_or_create_context(chat_b, user_id=_USER).last_offer
        assert offer is not None and offer.offer_type == "process_resume"

    async def test_start_path_in_chat_b(self):
        service = _service(_ExplosiveLLM())
        chat_a, chat_b = str(uuid4()), str(uuid4())
        with _World() as w:
            await w.suspended(chat_a)
            result = await service._start_standup_conversation(_USER, chat_b)
            assert len(w.manager._conversations) == 1
        assert result.message == STANDUP_SESSION_EXISTS_ASK
