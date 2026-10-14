"""#1771 -- DEFER tier in the acceptance contract (#1739).

"not now" / "maybe later" are deferrals, not refusals. The shared DECLINE
vocabulary used to swallow them, which was harmless where a decline only
cancels a one-turn offer and wrong at the resume-offer seam (#1769), where
DECLINE abandons the suspended standup. Contract after #1771:

- ``evaluate_acceptance`` returns DEFER for the deferral phrasings.
- Every adopted seam reads DEFER as DECLINE (``defer_as_decline``) -- their
  old behavior -- EXCEPT the resume-offer seam, where DEFER leaves the flow
  SUSPENDED (nothing abandoned) and says so in one line.
"""

import ast
import pathlib
import re
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.intent_service import delete_todo_pick as dtp
from services.intent_service.acceptance import (
    AcceptanceVerdict,
    declared_axes_for_workflow,
    defer_as_decline,
    evaluate_acceptance,
)
from services.intent_service.soft_invocation import (
    DECLINE_PATTERNS,
    DEFER_PATTERNS,
    detect_confirm_response,
    detect_offer_response,
    is_bare_decline,
)
from services.process.registry import ProcessType, SuspendedInfo
from services.shared_types import EffectClass, Outwardness

RESUME_ASK = "Welcome back! Your standup was paused. Would you like to continue, or start fresh?"
DEFERRALS = ["not now", "not right now", "not today", "maybe later"]


@pytest.mark.parametrize("effect", [EffectClass.READ, EffectClass.DESTRUCTIVE])
class TestVerdict:
    @pytest.mark.parametrize("turn", DEFERRALS)
    def test_deferral_phrasings_are_defer(self, turn, effect):
        assert evaluate_acceptance(turn, effect=effect, armed_question=RESUME_ASK) is (
            AcceptanceVerdict.DEFER
        )

    @pytest.mark.parametrize("turn", ["no", "no thanks", "nope", "never mind", "no, not now"])
    def test_refusals_stay_decline(self, turn, effect):
        assert evaluate_acceptance(turn, effect=effect, armed_question=RESUME_ASK) is (
            AcceptanceVerdict.DECLINE
        )


class TestVocabulary:
    def test_deferrals_live_in_defer_patterns_only(self):
        for turn in DEFERRALS:
            assert any(p.search(turn) for p in DEFER_PATTERNS)
            assert not any(p.search(turn) for p in DECLINE_PATTERNS)

    def test_defer_as_decline_collapses_only_defer(self):
        assert defer_as_decline(AcceptanceVerdict.DEFER) is AcceptanceVerdict.DECLINE
        for v in (
            AcceptanceVerdict.ACCEPT,
            AcceptanceVerdict.DECLINE,
            AcceptanceVerdict.PASS,
            AcceptanceVerdict.STATE_QUESTION,
        ):
            assert defer_as_decline(v) is v

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
        assert result is not None and result.message == RESUME_DEFER_REPLY
        assert result.intent_data["action"] == "suspended_session_deferred"
        resume.assert_not_called()
        abandon.assert_not_called()


class TestOtherSeamsReadDeferAsDecline:
    @pytest.mark.asyncio
    async def test_delete_pick_seam_defer_matches_decline(self):
        """Drives the real predicate through a real adopted seam."""
        axes = declared_axes_for_workflow(dtp.CLARIFY_DELETE_PICK_WORKFLOW)
        assert axes is not None
        offer = {
            "pending_action": {
                "kind": dtp.DELETE_PICK_KIND,
                "user_id": "u1",
                "pick_ids": ["a", "b"],
                "pick_texts": ["one", "two"],
            },
            "question": "Which one?",
        }
        outcomes = {}
        for turn in ("no", "not now"):
            with patch.object(dtp, "logger") as log:
                result = await dtp.handle_delete_todo_pick_turn(
                    offer, turn, session_id="s", user_id="u1", intent_service=MagicMock()
                )
            events = [c.args[0] for c in log.info.call_args_list]
            outcomes[turn] = (result, events)
        assert outcomes["not now"] == outcomes["no"]
        assert "delete_todo_pick_declined" in outcomes["not now"][1]

    def test_every_other_call_site_collapses_defer(self):
        """Structural: all production verdict consumers wrap the predicate in
        ``defer_as_decline`` except the resume seam and the one STATE_QUESTION-
        only probe (reminder_clear correction), which never reads DECLINE."""
        root = pathlib.Path(__file__).resolve().parents[4]
        unwrapped = []
        for top in ("services", "web"):
            for path in (root / top).rglob("*.py"):
                if path.name == "acceptance.py":
                    continue
                src = path.read_text()
                if "evaluate_acceptance(" not in src:
                    continue
                tree = ast.parse(src)
                wrapped = {
                    id(n.args[0])
                    for n in ast.walk(tree)
                    if isinstance(n, ast.Call)
                    and getattr(n.func, "id", None) == "defer_as_decline"
                    and n.args
                }
                for n in ast.walk(tree):
                    if (
                        isinstance(n, ast.Call)
                        and getattr(n.func, "id", None) == "evaluate_acceptance"
                        and id(n) not in wrapped
                    ):
                        unwrapped.append(f"{path.relative_to(root)}:{n.lineno}")
        # Allowed: resume seam (3 calls: raw verdict by design), the
        # detect_confirm_response alias (maps DEFER itself), and the
        # STATE_QUESTION-only probe in reminder_clear.
        allowed = re.compile(
            r"services/intent/intent_service\.py|services/intent_service/soft_invocation\.py"
            r"|services/intent_service/reminder_clear\.py"
        )
        stray = [u for u in unwrapped if not allowed.match(u)]
        assert not stray, f"unwrapped evaluate_acceptance call sites: {stray}"
