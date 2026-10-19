"""#2083 — /health reports the database, bounded, with HTTP 200 either way.

On 2026-10-19 alpha's Postgres stopped answering for hours. /health kept saying
"healthy" (it had no DB check), so sign-in returned 500 for everyone while the
deploy gate, the promotion grant and the PM test card all read the page as fine.
Arch's ruling (issue comment 6272010753): `services.database` healthy|unreachable
in the body, top-level `status` degraded on failure, HTTP 200 always (Fly restarts
the only machine on a non-200, which cannot fix a DB outage and would take down
the DB-free pages), a bounded `SELECT 1`, and no DSN, host or exception text in
the body.

LAYER (m-43): route, real TestClient on the served /health; the engine is replaced
at its one seam (`services.database.connection.db`), nothing else is faked.
DENOMINATOR: the one ungated /health route; four behaviours (healthy, failing,
hung, no-secrets).
"""

import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.testclient import TestClient

import web.api.routes.admin as admin_module
from web.api.routes.admin import router as admin_router

FAKE_DSN_HOST = "secret-db-host-2083.flycast"
FAKE_DSN_PASSWORD = "hunter2-2083-never-in-a-body"


def _client() -> TestClient:
    app = FastAPI()
    app.include_router(admin_router)
    return TestClient(app)


class _FakeConnection:
    def __init__(self, behaviour):
        self._behaviour = behaviour

    async def execute(self, _statement):
        await self._behaviour()
        return None


class _FakeEngine:
    """The shape `_database_probe` reads: `connect()` and `dispose()`."""

    disposed = 0

    def __init__(self, behaviour):
        self._behaviour = behaviour

    @asynccontextmanager
    async def connect(self):
        yield _FakeConnection(self._behaviour)

    async def dispose(self):
        _FakeEngine.disposed += 1


def _install(monkeypatch, behaviour, timeout=None):
    """Replace the probe's engine factory at its one seam; the global singleton is untouched."""
    monkeypatch.setattr(admin_module, "create_async_engine", lambda *a, **k: _FakeEngine(behaviour))
    if timeout is not None:
        monkeypatch.setattr(admin_module, "DATABASE_PROBE_SECONDS", timeout)
    monkeypatch.setenv(
        "DATABASE_URL",
        f"postgresql://piper:{FAKE_DSN_PASSWORD}@{FAKE_DSN_HOST}:5432/piper",
    )


class TestHealthDatabaseProbe2083:
    def test_answering_database_reads_healthy(self, monkeypatch):
        async def answers():
            return None

        _install(monkeypatch, answers)

        response = _client().get("/health")

        assert response.status_code == 200
        body = response.json()
        assert body["services"]["database"] == "healthy"
        # intent_service is absent on this bare app, so the top line is degraded for
        # THAT reason; the database line is the one under test here.
        assert body["status"] in ("healthy", "degraded")

    def test_failing_database_reads_unreachable_degraded_and_still_200(self, monkeypatch):
        async def refuses():
            raise ConnectionRefusedError(f"connection to {FAKE_DSN_HOST} refused")

        _install(monkeypatch, refuses)

        response = _client().get("/health")

        assert response.status_code == 200, "Fly restarts the machine on a non-200; never"
        body = response.json()
        assert body["services"]["database"] == "unreachable"
        assert body["status"] == "degraded"

    def test_body_never_carries_the_dsn_host_password_or_exception_text(self, monkeypatch):
        async def refuses():
            raise ConnectionRefusedError(
                f"connection to server at {FAKE_DSN_HOST} password {FAKE_DSN_PASSWORD} refused"
            )

        _install(monkeypatch, refuses)

        text = _client().get("/health").text

        assert FAKE_DSN_HOST not in text
        assert FAKE_DSN_PASSWORD not in text
        assert "refused" not in text
        assert "ConnectionRefusedError" not in text

    def test_hung_database_returns_within_the_bound_as_unreachable(self, monkeypatch):
        async def hangs():
            await asyncio.sleep(30)

        _install(monkeypatch, hangs, timeout=0.2)

        import time

        started = time.monotonic()
        body = _client().get("/health").json()
        elapsed = time.monotonic() - started

        assert body["services"]["database"] == "unreachable"
        assert body["status"] == "degraded"
        assert elapsed < 5.0, f"the probe must return inside Fly's 5 s check, took {elapsed:.1f}s"

    def test_health_stays_ungated_with_the_probe(self, monkeypatch):
        async def answers():
            return None

        _install(monkeypatch, answers)
        assert _client().get("/health").status_code == 200

    def test_probe_never_initializes_the_global_singleton_and_disposes_its_engine(
        self, monkeypatch
    ):
        """13716892ee's red: the probe initialized `services.database.connection.db`
        under the TestClient's loop and a cancelled asyncpg operation poisoned its pool,
        so later DB tests in the same process failed with "another operation is in
        progress". The probe must own its engine and let the singleton alone."""
        import services.database.connection as connection_module

        async def answers():
            return None

        _install(monkeypatch, answers)
        # A fresh, uninitialized singleton for this test only (an earlier test in the
        # same process may have initialized the real one; order must not matter).
        fresh = connection_module.DatabaseConnection()
        monkeypatch.setattr(connection_module, "db", fresh)
        before = _FakeEngine.disposed
        assert fresh._initialized is False

        _client().get("/health")

        assert fresh._initialized is False
        assert fresh.engine is None
        assert _FakeEngine.disposed == before + 1

    def test_hung_probe_still_disposes_its_engine(self, monkeypatch):
        async def hangs():
            await asyncio.sleep(30)

        _install(monkeypatch, hangs, timeout=0.2)
        before = _FakeEngine.disposed

        _client().get("/health")

        assert _FakeEngine.disposed == before + 1
