"""#1771 -- DEFER tier in the acceptance contract (#1739), opt-in at the predicate.

"not now" / "maybe later" are deferrals, not refusals. Arch's shape: the
predicate returns DECLINE for them by DEFAULT (byte-identical to pre-#1771),
and DEFER only when the caller passes ``distinguish_defer=True``. Only the
resume-offer seam (#1769) does, because only there DECLINE abandons a
suspended standup; DEFER leaves it SUSPENDED. A seam added later cannot
silently stop declining "not now".
"""

import ast
import pathlib
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.intent_service.acceptance import AcceptanceVerdict, evaluate_acceptance
from services.intent_service.soft_invocation import (
    DECLINE_PATTERNS,
    DEFER_PATTERNS,
    detect_confirm_response,
    detect_offer_response,
    is_bare_decline,
)
from services.process.registry import ProcessType, SuspendedInfo
from services.shared_types import EffectClass

RESUME_ASK = "Welcome back! Your standup was paused. Would you like to continue, or start fresh?"
DEFERRALS = ["not now", "not right now", "not today", "maybe later"]


@pytest.mark.parametrize("effect", [EffectClass.READ, EffectClass.DESTRUCTIVE])
class TestVerdict:
    @pytest.mark.parametrize("turn", DEFERRALS)
    def test_default_call_declines_deferrals(self, turn, effect):
        verdict = evaluate_acceptance(turn, effect=effect, armed_question=RESUME_ASK)
        assert verdict is AcceptanceVerdict.DECLINE

    @pytest.mark.parametrize("turn", DEFERRALS)
    def test_distinguish_defer_returns_defer(self, turn, effect):
        verdict = evaluate_acceptance(
            turn, effect=effect, armed_question=RESUME_ASK, distinguish_defer=True
        )
        assert verdict is AcceptanceVerdict.DEFER

    @pytest.mark.parametrize("turn", ["no", "no thanks", "nope", "never mind", "no, not now"])
    @pytest.mark.parametrize("distinguish", [False, True])
    def test_refusals_stay_decline(self, turn, effect, distinguish):
        verdict = evaluate_acceptance(
            turn, effect=effect, armed_question=RESUME_ASK, distinguish_defer=distinguish
        )
        assert verdict is AcceptanceVerdict.DECLINE


class TestVocabulary:
    def test_deferrals_live_in_defer_patterns_only(self):
        for turn in DEFERRALS:
            assert any(p.search(turn) for p in DEFER_PATTERNS)
            assert not any(p.search(turn) for p in DECLINE_PATTERNS)

    @pytest.mark.parametrize("turn", DEFERRALS)
    def test_legacy_detectors_still_read_decline(self, turn):
        assert detect_offer_response(turn) == "decline"
        assert detect_confirm_response(turn) == "decline"

    @pytest.mark.parametrize("turn", ["not now", "Not right now."])
    def test_bare_deferral_still_bare_for_nothing_open(self, turn):
        assert is_bare_decline(turn)


def _service():
    from services.intent.intent_service import IntentService

    return IntentService()


class TestResumeSeamKeepsFlowSuspended:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", DEFERRALS)
    async def test_defer_does_not_abandon_or_resume(self, turn):
        from services.intent.intent_service import RESUME_DEFER_REPLY

        service = _service()
        suspended = SuspendedInfo(
            process_type=ProcessType.STANDUP,
            suspended_at=datetime.now(),
            description="Your standup was paused.",
        )
        with (
            patch("services.intent.intent_service.get_process_registry") as reg_fn,
            patch.object(service, "_resume_suspended_standup", new_callable=AsyncMock) as resume,
            patch.object(service, "_abandon_suspended_standup", new_callable=AsyncMock) as abandon,
        ):
            reg = MagicMock()
            reg.check_suspended_processes = AsyncMock(return_value=suspended)
            reg_fn.return_value = reg
            result = await service._check_pending_resume_offer(
                "user-1",
                str(uuid4()),
                turn,
                resume_offer_pending=True,
                resume_offer_question=RESUME_ASK,
            )
        assert result is not None and result.message == RESUME_DEFER_REPLY  # CXO-pending copy
        assert result.intent_data["action"] == "suspended_session_deferred"
        resume.assert_not_called()
        abandon.assert_not_called()


class TestNoOtherSeamOptsIn:
    def test_only_the_resume_seam_opts_into_defer(self):
        """Structural: no production `evaluate_acceptance(` call passes
        ``distinguish_defer=True`` except `_check_pending_resume_offer`."""
        root = pathlib.Path(__file__).resolve().parents[4]
        opted = set()
        for top in ("services", "web"):
            for path in (root / top).rglob("*.py"):
                src = path.read_text()
                if "distinguish_defer" not in src:
                    continue
                for fn in ast.walk(ast.parse(src)):
                    if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    for n in ast.walk(fn):
                        if (
                            isinstance(n, ast.Call)
                            and getattr(n.func, "id", None) == "evaluate_acceptance"
                            and any(
                                k.arg == "distinguish_defer"
                                and not (
                                    isinstance(k.value, ast.Constant) and k.value.value is False
                                )
                                for k in n.keywords
                            )
                        ):
                            opted.add((str(path.relative_to(root)), fn.name))
        assert opted == {("services/intent/intent_service.py", "_check_pending_resume_offer")}


class TestAfterDeferTheStandupIsReachable:
    """CXO's honesty condition on the DEFER reply ("Just ask when you want to
    pick it back up"): pinned FROM SOURCE, not assumed.

    2007: a fresh standup ASK reaches ``_start_standup_conversation``, whose
    lookup passes ``include_suspended=True``; a SUSPENDED standup therefore
    takes the existing "continue where you left off, or start fresh?" branch
    and ARMS the resume offer instead of being orphaned by a new
    conversation. The taught resume commands ("resume", "continue", "pick it
    up", "let's continue") also resume at ``_check_pending_resume_offer``.
    """

    @staticmethod
    def _suspended():
        return SuspendedInfo(
            process_type=ProcessType.STANDUP,
            suspended_at=datetime.now(),
            description="Your standup was paused.",
        )

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["resume", "continue", "pick it up", "let's continue"])
    async def test_taught_commands_resume_with_no_offer_pending(self, turn):
        service = _service()
        with (
            patch("services.intent.intent_service.get_process_registry") as reg_fn,
            patch.object(
                service,
                "_resume_suspended_standup",
                new_callable=AsyncMock,
                return_value=MagicMock(success=True),
            ) as resume,
        ):
            reg = MagicMock()
            reg.check_suspended_processes = AsyncMock(return_value=self._suspended())
            reg_fn.return_value = reg
            result = await service._check_pending_resume_offer(
                "user-1", str(uuid4()), turn, resume_offer_pending=False
            )
        assert result is not None
        resume.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "turn",
        ["show my standup", "do a standup", "let's do a standup", "what's on my standup today"],
    )
    async def test_a_new_standup_ask_does_not_resume_at_the_resume_seam(self, turn):
        service = _service()
        with (
            patch("services.intent.intent_service.get_process_registry") as reg_fn,
            patch.object(service, "_resume_suspended_standup", new_callable=AsyncMock) as resume,
            patch.object(service, "_abandon_suspended_standup", new_callable=AsyncMock) as aband,
        ):
            reg = MagicMock()
            reg.check_suspended_processes = AsyncMock(return_value=self._suspended())
            reg_fn.return_value = reg
            result = await service._check_pending_resume_offer(
                "user-1", str(uuid4()), turn, resume_offer_pending=False
            )
        assert result is None
        resume.assert_not_called()
        aband.assert_not_called()

    @staticmethod
    def _start_harness(service, existing):
        manager = MagicMock()
        manager.get_conversation_by_session = AsyncMock(return_value=existing)
        handler = MagicMock()
        handler.start_conversation = AsyncMock(
            return_value=MagicMock(message="Ready?", state=MagicMock(value="initiated"))
        )
        return manager, handler

    @pytest.mark.asyncio
    @pytest.mark.parametrize("state_name", ["SUSPENDED", "GATHERING_YESTERDAY"])
    async def test_existing_standup_offers_continue_or_restart_and_arms(self, state_name):
        """2007: SUSPENDED (and ACTIVE, unchanged) -> the continue/restart ask,
        armed, and no new conversation is created."""
        from services.shared_types import StandupConversationState

        service = _service()
        existing = MagicMock(state=getattr(StandupConversationState, state_name), id="c1")
        manager, handler = self._start_harness(service, existing)
        with (
            patch(
                "services.conversation.conversation_handler._get_standup_components",
                return_value=(manager, handler),
            ),
            patch.object(service, "_arm_resume_offer") as arm,
        ):
            result = await service._start_standup_conversation("user-1", "sess-1")
        assert result.intent_data["action"] == "standup_session_exists"
        arm.assert_called_once()
        handler.start_conversation.assert_not_called()
        manager.get_conversation_by_session.assert_awaited_once_with(
            "sess-1", include_suspended=True
        )

    @pytest.mark.asyncio
    async def test_no_standup_at_all_still_starts_one(self):
        service = _service()
        manager, handler = self._start_harness(service, None)
        with (
            patch(
                "services.conversation.conversation_handler._get_standup_components",
                return_value=(manager, handler),
            ),
            patch.object(service, "_arm_resume_offer") as arm,
        ):
            await service._start_standup_conversation("user-1", "sess-1")
        handler.start_conversation.assert_awaited_once()
        arm.assert_not_called()

    @pytest.mark.asyncio
    async def test_real_manager_lookup_sees_a_suspended_conversation_only_when_asked(self):
        """The lookup contract 2007 leans on, against the REAL manager filter."""
        from services.shared_types import StandupConversationState
        from services.standup.conversation_manager import StandupConversationManager

        conv = MagicMock(state=StandupConversationState.SUSPENDED)
        mgr = StandupConversationManager.__new__(StandupConversationManager)
        repo = MagicMock()
        repo.get_by_session_id = AsyncMock(return_value=conv)
        cm = MagicMock()
        cm.__aenter__ = AsyncMock(return_value=MagicMock())
        cm.__aexit__ = AsyncMock(return_value=False)
        mgr._session_scope = lambda: cm
        mgr._new_repo = lambda _s: repo
        assert await mgr.get_conversation_by_session("s") is None
        assert await mgr.get_conversation_by_session("s", include_suspended=True) is conv


class TestFlowExitBypassKeyedOnThePredicate:
    """#1529's exit vocabulary stays ignorant of 'defer'; the resume seam
    bypasses the exit exactly when the predicate says DEFER (offer pending)."""

    @staticmethod
    def _run(turn, pending):
        service = _service()
        suspended = SuspendedInfo(
            process_type=ProcessType.STANDUP,
            suspended_at=datetime.now(),
            description="Your standup was paused.",
        )

        async def go():
            with (
                patch("services.intent.intent_service.get_process_registry") as reg_fn,
                patch.object(service, "_resume_suspended_standup", new_callable=AsyncMock),
                patch.object(
                    service,
                    "_abandon_suspended_standup",
                    new_callable=AsyncMock,
                    return_value=MagicMock(success=True),
                ) as abandon,
            ):
                reg = MagicMock()
                reg.check_suspended_processes = AsyncMock(return_value=suspended)
                reg_fn.return_value = reg
                result = await service._check_pending_resume_offer(
                    "user-1",
                    str(uuid4()),
                    turn,
                    resume_offer_pending=pending,
                    resume_offer_question=RESUME_ASK if pending else None,
                )
            return result, abandon

        return go()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", DEFERRALS)
    async def test_all_defer_phrasings_bypass_the_exit_with_offer_pending(self, turn):
        from services.intent.intent_service import RESUME_DEFER_REPLY

        result, abandon = await self._run(turn, True)
        assert result.message == RESUME_DEFER_REPLY
        abandon.assert_not_called()

    @pytest.mark.asyncio
    async def test_no_does_not_bypass_it_declines_and_abandons(self):
        result, abandon = await self._run("no", True)
        assert result is not None
        abandon.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", DEFERRALS)
    async def test_no_offer_pending_deferral_never_abandons(self, turn):
        """#1771 second seam (Web, served 2026-10-14 21:42): this pin used to
        read "no offer pending: a bare 'not now' stays the #1529 exit" and
        asserted the abandon, which is the defect Web served ("The paused
        standup has been cleared"). A deferral protects a SUSPENDED standup
        with or without an offer: nothing abandoned, the turn falls through.
        (An ACTIVE flow's "not now" is the registry's #1529 exit, another
        seam, unchanged.)"""
        result, abandon = await self._run(turn, False)
        assert result is None
        abandon.assert_not_called()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("turn", ["cancel that", "forget it", "start over", "end standup"])
    async def test_no_offer_pending_explicit_cancel_still_abandons(self, turn):
        result, abandon = await self._run(turn, False)
        assert result is not None
        abandon.assert_called_once()
