"""#2077: credential inputs must not receive the browser's saved Piper password.

Chrome ignores ``autocomplete="off"`` on ``type="password"`` inputs and fills in the
saved sign-in password for the site. On Settings → GitHub that means the personal
access token field can silently hold the user's Piper password, and the form's
Reconnect would send it to GitHub as a token. ``autocomplete="new-password"`` is
the hint Chrome honours. This pins it on every credential input (tokens, API keys,
client secrets) in the settings and setup templates; the real account-password
fields (login, reset, setup account) are deliberately NOT in the list, since the
password manager is wanted there.

Layer: static read of the template files, plus the rendered GitHub, Notion, Slack
and Calendar settings pages through the app's TestClient (template render). Does
NOT execute the browser's autofill.
"""

from __future__ import annotations

import re
import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from services.auth.container import AuthContainer
from web.app import app

REPO = Path(__file__).resolve().parents[3]

# template -> credential input ids that must carry autocomplete="new-password"
CREDENTIAL_INPUTS = {
    "settings_github.html": ["token"],
    "settings_notion.html": ["api-key"],
    "settings_slack.html": ["slack-client-secret", "slack-app-token"],
    "settings_calendar.html": ["calendar-client-secret"],
    "settings_llm_keys.html": ["llm-key-input"],
    "setup.html": ["llm-key", "notion-key", "slack-client-secret", "calendar-client-secret"],
}
# password-type inputs that ARE account passwords and keep normal autofill
ACCOUNT_PASSWORD_IDS = {"setup.html": {"password", "password-confirm"}}

RENDERED_PAGES = {
    "/settings/integrations/github": "token",
    "/settings/integrations/notion": "api-key",
    "/settings/integrations/slack": "slack-client-secret",
    "/settings/integrations/calendar": "calendar-client-secret",
}


def _input_tags(html: str) -> list[str]:
    return re.findall(r"<input\b[^>]*>", html, flags=re.S)


def _tag_with_id(tags: list[str], ident: str) -> str:
    hits = [t for t in tags if re.search(rf'\bid="{re.escape(ident)}"', t)]
    assert len(hits) == 1, f"expected exactly one input id={ident!r}, found {len(hits)}"
    return hits[0]


@pytest.mark.parametrize("template,ids", list(CREDENTIAL_INPUTS.items()))
def test_credential_inputs_opt_out_of_password_autofill(template, ids):
    tags = _input_tags((REPO / "templates" / template).read_text(encoding="utf-8"))
    for ident in ids:
        tag = _tag_with_id(tags, ident)
        assert 'type="password"' in tag, f"{template} #{ident} is no longer a password input"
        assert 'autocomplete="new-password"' in tag, (
            f'{template} #{ident}: a credential input needs autocomplete="new-password" '
            f'(Chrome ignores "off" and fills the saved Piper password, #2077)'
        )


@pytest.mark.parametrize("template,ids", list(CREDENTIAL_INPUTS.items()))
def test_every_password_input_in_these_templates_is_accounted_for(template, ids):
    tags = _input_tags((REPO / "templates" / template).read_text(encoding="utf-8"))
    password_ids = set()
    for t in tags:
        if 'type="password"' in t:
            m = re.search(r'\bid="([^"]+)"', t)
            assert m, f"{template}: a password input without an id: {t[:80]}"
            password_ids.add(m.group(1))
    allowed = set(ids) | ACCOUNT_PASSWORD_IDS.get(template, set())
    assert password_ids <= allowed, (
        f"{template}: new password-type input(s) {sorted(password_ids - allowed)}; "
        f"add them to CREDENTIAL_INPUTS (or ACCOUNT_PASSWORD_IDS if they hold the account password)"
    )


@pytest.fixture(scope="module")
def client():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates  # noqa: PLC0415

        app.state.templates = Jinja2Templates(directory=str(REPO / "templates"))
    return TestClient(app, follow_redirects=False)


def _token() -> str:
    return AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2077@example.com", scopes=["user"]
    )


@pytest.mark.parametrize("path,ident", list(RENDERED_PAGES.items()))
def test_rendered_settings_page_credential_input_opts_out(client, path, ident):
    client.cookies.set("auth_token", _token())
    try:
        r = client.get(path)
    finally:
        client.cookies.delete("auth_token")
    assert r.status_code == 200, f"{path} -> {r.status_code}"
    tag = _tag_with_id(_input_tags(r.text), ident)
    assert 'autocomplete="new-password"' in tag, f"{path}: rendered #{ident} lacks the hint"
