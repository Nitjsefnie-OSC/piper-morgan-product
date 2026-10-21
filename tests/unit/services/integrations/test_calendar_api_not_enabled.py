"""A Google 403 "accessNotConfigured" (the Calendar API not enabled for the app's
project) is its own class, said as a setup step on our side, and the Settings
probe logs the class (never the text or the token).

2026-10-21: xian's connect on the "Piper Morgan (Alpha)" project passed consent and
the first read came back "Google refused the calendar read (error)", with no server
line to read.
"""

from unittest.mock import patch

import pytest

from services.integrations.calendar.read_errors import classify_calendar_read_error
from services.intent.intent_service import calendar_read_failed_line


class _HttpError(Exception):
    pass


ACCESS_NOT_CONFIGURED = _HttpError(
    "<HttpError 403 when requesting https://www.googleapis.com/calendar/v3/calendars/primary/events "
    'returned "Google Calendar API has not been used in project 43539582958 before or it is '
    "disabled. Enable it by visiting https://console.developers.google.com/apis/api/"
    'calendar-json.googleapis.com/overview?project=43539582958 then retry." '
    'Details: [{"reason": "accessNotConfigured"}]>'
)


def test_access_not_configured_is_its_own_class():
    assert classify_calendar_read_error(ACCESS_NOT_CONFIGURED) == "api_not_enabled"


def test_the_other_classes_are_unchanged():
    assert (
        classify_calendar_read_error(
            _HttpError("403 Request had insufficient authentication scopes")
        )
        == "insufficient_scope"
    )
    assert classify_calendar_read_error(_HttpError("401 invalid_grant")) == "unauthorized"
    assert classify_calendar_read_error(_HttpError("404 Not Found")) == "not_found"
    assert classify_calendar_read_error(_HttpError("something else")) == "error"


def test_the_chat_line_names_a_setup_step_on_our_side():
    line = calendar_read_failed_line("api_not_enabled")
    assert "Calendar API isn't switched on" in line
    assert "on our side" in line


@pytest.mark.asyncio
async def test_the_settings_probe_logs_the_class_not_the_text():
    """Exec's ask (10-21): the server log for the read. The probe now logs the class
    and the exception type; never the text (ids, URLs) and never the token."""
    from services.integrations.calendar import oauth_handler

    async def _raise(fn, *a, **k):
        raise ACCESS_NOT_CONFIGURED

    with (
        patch.object(oauth_handler, "logger") as log,
        patch("asyncio.to_thread", new=_raise),
    ):
        result = await oauth_handler.probe_calendar_read("ya29.not-a-real-token")
    assert result == "api_not_enabled"
    log.warning.assert_called_once()
    args, kwargs = log.warning.call_args
    assert args[0] == "calendar_read_probe_failed"
    assert kwargs["error_class"] == "api_not_enabled"
    assert kwargs["exception_type"] == "_HttpError"
    assert "ya29" not in str(kwargs) and "43539582958" not in str(kwargs)
