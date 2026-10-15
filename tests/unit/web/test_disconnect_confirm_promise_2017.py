"""#2017: Disconnect confirms use the promise-style Dialog.confirm.

The callback style (`onConfirm:`) falls into the legacy Dialog.show() path,
which returns early when the #confirmation-dialog partial is absent -- and it
is absent on these five pages, so the Disconnect button did nothing. The
promise style is self-contained (Dialog.open builds its own DOM).

Layer: rendered HTML through the app's TestClient (template render), plus a
static pin on the template files. Does NOT execute the JS in a browser.
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

# page path -> (template, disconnect endpoint fragment expected in the handler)
PAGES = {
    "/settings/integrations": (
        "integrations.html",
        "/api/v1/settings/integrations/${integrationName}/disconnect",
    ),
    "/settings/integrations/github": (
        "settings_github.html",
        "/api/v1/settings/integrations/github/disconnect",
    ),
    "/settings/integrations/notion": (
        "settings_notion.html",
        "/api/v1/settings/integrations/notion/disconnect",
    ),
    "/settings/integrations/slack": (
        "settings_slack.html",
        "/api/v1/settings/integrations/slack/disconnect",
    ),
    "/settings/integrations/calendar": (
        "settings_calendar.html",
        "/api/v1/settings/integrations/calendar/disconnect",
    ),
}


@pytest.fixture(scope="module")
def client():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates

        app.state.templates = Jinja2Templates(directory=str(REPO / "templates"))
    return TestClient(app, follow_redirects=False)


def _token() -> str:
    return AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2017@example.com", scopes=["user"]
    )


@pytest.mark.parametrize("path", list(PAGES))
def test_rendered_page_uses_promise_style_disconnect(client, path):
    client.cookies.set("auth_token", _token())
    try:
        r = client.get(path)
    finally:
        client.cookies.delete("auth_token")
    assert r.status_code == 200, f"{path} -> {r.status_code}"
    body = r.text
    assert "onConfirm" not in body, f"{path} still has an onConfirm callback"
    assert re.search(r"const ok = await Dialog\.confirm\(\{", body)
    assert "if (!ok) return;" in body
    # The Disconnect handler is async and the endpoint is unchanged.
    assert PAGES[path][1] in body
    # Dialog primitive is loaded on the page (via the app shell).
    assert "/static/js/dialog.js" in body


@pytest.mark.parametrize("path", list(PAGES))
def test_every_dialog_confirm_on_page_is_awaited(path):
    src = (REPO / "templates" / PAGES[path][0]).read_text()
    calls = re.findall(r"^.*Dialog\.confirm\(\{", src, flags=re.M)
    assert calls, "expected at least one Dialog.confirm"
    for line in calls:
        assert "await Dialog.confirm({" in line, f"unawaited confirm: {line.strip()}"
    assert "onConfirm" not in src


def test_static_pin_no_onconfirm_on_five_pages():
    for template, _ in PAGES.values():
        assert "onConfirm" not in (REPO / "templates" / template).read_text(), template
