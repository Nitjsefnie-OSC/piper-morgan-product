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


class TestAfterDeferTheStandupIsReachableOnlyByTheTaughtCommands:
    """CXO's honesty condition on the DEFER reply ("Just ask when you want to
    pick it back up"): pinned FROM SOURCE, not assumed.

    Finding: a fresh standup ASK ("do a standup", "show my standup") does NOT
    resume the suspended flow and does NOT re-arm the resume offer --
    ``_start_standup_conversation`` looks up the session conversation with
    ``include_suspended=False``, finds nothing, and starts a NEW conversation
    (the SUSPENDED one is left in place). The suspended flow comes back via
    (a) the greeting re-offer, or (b) the taught resume commands handled at
    ``_check_pending_resume_offer`` with no offer pending: exactly "resume",
    "continue", "pick it up", "let's continue".
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

    @pytest.mark.asyncio
    async def test_starting_a_standup_creates_a_new_conversation_and_does_not_rearm(self):
        """The start path never sees the SUSPENDED conversation (the manager's
        default lookup excludes it), so it starts fresh and arms no offer."""
        service = _service()
        manager = MagicMock()
        manager.get_conversation_by_session = AsyncMock(return_value=None)
        handler = MagicMock()
        handler.start_conversation = AsyncMock(
            return_value=MagicMock(message="Ready?", state=MagicMock(value="initiated"))
        )
        with (
            patch(
                "services.conversation.conversation_handler._get_standup_components",
                return_value=(manager, handler),
            ),
            patch.object(service, "_arm_resume_offer") as arm,
            patch.object(service, "_resume_suspended_standup", new_callable=AsyncMock) as resume,
        ):
            await service._start_standup_conversation("user-1", str(uuid4()))
        handler.start_conversation.assert_awaited_once()
        arm.assert_not_called()
        resume.assert_not_called()
        # The lookup it made is the default one, which excludes SUSPENDED.
        assert "include_suspended" not in manager.get_conversation_by_session.call_args.kwargs
