"""1771 invitation edges: the "ready to start?" turn, read whole-message.

CXO 2026-10-15 09:55 + 10:10, Arch 10:1x. At the invitation
(``_handle_initiated``):

- Leaving reads ``is_bare_decline`` (the shared full-message decline row plus
  the bare deferrals), the predicate's DEFER verdict, a DECLINE verdict that
  also carries a deferral row ("no, not now"), and bare "later" as a whole
  message. The anywhere word set ``{"no", "nope", "cancel", "later"}`` and the
  ``"not now"`` substring are gone, so "I'm good to go" and "no, let's start"
  are no longer told "no standup for now".
- The quick bypass is exact whole-message entries only; "skip the questions"
  is one (the user said what they want). "quick question before we start" is
  not a bypass.

Every leave gets CXO's invitation line and leaves no suspended record.

Layer: handler. The real ``ProcessRegistry`` + ``StandupProcessAdapter`` + the
real ``StandupConversationHandler`` over the in-memory manager double;
generation is stubbed (an LLM path). Not a served run.
"""

from unittest.mock import AsyncMock, patch
from uuid import uuid4

import pytest

from services.process.adapters import StandupProcessAdapter
from services.process.registry import ProcessRegistry
from services.shared_types import StandupConversationState
from services.standup.conversation_handler import (
    _QUICK_BYPASS_ENTRIES,
    ConversationResponse,
    StandupConversationHandler,
)
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

S = StandupConversationState
_USER = "3f7b8a52-1771-4c00-9e00-00000017710e"
CXO_INVITATION_END = "Okay, no standup for now. Say 'do a standup' whenever you want one."
FIRST_QUESTION = "What did you work on yesterday?"
_GENERATED = "GENERATED-STANDUP-STUB"


class _World:
    def __init__(self):
        self.manager = FakeStandupConversationManager()
        self.handler = StandupConversationHandler(conversation_manager=self.manager)
        self.generate = AsyncMock(
            return_value=ConversationResponse(
                message=_GENERATED, state=S.REFINING, requires_input=True
            )
        )
        self.handler._generate_standup = self.generate
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

    async def invite_then(self, turn):
        sid = str(uuid4())
        conv = await self.manager.create_conversation(sid, _USER)
        assert conv.state == S.INITIATED
        result = await self.registry.check_active_processes(_USER, sid, turn)
        state = (await self.manager.get_conversation(conv.id)).state
        return result, state


class TestYesShapedTurnsStartTheInterview:
    """CXO 09:55 item 2: the predicate's unanchored decline rows read these
    as a no; at the invitation only the whole-message row is read."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        [
            "I'm good to go",
            "no, let's start",
            "skip docs",
            "quick question before we start",
            "yes, let's do it",
        ],
    )
    async def test_starts_the_interview(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.response_message == FIRST_QUESTION
            assert state == S.GATHERING_YESTERDAY
            w.generate.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["skip docs", "skip the docs", "skip the questions please"])
    async def test_skip_something_else_starts_the_interview(self, turn):
        """Only the flow's own name makes "skip" an exit (Arch 10:4x)."""
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert not result.escaped
            assert result.response_message == FIRST_QUESTION
            assert state == S.GATHERING_YESTERDAY


class TestSkipTheStandupLeaves:
    """CXO 10:25 item 2 / Arch 10:4x: "skip the standup" is a #1529 exit on
    the flow's own name (``escape._skip_flow_re``, flow-specific words only).
    Was ``test_skip_the_standup_starts_the_interview`` (f76a307ecb: the
    predicate read it PASS, so the interview started)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        [
            "skip the standup",
            "skip standup",
            "Skip the standup.",
            "please skip the standup",
            "skip my standup",
            "skip the daily standup",
            "skip stand-up",
        ],
    )
    async def test_ends_with_the_invitation_line(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert state == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            assert await w.registry.check_suspended_processes(_USER) is None
            w.generate.assert_not_called()


class TestLeavingGetsTheInvitationLine:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        [
            # whole-message declines (is_bare_decline)
            "no thanks",
            "nah",
            "nope",
            "I'm good",
            "skip",
            "No.",
            # deferrals: the bare-deferral set and the predicate's DEFER verdict
            "not now",
            "maybe later",
            "not right now",
            # a decline carrying a deferral row (decline is ordered first)
            "no, not now",
            "no, maybe later",
            # bare "later", whole message only
            "later",
            "Later.",
        ],
    )
    async def test_ends_with_no_suspended_record(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.handled
            assert result.response_message == CXO_INVITATION_END
            assert state == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            assert await w.registry.check_suspended_processes(_USER) is None
            w.generate.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["later today works, let's go", "I'll know more later, start"])
    async def test_later_inside_a_turn_is_not_a_leave(self, turn):
        """Was: ``later`` matched anywhere in the turn and ended the standup."""
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert state == S.GATHERING_YESTERDAY


class TestCancelShapedTurnsLeave:
    """CXO 10:25 item 1 / Arch 10:4x. At the invitation these END with the
    invitation line and leave no suspended record:

    - the polite #888 words: the hatch strips one "please", so "please
      cancel" is ``cancel`` and "stop please" is ``stop`` (escaped, the
      handler never sees them);
    - turns that ALREADY left through the #1529 whole-message exit before
      this change (Arch read them from ``_exit_re`` / ``BARE_EXIT_COMMANDS``;
      these pins confirm by running them).

    "can you cancel my 3pm meeting?" is not a leave: it reaches the handler
    and starts the interview (the normal answer path)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn", ["please cancel", "cancel please", "please stop", "stop please"]
    )
    async def test_polite_hatch_word_ends(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert state == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            w.generate.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        ["cancel that", "cancel it", "please cancel it", "forget it", "please cancel the standup"],
    )
    async def test_already_a_1529_exit_ends(self, turn):
        from services.process.escape import detect_flow_exit
        from services.process.registry import ProcessType

        assert detect_flow_exit(turn, ProcessType.STANDUP)
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert state == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            w.generate.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn", ["can you cancel my 3pm meeting?", "please cancel my 3pm meeting"]
    )
    async def test_a_request_naming_cancel_is_not_a_leave(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert not result.escaped
            assert result.response_message == FIRST_QUESTION
            assert state == S.GATHERING_YESTERDAY


class TestQuickBypassIsWholeMessage:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        [
            "quick",
            "Quick.",
            "fast",
            "just the report",
            "the quick one",
            "quick standup",
            "Quick standup",
            "quick report",
            "the quick report",
            "skip the questions",
            "skip the questions.",
            "skip questions",
        ],
    )
    async def test_generates_the_quick_standup(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.response_message == _GENERATED
            w.generate.assert_awaited_once()
            assert state == S.GENERATING

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn", ["quick question before we start", "skip docs", "skip the standup", "fast please"]
    )
    async def test_not_a_bypass(self, turn):
        with _World() as w:
            await w.invite_then(turn)
            w.generate.assert_not_called()

    def test_the_entries_are_exactly_cxos(self):
        assert _QUICK_BYPASS_ENTRIES == {
            "quick",
            "fast",
            "just the report",
            "the quick one",
            "quick standup",
            "quick report",
            "the quick report",
            "skip the questions",
            "skip questions",
        }


class TestDeferralReadThroughTheContractHelper:
    """Arch 10:4x (deviation 1): "no, not now" keeps leaving, but the standup
    reads the deferral through ``soft_invocation.contains_deferral``, not the
    ``DEFER_PATTERNS`` list. No new row."""

    def test_the_standup_package_does_not_name_the_pattern_list(self):
        import pathlib

        root = pathlib.Path(__file__).resolve().parents[4]
        offenders = [
            str(path.relative_to(root))
            for path in sorted((root / "services/standup").rglob("*.py"))
            if "DEFER_PATTERNS" in path.read_text()
        ]
        assert offenders == []

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("no, not now", True),
            ("no, maybe later", True),
            ("not right now", True),
            ("Not yet.", True),
            ("no", False),
            ("later", False),
            ("let's start", False),
            ("", False),
        ],
    )
    def test_contains_deferral(self, text, expected):
        from services.intent_service.soft_invocation import contains_deferral

        assert contains_deferral(text) is expected

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["no, not now", "No, not now."])
    async def test_no_not_now_still_leaves(self, turn):
        with _World() as w:
            result, state = await w.invite_then(turn)
            assert result.response_message == CXO_INVITATION_END
            assert state == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
