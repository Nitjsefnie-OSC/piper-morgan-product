"""#2091 — a day the calendar parser cannot read refuses; it never answers for today.

xian, alpha e801b1a309, 2026-10-19 13:43: "what's my agenda Thursday?" and "how about on
Thursday?" both got "You have no meetings scheduled for today." CXO: Class 3 (the reply
states something false about what it did); interim words until the router's ``when`` is
resolved in code (Arch): "I can show today, tomorrow or this week, but I can't look up a
particular weekday. Want one of those?"

LAYER: the parser helper directly, and the handler through its method with the calendar
router replaced at its one seam (authenticated, no events). DENOMINATOR: the seven weekday
words, eleven month words, the four known modifiers, and xian's two turns.
"""

import logging
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.temporal_utils import (
    MONTH_WORDS,
    UNRESOLVED_DAY_REFUSAL,
    WEEKDAY_WORDS,
    unresolved_day_reference,
)
from services.shared_types import IntentCategory

ROUTER = "services.integrations.calendar.calendar_integration_router.CalendarIntegrationRouter"


class TestUnresolvedDayReference:
    @pytest.mark.parametrize("day", WEEKDAY_WORDS)
    def test_every_weekday_word_is_unresolved(self, day):
        assert unresolved_day_reference(f"what's my agenda {day.title()}?") == day

    @pytest.mark.parametrize("month", MONTH_WORDS)
    def test_every_month_word_is_unresolved(self, month):
        assert unresolved_day_reference(f"meetings on {month.title()} 23") == month

    def test_xians_follow_up_is_unresolved_too(self):
        assert unresolved_day_reference("how about on Thursday?") == "thursday"

    @pytest.mark.parametrize(
        "message",
        [
            "what's my agenda today?",
            "meetings tomorrow",
            "how much time in meetings this week",
            "next week",
            "what's my agenda?",
        ],
    )
    def test_known_modifiers_and_bare_asks_resolve(self, message):
        assert unresolved_day_reference(message) is None

    def test_may_is_not_a_month_here(self):
        assert unresolved_day_reference("may I see my meetings") is None

    def test_empty_and_none(self):
        assert unresolved_day_reference("") is None and unresolved_day_reference(None) is None


def _service() -> IntentService:
    svc = IntentService.__new__(IntentService)
    svc.logger = MagicMock(spec=logging.Logger)
    return svc


def _intent(message: str) -> Intent:
    return Intent(
        original_message=message,
        category=IntentCategory.QUERY,
        action="meeting_time",
        confidence=0.9,
        context={"original_message": message},
    )


def _router(events=None):
    router = MagicMock()
    router.authenticate = AsyncMock(return_value=True)
    router.get_events_in_range = AsyncMock(return_value=events or [])
    return router


class TestMeetingTimeHandlerRefuses:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("message", ["what's my agenda Thursday?", "how about on Thursday?"])
    async def test_a_weekday_question_gets_the_refusal_never_today(self, message):
        router = _router()
        with patch(ROUTER, return_value=router):
            result = await _service()._handle_meeting_time_query(_intent(message), "wf-1")
        assert result.message == UNRESOLVED_DAY_REFUSAL
        assert "today" not in result.message.lower().replace("today, tomorrow", "")
        assert result.requires_clarification is True
        assert result.implemented is False
        assert result.intent_data["unresolved_day_reference"] == "thursday"
        router.get_events_in_range.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_a_today_question_still_answers_for_today(self):
        router = _router()
        with patch(ROUTER, return_value=router):
            result = await _service()._handle_meeting_time_query(
                _intent("what's my agenda today?"), "wf-1"
            )
        assert result.message == "You have no meetings scheduled for today."
        router.get_events_in_range.assert_awaited_once()
