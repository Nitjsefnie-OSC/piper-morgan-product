"""#2081 — the Invites page renders for the admin, refuses a non-admin, and the
settings index shows its card only to an admin. Layer: TestClient render with
the admin DB read patched at its boundary."""

from __future__ import annotations

import uuid
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from services.auth.container import AuthContainer
from web.app import app

REPO = Path(__file__).resolve().parents[3]
ADMIN_ID = uuid.uuid4()
NON_ADMIN_ID = uuid.uuid4()


@pytest.fixture(scope="module")
def client():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates

        app.state.templates = Jinja2Templates(directory=str(REPO / "templates"))
    return TestClient(app, follow_redirects=False)


def _token(user_id) -> str:
    return AuthContainer.get_jwt_service().generate_access_token(
        user_id=user_id, user_email="u2081@example.com", scopes=["user"]
    )


def _is_admin_patch():
    async def fake(user_id):
        return str(user_id) == str(ADMIN_ID)

    return patch("services.auth.auth_middleware._user_is_admin", side_effect=fake)


def test_admin_sees_the_invites_page(client):
    client.cookies.set("auth_token", _token(ADMIN_ID))
    try:
        with _is_admin_patch():
            r = client.get("/settings/invites")
    finally:
        client.cookies.clear()
    assert r.status_code == 200, r.text[:300]
    html = r.text
    assert "Mint codes" in html and "All codes" in html
    assert "Copy these now." in html and "They will not be shown again." in html
    assert "/api/v1/admin/invites" in html
    assert "signed-out-modal" in html  # #2067 shared handler
    assert "Dialog.confirm(" in html  # revoke behind the #1190-style confirm
    # xian's D5 read (2026-10-19): the list re-read must bypass the browser cache, and the
    # revoked row changes at once rather than waiting on the re-read.
    assert "fetch(API, { cache: 'no-store' })" in html
    assert "status-pill status-revoked" in html and "btn.remove();" in html


def test_non_admin_is_refused(client):
    client.cookies.set("auth_token", _token(NON_ADMIN_ID))
    try:
        with _is_admin_patch():
            r = client.get("/settings/invites")
    finally:
        client.cookies.clear()
    assert r.status_code == 403


def test_settings_index_card_is_admin_only():
    src = (REPO / "templates" / "settings-index.html").read_text(encoding="utf-8")
    i = src.index('href="/settings/invites"')
    guard = src.rfind("{% if user and user.is_admin %}", 0, i)
    close = src.find("{% endif %}", i)
    assert guard != -1 and close != -1, "the Invites card must sit inside the admin guard"
    assert "Admin only" in src[i:close]
