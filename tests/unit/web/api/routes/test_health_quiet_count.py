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
    # CIO 10-21: the public body serves only the verdict and the marker; counts go to the log
    assert quiet["services"]["chat_turns_last_30m"] == {
        "quiet": True,
        "record_failed_in_window": False,
    }
    turn_activity.TURN_ACTIVITY.record("user-a")
    turn_activity.TURN_ACTIVITY.record("user-b")
    busy = _client().get("/health").json()
    assert busy["services"]["chat_turns_last_30m"] == {
        "quiet": False,
        "record_failed_in_window": False,
    }
    assert "accounts" not in busy["services"]["chat_turns_last_30m"]
    # informational: the status line is what the DB and intent service say
    assert busy["status"] == quiet["status"]


def test_health_serves_uptime_beside_the_count(monkeypatch):
    _install(monkeypatch)
    body = _client().get("/health").json()
    assert isinstance(body["services"]["uptime_seconds"], int)
    assert body["services"]["uptime_seconds"] >= 0


def test_a_broken_counter_serves_a_marker_not_a_quiet_zero(monkeypatch):
    """Arch 10-21: a counter that cannot count must not read as quiet."""
    _install(monkeypatch)

    class _Exploding:
        def snapshot(self):
            raise RuntimeError("counter down")

    monkeypatch.setattr(turn_activity, "TURN_ACTIVITY", _Exploding())
    body = _client().get("/health").json()
    field = body["services"]["chat_turns_last_30m"]
    assert "quiet" not in field and field.get("error") == "unavailable"
    assert body["status"] in ("healthy", "degraded")  # /health itself stays up


def test_a_record_failure_in_the_window_is_served(monkeypatch):
    _install(monkeypatch)
    turn_activity.TURN_ACTIVITY.note_record_failure()
    body = _client().get("/health").json()
    field = body["services"]["chat_turns_last_30m"]
    assert field["record_failed_in_window"] is True
    assert field["quiet"] is False  # a count that may be missing turns never reads quiet
