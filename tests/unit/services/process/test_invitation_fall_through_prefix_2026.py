"""#2026: an off-topic or off-intent turn at the standup invitation makes no pause claim.

Since e08a9bcd50 the standup adapter's ``suspend()`` CLOSES an unstarted
standup (INITIATED, "ready to start?", nothing captured) instead of suspending
it. The two fall-through callers of ``suspend()`` (#899 off-topic, #1529
off-intent) still prefixed the answer with "I've paused it — you can say
'resume'", untrue there: nothing was paused and ``resume`` finds nothing.

CXO 2026-10-15 (item 4, and the #2028 memo): at the invitation drop the prefix
and just answer the question, no invitation line either; a later
``do a standup`` starts fresh. Mid-interview the prefix stays true and stays.

Built so the prefix FOLLOWS the transition (Lead's brief): ``suspend()``
reports what it did (``SuspendOutcome``), and the registry renders the prefix
only when something was paused. No stage check in the registry.

Layer: handler. The real ``ProcessRegistry`` + ``StandupProcessAdapter`` +
``StandupConversationHandler`` over the in-memory manager double, plus the
intent-service seam that turns the registry result into the prefix. Not a
served run.
"""

from unittest.mock import patch
from uuid import uuid4

import pytest

from services.domain.models import StandupItem, StandupPartialCapture
from services.process.adapters import StandupProcessAdapter
from services.process.off_topic import format_off_topic_pause_message
from services.process.registry import ProcessRegistry, ProcessType, SuspendOutcome
from services.shared_types import StandupConversationState
from services.standup.conversation_handler import StandupConversationHandler
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

S = StandupConversationState
_USER = "3f7b8a52-2026-4c00-9e00-000000002026"

# #899 fixtures (test_off_topic.py: weather/time, identity, capability).
OFF_TOPIC_TURNS = ["What's the weather like?", "Who are you?", "What can you do?"]
# #1529 off-intent fixtures (test_flow_escape_1529.py: cross-domain actions).
OFF_INTENT_TURNS = ["restore CoVa", "remind me to check the deploy"]
ALL_FALL_THROUGH = OFF_TOPIC_TURNS + OFF_INTENT_TURNS

MID_INTERVIEW = [S.GATHERING_YESTERDAY, S.GATHERING_TODAY, S.GATHERING_BLOCKERS]

# The claim words: none may appear when nothing was paused.
_PAUSE_CLAIM_WORDS = ("paused", "resume")


class _World:
    def __init__(self):
        self.manager = FakeStandupConversationManager()
        self.handler = StandupConversationHandler(conversation_manager=self.manager)
        self.adapter = StandupProcessAdapter()
        self.registry = ProcessRegistry()
        self.registry.register(self.adapter)
        self._patch = patch(
            "services.conversation.conversation_handler._get_standup_components",
            return_value=(self.manager, self.handler),
        )

    def __enter__(self):
        self._patch.start()
        return self

    def __exit__(self, *exc):
        self._patch.stop()
        return False

    async def at(self, session_id, stage):
        conv = await self.manager.create_conversation(session_id, _USER)
        if stage == S.INITIATED:
            return conv
        await self.manager.transition_state(conv.id, S.GATHERING_YESTERDAY)
        capture = StandupPartialCapture()
        capture.yesterday.append(StandupItem(display="shipped the cut", source="user"))
        await self.manager.update_partial_capture(conv.id, capture)
        for nxt in (S.GATHERING_TODAY, S.GATHERING_BLOCKERS):
            if MID_INTERVIEW.index(nxt) > MID_INTERVIEW.index(stage):
                break
            await self.manager.transition_state(conv.id, nxt)
        return conv

    async def state(self, conv):
        return (await self.manager.get_conversation(conv.id)).state


def _no_pause_claim(text):
    return text is None or not any(w in text.lower() for w in _PAUSE_CLAIM_WORDS)


class TestAtTheInvitation:
    """INITIATED: the turn falls through with no prefix; nothing is left to resume."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ALL_FALL_THROUGH)
    async def test_no_prefix_and_nothing_suspended(self, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.INITIATED)
            result = await w.registry.check_active_processes(_USER, sid, turn)
            # still a fall-through: the question gets answered by normal processing
            assert result.handled is False and result.escaped is True
            assert result.process_type == ProcessType.STANDUP
            # no "I've paused it — say 'resume'" claim, and no invitation line
            assert result.response_message is None
            assert await w.state(conv) == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            assert await w.registry.check_suspended_processes(_USER) is None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ALL_FALL_THROUGH)
    async def test_intent_seam_prepends_nothing_but_names_the_flow(self, turn, intent_service):
        """The seam's prefix is None (nothing glued onto the answer); the flow
        is still named so #1596 tells the floor not to re-open "ready to start?"."""
        sid = str(uuid4())
        with _World() as w:
            await w.at(sid, S.INITIATED)
            with patch(
                "services.intent.intent_service.get_process_registry",
                return_value=w.registry,
            ):
                result, prefix, escaped = await intent_service._check_active_guided_process(
                    _USER, sid, turn
                )
            assert result is None  # falls through to be answered
            assert prefix is None
            assert _no_pause_claim(prefix)
            assert escaped == ProcessType.STANDUP

    @pytest.mark.asyncio
    async def test_a_later_do_a_standup_starts_fresh(self):
        """Nothing is offered back: the next standup ask finds no suspended row."""
        sid = str(uuid4())
        with _World() as w:
            await w.at(sid, S.INITIATED)
            await w.registry.check_active_processes(_USER, sid, OFF_TOPIC_TURNS[0])
            assert await w.adapter.check_active(_USER, sid) is False
            assert await w.registry.check_suspended_processes(_USER) is None


class TestMidInterview:
    """Mid-interview the prefix is true (the standup is SUSPENDED) and stays."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("stage", MID_INTERVIEW, ids=lambda s: s.value)
    @pytest.mark.parametrize("turn", ALL_FALL_THROUGH)
    async def test_prefix_stays_and_standup_is_suspended(self, turn, stage):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, stage)
            result = await w.registry.check_active_processes(_USER, sid, turn)
            assert result.handled is False and result.escaped is True
            assert result.response_message == format_off_topic_pause_message(ProcessType.STANDUP)
            assert await w.state(conv) == S.SUSPENDED
            assert await w.adapter.has_suspended_session(_USER) is not None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ALL_FALL_THROUGH)
    async def test_intent_seam_returns_the_prefix(self, turn, intent_service):
        sid = str(uuid4())
        with _World() as w:
            await w.at(sid, S.GATHERING_TODAY)
            with patch(
                "services.intent.intent_service.get_process_registry",
                return_value=w.registry,
            ):
                result, prefix, escaped = await intent_service._check_active_guided_process(
                    _USER, sid, turn
                )
            assert result is None
            assert prefix == format_off_topic_pause_message(ProcessType.STANDUP)
            assert escaped == ProcessType.STANDUP


class TestTheOutcomeDrivesThePrefix:
    """The registry reads the handler's reported transition, not the stage."""

    class _Flow:
        process_type = ProcessType.PLANNING

        def __init__(self, outcome=None, raises=False):
            self._outcome = outcome
            self._raises = raises

        async def check_active(self, user_id, session_id):
            return True

        async def handle_message(self, user_id, session_id, message):  # pragma: no cover
            raise AssertionError("an off-topic turn never reaches the flow")

        async def suspend(self, user_id, session_id):
            if self._raises:
                raise RuntimeError("boom")
            return self._outcome

        async def has_suspended_session(self, user_id):
            return None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", [OFF_TOPIC_TURNS[0], OFF_INTENT_TURNS[0]])
    async def test_closed_means_no_prefix(self, turn):
        registry = ProcessRegistry()
        registry.register(self._Flow(SuspendOutcome.CLOSED))
        result = await registry.check_active_processes(_USER, "s", turn)
        assert result.escaped and result.response_message is None

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "flow_kwargs",
        [{"outcome": SuspendOutcome.PAUSED}, {"outcome": None}, {"raises": True}],
        ids=["paused", "legacy-none", "raising"],
    )
    @pytest.mark.parametrize("turn", [OFF_TOPIC_TURNS[0], OFF_INTENT_TURNS[0]])
    async def test_paused_or_unknown_keeps_the_prefix(self, turn, flow_kwargs):
        registry = ProcessRegistry()
        registry.register(self._Flow(**flow_kwargs))
        result = await registry.check_active_processes(_USER, "s", turn)
        assert result.escaped
        assert result.response_message == format_off_topic_pause_message(ProcessType.PLANNING)

    def test_registry_holds_no_stage_check(self):
        """The registry never names a standup state: the adapter reports."""
        import pathlib

        root = pathlib.Path(__file__).resolve().parents[4]
        src = (root / "services/process/registry.py").read_text()
        assert "StandupConversationState" not in src
        assert "INITIATED" not in src


@pytest.fixture
def intent_service():
    from services.intent.intent_service import IntentService

    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()
