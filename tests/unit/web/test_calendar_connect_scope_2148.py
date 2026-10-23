"""#2148: a Google grant without calendar access is not 'Calendar Connected' (CXO 10-23).

Google's consent page for the unverified app shows the calendar scope as a box
that starts unticked. The callbacks (Settings and the setup wizard) read the
granted scopes from the token response: missing → store nothing and say so in
CXO's words; unreadable → no success state; present → unchanged.
"""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.integrations.calendar.oauth_handler import (
    CALENDAR_READ_SCOPE,
    CALENDAR_SCOPE_MISSING_LINE,
    CALENDAR_SCOPE_UNCONFIRMED_LINE,
    calendar_access_granted,
)

ROOT = Path(__file__).resolve().parents[3]
EMAIL = "openid https://www.googleapis.com/auth/userinfo.email"


def test_granted_scopes_are_read_from_the_token_response():
    assert calendar_access_granted(f"{EMAIL} {CALENDAR_READ_SCOPE}") is True
    assert calendar_access_granted(EMAIL) is False  # the unticked box
    assert calendar_access_granted("") is None and calendar_access_granted(None) is None


def _patches(scope):
    tokens = SimpleNamespace(refresh_token="r-token", scope=scope)
    handler = MagicMock()
    handler.handle_oauth_callback = AsyncMock(
        return_value={"tokens": tokens, "user_id": "u-2148", "user": {"email": "a@example.com"}}
    )
    keychain = MagicMock()
    return (
        patch(
            "services.integrations.calendar.oauth_handler.GoogleCalendarOAuthHandler",
            return_value=handler,
        ),
        patch("services.infrastructure.keychain_service.KeychainService", return_value=keychain),
        keychain,
    )


async def _settings(scope):
    from web.api.routes.settings_integrations import handle_calendar_callback

    p1, p2, keychain = _patches(scope)
    with p1, p2:
        resp = await handle_calendar_callback(code="c", state="s", error=None)
    return resp.headers["location"], keychain


async def _setup(scope):
    from web.api.routes.setup import handle_calendar_oauth_callback

    p1, p2, keychain = _patches(scope)
    with p1, p2:
        resp = await handle_calendar_oauth_callback(code="c", state="s", error=None)
    return resp.headers["location"], keychain


@pytest.mark.asyncio
@pytest.mark.parametrize("call", [_settings, _setup])
async def test_an_unticked_box_stores_nothing_and_is_not_success(call):
    location, keychain = await call(EMAIL)
    assert "calendar_error=scope_missing" in location
    assert "calendar_success" not in location
    keychain.store_api_key.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize("call", [_settings, _setup])
async def test_a_ticked_box_connects_as_before(call):
    location, keychain = await call(f"{EMAIL} {CALENDAR_READ_SCOPE}")
    assert "calendar_success=true" in location
    keychain.store_api_key.assert_called_once()


@pytest.mark.asyncio
@pytest.mark.parametrize("call", [_settings, _setup])
async def test_unreadable_scopes_are_never_a_success_state(call):
    location, _ = await call("")
    assert "calendar_unconfirmed=true" in location
    assert "calendar_success" not in location


def test_the_pages_carry_cxos_words():
    page = (ROOT / "templates" / "integrations.html").read_text()
    wizard = (ROOT / "web" / "static" / "js" / "setup.js").read_text()
    for text in (page, wizard):
        assert CALENDAR_SCOPE_MISSING_LINE in text
        assert CALENDAR_SCOPE_UNCONFIRMED_LINE in text
    # the scope_missing branch comes before the generic "Failed to connect" one
    assert page.index("scope_missing") < page.index("Calendar Connection Failed")
