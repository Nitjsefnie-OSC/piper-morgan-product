"""#1771 second seam -- Web's served finding on alpha 5e5f3366c4 (2026-10-14 21:42 PT).

Web's three runs (same chat, clean chat, across a new chat; an account with no
connected source): ``my standup interview`` -> ``yes`` -> one answer -> ``stop``
-> "No problem -- I've paused standup. We can pick it up anytime." ->
``do a standup`` -> the EMPTY-SOURCE reply, no resume offer -> ``not now`` ->
"No problem! The paused standup has been cleared. Just say /standup ...".

Two defects, one seam (Lead's reading on the issue, CXO's memo 21:50):

1. A deferral with a SUSPENDED standup and NO resume offer pending fell to the
   #1529 bare exit (``detect_flow_exit``) and abandoned the paused standup.
   A deferral now protects a suspended flow with or without an offer; only an
   explicit cancel abandons.
2. ``do a standup`` on an account with no source answered from the empty-source
   branch before any suspended-session check, so the continue/restart offer was
   unreachable. The paused standup now outranks the empty-source reply.

Strings are CXO's (memo 2026-10-14 21:50): the pause line after ``stop``, the
abandon line on an explicit cancel, the defer line unchanged.

Layer: handler (the real ``ProcessRegistry`` + ``StandupProcessAdapter`` over the
in-memory manager double, the real ``IntentService`` seams with the assembler
patched at its import seam and an explosive LLM). Not a served run; Web's
re-run after promotion is the acceptance.
"""

import pathlib
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.domain.models import Intent
from services.intent.intent_service import (
    RESUME_ABANDON_REPLY,
    RESUME_DEFER_REPLY,
    STANDUP_SESSION_EXISTS_ASK,
    IntentService,
)
from services.intent_service import standup_preferences as sp
from services.intent_service import verified_inference as vi
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.process.adapters import STANDUP_PAUSE_REPLY, StandupProcessAdapter
from services.process.registry import ESCAPE_COMMANDS, ProcessRegistry, pause_message_for
from services.shared_types import IntentCategory, StandupConversationState
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

_USER = "3f7b8a52-1771-4b00-9e00-000000001771"
DEFERRALS = ["not now", "not right now", "not today", "maybe later"]
EXPLICIT_CANCELS = ["cancel that", "forget it", "start over"]

# CXO's ruled strings, quoted here so a drift in the constants fails loudly.
CXO_PAUSE = "No problem — I've paused your standup. Just ask when you want to pick it back up."
CXO_ABANDON = (
    "Okay, I've dropped your paused standup. Say 'do a standup' whenever you want a fresh one."
)
CXO_DEFER = "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name}); these turns are deterministic")


@pytest.fixture(autouse=True)
def _clean_transient_state():
    sp._MODE_CHOICES.clear()
    vi._SESSION_DECLINES.clear()
    yield
    sp._MODE_CHOICES.clear()
    vi._SESSION_DECLINES.clear()


@pytest.fixture
def mem_prefs(monkeypatch):
    store: dict = {_USER: {}}

    async def _load(user_id):
        return dict(store.get(str(user_id), {}))

    async def _save(user_id, key, value):
        if str(user_id) not in store:
            return False
        store[str(user_id)][key] = value
        return True

    from services.intent_service import collaboration_gate

    monkeypatch.setattr(collaboration_gate, "_load_preferences", _load)
    monkeypatch.setattr(collaboration_gate, "_save_preference", _save)
    return store


@pytest.fixture
def service(mem_prefs):
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


class _World:
    """One user's standup world: the in-memory manager, the real registry with
    the real standup adapter, and the patches that make every seam see them."""

    def __init__(self):
        self.manager = FakeStandupConversationManager()
        self.registry = ProcessRegistry()
        self.registry.register(StandupProcessAdapter())
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

    async def interview_mid_answer(self, session_id):
        """``my standup interview`` -> ``yes`` -> one answer: mid-gathering."""
        conv = await self.manager.create_conversation(session_id, _USER)
        await self.manager.transition_state(conv.id, StandupConversationState.GATHERING_YESTERDAY)
        await self.manager.transition_state(conv.id, StandupConversationState.GATHERING_TODAY)
        return conv

    async def state(self, conv):
        return (await self.manager.get_conversation(conv.id)).state


def _summary(empty):
    summary = MagicMock()
    summary.is_empty.return_value = empty
    summary.to_prose.return_value = "Here's your derived standup."
    summary.to_dict.return_value = {"sections": []}
    return summary


async def _do_a_standup(service, sid, empty=True):
    """``do a standup`` at the standup handler (the served empty-source reply
    came from this handler's empty branch)."""
    intent = Intent(
        category=IntentCategory.STATUS,
        action="get_standup",
        original_message="do a standup",
        confidence=1.0,
    )
    with patch(
        "services.standup.assembler.build_user_standup_summary",
        new=AsyncMock(return_value=_summary(empty)),
    ):
        return await service._handle_standup_query(intent, "wf-1771", session_id=sid, user_id=_USER)


def _armed_resume(sid):
    """What process_intent reads back on the next turn (the one-turn
    ``last_offer`` rail): (pending, rendered ask)."""
    offer = get_or_create_context(sid, user_id=_USER).last_offer
    if offer is not None and offer.offer_type == "process_resume":
        return True, offer.offer_text
    return False, None


async def _reply(service, sid, message):
    pending, question = _armed_resume(sid)
    get_or_create_context(sid, user_id=_USER).last_offer = None  # one-turn memory
    return await service._check_pending_resume_offer(
        _USER,
        sid,
        message,
        resume_offer_pending=pending,
        resume_offer_question=question,
    )


class TestRuledStrings:
    def test_constants_are_cxos_strings(self):
        assert STANDUP_PAUSE_REPLY == CXO_PAUSE
        assert RESUME_ABANDON_REPLY == CXO_ABANDON
        assert RESUME_DEFER_REPLY == CXO_DEFER  # unchanged since 10-14 11:20

    def test_cleared_and_slash_form_are_gone_from_the_abandon_path(self):
        src = (
            pathlib.Path(__file__).resolve().parents[4]
            / "services"
            / "intent"
            / "intent_service.py"
        )
        text = src.read_text()
        assert "The paused standup has been cleared" not in text
        assert "/standup" not in RESUME_ABANDON_REPLY


class TestStopPausesWithTheRuledLine:
    """(c) ``stop`` mid-interview: SUSPENDED, CXO's pause line, from the handler."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", sorted(ESCAPE_COMMANDS))
    async def test_every_escape_word_pauses_the_standup(self, word):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.interview_mid_answer(sid)
            result = await w.registry.check_active_processes(_USER, sid, word)
            assert result.handled and result.escaped
            assert result.response_message == CXO_PAUSE
            assert await w.state(conv) == StandupConversationState.SUSPENDED

    def test_registry_keeps_the_generic_default_for_other_processes(self):
        handler = MagicMock(spec=["process_type"])
        handler.process_type.value = "onboarding"
        assert (
            pause_message_for(handler)
            == "No problem — I've paused onboarding. We can pick it up anytime."
        )

    def test_a_failing_or_async_hook_falls_back_to_the_generic_line(self):
        broken = MagicMock()
        broken.process_type.value = "planning"
        broken.pause_message.side_effect = RuntimeError("boom")
        assert pause_message_for(broken).startswith("No problem — I've paused planning.")
        async_double = MagicMock()
        async_double.process_type.value = "planning"
        async_double.pause_message = AsyncMock(return_value="never awaited")
        assert pause_message_for(async_double).startswith("No problem — I've paused planning.")


class TestDeferralWithNoOfferKeepsTheSuspension:
    """(a) the served defect: suspended standup, no offer on screen, a deferral."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", DEFERRALS)
    async def test_deferral_does_not_abandon(self, service, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.interview_mid_answer(sid)
            await w.registry.check_active_processes(_USER, sid, "stop")
            assert _armed_resume(sid) == (False, None)
            result = await _reply(service, sid, turn)
            assert result is None  # not ours to answer; normal processing serves it
            assert await w.state(conv) == StandupConversationState.SUSPENDED


class TestExplicitCancelAbandons:
    """(b) only an explicit cancel drops the paused standup, with CXO's line."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", EXPLICIT_CANCELS)
    async def test_explicit_cancel_abandons_with_the_ruled_line(self, service, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.interview_mid_answer(sid)
            await w.registry.check_active_processes(_USER, sid, "stop")
            result = await _reply(service, sid, turn)
            assert result is not None and result.message == CXO_ABANDON
            assert await w.state(conv) == StandupConversationState.ABANDONED


class TestPausedStandupOutranksTheEmptySourceReply:
    """(d) no connected source: ``do a standup`` with a paused standup renders
    the continue/restart offer, armed, not the empty-source reply."""

    @pytest.mark.asyncio
    async def test_offer_not_empty_source_reply(self, service):
        sid = str(uuid4())
        with _World() as w:
            await w.interview_mid_answer(sid)
            await w.registry.check_active_processes(_USER, sid, "stop")
            result = await _do_a_standup(service, sid, empty=True)
        assert result.message == STANDUP_SESSION_EXISTS_ASK
        assert "build your standup from yet" not in result.message
        assert result.intent_data["action"] == "standup_session_exists"
        assert _armed_resume(sid) == (True, STANDUP_SESSION_EXISTS_ASK)
        # the empty-lead interview invitation was not armed over it
        assert service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER) is None

    @pytest.mark.asyncio
    async def test_no_paused_standup_keeps_the_empty_source_reply(self, service):
        sid = str(uuid4())
        with _World():
            result = await _do_a_standup(service, sid, empty=True)
        assert result.message == sp.INVITE_EMPTY_LEAD
        assert _armed_resume(sid) == (False, None)

    @pytest.mark.asyncio
    async def test_a_non_empty_report_still_renders_as_asked(self, service):
        """Scope: the empty branch only; a report with content is unchanged."""
        sid = str(uuid4())
        with _World() as w:
            await w.interview_mid_answer(sid)
            await w.registry.check_active_processes(_USER, sid, "stop")
            result = await _do_a_standup(service, sid, empty=False)
        assert "Here's your derived standup." in result.message
        assert STANDUP_SESSION_EXISTS_ASK not in result.message
        assert _armed_resume(sid) == (False, None)

    @pytest.mark.asyncio
    async def test_explicit_interview_ask_in_a_new_chat_offers_the_paused_one(self, service):
        """The #2007 door, cross-chat: a paused standup is the user's, not the
        session's; a new chat's ask no longer orphans it."""
        first, second = str(uuid4()), str(uuid4())
        with _World() as w:
            conv = await w.interview_mid_answer(first)
            await w.registry.check_active_processes(_USER, first, "stop")
            result = await service._start_standup_conversation(_USER, second)
            assert result.message == STANDUP_SESSION_EXISTS_ASK
            assert await w.state(conv) == StandupConversationState.SUSPENDED
            assert len(w.manager._conversations) == 1  # no second conversation
        assert _armed_resume(second) == (True, STANDUP_SESSION_EXISTS_ASK)


class TestWebsServedRuns:
    """(e) Web's three runs at the handler layer: ``stop`` -> ``do a standup``
    -> ``not now``. Expected after the fix: the pause line; the continue/restart
    offer; the defer line with the standup still SUSPENDED; and a later
    ``continue`` picks it back up (the defer line's promise)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("run", ["same_chat", "clean_chat", "across_new_chat"])
    async def test_run(self, service, run):
        start = str(uuid4())
        later = start if run in ("same_chat", "clean_chat") else str(uuid4())
        with _World() as w:
            if run == "clean_chat":
                # a fresh chat with nothing else in it before the interview
                assert w.manager._conversations == {}
            conv = await w.interview_mid_answer(start)

            paused = await w.registry.check_active_processes(_USER, start, "stop")
            assert paused.response_message == CXO_PAUSE

            offered = await _do_a_standup(service, later, empty=True)
            assert offered.message == STANDUP_SESSION_EXISTS_ASK

            deferred = await _reply(service, later, "not now")
            assert deferred is not None and deferred.message == CXO_DEFER
            assert "cleared" not in deferred.message
            assert await w.state(conv) == StandupConversationState.SUSPENDED

            # the offer was one-turn; asking again re-offers, continue resumes
            reoffered = await _do_a_standup(service, later, empty=True)
            assert reoffered.message == STANDUP_SESSION_EXISTS_ASK
            resumed = await _reply(service, later, "continue")
            assert resumed is not None
            assert resumed.intent_data["action"] == "standup_conversation_resumed"
            assert await w.state(conv) != StandupConversationState.SUSPENDED
