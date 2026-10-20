"""#2101 — the credential store's async surface and the read-cache generation counter.

Arch's shape (2026-10-19): ``KeychainService`` gains ``aget_api_key`` / ``aread_secret`` /
``astore_api_key`` / ``adelete_api_key``, each the sync op in ``asyncio.to_thread``, so a
coroutine on the chat path no longer blocks the event loop for a store connect; and the
process-wide read cache carries a per-name generation so a delete that lands while a read
is in flight is never overwritten by that read's stale answer.

LAYER: ``KeychainService`` with its sync methods replaced by instrumented fakes (no store,
no keyring), and ``EncryptedDBCredentialStore`` against a fake engine (no database).
DENOMINATOR: the four async methods delegate with the same arguments and return; a read
runs off the loop's thread; two slow reads overlap; the generation interleaving.
"""

from __future__ import annotations

import asyncio
import threading
import time
from contextlib import contextmanager

import pytest

from services.infrastructure import secure_credential_store as mod
from services.infrastructure.keychain_service import KeychainService, SecretProvenance, SecretRead
from services.infrastructure.secure_credential_store import EncryptedDBCredentialStore


def _service() -> KeychainService:
    svc = KeychainService.__new__(KeychainService)
    svc.service_name = "test"
    svc._db_store = None
    svc._no_secure_store = None
    return svc


@pytest.fixture(autouse=True)
def _clear_cache():
    mod._READ_CACHE.clear()
    mod._READ_GENERATION.clear()
    yield
    mod._READ_CACHE.clear()
    mod._READ_GENERATION.clear()


class TestAsyncSurface:
    def test_aget_runs_off_the_loop_thread_and_returns_the_value(self):
        svc = _service()
        seen = {}

        def fake_get(provider, username=None):
            seen["thread"] = threading.current_thread()
            seen["args"] = (provider, username)
            return "v1"

        svc.get_api_key = fake_get  # type: ignore[method-assign]

        async def run():
            loop_thread = threading.current_thread()
            value = await svc.aget_api_key("github_token", username="u1")
            return value, loop_thread

        value, loop_thread = asyncio.run(run())
        assert value == "v1"
        assert seen["args"] == ("github_token", "u1")
        assert seen["thread"] is not loop_thread

    def test_aread_secret_delegates(self):
        svc = _service()
        svc.read_secret = lambda p, u=None: SecretRead(SecretProvenance.PRESENT, value="s")  # type: ignore[method-assign]
        got = asyncio.run(svc.aread_secret("slack_bot", username="u"))
        assert got.provenance is SecretProvenance.PRESENT and got.value == "s"

    def test_astore_and_adelete_delegate_with_their_contracts(self):
        svc = _service()
        calls = []
        svc.store_api_key = lambda p, k, u=None: calls.append(("store", p, k, u))  # type: ignore[method-assign]
        svc.delete_api_key = lambda p, u=None: calls.append(("delete", p, u)) or True  # type: ignore[method-assign]

        async def run():
            await svc.astore_api_key("github_token", "tok", username="u1")
            return await svc.adelete_api_key("github_token", username="u1")

        assert asyncio.run(run()) is True
        assert calls == [("store", "github_token", "tok", "u1"), ("delete", "github_token", "u1")]

    def test_astore_raises_as_the_sync_method_does(self):
        svc = _service()

        def boom(p, k, u=None):
            raise RuntimeError("Failed to store API key: no store")

        svc.store_api_key = boom  # type: ignore[method-assign]
        with pytest.raises(RuntimeError, match="no store"):
            asyncio.run(svc.astore_api_key("x", "y"))

    def test_two_slow_reads_overlap_instead_of_queueing_on_the_loop(self):
        svc = _service()

        def slow_get(provider, username=None):
            time.sleep(0.2)
            return provider

        svc.get_api_key = slow_get  # type: ignore[method-assign]

        async def run():
            started = time.monotonic()
            a, b = await asyncio.gather(svc.aget_api_key("a"), svc.aget_api_key("b"))
            return a, b, time.monotonic() - started

        a, b, elapsed = asyncio.run(run())
        assert (a, b) == ("a", "b")
        assert elapsed < 0.38, f"two 0.2 s reads took {elapsed:.2f} s: they ran one after the other"


class _Enc:
    def encrypt(self, value, ctx):
        return f"enc:{value}"

    def decrypt(self, value, ctx):
        return value.split("enc:", 1)[1]


class _Engine:
    """Answers one row for 'k'; ``during_fetch`` runs inside the connect, before the row."""

    def __init__(self):
        self.rows = {"k": ("enc:v1",)}
        self.during_fetch = None
        self.connects = 0

    @contextmanager
    def connect(self):
        self.connects += 1
        if self.during_fetch is not None:
            hook, self.during_fetch = self.during_fetch, None
            hook()
        yield self

    def execute(self, stmt, params=None):
        eng = self

        class _R:
            def first(self_inner):
                return eng.rows.get((params or {}).get("name"))

        return _R()


def _store(engine):
    st = EncryptedDBCredentialStore.__new__(EncryptedDBCredentialStore)
    st._encryptor = _Enc()
    st._engine = engine
    st._get_engine = lambda: engine  # type: ignore[method-assign]
    return st


class TestReadGeneration:
    def test_forget_bumps_the_generation(self):
        assert EncryptedDBCredentialStore._generation("k") == 0
        EncryptedDBCredentialStore._forget("k")
        EncryptedDBCredentialStore._forget("k")
        assert EncryptedDBCredentialStore._generation("k") == 2

    def test_a_read_that_overlaps_a_forget_does_not_cache_its_stale_answer(self):
        eng = _Engine()
        st = _store(eng)
        # The delete lands while the read is inside its connect: the read must not
        # store v1 under the generation the delete already retired.
        eng.during_fetch = lambda: EncryptedDBCredentialStore._forget("k")
        assert st.get("k") == "v1"
        assert "k" not in mod._READ_CACHE
        # The next read goes to the store again (and sees whatever is there now).
        eng.rows.pop("k")
        assert st.get("k") is None
        assert eng.connects == 2

    def test_an_undisturbed_read_caches_under_its_generation(self):
        eng = _Engine()
        st = _store(eng)
        assert st.get("k") == "v1"
        assert mod._READ_CACHE["k"][0] == "v1"
        assert st.get("k") == "v1"
        assert eng.connects == 1
