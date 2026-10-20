"""#2101 — /health says whether the event-loop watchdog is running.

PA, 2026-10-20: alpha emits no INFO lines, so the watchdog's start could not be seen and
its silence on a stalled run could not be told from a watchdog that never started. The body
now carries `services.loop_watchdog`: "running" while the checker thread is alive, "absent"
otherwise. Informational: it never moves the top-level status.

LAYER: route, real TestClient on the served /health; the DB probe's engine replaced at its
seam as the 2083 pins do. DENOMINATOR: the one ungated /health route; running, absent, and
the status line unchanged by either.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

import web.api.routes.admin as admin_module
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


def _client(watchdog=None) -> TestClient:
    app = FastAPI()
    app.include_router(admin_router)
    if watchdog is not None:
        app.state.loop_watchdog = watchdog
    return TestClient(app)


def _install(monkeypatch):
    monkeypatch.setattr(admin_module, "create_async_engine", lambda *a, **k: _FakeEngine())
    monkeypatch.setenv("DATABASE_URL", "postgresql://piper:pw@db-2101.flycast:5432/piper")


def test_running_watchdog_reads_running(monkeypatch):
    _install(monkeypatch)
    body = _client(SimpleNamespace(is_running=True)).get("/health").json()
    assert body["services"]["loop_watchdog"] == "running"
    assert body["services"]["database"] == "healthy"


def test_stopped_or_missing_watchdog_reads_absent_without_degrading(monkeypatch):
    _install(monkeypatch)
    stopped = _client(SimpleNamespace(is_running=False)).get("/health").json()
    missing = _client().get("/health").json()
    assert stopped["services"]["loop_watchdog"] == "absent"
    assert missing["services"]["loop_watchdog"] == "absent"
    # the field is informational: the status line is what the DB and intent service say
    assert stopped["status"] == missing["status"]
