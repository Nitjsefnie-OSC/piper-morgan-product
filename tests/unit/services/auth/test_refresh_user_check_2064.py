"""#2064 (Arch's 2026-10-16 condition): refresh refuses for an erased or inactive user.

Before this, ``JWTService.refresh_access_token`` checked only the refresh
token's signature and the blacklist, and ``POST /api/v1/auth/refresh`` rotates
the 7-day refresh token on every use, so an erased user's open tab stayed
signed in for ever and its writes landed in owner columns with no FK to users.

Pins, at two layers:
- service: with a session, one select of ``users.is_active`` by the claim's
  id; absent -> None, inactive -> None, active -> a new access token. Without a
  session the old behaviour stands (no caller in the app omits it).
- route (the app's TestClient, the real #283/#1078 handler): absent or
  inactive -> 401 with both auth cookies cleared; active -> 200 and rotated
  cookies. Token formats and lifetimes are untouched.
"""

from __future__ import annotations

import uuid
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from services.auth.jwt_service import JWTService

SECRET = "test-secret-2064"


class _Result:
    def __init__(self, value):
        self._value = value

    def scalar_one_or_none(self):
        return self._value


class _Session:
    """Answers the one users.is_active select with ``value`` (None = no row)."""

    def __init__(self, value):
        self.value = value
        self.statements: list = []

    async def execute(self, stmt, *a, **k):
        self.statements.append(stmt)
        return _Result(self.value)


@pytest.fixture
def jwt():
    return JWTService(secret_key=SECRET)


@pytest.fixture(autouse=True)
def _no_audit_writes(monkeypatch):
    from services.security import audit_logger as al

    monkeypatch.setattr(al.audit_logger, "log_auth_event", AsyncMock())


def _refresh(jwt, uid=None):
    uid = uid or uuid.uuid4()
    return uid, jwt.generate_refresh_token(user_id=uid, user_email="u2064@example.com")


# --- service layer ---------------------------------------------------------------


@pytest.mark.asyncio
@pytest.mark.parametrize("value", [None, False], ids=["absent", "inactive"])
async def test_service_refuses_absent_or_inactive_user(jwt, value):
    uid, token = _refresh(jwt)
    session = _Session(value)
    assert await jwt.refresh_access_token(token, session=session) is None
    assert len(session.statements) == 1
    sql = str(session.statements[0])
    assert "users.is_active" in sql and "users.id" in sql
    params = session.statements[0].compile().params
    assert list(params.values()) == [uid]


@pytest.mark.asyncio
async def test_service_refreshes_an_active_user(jwt):
    uid, token = _refresh(jwt)
    new = await jwt.refresh_access_token(token, session=_Session(True))
    assert new
    claims = await jwt.validate_token(new)
    assert str(claims.user_id) == str(uid) and claims.token_type == "access"


@pytest.mark.asyncio
async def test_service_without_session_keeps_old_behaviour(jwt):
    _, token = _refresh(jwt)
    assert await jwt.refresh_access_token(token) is not None


# --- route layer -------------------------------------------------------------------


@pytest.fixture
def client_with_user(monkeypatch, jwt):
    """The app's TestClient with the refresh route's session answering
    ``is_active`` with the value the test sets."""
    from web.api.routes import auth as auth_routes
    from web.app import app

    state = {"value": None, "session": None}

    @asynccontextmanager
    async def fake_scope():
        state["session"] = _Session(state["value"])
        yield state["session"]

    monkeypatch.setattr(
        auth_routes.AsyncSessionFactory, "session_scope_fresh", staticmethod(fake_scope)
    )
    app.dependency_overrides[auth_routes.get_jwt_service] = lambda: jwt
    client = TestClient(app, follow_redirects=False)
    try:
        yield client, state
    finally:
        app.dependency_overrides.pop(auth_routes.get_jwt_service, None)


def _cleared(response, name):
    return any(
        h.startswith(f"{name}=") and ("Max-Age=0" in h or "expires=" in h.lower())
        for h in response.headers.get_list("set-cookie")
    )


@pytest.mark.parametrize("value", [None, False], ids=["absent", "inactive"])
def test_route_401_clears_cookies_for_absent_or_inactive_user(client_with_user, jwt, value):
    client, state = client_with_user
    state["value"] = value
    _, token = _refresh(jwt)
    client.cookies.set("refresh_token", token)
    r = client.post("/api/v1/auth/refresh")
    assert r.status_code == 401, r.text
    assert _cleared(r, "auth_token") and _cleared(r, "refresh_token"), r.headers.get_list(
        "set-cookie"
    )
    assert len(state["session"].statements) == 1


def test_route_rotates_for_an_active_user(client_with_user, jwt):
    client, state = client_with_user
    state["value"] = True
    _, token = _refresh(jwt)
    client.cookies.set("refresh_token", token)
    r = client.post("/api/v1/auth/refresh")
    assert r.status_code == 200, r.text
    assert r.json()["token"]
    set_cookies = r.headers.get_list("set-cookie")
    new_refresh = [h for h in set_cookies if h.startswith("refresh_token=")]
    assert new_refresh and token not in new_refresh[0]
    assert any(h.startswith("auth_token=") for h in set_cookies)
