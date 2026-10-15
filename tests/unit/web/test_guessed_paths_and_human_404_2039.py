"""#2039: guessed URLs redirect to the real page; unknown browser paths get a human 404.

Authenticated client throughout (the auth gate sends signed-out page requests
to /login?next=..., one test pins that). Layer: rendered response through the app's TestClient (template render, handler
negotiation). Does not run a browser.
"""

from __future__ import annotations

import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from services.auth.container import AuthContainer
from web.app import app

REPO = Path(__file__).resolve().parents[3]

REDIRECTS = {
    "/settings/github": "/settings/integrations/github",
    "/settings/notion": "/settings/integrations/notion",
    "/settings/slack": "/settings/integrations/slack",
    "/settings/calendar": "/settings/integrations/calendar",
    "/settings/google-calendar": "/settings/integrations/calendar",
    "/integrations": "/settings/integrations",
    "/settings/api-keys": "/settings/llm-keys",
    "/settings/llm": "/settings/llm-keys",
}
HTML = {"Accept": "text/html,application/xhtml+xml"}


@pytest.fixture(scope="module")
def client():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates

        app.state.templates = Jinja2Templates(directory=str(REPO / "templates"))
    return TestClient(app, follow_redirects=False)


@pytest.fixture
def authed(client):
    token = AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2039@example.com", scopes=["user"]
    )
    client.cookies.set("auth_token", token)
    yield client
    client.cookies.delete("auth_token")


@pytest.mark.parametrize("path,target", list(REDIRECTS.items()))
def test_guess_redirects_302_to_exact_target(authed, path, target):
    r = authed.get(path, headers=HTML)
    assert r.status_code == 302
    assert r.headers["location"] == target


def test_unauthenticated_guess_goes_to_login_then_back(client):
    """The auth gate runs first: a signed-out guess keeps its path in next=."""
    r = client.get("/settings/github", headers=HTML)
    assert r.status_code == 302
    assert r.headers["location"] == "/login?next=%2Fsettings%2Fgithub"


@pytest.mark.parametrize("target", sorted(set(REDIRECTS.values())))
def test_redirect_target_renders_200_when_authenticated(authed, target):
    assert authed.get(target).status_code == 200


@pytest.mark.parametrize("path", ["/settings/account", "/no-such-page"])
def test_unknown_browser_path_gets_human_404_in_shell(authed, path):
    r = authed.get(path, headers=HTML)
    assert r.status_code == 404
    assert r.headers["content-type"].startswith("text/html")
    body = r.text
    assert "That page isn&#39;t here." in body or "That page isn't here." in body
    assert "Check the address, or head back to one of these." in body
    for href, label in [
        ("/", "Home"),
        ("/settings", "Settings"),
        ("/settings/integrations", "Integrations"),
    ]:
        assert f'<a href="{href}">{label}</a>' in body
    assert 'id="main-content"' in body  # the app shell
    low = body.lower()
    assert "oops" not in low and "sorry" not in low and "404" not in low.split("<main")[1]


@pytest.mark.parametrize("path", ["/settings/account", "/no-such-page"])
@pytest.mark.parametrize("accept", ["application/json", None])
def test_non_html_request_keeps_json_404(authed, path, accept):
    headers = {"Accept": accept} if accept else {"Accept": "*/*"}
    r = authed.get(path, headers=headers)
    assert r.status_code == 404
    assert r.json() == {"detail": "Not Found"}


@pytest.mark.parametrize("accept", ["text/html", "application/json"])
def test_api_path_always_json_404(authed, accept):
    r = authed.get("/api/v1/no-such", headers={"Accept": accept})
    assert r.status_code == 404
    assert r.json() == {"detail": "Not Found"}


def test_settings_index_links_integrations_and_llm_keys(authed):
    body = authed.get("/settings").text
    assert 'href="/settings/integrations"' in body
    assert 'href="/settings/llm-keys"' in body
