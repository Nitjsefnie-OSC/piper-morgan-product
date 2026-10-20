"""#2102 — a bare SlackClient leaks no aiohttp session.

PA's read on alpha ef907b2cd7 (2026-10-20): 8 "Unclosed client session" warnings in four
bursts, all on the standup/context-assembly path, held connections aged 500 to 850 s. The
per-turn integration router builds ``SlackClient(...)`` bare; ``_ensure_session`` made a
persistent ``ClientSession`` on the first request and nothing closed it. Now a bare client
uses a short-lived session per request; ``async with SlackClient(...)`` keeps the held one.

LAYER: the client against a fake ``ClientSession`` (no network). DENOMINATOR: a bare
client's request opens and closes one session and holds none; two requests, two sessions,
both closed; an entered client reuses one session and closes it on exit.
"""

from __future__ import annotations

import contextlib
from types import SimpleNamespace

import pytest

from services.integrations.slack import slack_client as mod
from services.integrations.slack.slack_client import SlackClient


class _FakeResponse:
    status = 200
    ok = True
    headers: dict = {}

    async def json(self):
        return {"ok": True, "user": "U1"}


class _FakeSession:
    instances: list = []

    def __init__(self, timeout=None):
        self.closed = False
        self.requests = 0
        _FakeSession.instances.append(self)

    async def close(self):
        self.closed = True

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.close()

    @contextlib.asynccontextmanager
    async def request(self, **kwargs):
        self.requests += 1
        yield _FakeResponse()


def _config_service():
    cfg = SimpleNamespace(
        timeout_seconds=5,
        api_base_url="https://slack.example/api",
        bot_token="xoxb-test",
        user_token=None,
        requests_per_minute=100,
    )
    return SimpleNamespace(get_config=lambda user_id: cfg)


@pytest.fixture(autouse=True)
def _fake_session(monkeypatch):
    _FakeSession.instances = []
    monkeypatch.setattr(mod, "ClientSession", _FakeSession)
    yield


@pytest.mark.asyncio
async def test_bare_client_opens_and_closes_a_session_per_request_and_holds_none():
    client = SlackClient(_config_service(), user_id="u1")
    r1 = await client._make_request("GET", "auth.test")
    r2 = await client._make_request("GET", "auth.test")
    assert r1.success and r2.success
    assert len(_FakeSession.instances) == 2
    assert all(s.closed for s in _FakeSession.instances)
    assert client._session is None


@pytest.mark.asyncio
async def test_entered_client_reuses_one_session_and_closes_it_on_exit():
    async with SlackClient(_config_service(), user_id="u1") as client:
        await client._make_request("GET", "auth.test")
        await client._make_request("GET", "auth.test")
        assert len(_FakeSession.instances) == 1
        assert _FakeSession.instances[0].requests == 2
        assert not _FakeSession.instances[0].closed
    assert _FakeSession.instances[0].closed
    assert client._entered is False
