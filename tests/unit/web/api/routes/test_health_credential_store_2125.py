"""#2125, Arch's point (2): the encryptor is probed at startup and /health reads the
credential store, so a box whose master key is unusable reads degraded before anyone
presses Validate (and the promote step's health refusal holds)."""

from __future__ import annotations

import base64
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.testclient import TestClient

import web.api.routes.admin as admin_module
from services.infrastructure import turn_activity
from services.security import field_encryption
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


def _install(monkeypatch, master_key_bytes: int | None):
    monkeypatch.setattr(admin_module, "create_async_engine", lambda *a, **k: _FakeEngine())
    monkeypatch.setenv("DATABASE_URL", "postgresql://piper:pw@db-x.flycast:5432/piper")
    monkeypatch.setattr(turn_activity, "TURN_ACTIVITY", turn_activity.TurnActivity())
    monkeypatch.delenv("ENCRYPTION_SCOPED_SUBKEYS", raising=False)
    if master_key_bytes is None:
        monkeypatch.delenv("ENCRYPTION_MASTER_KEY", raising=False)
    else:
        monkeypatch.setenv(
            "ENCRYPTION_MASTER_KEY", base64.b64encode(b"x" * master_key_bytes).decode()
        )
    field_encryption.reset_credential_store_probe()


def test_a_48_byte_master_key_reads_the_credential_store_unavailable_and_degraded(monkeypatch):
    """Arch's pin (2): staging's key, as /health would have read it."""
    _install(monkeypatch, 48)
    body = _client().get("/health").json()
    assert body["services"]["credential_store"] == "unavailable"
    assert body["status"] == "degraded"
    assert "master_key" not in str(body)  # the parameter never reaches the public body
    field_encryption.reset_credential_store_probe()


def test_a_32_byte_master_key_reads_healthy(monkeypatch):
    _install(monkeypatch, 32)
    body = _client().get("/health").json()
    assert body["services"]["credential_store"] == "healthy"
    field_encryption.reset_credential_store_probe()


def test_no_master_key_reads_not_configured_and_does_not_degrade_on_a_local_box(monkeypatch):
    """A local dev box without the variable falls back to the OS keychain; boot is never
    refused and /health does not degrade for it."""
    _install(monkeypatch, None)
    monkeypatch.delenv("FLY_APP_NAME", raising=False)
    body = _client().get("/health").json()
    assert body["services"]["credential_store"] == "not_configured"
    # (the bare test app has no intent service, so the overall status is degraded for
    # that reason alone; the probe's own verdict is the assertion here)
    field_encryption.reset_credential_store_probe()


def test_no_master_key_on_a_fly_box_reads_unavailable_and_degraded(monkeypatch):
    """Arch 10-22 10:07: no OS keyring on a Fly machine, so a box missing the variable
    cannot store a key and must not read clear."""
    _install(monkeypatch, None)
    monkeypatch.setenv("FLY_APP_NAME", "piper-morgan-test")
    body = _client().get("/health").json()
    assert body["services"]["credential_store"] == "unavailable"
    assert body["status"] == "degraded"
    field_encryption.reset_credential_store_probe()


def test_scoped_subkeys_on_a_fly_box_read_healthy(monkeypatch):
    """The MCP app holds ENCRYPTION_SCOPED_SUBKEYS, never the master key (fly.mcp.toml)."""
    _install(monkeypatch, None)
    monkeypatch.setenv("FLY_APP_NAME", "piper-morgan-mcp-test")
    monkeypatch.setenv(
        "ENCRYPTION_SCOPED_SUBKEYS", "github=" + base64.b64encode(b"s" * 32).decode()
    )
    field_encryption.reset_credential_store_probe()
    assert field_encryption.probe_credential_store()["status"] == "healthy"
    field_encryption.reset_credential_store_probe()


def test_the_probe_is_cached_per_process_and_never_raises(monkeypatch):
    _install(monkeypatch, 48)
    first = field_encryption.probe_credential_store()
    monkeypatch.setenv("ENCRYPTION_MASTER_KEY", base64.b64encode(b"x" * 32).decode())
    assert field_encryption.probe_credential_store() == first  # cached
    assert field_encryption.probe_credential_store(force=True)["status"] == "healthy"
    field_encryption.reset_credential_store_probe()
