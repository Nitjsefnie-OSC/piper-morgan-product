"""#2067 — a lapsed sign-in is a modal, never an integration result.

xian, alpha d741214b6c, 2026-10-16: after ~an hour away, Test on the GitHub
card printed Piper's own 401 body ("Token has expired") under GitHub, and the
summary read "1 of 4 integrations healthy". CXO's words (2026-10-18): one modal
over the page, title "You've been signed out", body as below, ONE "Sign in"
button that returns to this page, no close, no Cancel; no card changes state;
a health load failing for any other reason says "Couldn't check just now.
Press Test to try again."; never "Status: unknown".

Layer: rendered HTML through the app's TestClient (template render) plus
static pins on the template files. The JS is not executed in a browser; the
served acceptance on the issue covers that.
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
TEMPLATES = REPO / "templates"

TITLE = "You've been signed out"
BODY = (
    "Your sign-in expired while you were away. Nothing about your integrations "
    "has changed. Sign in again and you'll come back to this page."
)
HEALTH_LINE = "Couldn't check just now. Press Test to try again."

PAGES = {
    "/settings/integrations": "integrations.html",
    "/settings/integrations/github": "settings_github.html",
    "/settings/integrations/notion": "settings_notion.html",
    "/settings/integrations/slack": "settings_slack.html",
    "/settings/integrations/calendar": "settings_calendar.html",
}


@pytest.fixture(scope="module")
def client():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates

        app.state.templates = Jinja2Templates(directory=str(TEMPLATES))
    return TestClient(app, follow_redirects=False)


def _token() -> str:
    return AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2067@example.com", scopes=["user"]
    )


def _modal_block(html: str) -> str:
    start = html.index('id="signed-out-modal"')
    end = html.index("</div>\n</div>", start)
    return html[start:end]


@pytest.mark.parametrize("path", list(PAGES))
def test_rendered_page_carries_the_signed_out_modal_with_cxos_words(client, path):
    client.cookies.set("auth_token", _token())
    try:
        r = client.get(path)
    finally:
        client.cookies.clear()
    assert r.status_code == 200, (path, r.status_code)
    html = r.text
    assert TITLE in html, path
    assert BODY in html, path
    block = _modal_block(html)
    assert ">Sign in<" in block, path
    # One button, no close and no Cancel: the page behind cannot be trusted.
    assert block.count("<button") == 1, path
    assert "Cancel" not in block and "close" not in block.lower(), path
    assert 'role="dialog"' in block and 'aria-modal="true"' in block, path
    # The one place every fetch passes through, and the way back here.
    assert "window.PiperSession" in html, path
    assert "response.status === 401 && sameOriginApi" in html, path
    assert "'/login?next=' + encodeURIComponent(window.location.pathname" in html, path


def test_integrations_page_health_failure_line_and_no_status_unknown(client):
    client.cookies.set("auth_token", _token())
    try:
        r = client.get("/settings/integrations")
    finally:
        client.cookies.clear()
    assert r.status_code == 200
    html = r.text
    assert HEALTH_LINE in html
    assert "Status: unknown" not in html
    # Every render-from-fetch path checks the 401 before touching a card.
    assert html.count("response.status === 401") >= 6, html.count("response.status === 401")


def test_integrations_template_test_handler_restores_the_card_on_401():
    src = (TEMPLATES / "integrations.html").read_text(encoding="utf-8")
    assert "const lineBefore = statusEl.textContent;" in src
    assert "statusEl.textContent = lineBefore;" in src
    assert "statusEl.className = classesBefore;" in src
    assert "if (response.status === 401) return; // #2067" in src
    # The old shape: the 401 body rendered as the integration's result.
    m = re.search(r"const result = await response\.json\(\);", src)
    assert m is not None
    assert (
        src.index("if (response.status === 401) {", src.index("async function testConnection("))
        < m.start()
    )


@pytest.mark.parametrize(
    "template,old_text",
    [
        ("settings_github.html", "Connect GitHub first to see repositories"),
        ("settings_notion.html", "Connect Notion first to see databases"),
        ("settings_calendar.html", "Please connect your Google Calendar first."),
    ],
)
def test_settings_pages_no_longer_read_a_401_as_not_connected(template, old_text):
    src = (TEMPLATES / template).read_text(encoding="utf-8")
    assert old_text not in src, f"{template} still renders a 401 as 'not connected'"
    assert "signed_out_modal.html" in src


def test_app_credentials_status_401_renders_nothing(client):
    """The Slack and Calendar app-credentials status loads used to collapse any
    non-OK response into "not configured"; a 401 is the sign-in lapsing."""
    for template in ("settings_slack.html", "settings_calendar.html"):
        src = (TEMPLATES / template).read_text(encoding="utf-8")
        assert "if (response.status === 401) return; // #2067" in src, template
