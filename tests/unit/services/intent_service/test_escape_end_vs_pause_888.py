"""#888 split: the escape hatch's words END or PAUSE, generically (Arch 2026-10-15).

Arch's ruling on #1771 (09:0x, "don't carve #888, split its words"): the
registry's six escape words are two frozensets. The registry chooses the
transition from the WORD alone, before any handler runs (PPM's 2026-03-13
#888 direction: escape words are never passed to the handler for
interpretation). The handler supplies only the line for each outcome
(``pause_message`` / ``drop_message``, optional hooks).

- END words -> ``_close_process`` (the handler's ``close()``; terminal; no
  resume re-offer, the #1529 anti-nag).
- PAUSE words -> ``suspend()`` (resumable).

Arch's follow-up (09:1x, "fix in the handler, not the hatch"): an UNSTARTED
standup (INITIATED, "ready to start?") is never suspended. The standup
adapter's ``suspend()`` closes it, and every way of leaving there gets the
invitation line, so no empty SUSPENDED row is ever offered back.

Belt pins (Arch): for EVERY escape word at EVERY standup stage the result is
``escaped`` and ``check_active`` is False afterwards; at INITIATED every escape
word, every whole-message #1529 exit and a deferral leave
``has_suspended_session`` returning None.

Layer: handler. The real ``ProcessRegistry`` + ``StandupProcessAdapter`` + the
real ``StandupConversationHandler`` over the in-memory manager double. Not a
served run.
"""

from unittest.mock import patch
from uuid import uuid4

import pytest

from services.domain.models import StandupItem, StandupPartialCapture
from services.process.adapters import StandupProcessAdapter
from services.process.escape import BARE_EXIT_COMMANDS, format_exit_message
from services.process.registry import (
    ESCAPE_COMMANDS,
    ESCAPE_END_WORDS,
    ESCAPE_PAUSE_WORDS,
    ProcessRegistry,
    ProcessType,
    drop_message_for,
    escape_reply_for,
    pause_message_for,
)
from services.shared_types import StandupConversationState
from services.standup.conversation_handler import StandupConversationHandler
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

_USER = "3f7b8a52-0888-4c00-9e00-000000000888"

# CXO's ruled strings, quoted so a drift in a constant fails loudly.
CXO_PAUSE = "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
CXO_DROP = "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
CXO_INVITATION_END = "Okay, no standup for now. Say 'do a standup' whenever you want one."

S = StandupConversationState
MID_INTERVIEW_STAGES = [
    S.GATHERING_PREFERENCES,  # legacy preference path, still reachable from INITIATED
    S.GATHERING_YESTERDAY,
    S.GATHERING_TODAY,
    S.GATHERING_BLOCKERS,
]
ALL_STAGES = [S.INITIATED] + MID_INTERVIEW_STAGES

# Whole-message #1529 exits (the bare-exit set plus the flow-named forms the
# four-seams pins use) and deferrals the predicate reads at the invitation.
WHOLE_MESSAGE_EXITS = sorted(BARE_EXIT_COMMANDS) + ["cancel that", "end standup", "forget it"]
DEFERRALS = ["not right now", "not today", "maybe later", "not yet"]


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
        if stage == S.GATHERING_PREFERENCES:
            await self.manager.transition_state(conv.id, S.GATHERING_PREFERENCES)
            return conv
        await self.manager.transition_state(conv.id, S.GATHERING_YESTERDAY)
        capture = StandupPartialCapture()
        capture.yesterday.append(StandupItem(display="shipped the cut", source="user"))
        await self.manager.update_partial_capture(conv.id, capture)
        for nxt in (S.GATHERING_TODAY, S.GATHERING_BLOCKERS):
            if MID_INTERVIEW_STAGES.index(nxt) > MID_INTERVIEW_STAGES.index(stage):
                break
            await self.manager.transition_state(conv.id, nxt)
        return conv

    async def state(self, conv):
        return (await self.manager.get_conversation(conv.id)).state


# --- The word sets ------------------------------------------------------------


class TestTheWordSets:
    def test_arch_default_map(self):
        assert ESCAPE_END_WORDS == {"cancel", "quit", "exit", "never mind"}
        assert ESCAPE_PAUSE_WORDS == {"stop", "skip"}  # skip: CXO to place

    def test_the_union_is_todays_six_words_and_the_sets_are_disjoint(self):
        assert ESCAPE_COMMANDS == {"cancel", "exit", "stop", "skip", "quit", "never mind"}
        assert ESCAPE_END_WORDS | ESCAPE_PAUSE_WORDS == ESCAPE_COMMANDS
        assert not ESCAPE_END_WORDS & ESCAPE_PAUSE_WORDS


# --- Belt pin: every word, every stage ----------------------------------------


class TestBeltEveryWordEveryStage:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("stage", ALL_STAGES, ids=lambda s: s.value)
    @pytest.mark.parametrize("word", sorted(ESCAPE_COMMANDS))
    async def test_escaped_and_no_longer_active(self, word, stage):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, stage)
            result = await w.registry.check_active_processes(_USER, sid, word)
            assert result.handled and result.escaped
            assert await w.adapter.check_active(_USER, sid) is False
            after = await w.state(conv)
            if stage == S.INITIATED:
                # unstarted: every word ends, with the invitation line
                assert after == S.ABANDONED
                assert result.response_message == CXO_INVITATION_END
            elif word in ESCAPE_END_WORDS:
                assert after == S.ABANDONED
                assert result.response_message == CXO_DROP
            else:
                assert after == S.SUSPENDED
                assert result.response_message == CXO_PAUSE

    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", sorted(ESCAPE_END_WORDS))
    async def test_an_end_word_is_not_offered_back(self, word):
        sid = str(uuid4())
        with _World() as w:
            await w.at(sid, S.GATHERING_TODAY)
            await w.registry.check_active_processes(_USER, sid, word)
            assert await w.adapter.has_suspended_session(_USER) is None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", sorted(ESCAPE_PAUSE_WORDS))
    async def test_a_pause_word_keeps_the_answers_and_is_offered_back(self, word):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.GATHERING_TODAY)
            await w.registry.check_active_processes(_USER, sid, word)
            assert await w.adapter.has_suspended_session(_USER) is not None
            after = await w.manager.get_conversation(conv.id)
            assert [i.display for i in after.partial_capture.yesterday] == ["shipped the cut"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", ["Cancel", "  QUIT  ", "Never Mind", "STOP"])
    async def test_case_and_whitespace_do_not_change_the_set(self, word):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.GATHERING_TODAY)
            await w.registry.check_active_processes(_USER, sid, word)
            expected = S.SUSPENDED if word.strip().lower() == "stop" else S.ABANDONED
            assert await w.state(conv) == expected


# --- Belt pin: nothing unstarted is ever suspended ----------------------------


class TestNoEmptySuspendedRecordAtTheInvitation:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn", sorted(ESCAPE_COMMANDS) + WHOLE_MESSAGE_EXITS + DEFERRALS + ["no", "later"]
    )
    async def test_every_way_of_leaving_leaves_nothing_to_offer(self, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.INITIATED)
            result = await w.registry.check_active_processes(_USER, sid, turn)
            assert result.handled
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            assert await w.registry.check_suspended_processes(_USER) is None

    @pytest.mark.asyncio
    async def test_suspend_itself_closes_an_unstarted_standup(self):
        """The handler's own definition of suspend (#888 "handler owns
        semantics"), so every caller of suspend (off-topic, off-intent) gets it."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.INITIATED)
            await w.adapter.suspend(_USER, sid)
            assert await w.state(conv) == S.ABANDONED

    @pytest.mark.asyncio
    async def test_suspend_mid_interview_is_unchanged(self):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.GATHERING_YESTERDAY)
            await w.adapter.suspend(_USER, sid)
            assert await w.state(conv) == S.SUSPENDED


# --- The handler supplies copy, never the choice ------------------------------


class _Bare:
    """A process with close/suspend but no copy hooks."""

    process_type = ProcessType.PLANNING

    def __init__(self):
        self.closed = False
        self.suspended = False

    async def check_active(self, user_id, session_id):
        return not (self.closed or self.suspended)

    async def handle_message(self, user_id, session_id, message):  # pragma: no cover
        raise AssertionError("an escape word never reaches the flow")

    async def suspend(self, user_id, session_id):
        self.suspended = True

    async def close(self, user_id, session_id):
        self.closed = True

    async def has_suspended_session(self, user_id):
        return None


class TestGenericAcrossProcesses:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", sorted(ESCAPE_END_WORDS))
    async def test_end_word_closes_with_the_generic_drop_line(self, word):
        registry, bare = ProcessRegistry(), _Bare()
        registry.register(bare)
        result = await registry.check_active_processes(_USER, "s", word)
        assert result.escaped and bare.closed and not bare.suspended
        assert result.response_message == format_exit_message(ProcessType.PLANNING)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("word", sorted(ESCAPE_PAUSE_WORDS))
    async def test_pause_word_suspends_with_the_generic_pause_line(self, word):
        registry, bare = ProcessRegistry(), _Bare()
        registry.register(bare)
        result = await registry.check_active_processes(_USER, "s", word)
        assert result.escaped and bare.suspended and not bare.closed
        assert result.response_message == pause_message_for(bare)

    @pytest.mark.asyncio
    async def test_a_hook_cannot_change_the_transition(self):
        """A copy hook that answers anything still only supplies copy: the
        word chose before the hook ran."""
        registry, bare = ProcessRegistry(), _Bare()
        bare.drop_message = lambda: "custom drop"
        registry.register(bare)
        result = await registry.check_active_processes(_USER, "s", "cancel")
        assert result.response_message == "custom drop"
        assert bare.closed and not bare.suspended

    @pytest.mark.asyncio
    async def test_a_raising_or_empty_hook_falls_back(self):
        bare = _Bare()

        async def _boom(user_id, session_id):
            raise RuntimeError("boom")

        bare.drop_message = _boom
        bare.pause_message = lambda: ""
        assert await escape_reply_for(bare, _USER, "s", end=True) == format_exit_message(
            ProcessType.PLANNING
        )
        assert await escape_reply_for(bare, _USER, "s", end=False) == pause_message_for(bare)
        assert drop_message_for(bare) == format_exit_message(ProcessType.PLANNING)

    def test_registry_source_holds_no_standup_copy(self):
        import pathlib

        root = pathlib.Path(__file__).resolve().parents[4]
        src = (root / "services/process/registry.py").read_text()
        for line in (CXO_PAUSE, CXO_DROP, CXO_INVITATION_END):
            assert line not in src
