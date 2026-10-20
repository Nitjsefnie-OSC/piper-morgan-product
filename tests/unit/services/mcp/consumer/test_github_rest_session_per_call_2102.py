"""#2102 — the GitHub adapter opens no aiohttp session at configure time; each REST call
opens and closes its own.

PA's log read for the #2101 stall window (alpha, 2026-10-19): 40 "Unclosed client session"
warnings in six minutes, clustered with the integration-status burst. Routers are built per
chat turn, ``configure_github_api()`` opened a ``ClientSession`` on each, and nothing closed
them (the #1279 ``close()`` exists but the per-turn callers never call it).

LAYER: the adapter with ``aiohttp.ClientSession`` replaced by a recording fake. DENOMINATOR:
configure opens nothing; a GET, a POST and a PATCH each open one session and close it; an
assigned session is used as is and not closed; the unconfigured warning path is unchanged.
"""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from unittest.mock import patch

import pytest

from services.mcp.consumer import github_adapter as mod
from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter

pytestmark = pytest.mark.asyncio


class _Resp:
    status = 200

    async def json(self):
        return {"ok": True}


class _FakeSession:
    instances: list["_FakeSession"] = []

    def __init__(self, headers=None, **kw):
        self.headers = headers or {}
        self.closed = False
        _FakeSession.instances.append(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        self.closed = True

    async def close(self):
        self.closed = True

    def _call(self, *a, **kw):
        @asynccontextmanager
        async def _cm():
            yield _Resp()

        return _cm()

    get = post = patch = _call


@pytest.fixture(autouse=True)
def _fake_sessions(monkeypatch):
    _FakeSession.instances = []
    monkeypatch.setattr(mod.aiohttp, "ClientSession", _FakeSession)
    yield


async def test_configure_opens_no_session():
    adapter = GitHubMCPSpatialAdapter()
    with patch.object(adapter, "_configure_api_base", create=True):
        await adapter.configure_github_api("tok")
    assert adapter._session is None
    assert _FakeSession.instances == []
    assert adapter._rest_headers["Authorization"] == "token tok"


async def test_each_rest_call_opens_one_session_and_closes_it():
    adapter = GitHubMCPSpatialAdapter()
    await adapter.configure_github_api("tok")
    assert await adapter._call_github_api("repos/o/r") == {"ok": True}
    assert await adapter._post_github_api("repos/o/r/issues", {"title": "t"}) == {"ok": True}
    assert await adapter._patch_github_api("repos/o/r/issues/1", {"state": "closed"}) == {
        "ok": True
    }
    assert len(_FakeSession.instances) == 3
    assert all(s.closed for s in _FakeSession.instances)
    assert all(s.headers["Authorization"] == "token tok" for s in _FakeSession.instances)


async def test_an_assigned_session_is_used_and_not_closed():
    adapter = GitHubMCPSpatialAdapter()
    own = _FakeSession()
    adapter._session = own
    assert await adapter._call_github_api("repos/o/r") == {"ok": True}
    assert own.closed is False
    assert len(_FakeSession.instances) == 1  # no second session opened
    await adapter.disconnect()
    assert own.closed is True and adapter._session is None


async def test_unconfigured_rest_still_says_so():
    adapter = GitHubMCPSpatialAdapter()
    assert await adapter._call_github_api("repos/o/r") is None
    assert _FakeSession.instances == []
