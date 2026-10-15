"""#1771 four further standup seams (CXO ruling + Arch mechanism, 2026-10-15).

One rule (CXO): a deferral ("not now", "maybe later") PAUSES and never
destroys; only an explicit cancel, or a "no" to the invitation, ENDS a standup.
Arch's constraint: one deferral predicate (``evaluate_acceptance`` with
``distinguish_defer=True``, read by ``standup_reads_as_deferral``), the #1529
exit stays the generic escape, and the pause-or-end choice is the handler's
(``StandupProcessAdapter.exit_reply``), never a phrase list in the registry.

1. Active interview: "not now" pauses (the defer line); "cancel that" / "end
   standup" / "forget it" drop (the drop line, no "/standup").
2. The "ready to start?" invitation: a bare "no" or a cancel ends ("Okay, no
   standup for now. ..."). Deferrals END there too, with the same line (Arch
   2026-10-15 09:1x, shape A: an unstarted standup has nothing to pause; was
   "pause with the defer line", CXO 08:30 item 2, re-pinned).
3. ``_resume_suspended_standup``'s couldn't-find line: a statement plus an
   instruction, nothing armed.
4. Bare "later" with the resume offer pending: the safety property only.
   Nothing resumed, nothing abandoned, the standup stays SUSPENDED.

Layer: handler. The real ``ProcessRegistry`` + ``StandupProcessAdapter`` + the
real ``StandupConversationHandler`` over the in-memory manager double, and the
real ``IntentService`` seams with an explosive LLM. Not a served run.
"""

import pathlib
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.domain.models import Intent, StandupItem, StandupPartialCapture
from services.intent.intent_service import IntentService
from services.intent_service import standup_preferences as sp
from services.intent_service import verified_inference as vi
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.process import standup_copy
from services.process.adapters import StandupProcessAdapter
from services.process.escape import format_exit_message
from services.process.registry import ProcessRegistry, ProcessType
from services.process.standup_copy import (
    STANDUP_DEFER_PAUSE_REPLY,
    STANDUP_DROP_PAUSED_REPLY,
    STANDUP_DROP_REPLY,
    STANDUP_ESCAPE_PAUSE_REPLY,
    STANDUP_INVITATION_DECLINE_REPLY,
    STANDUP_RESUME_NOT_FOUND_REPLY,
)
from services.shared_types import IntentCategory, StandupConversationState
from services.standup.conversation_handler import StandupConversationHandler
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

_USER = "3f7b8a52-1771-4c00-9e00-000000001771"

# CXO's ruled strings, quoted so a drift in a constant fails loudly.
CXO_DEFER_PAUSE = (
    "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
)
# CXO 2026-10-15 08:35: one pause line for `stop` and a deferral.
CXO_ESCAPE_PAUSE = (
    "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
)
CXO_DROP = "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
CXO_DROP_PAUSED = (
    "Okay, I've dropped your paused standup. Say 'do a standup' whenever you want a fresh one."
)
CXO_INVITATION_END = "Okay, no standup for now. Say 'do a standup' whenever you want one."
CXO_NOT_FOUND = "I couldn't find your paused standup. Say 'do a standup' to start a new one."

STANDUP_SESSION_EXISTS_ASK = (
    "You have a standup conversation in progress. "
    "Would you like to continue where you left off, or start fresh?\n"
    "Reply 'continue' or 'restart'."
)

# Deferrals as THE predicate reads them. "not now" is also a #1529 whole-
# message exit, so it reaches the adapter's exit_reply; the others reach the
# handler (at the invitation) as ordinary turns.
EXIT_DEFERRALS = ["not now", "Not now."]
HANDLER_DEFERRALS = ["not right now", "not today", "maybe later", "not yet"]
EXPLICIT_EXITS = ["cancel that", "end standup", "forget it", "stop the standup", "cancel this"]
GATHERING_STATES = [
    StandupConversationState.GATHERING_YESTERDAY,
    StandupConversationState.GATHERING_TODAY,
    StandupConversationState.GATHERING_BLOCKERS,
]


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
def service(monkeypatch):
    store: dict = {_USER: {}}

    async def _load(user_id):
        return dict(store.get(str(user_id), {}))

    async def _save(user_id, key, value):
        store.setdefault(str(user_id), {})[key] = value
        return True

    from services.intent_service import collaboration_gate

    monkeypatch.setattr(collaboration_gate, "_load_preferences", _load)
    monkeypatch.setattr(collaboration_gate, "_save_preference", _save)
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


class _World:
    """One user's standup world: the in-memory manager, the REAL standup
    handler on it, the real registry with the real adapter, patched in at
    every seam that looks them up."""

    def __init__(self):
        self.manager = FakeStandupConversationManager()
        self.handler = StandupConversationHandler(conversation_manager=self.manager)
        self.registry = ProcessRegistry()
        self.registry.register(StandupProcessAdapter())
        self._patches = [
            patch(
                "services.conversation.conversation_handler._get_standup_components",
                return_value=(self.manager, self.handler),
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

    async def invitation(self, session_id):
        """The standup is just starting: "ready to start?" is on screen."""
        conv = await self.manager.create_conversation(session_id, _USER)
        assert conv.state == StandupConversationState.INITIATED
        return conv

    async def mid_interview(self, session_id, state=StandupConversationState.GATHERING_TODAY):
        """One answer in: yesterday captured, ``state``'s question pending."""
        conv = await self.manager.create_conversation(session_id, _USER)
        await self.manager.transition_state(conv.id, StandupConversationState.GATHERING_YESTERDAY)
        capture = StandupPartialCapture()
        capture.yesterday.append(StandupItem(display="shipped the cut", source="user"))
        await self.manager.update_partial_capture(conv.id, capture)
        for nxt in GATHERING_STATES[1:]:
            if GATHERING_STATES.index(nxt) > GATHERING_STATES.index(state):
                break
            await self.manager.transition_state(conv.id, nxt)
        return conv

    async def conv(self, conv):
        return await self.manager.get_conversation(conv.id)

    async def state(self, conv):
        return (await self.conv(conv)).state

    async def turn(self, session_id, message):
        return await self.registry.check_active_processes(_USER, session_id, message)


def _summary(empty=True):
    summary = MagicMock()
    summary.is_empty.return_value = empty
    summary.to_prose.return_value = "Here's your derived standup."
    summary.to_dict.return_value = {"sections": []}
    return summary


async def _do_a_standup(service, sid):
    intent = Intent(
        category=IntentCategory.STATUS,
        action="get_standup",
        original_message="do a standup",
        confidence=1.0,
    )
    with patch(
        "services.standup.assembler.build_user_standup_summary",
        new=AsyncMock(return_value=_summary(True)),
    ):
        return await service._handle_standup_query(intent, "wf-1771", session_id=sid, user_id=_USER)


def _armed_resume(sid):
    offer = get_or_create_context(sid, user_id=_USER).last_offer
    if offer is not None and offer.offer_type == "process_resume":
        return True, offer.offer_text
    return False, None


async def _reply(service, sid, message):
    pending, question = _armed_resume(sid)
    get_or_create_context(sid, user_id=_USER).last_offer = None  # one-turn memory
    return await service._check_pending_resume_offer(
        _USER, sid, message, resume_offer_pending=pending, resume_offer_question=question
    )


# --- The ruled strings --------------------------------------------------------


class TestRuledStrings:
    def test_every_constant_is_cxos_string(self):
        assert STANDUP_DEFER_PAUSE_REPLY == CXO_DEFER_PAUSE
        assert STANDUP_ESCAPE_PAUSE_REPLY == CXO_ESCAPE_PAUSE  # the landed `stop` line, kept
        assert STANDUP_DROP_REPLY == CXO_DROP
        assert STANDUP_DROP_PAUSED_REPLY == CXO_DROP_PAUSED
        assert STANDUP_INVITATION_DECLINE_REPLY == CXO_INVITATION_END
        assert STANDUP_RESUME_NOT_FOUND_REPLY == CXO_NOT_FOUND

    def test_no_line_teaches_a_slash_command(self):
        lines = [v for k, v in vars(standup_copy).items() if k.isupper()]
        # 7 since #2033 added STANDUP_NOT_RUNNING_REPLY (nothing running).
        assert len(lines) == 7
        assert not [line for line in lines if "/standup" in line]

    def test_the_1529_fallback_copy_is_the_drop_line(self):
        assert format_exit_message(ProcessType.STANDUP) == CXO_DROP

    def test_retired_strings_are_gone_from_the_flow_sources(self):
        root = pathlib.Path(__file__).resolve().parents[4]
        for rel, retired in [
            ("services/process/escape.py", "Say '/standup' whenever"),
            ("services/standup/conversation_handler.py", "Just say 'standup' when you're ready"),
            ("services/intent/intent_service.py", "start a fresh one with /standup"),
        ]:
            assert retired not in (root / rel).read_text(), rel


# --- 1. Active interview ------------------------------------------------------


class TestActiveInterviewDeferralPauses:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("state", GATHERING_STATES)
    @pytest.mark.parametrize("turn", EXIT_DEFERRALS)
    async def test_not_now_suspends_with_the_defer_line(self, state, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid, state)
            result = await w.turn(sid, turn)
            assert result.handled and result.escaped
            assert result.response_message == CXO_DEFER_PAUSE
            after = await w.conv(conv)
            assert after.state == StandupConversationState.SUSPENDED
            # paused, not destroyed: the captured answer survives
            assert [i.display for i in after.partial_capture.yesterday] == ["shipped the cut"]

    @pytest.mark.asyncio
    async def test_paused_by_not_now_is_offered_back_and_resumes(self, service):
        """The defer line's promise ("Just ask when you want to pick it back
        up") holds from this seam too: do a standup -> offer -> continue."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            await w.turn(sid, "not now")
            offered = await _do_a_standup(service, sid)
            assert offered.message == STANDUP_SESSION_EXISTS_ASK
            resumed = await _reply(service, sid, "continue")
            assert resumed is not None
            assert resumed.intent_data["action"] == "standup_conversation_resumed"
            assert await w.state(conv) == StandupConversationState.GATHERING_TODAY

    @pytest.mark.asyncio
    async def test_a_deferral_clause_inside_an_answer_is_still_an_answer(self):
        """Scope guard: the predicate is read only on a turn the #1529 exit
        already claims as a WHOLE-message exit. Mid-interview, "not yet" inside
        an answer is interview content, never a pause."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            result = await w.turn(sid, "PR 1771 review, not yet merged")
            assert result.handled and not result.escaped
            after = await w.conv(conv)
            assert after.state != StandupConversationState.SUSPENDED
            assert "PR 1771 review, not yet merged" in [
                i.display for i in after.partial_capture.today
            ]


class TestActiveInterviewExplicitExitDrops:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", EXPLICIT_EXITS)
    async def test_explicit_exit_abandons_with_the_drop_line(self, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            result = await w.turn(sid, turn)
            assert result.handled and result.escaped
            assert result.response_message == CXO_DROP
            assert "/standup" not in result.response_message
            assert await w.state(conv) == StandupConversationState.ABANDONED

    @pytest.mark.asyncio
    async def test_escape_words_keep_the_landed_pause_line(self):
        """The #888 hatch's PAUSE word ("stop") pauses with CXO's one pause
        line (08:35). END words ("cancel") drop: see
        ``test_escape_end_vs_pause_888.py``."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            result = await w.turn(sid, "stop")
            assert result.response_message == CXO_ESCAPE_PAUSE
            assert await w.state(conv) == StandupConversationState.SUSPENDED


class TestTheChoiceIsTheHandlers:
    """Arch's constraint: the registry holds no deferral words. A process
    without ``exit_reply`` still closes on "not now" (#1529 unchanged), and a
    hook that raises never traps the user."""

    class _Bare:
        process_type = ProcessType.PLANNING

        def __init__(self):
            self.closed = False
            self.suspended = False

        async def check_active(self, user_id, session_id):
            return True

        async def handle_message(self, user_id, session_id, message):  # pragma: no cover
            raise AssertionError("an exit never reaches the flow")

        async def suspend(self, user_id, session_id):
            self.suspended = True

        async def close(self, user_id, session_id):
            self.closed = True

        async def has_suspended_session(self, user_id):
            return None

    @pytest.mark.asyncio
    async def test_no_hook_means_the_generic_close(self):
        registry = ProcessRegistry()
        bare = self._Bare()
        registry.register(bare)
        result = await registry.check_active_processes(_USER, "s", "not now")
        assert result.escaped and bare.closed and not bare.suspended

    @pytest.mark.asyncio
    async def test_a_raising_hook_falls_back_to_the_generic_close(self):
        registry = ProcessRegistry()
        bare = self._Bare()

        async def _boom(user_id, session_id, message):
            raise RuntimeError("boom")

        bare.exit_reply = _boom
        registry.register(bare)
        result = await registry.check_active_processes(_USER, "s", "not now")
        assert result.escaped and bare.closed
        assert result.response_message == format_exit_message(ProcessType.PLANNING)

    def test_registry_source_names_no_deferral(self):
        root = pathlib.Path(__file__).resolve().parents[4]
        src = (root / "services/process/registry.py").read_text()
        assert "distinguish_defer" not in src
        assert "maybe later" not in src


# --- 2. The invitation ("ready to start?") ------------------------------------


class TestInvitation:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", EXIT_DEFERRALS + HANDLER_DEFERRALS)
    async def test_deferral_ends_with_the_invitation_line(self, turn):
        """Re-pinned (Arch 2026-10-15 09:1x, shape A): a deferral at the
        invitation ENDS with the invitation line and leaves nothing to offer
        back. Was: pauses with the defer line (CXO 08:30 item 2), which left
        an empty SUSPENDED standup the next ``do a standup`` offered back."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            result = await w.turn(sid, turn)
            assert result.handled
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == StandupConversationState.ABANDONED
            assert await w.registry.check_suspended_processes(_USER) is None

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        ["no", "nope", "No.", "no, not now", "cancel that", "end standup", "please cancel"],
    )
    async def test_no_or_cancel_ends_with_the_invitation_line(self, turn):
        """ "please cancel" is back on this list (1771 politeness, Arch
        2026-10-15): the #888 hatch strips one "please", so it is ``cancel``.
        Was: a known miss that started the interview (f76a307ecb), after the
        anywhere word set (``cancel``) was dropped."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            result = await w.turn(sid, turn)
            assert result.handled
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == StandupConversationState.ABANDONED

    @pytest.mark.asyncio
    async def test_yes_still_starts_the_interview(self):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            await w.turn(sid, "yes, let's do it")
            assert await w.state(conv) == StandupConversationState.GATHERING_YESTERDAY

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["cancel", "stop", "quit", "never mind", "exit"])
    async def test_bare_escape_words_end_at_the_invitation(self, turn):
        """OPEN POINT closed (Arch 2026-10-15): bare "cancel" (and every #888
        escape word) at the invitation ENDS with the invitation line. The
        hatch is not carved: it still intercepts first; the standup adapter's
        ``suspend()`` closes an unstarted standup, and its copy hooks read the
        state. Was: "cancel" pauses with the escape line (the landed
        behaviour, pinned as an open point). "skip" left this list with the
        #888 word map (2026-10-15): it is no longer an escape word; its
        invitation pin is ``test_escape_end_vs_pause_888``
        ``TestSkipAtTheInvitationLeaves`` (same line, via the handler)."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            result = await w.turn(sid, turn)
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == StandupConversationState.ABANDONED

    @pytest.mark.asyncio
    async def test_bare_later_is_the_known_miss_and_ends(self):
        """KNOWN MISS, pinned as it stands (Arch 10-15: bare "later" is not a
        DEFER phrasing, no new row). At the invitation it ENDS through the
        handler's whole-message ``later`` check (Arch 10:1x: anchored, was a
        word matched anywhere in the turn). CXO's item 2 names "later" as a
        pause; the accepted fix shape is Arch's exact full-message entry, on
        CXO's served read."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            result = await w.turn(sid, "later")
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == StandupConversationState.ABANDONED

    @pytest.mark.asyncio
    async def test_please_cancel_is_cancel_at_the_hatch(self):
        """Was ``test_please_cancel_is_a_known_miss_and_starts_the_interview``
        (f76a307ecb). CXO 10:25 ruled it must leave; Arch 10:4x put it at the
        #888 hatch (one "please" stripped, then the exact-match lookup), not
        in the #1529 exits, so it is the hatch's END and never reaches the
        handler."""
        sid = str(uuid4())
        with _World() as w:
            conv = await w.invitation(sid)
            result = await w.turn(sid, "please cancel")
            assert result.escaped
            assert result.response_message == CXO_INVITATION_END
            assert await w.state(conv) == StandupConversationState.ABANDONED


# --- 3. The couldn't-find line ------------------------------------------------


class TestResumeNotFound:
    @pytest.mark.asyncio
    async def test_statement_plus_instruction_nothing_armed(self, service):
        sid = str(uuid4())
        with _World():
            result = await service._resume_suspended_standup(_USER, sid)
        assert result.message == CXO_NOT_FOUND
        assert result.intent_data["action"] == "suspended_session_resume_failed"
        assert "?" not in result.message
        assert _armed_resume(sid) == (False, None)


# --- 4. Bare "later" at the resume offer --------------------------------------


class TestBareLaterAtTheResumeOffer:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["later", "later.", "Later"])
    async def test_resumes_nothing_abandons_nothing_stays_suspended(self, service, turn):
        sid = str(uuid4())
        with _World() as w:
            conv = await w.mid_interview(sid)
            await w.turn(sid, "stop")
            offered = await _do_a_standup(service, sid)
            assert offered.message == STANDUP_SESSION_EXISTS_ASK
            assert _armed_resume(sid)[0] is True  # the offer IS pending
            with (
                patch.object(service, "_resume_suspended_standup", new=AsyncMock()) as resume,
                patch.object(service, "_abandon_suspended_standup", new=AsyncMock()) as abandon,
            ):
                result = await _reply(service, sid, turn)
            assert result is None  # normal processing answers the turn
            resume.assert_not_called()
            abandon.assert_not_called()
            after = await w.conv(conv)
            assert after.state == StandupConversationState.SUSPENDED
            assert [i.display for i in after.partial_capture.yesterday] == ["shipped the cut"]
