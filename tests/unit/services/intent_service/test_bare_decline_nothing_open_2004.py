"""#2004 — a bare "never mind" with nothing open gets a short acknowledgement
and nothing else. Served on alpha b713b91cb5 (Web, 2026-10-13): after the
#1987 gone-row line, `never mind` → "Got it, leaving it alone." plus an
unrequested todo list — the floor assembled context and composed both.

Layer (m-43): the shared decline vocabulary on strings; the gate method
``IntentService._bare_decline_nothing_open`` on stub Intents (no LLM, no
DB, no floor); and a source pin that the gate sits BEFORE the floor call
at the Action Gate. The served check is owed on the card after the next
promotion.
"""

from __future__ import annotations

import inspect
from unittest.mock import MagicMock

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentProcessingResult, IntentService
from services.intent_service.soft_invocation import (
    DECLINE_PATTERNS,
    FULL_MESSAGE_DECLINE_RE,
    is_bare_decline,
)
from services.shared_types import IntentCategory
from services.ui_messages.keyless_pleasantry import BARE_DECLINE_NOTHING_OPEN


class TestVocabulary:
    @pytest.mark.parametrize(
        "text",
        [
            "never mind",
            "Never mind.",
            "never mind!",
            "no thanks",
            "nope",
            "skip",
            "not now",
            " no ",
        ],
    )
    def test_bare_declines(self, text):
        assert is_bare_decline(text)

    @pytest.mark.parametrize(
        "text",
        [
            "never mind, show my todos",
            "no, delete the second one",
            "just wondering what's due",  # the unanchored prose row must NOT count
            "maybe later",  # same
            "I'm fine with that plan",
            "",
            "   ",
        ],
    )
    def test_not_bare(self, text):
        assert not is_bare_decline(text)

    def test_the_named_row_is_the_first_shared_decline_row(self):
        """One vocabulary: the armed seams decline on exactly this row too."""
        assert DECLINE_PATTERNS[0] is FULL_MESSAGE_DECLINE_RE


def _intent(message, category=IntentCategory.CONVERSATION, action="general_chat", context=None):
    return Intent(
        category=category,
        action=action,
        original_message=message,
        confidence=0.9,
        context=dict(context or {}),
    )


@pytest.fixture
def service():
    svc = IntentService.__new__(IntentService)
    svc.logger = MagicMock()
    return svc


class TestGate:
    def test_bare_never_mind_nothing_open_is_the_short_ack(self, service):
        out = service._bare_decline_nothing_open(_intent("never mind"))
        assert isinstance(out, IntentProcessingResult)
        assert out.success is True
        assert out.message == BARE_DECLINE_NOTHING_OPEN
        assert out.message.count("\n") == 0 and len(out.message) < 40  # short, one line
        assert out.intent_data["bare_decline_nothing_open"] is True
        assert out.requires_clarification is False

    def test_unknown_category_too(self, service):
        out = service._bare_decline_nothing_open(
            _intent("no thanks", IntentCategory.UNKNOWN, "unknown")
        )
        assert out is not None and out.message == BARE_DECLINE_NOTHING_OPEN

    def test_armed_turn_is_left_to_its_seam(self, service):
        out = service._bare_decline_nothing_open(
            _intent("never mind", context={"armed_offer_rail": "WorkflowOffer"})
        )
        assert out is None

    @pytest.mark.parametrize(
        "text", ["never mind, show my todos", "what's due today?", "no, the first one"]
    )
    def test_compound_or_prose_goes_to_the_floor(self, service, text):
        assert service._bare_decline_nothing_open(_intent(text)) is None

    def test_other_categories_untouched(self, service):
        assert (
            service._bare_decline_nothing_open(
                _intent("skip", IntentCategory.EXECUTION, "delete_todo")
            )
            is None
        )

    def test_message_falls_back_to_context(self, service):
        i = _intent("", context={"original_message": "never mind"})
        i.original_message = ""
        assert service._bare_decline_nothing_open(i) is not None


class TestSourcePin:
    def test_gate_sits_before_the_floor_call_at_the_action_gate(self):
        import services.intent.intent_service as mod

        src = inspect.getsource(mod)
        gate = src.index("self._bare_decline_nothing_open(intent)")
        floor = src.index("await self._handle_floor_with_context(", gate)
        assert gate < floor
        # inside the floor-routing branch, not before the whole gate
        assert src.rindex("if self._should_route_to_floor(intent):", 0, gate) > 0
