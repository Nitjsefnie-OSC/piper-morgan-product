"""#2043 (#1324 class): the GitHub settings-flow callback and the calendar setup-wizard
callback derive their DEFAULT redirect URI from PIPER_BASE_URL, so a deployed host needs
no per-provider redirect secret; localhost only when the variable is absent. The calendar
wizard default also carries the router's real path (/api/v1/setup/...).

Layer: handler construction under a controlled environment; the explicit per-provider
variable still wins when set (alpha carries GITHUB_OAUTH_REDIRECT_URI today).
"""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

BASE = "https://alpha.example.test"
GITHUB_PATH = "/api/v1/settings/integrations/github/callback"
CAL_PATH = "/api/v1/setup/calendar/oauth/callback"

_ENV_CLEAR = {
    "PIPER_BASE_URL": "",
    "GITHUB_OAUTH_REDIRECT_URI": "",
    "GOOGLE_CALENDAR_REDIRECT_URI": "",
}


def _env(**over):
    env = {k: v for k, v in os.environ.items() if k not in _ENV_CLEAR}
    env.update({k: v for k, v in over.items() if v is not None})
    return patch.dict(os.environ, env, clear=True)


def _github_redirect() -> str:
    from services.mcp.consumer import github_oauth_handler as mod

    with patch.object(mod.GitHubOAuthHandler, "_load_credentials", return_value=("id", "secret")):
        return mod.GitHubOAuthHandler().redirect_uri


def _calendar_redirect() -> str:
    from services.integrations.calendar.oauth_handler import GoogleCalendarOAuthHandler

    with patch.dict(os.environ, {"GOOGLE_CLIENT_ID": "id", "GOOGLE_CLIENT_SECRET": "secret"}):
        return GoogleCalendarOAuthHandler().redirect_uri


@pytest.mark.parametrize("base", [BASE, BASE + "/"])
def test_github_default_derives_from_piper_base_url(base):
    with _env(PIPER_BASE_URL=base):
        assert _github_redirect() == BASE + GITHUB_PATH


def test_github_default_is_localhost_only_when_base_is_absent():
    with _env():
        assert _github_redirect() == "http://localhost:8001" + GITHUB_PATH


def test_github_explicit_variable_still_wins():
    with _env(PIPER_BASE_URL=BASE, GITHUB_OAUTH_REDIRECT_URI="https://other.test/cb"):
        assert _github_redirect() == "https://other.test/cb"


@pytest.mark.parametrize("base", [BASE, BASE + "/"])
def test_calendar_wizard_default_derives_from_piper_base_url_with_the_router_path(base):
    with _env(PIPER_BASE_URL=base):
        assert _calendar_redirect() == BASE + CAL_PATH


def test_calendar_wizard_default_is_localhost_with_the_router_path_when_base_is_absent():
    with _env():
        got = _calendar_redirect()
        assert got == "http://localhost:8001" + CAL_PATH
        assert "/api/v1/setup/" in got  # the old default lacked the router prefix


def test_calendar_explicit_variable_still_wins():
    with _env(PIPER_BASE_URL=BASE, GOOGLE_CALENDAR_REDIRECT_URI="https://other.test/cal"):
        assert _calendar_redirect() == "https://other.test/cal"


def test_the_setup_router_really_serves_that_calendar_path():
    from web.api.routes import setup as setup_routes

    paths = {getattr(r, "path", None) for r in setup_routes.router.routes}
    assert CAL_PATH in paths, sorted(p for p in paths if p and "calendar" in p)
