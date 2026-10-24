"""Calendar list endpoint tests (Issue #571).

#1400 rewrite: the flat-file preference classes this suite carried
(TestGetCalendarPreferences / TestSaveCalendarPreferences /
TestCalendarPreferencesFileStorage) pinned the deleted data/*.json helpers.
Calendar pref round-trips, owner isolation, the legacy-file migration shim,
and merge semantics now live in test_settings_notion_preferences.py's shared
DB-store suite (the helpers are connector-parameterized). What remains here is
this file's unique surface: the Google-API-mocked calendar LIST endpoint,
ported with the prefs helper swapped to the DB one.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from web.api.routes.settings_integrations import (
    CALENDAR_NEEDS_RECONNECT_LINE,
    CALENDAR_NOT_CONNECTED_LINE,
    get_calendar_list,
)


class TestGetCalendarList:
    """Tests for GET /api/v1/settings/integrations/calendar/calendars"""

    @pytest.mark.asyncio
    async def test_returns_409_not_connected_line_when_no_credential(self):
        """#2105: no refresh token is NOT a lapsed sign-in: 409 with CXO's line, never 401 (the modal's trigger)."""
        mock_keychain = MagicMock()
        mock_keychain.aget_api_key = AsyncMock(
            side_effect=lambda *a, **k: mock_keychain.get_api_key(*a, **k)
        )  # #2101
        mock_keychain.get_api_key.return_value = None

        mock_user = MagicMock()
        mock_user.sub = "test-user-123"

        with patch(
            "services.infrastructure.keychain_service.KeychainService",
            return_value=mock_keychain,
        ):
            from fastapi import HTTPException

            with pytest.raises(HTTPException) as exc_info:
                await get_calendar_list(current_user=mock_user)

            assert exc_info.value.status_code == 409
            assert exc_info.value.detail == CALENDAR_NOT_CONNECTED_LINE

    @pytest.mark.asyncio
    async def test_returns_409_reconnect_line_when_token_refresh_fails(self):
        """#2105: a failed token refresh is the calendar credential, not the session: 409 with the reconnect line."""
        mock_keychain = MagicMock()
        mock_keychain.aget_api_key = AsyncMock(
            side_effect=lambda *a, **k: mock_keychain.get_api_key(*a, **k)
        )  # #2101
        mock_keychain.get_api_key.return_value = "test_refresh_token"

        mock_handler = MagicMock()
        mock_handler.refresh_access_token = AsyncMock(return_value=None)

        mock_user = MagicMock()
        mock_user.sub = "test-user-123"

        with (
            patch(
                "services.infrastructure.keychain_service.KeychainService",
                return_value=mock_keychain,
            ),
            patch(
                "services.integrations.calendar.oauth_handler.GoogleCalendarOAuthHandler",
                return_value=mock_handler,
            ),
        ):
            from fastapi import HTTPException

            with pytest.raises(HTTPException) as exc_info:
                await get_calendar_list(current_user=mock_user)

            assert exc_info.value.status_code == 409
            assert exc_info.value.detail == CALENDAR_NEEDS_RECONNECT_LINE

    @pytest.mark.asyncio
    async def test_returns_calendar_list_when_connected(self):
        """Should return list of calendars when connected"""
        mock_keychain = MagicMock()
        mock_keychain.aget_api_key = AsyncMock(
            side_effect=lambda *a, **k: mock_keychain.get_api_key(*a, **k)
        )  # #2101
        mock_keychain.get_api_key.return_value = "test_refresh_token"

        mock_tokens = MagicMock()
        mock_tokens.access_token = "test_access_token"
        mock_tokens.scope = "https://www.googleapis.com/auth/calendar.readonly"

        mock_handler = MagicMock()
        mock_handler.refresh_access_token = AsyncMock(return_value=mock_tokens)

        mock_user = MagicMock()
        mock_user.sub = "test-user-123"

        # Mock Google API response
        mock_google_response = {
            "items": [
                {
                    "id": "primary",
                    "summary": "Work Calendar",
                    "description": "Main work calendar",
                    "primary": True,
                },
                {
                    "id": "personal@gmail.com",
                    "summary": "Personal",
                    "description": "",
                    "primary": False,
                },
            ]
        }

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=mock_google_response)

        mock_session_instance = MagicMock()
        mock_session_instance.get = MagicMock(
            return_value=AsyncMock(
                __aenter__=AsyncMock(return_value=mock_response), __aexit__=AsyncMock()
            )
        )

        mock_session = MagicMock()
        mock_session.__aenter__ = AsyncMock(return_value=mock_session_instance)
        mock_session.__aexit__ = AsyncMock()

        with (
            patch(
                "services.infrastructure.keychain_service.KeychainService",
                return_value=mock_keychain,
            ),
            patch(
                "services.integrations.calendar.oauth_handler.GoogleCalendarOAuthHandler",
                return_value=mock_handler,
            ),
            patch("aiohttp.ClientSession", return_value=mock_session),
            patch(
                "web.api.routes.settings_integrations._load_prefs_db",
                new=AsyncMock(return_value={}),
            ),
        ):
            result = await get_calendar_list(current_user=mock_user)

            assert len(result.calendars) == 2
            assert result.calendars[0].id == "primary"
            assert result.calendars[0].name == "Work Calendar"
            assert result.calendars[0].primary is True
            assert result.calendars[1].id == "personal@gmail.com"
