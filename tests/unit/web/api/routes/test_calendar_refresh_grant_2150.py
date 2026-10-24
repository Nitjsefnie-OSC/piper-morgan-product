"""Calendar refreshes derive access from Google's grant, never token presence."""

import json
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from services.integrations.calendar.oauth_handler import (
    CALENDAR_READ_SCOPE,
    CALENDAR_SCOPE_MISSING_LINE,
    CALENDAR_SCOPE_UNCONFIRMED_LINE,
)
from services.integrations.principal_test_results import PrincipalTestResultStore
from web.api.routes import integrations, settings_integrations

OAUTH = "services.integrations.calendar.oauth_handler"
USER = SimpleNamespace(sub="calendar-user")


@pytest.fixture
def refresh():
    keychain = MagicMock()
    keychain.get_api_key.return_value = "refresh-token"
    keychain.aget_api_key = AsyncMock(return_value="refresh-token")
    handler = MagicMock()
    handler.refresh_access_token = AsyncMock()
    with (
        patch("services.infrastructure.keychain_service.KeychainService", return_value=keychain),
        patch(f"{OAUTH}.GoogleCalendarOAuthHandler", return_value=handler),
        patch(f"{OAUTH}.probe_calendar_read", new_callable=AsyncMock) as probe,
        patch("aiohttp.ClientSession") as session,
        patch.object(settings_integrations, "_load_prefs_db", new_callable=AsyncMock) as prefs,
    ):
        probe.return_value = None
        prefs.return_value = {}
        session.return_value.__aenter__.return_value = MagicMock()
        response = session.return_value.__aenter__.return_value.get.return_value
        response.__aenter__.return_value.status = 200
        response.__aenter__.return_value.json = AsyncMock(return_value={"items": []})
        yield handler, probe


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "scope, read_error, valid, error",
    [
        (CALENDAR_READ_SCOPE, "insufficient_scope", True, None),
        ("https://www.googleapis.com/auth/calendar", "error", True, None),
        ("openid email", None, False, CALENDAR_SCOPE_MISSING_LINE),
        (f"{CALENDAR_READ_SCOPE}.events", None, False, CALENDAR_SCOPE_MISSING_LINE),
        ("", None, True, None),
        (None, "insufficient_scope", False, CALENDAR_SCOPE_MISSING_LINE),
        ("", "error", False, CALENDAR_SCOPE_UNCONFIRMED_LINE),
        (42, "api_not_enabled", False, CALENDAR_SCOPE_UNCONFIRMED_LINE),
        ("", TimeoutError(), False, CALENDAR_SCOPE_UNCONFIRMED_LINE),
    ],
)
async def test_settings_derives_the_refreshed_grant(refresh, scope, read_error, valid, error):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    if isinstance(read_error, Exception):
        probe.side_effect = read_error
    else:
        probe.return_value = read_error

    result = await settings_integrations.get_calendar_settings(current_user=USER)

    assert result == {"configured": True, "valid": valid, "email": None, "error": error}


@pytest.mark.asyncio
async def test_settings_with_no_scope_attribute_uses_the_read(refresh):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(access_token="access")
    probe.return_value = "insufficient_scope"

    result = await settings_integrations.get_calendar_settings(current_user=USER)

    assert result["valid"] is False
    assert result["error"] == CALENDAR_SCOPE_MISSING_LINE


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "scope, read_error, error",
    [
        ("openid email", None, CALENDAR_SCOPE_MISSING_LINE),
        ("", "insufficient_scope", CALENDAR_SCOPE_MISSING_LINE),
        ("", "error", CALENDAR_SCOPE_UNCONFIRMED_LINE),
    ],
)
async def test_calendar_list_rejects_an_unusable_grant(refresh, scope, read_error, error):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error
    with pytest.raises(HTTPException) as exc:
        await settings_integrations.get_calendar_list(current_user=USER)
    assert exc.value.status_code == 409
    assert exc.value.detail == error


@pytest.mark.asyncio
@pytest.mark.parametrize("scope, read_error", [("openid email", None), ("", "insufficient_scope")])
async def test_test_button_reports_the_same_not_allowed_line(refresh, scope, read_error):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error

    result = await integrations._test_calendar(user_id=USER.sub)

    assert result == {
        "success": False,
        "error": CALENDAR_SCOPE_MISSING_LINE,
        "error_type": "insufficient_scope",
    }


@pytest.mark.asyncio
@pytest.mark.parametrize("previous_test_ok", [None, True, False])
@pytest.mark.parametrize(
    "scope, read_error, connected, error",
    [
        (CALENDAR_READ_SCOPE, None, True, None),
        ("openid email", None, False, CALENDAR_SCOPE_MISSING_LINE),
        ("", "error", False, CALENDAR_SCOPE_UNCONFIRMED_LINE),
    ],
)
async def test_calendar_card_checks_the_grant_before_cached_health(
    refresh, previous_test_ok, scope, read_error, connected, error
):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error
    results = PrincipalTestResultStore()
    if previous_test_ok is not None:
        results.record_test_result(USER.sub, "calendar", ok=previous_test_ok)
    with patch.object(integrations, "_get_test_result_store", return_value=results):
        card = await integrations._check_integration_health(
            "calendar", integrations.INTEGRATION_REGISTRY["calendar"], user_id=USER.sub
        )

    assert (card.status != "not_configured") is connected
    if connected:
        assert (
            card.status == {None: "connected", True: "healthy", False: "failed"}[previous_test_ok]
        )
    else:
        assert card.status_message == "Not connected"
        assert card.status_detail == error


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "scope, read_error, connected, info",
    [
        (CALENDAR_READ_SCOPE, None, True, None),
        ("openid email", None, False, CALENDAR_SCOPE_MISSING_LINE),
        ("", "error", False, CALENDAR_SCOPE_UNCONFIRMED_LINE),
        ("", None, True, None),
    ],
)
async def test_combined_oauth_status_uses_the_refreshed_grant(
    refresh, scope, read_error, connected, info
):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error

    result = await settings_integrations.get_all_oauth_status(current_user=USER)

    assert result["calendar"] == {"connected": connected, "info": info}


@pytest.mark.asyncio
@pytest.mark.parametrize("scope", [CALENDAR_READ_SCOPE, ""])
async def test_calendar_list_accepts_a_confirmed_grant(refresh, scope):
    handler, _ = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")

    result = await settings_integrations.get_calendar_list(current_user=USER)

    assert result.calendars == []


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "scope, read_error, success, error_type",
    [
        (CALENDAR_READ_SCOPE, None, True, None),
        (CALENDAR_READ_SCOPE, "insufficient_scope", False, "insufficient_scope"),
        (CALENDAR_READ_SCOPE, "api_not_enabled", False, "api_not_enabled"),
        (CALENDAR_READ_SCOPE, "error", False, "error"),
        (CALENDAR_READ_SCOPE, "auth_failed", False, "auth_failed"),
        ("", "api_not_enabled", False, "api_not_enabled"),
    ],
)
async def test_the_test_button_preserves_read_diagnostics(
    refresh, scope, read_error, success, error_type
):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error

    result = await integrations._test_calendar(user_id=USER.sub)

    assert result["success"] is success
    assert result.get("error_type") == error_type
    if read_error == "insufficient_scope":
        assert result["error"] == CALENDAR_SCOPE_MISSING_LINE


@pytest.mark.asyncio
async def test_unreadable_scope_and_missing_access_token_are_unconfirmed(refresh):
    handler, _ = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope="", access_token=None)

    result = await settings_integrations.get_calendar_settings(current_user=USER)

    assert result["valid"] is False
    assert result["error"] == CALENDAR_SCOPE_UNCONFIRMED_LINE


@pytest.mark.skipif(shutil.which("node") is None, reason="node not on PATH")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "scope, read_error, detail",
    [
        (CALENDAR_READ_SCOPE, None, None),
        ("openid email", None, CALENDAR_SCOPE_MISSING_LINE),
        ("", "error", CALENDAR_SCOPE_UNCONFIRMED_LINE),
    ],
)
async def test_settings_renderer_preserves_the_refreshed_grant_diagnosis(
    refresh, scope, read_error, detail
):
    handler, probe = refresh
    handler.refresh_access_token.return_value = SimpleNamespace(scope=scope, access_token="access")
    probe.return_value = read_error
    response = await settings_integrations.get_calendar_settings(current_user=USER)
    page = (Path(__file__).resolve().parents[5] / "templates/settings_calendar.html").read_text()
    renderer = page[
        page.index("function updateStatusUI(data)") : page.index("async function connectCalendar()")
    ]
    script = (
        "const elements = {};\n"
        "const document = {getElementById(id) {return elements[id] ||= {style: {}};}};\n"
        "function loadCalendarList() {}\n"
        + renderer
        + "\nupdateStatusUI(JSON.parse(process.argv[1]));\n"
        "process.stdout.write(JSON.stringify({\n"
        "  title: elements['status-title'].textContent,\n"
        "  detail: elements['status-subtitle'].textContent,\n"
        "  description: elements['oauth-description'].textContent,\n"
        "  selection: elements['calendar-selection-card'].style.display\n"
        "}));\n"
    )
    result = subprocess.run(
        ["node", "-e", script, json.dumps(response)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    rendered = json.loads(result.stdout)
    if detail is None:
        assert rendered == {
            "title": "Connected",
            "detail": "Google Calendar is connected",
            "description": "You can reconnect to a different account or refresh your connection.",
            "selection": "block",
        }
    else:
        assert rendered == {
            "title": "Connection Issue",
            "detail": detail,
            "description": "You can reconnect to review your Google Calendar access.",
            "selection": "none",
        }
