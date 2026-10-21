"""/health serves the quiet count as `services.chat_turns_last_30m` (grant condition 3).

LAYER: route, real TestClient on the served /health with the DB probe's engine replaced
at its seam (the 2101 watchdog pin's shape). The promote gate reads `.accounts`.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.testclient import TestClient

import web.api.routes.admin as admin_module
from services.infrastructure import turn_activity
from web.api.routes.admin import router as admin_router


class _FakeConnection:
    async def execute(self, _statement):
        return None


class _FakeEngine:
    @asynccontextmanager
    async def connect(self):
        yield _FakeConnection()

    async def dispose(self):
        return None


def _client() -> TestClient:
    app = FastAPI()
    app.include_router(admin_router)
    return TestClient(app)


def _install(monkeypatch):
    monkeypatch.setattr(admin_module, "create_async_engine", lambda *a, **k: _FakeEngine())
    monkeypatch.setenv("DATABASE_URL", "postgresql://piper:pw@db-quiet.flycast:5432/piper")
    monkeypatch.setattr(turn_activity, "TURN_ACTIVITY", turn_activity.TurnActivity())


def test_health_serves_the_quiet_count(monkeypatch):
    _install(monkeypatch)
    quiet = _client().get("/health").json()
    assert quiet["services"]["chat_turns_last_30m"] == {"accounts": 0, "turns": 0}
    turn_activity.TURN_ACTIVITY.record("user-a")
    turn_activity.TURN_ACTIVITY.record("user-b")
    busy = _client().get("/health").json()
    assert busy["services"]["chat_turns_last_30m"] == {"accounts": 2, "turns": 2}
    # informational: the status line is what the DB and intent service say
    assert busy["status"] == quiet["status"]
