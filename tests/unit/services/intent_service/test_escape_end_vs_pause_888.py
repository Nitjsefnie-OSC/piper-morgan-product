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

Word map (CXO 2026-10-15 09:15, Arch 09:4x / 09:5x, the converged ruling):
END = {cancel, quit, exit}; PAUSE = {stop, never mind} ("never mind" can mean
"forget that answer", so it takes the reversible path); ``skip`` is not an
escape word for any process. A bare "skip" reaches the handler: mid-interview
it is "nothing for this part, advance"; at the
invitation it is the shared predicate's DECLINE verdict and leaves with the
invitation line (dropped from the quick-bypass set; ``quick`` keeps it).

Belt pins (Arch): for EVERY escape word at EVERY standup stage the result is
``escaped`` and ``check_active`` is False afterwards; at INITIATED every escape
word, every whole-message #1529 exit and a deferral leave
``has_suspended_session`` returning None.

Layer: handler. The real ``ProcessRegistry`` + ``StandupProcessAdapter`` + the
real ``StandupConversationHandler`` over the in-memory manager double. Not a
served run.
"""

from unittest.mock import AsyncMock, patch
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
from services.standup.conversation_handler import (
    ConversationResponse,
    StandupConversationHandler,
)
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
    def test_cxo_word_map(self):
        """CXO 2026-10-15 09:15: a word that explicitly withdraws ends; a word
        that could mean "not right now" pauses. Was END {cancel, quit, exit,
        never mind} / PAUSE {stop, skip} (Arch's default, e08a9bcd50)."""
        assert ESCAPE_END_WORDS == {"cancel", "quit", "exit"}
        assert ESCAPE_PAUSE_WORDS == {"stop", "never mind"}

    def test_the_union_is_five_words_and_the_sets_are_disjoint(self):
        assert ESCAPE_COMMANDS == {"cancel", "exit", "stop", "quit", "never mind"}
        assert ESCAPE_END_WORDS | ESCAPE_PAUSE_WORDS == ESCAPE_COMMANDS
        assert not ESCAPE_END_WORDS & ESCAPE_PAUSE_WORDS

    def test_skip_is_not_an_escape_word(self):
        """Arch 2026-10-15: generic, every process; no per-process claim."""
        assert "skip" not in ESCAPE_COMMANDS
        assert not ProcessRegistry()._is_escape_command("skip")


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
            pauses = word.strip().lower() in ("stop", "never mind")
            expected = S.SUSPENDED if pauses else S.ABANDONED
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


# --- never mind: the reversible path ------------------------------------------


class TestNeverMindTakesTheReversiblePath:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("stage", MID_INTERVIEW_STAGES, ids=lambda s: s.value)
    async def test_mid_interview_never_mind_pauses_with_the_pause_line(self, stage):
        """Was: END, the drop line (e08a9bcd50). CXO 09:15: it can mean
        "forget that answer", so it pauses and keeps what was captured."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, stage)
            result = await w.registry.check_active_processes(_USER, sid, "never mind")
            assert result.escaped
            assert result.response_message == CXO_PAUSE
            assert await w.state(conv) == S.SUSPENDED
            assert await w.adapter.has_suspended_session(_USER) is not None

    @pytest.mark.asyncio
    async def test_never_mind_at_the_invitation_ends_with_the_invitation_line(self):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.at(sid, S.INITIATED)
            result = await w.registry.check_active_processes(_USER, sid, "never mind")
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None


# --- skip: the handler's word, not the hatch's ---------------------------------

_GENERATED = "GENERATED-STANDUP-STUB"


def _stub_generation(w):
    """Stand in for ``_generate_standup`` (an LLM path): record the call and
    hand back a marker, so a pin can see generation was reached."""
    stub = AsyncMock(
        return_value=ConversationResponse(message=_GENERATED, state=S.REFINING, requires_input=True)
    )
    w.handler._generate_standup = stub
    return stub


async def _at_question(w, session_id, stage):
    """``stage``'s question pending, every slot empty (nothing captured)."""
    conv = await w.manager.create_conversation(session_id, _USER)
    path = [S.GATHERING_YESTERDAY, S.GATHERING_TODAY, S.GATHERING_BLOCKERS]
    if stage == S.GATHERING_PREFERENCES:
        path = [S.GATHERING_PREFERENCES]
    for nxt in path:
        await w.manager.transition_state(conv.id, nxt)
        if nxt == stage:
            break
    return conv


class TestSkipMidInterviewAdvances:
    """The live chip defect (Arch 2026-10-15): Piper suggests ``skip`` at
    every interview question, and the hatch used to suspend on it. Now the
    handler reads it through ``_is_skip_signal``: nothing for this part,
    advance."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "stage,next_question,slot",
        [
            (S.GATHERING_YESTERDAY, "What's planned for today?", "yesterday"),
            (S.GATHERING_TODAY, "Any blockers or things you need help with?", "today"),
        ],
        ids=["yesterday", "today"],
    )
    async def test_skip_renders_the_next_question(self, stage, next_question, slot):
        sid = str(uuid4())
        with _World() as w:
            generate = _stub_generation(w)
            conv = await _at_question(w, sid, stage)
            result = await w.registry.check_active_processes(_USER, sid, "skip")
            assert result.handled and not result.escaped
            assert result.response_message == next_question
            generate.assert_not_called()
            after = await w.manager.get_conversation(conv.id)
            capture = after.partial_capture or StandupPartialCapture()
            assert getattr(capture, slot) == []
            assert await w.adapter.check_active(_USER, sid) is True
            assert await w.adapter.has_suspended_session(_USER) is None

    @pytest.mark.asyncio
    async def test_skip_at_blockers_advances_to_the_standup(self):
        """Blockers is the last question: "next" is the generated standup."""
        sid = str(uuid4())
        with _World() as w:
            generate = _stub_generation(w)
            conv = await _at_question(w, sid, S.GATHERING_BLOCKERS)
            result = await w.registry.check_active_processes(_USER, sid, "skip")
            assert result.handled and not result.escaped
            assert result.response_message == _GENERATED
            generate.assert_awaited_once()
            after = await w.manager.get_conversation(conv.id)
            capture = after.partial_capture or StandupPartialCapture()
            assert capture.blockers == []
            assert after.state != S.SUSPENDED
            assert await w.adapter.check_active(_USER, sid) is True
            assert await w.adapter.has_suspended_session(_USER) is None

    @pytest.mark.asyncio
    async def test_skip_at_the_legacy_preferences_stage_does_not_escape(self):
        sid = str(uuid4())
        with _World() as w:
            generate = _stub_generation(w)
            conv = await _at_question(w, sid, S.GATHERING_PREFERENCES)
            result = await w.registry.check_active_processes(_USER, sid, "skip")
            assert result.handled and not result.escaped
            generate.assert_awaited_once()
            assert (await w.state(conv)) not in (S.SUSPENDED, S.ABANDONED)
            assert await w.adapter.has_suspended_session(_USER) is None

    @pytest.mark.asyncio
    async def test_skip_keeps_earlier_answers(self):
        """A skip after a real answer: the captured answer stays, the skipped
        slot holds nothing."""
        sid = str(uuid4())
        with _World() as w:
            _stub_generation(w)
            conv = await w.at(sid, S.GATHERING_TODAY)
            result = await w.registry.check_active_processes(_USER, sid, "skip")
            assert not result.escaped
            after = await w.manager.get_conversation(conv.id)
            assert [i.display for i in after.partial_capture.yesterday] == ["shipped the cut"]
            assert after.partial_capture.today == []
            assert after.state == S.GATHERING_BLOCKERS


class TestSkipAtTheInvitationLeaves:
    """CXO 09:25 + Arch 09:5x: at "ready to start?" a bare "skip" leaves,
    through the predicate's DECLINE verdict (no word added to the handler's
    decline set); ``skip`` left the quick-bypass set."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["skip", "Skip", "skip."])
    async def test_skip_ends_with_the_invitation_line(self, turn):
        sid = str(uuid4())
        with _World() as w:
            generate = _stub_generation(w)
            conv = await w.at(sid, S.INITIATED)
            result = await w.registry.check_active_processes(_USER, sid, turn)
            assert result.handled and not result.escaped  # the handler, not the hatch
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == S.ABANDONED
            assert await w.adapter.has_suspended_session(_USER) is None
            assert await w.registry.check_suspended_processes(_USER) is None
            generate.assert_not_called()  # no standup generated

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["quick", "Quick standup", "fast", "just the report"])
    async def test_quick_still_generates_the_quick_standup(self, turn):
        sid = str(uuid4())
        with _World() as w:
            generate = _stub_generation(w)
            conv = await w.at(sid, S.INITIATED)
            result = await w.registry.check_active_processes(_USER, sid, turn)
            assert result.response_message == _GENERATED
            generate.assert_awaited_once()
            assert (await w.state(conv)) == S.GENERATING

    def test_skip_is_not_in_the_local_decline_set_or_the_bypass_set(self):
        """The verdict is the path: no word set in ``_handle_initiated``
        (the quick-bypass set, the local decline set) holds "skip".
        Mid-interview a typed "skip" advances (#2028 deleted the unrendered
        ``["nothing", "skip"]`` suggestion lists; typed input is the path)."""
        import ast
        import inspect
        import textwrap

        src = textwrap.dedent(inspect.getsource(StandupConversationHandler._handle_initiated))
        word_sets = [
            {e.value for e in node.elts if isinstance(e, ast.Constant)}
            for node in ast.walk(ast.parse(src))
            if isinstance(node, ast.Set)
        ]
        assert {"quick", "fast"} in word_sets  # the bypass set is still read here
        assert all("skip" not in ws for ws in word_sets)


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
