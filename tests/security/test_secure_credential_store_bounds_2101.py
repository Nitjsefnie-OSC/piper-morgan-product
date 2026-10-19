"""#2101 — the hosted credential store's synchronous reads are bounded.

PA's log window for the 16:13 alpha stall (2026-10-19): 33 s of silence inside a chat
turn, Fly's health check failing, no process restart, no DB-side error. Every
``EncryptedDBCredentialStore`` read is a synchronous psycopg2 connect on the event loop
(NullPool), and a chat turn reads several credentials. Three bounds: a connect timeout, a
short per-name read cache that writes and deletes invalidate, and a WARNING on a slow read.

LAYER: the store against a fake engine (no database). DENOMINATOR: the engine's connect
args, cache hit / expiry / invalidation on store and delete, the slow-read warning.
"""

from __future__ import annotations

import itertools
from contextlib import contextmanager
from unittest.mock import patch

import pytest

from services.infrastructure import secure_credential_store as mod
from services.infrastructure.secure_credential_store import EncryptedDBCredentialStore


class _Enc:
    def encrypt(self, value, ctx):
        return f"enc:{value}"

    def decrypt(self, value, ctx):
        return value.split("enc:", 1)[1]


class _Row(tuple):
    pass


class _FakeEngine:
    """Counts connects; answers one row for name 'k'."""

    def __init__(self):
        self.connects = 0
        self.rows = {"k": ("enc:v1",)}

    @contextmanager
    def connect(self):
        self.connects += 1
        yield self

    @contextmanager
    def begin(self):
        self.connects += 1
        yield self

    def execute(self, stmt, params=None):
        eng = self

        class _R:
            def first(self_inner):
                return eng.rows.get((params or {}).get("name"))

            rowcount = 1

        if "INSERT" in str(stmt):
            self.rows[params["name"]] = (params["val"],)
        if "DELETE" in str(stmt):
            self.rows.pop(params["name"], None)
        return _R()


def _store():
    eng = _FakeEngine()
    return EncryptedDBCredentialStore(encryptor=_Enc(), engine=eng), eng


class TestConnectTimeout:
    def test_engine_is_built_with_a_connect_timeout(self, monkeypatch):
        captured = {}

        def fake_create_engine(url, **kw):
            captured.update(kw)
            return _FakeEngine()

        monkeypatch.setattr(mod, "create_engine", fake_create_engine)
        monkeypatch.setattr(
            "services.database.session_factory.get_sync_migration_url", lambda: "postgresql://x"
        )
        store = EncryptedDBCredentialStore(encryptor=_Enc())
        store._get_engine()
        assert captured["connect_args"] == {"connect_timeout": mod.CONNECT_TIMEOUT_SECONDS}
        assert 1 <= mod.CONNECT_TIMEOUT_SECONDS <= 10


class TestReadCache:
    def test_second_read_within_ttl_does_not_connect(self):
        store, eng = _store()
        assert store.get("k") == "v1"
        assert store.get("k") == "v1"
        assert eng.connects == 1

    def test_a_miss_is_cached_too(self):
        store, eng = _store()
        assert store.get("absent") is None
        assert store.get("absent") is None
        assert eng.connects == 1

    def test_store_invalidates_its_name(self):
        store, eng = _store()
        assert store.get("k") == "v1"
        store.store("k", "v2")
        assert store.get("k") == "v2"

    def test_delete_invalidates_its_name(self):
        store, eng = _store()
        assert store.get("k") == "v1"
        store.delete("k")
        assert store.get("k") is None

    def test_expiry_reconnects(self, monkeypatch):
        store, eng = _store()
        clock = {"t": 1000.0}
        monkeypatch.setattr(mod, "_clock", lambda: clock["t"])
        assert store.get("k") == "v1"
        clock["t"] += mod.READ_CACHE_TTL_SECONDS + 1
        assert store.get("k") == "v1"
        assert eng.connects == 2


class TestSlowReadWarning:
    def test_a_slow_read_is_logged(self, monkeypatch):
        store, eng = _store()
        # The store's own clock is patched, never time.monotonic (asyncio reads it).
        ticks = itertools.chain([0.0, 3.0], itertools.repeat(3.0))
        monkeypatch.setattr(mod, "_clock", lambda: next(ticks))
        with patch.object(mod.logger, "warning") as warn:
            store.get("k")
        warn.assert_called_once()
        assert warn.call_args.args[0] == "credential_store_slow_read"
        assert warn.call_args.kwargs["elapsed_s"] >= mod.SLOW_READ_SECONDS

    def test_a_fast_read_is_not_logged(self):
        store, eng = _store()
        with patch.object(mod.logger, "warning") as warn:
            store.get("k")
        warn.assert_not_called()
