"""#1382 tier-2 — encrypted-at-rest DB credential store (the hosted keychain).

Hosted Linux containers have no OS keyring backend (python-keyring resolves to
``keyring.backends.fail.Keyring``, whose every operation raises — found live on
alpha 2026-07-08, where it broke OAuth token storage and all keychain reads).
This store is the drop-in fallback BEHIND the ``KeychainService`` seam: same
composed key names, values encrypted with ``FieldEncryptionService`` under a
per-name HKDF context (``secure_credentials.{name}``) into the
``secure_credentials`` table (migration g1382creds). No plaintext is ever
written; with no master key the store REFUSES to construct (fail closed) —
``keyrings.alt``-style plaintext fallbacks are explicitly rejected.

Sync by design: ``KeychainService`` is a sync interface called from sync and
async contexts alike. Credential ops are settings/connect-time rare, so a
small dedicated sync engine (NOT the app's async pool) is the honest trade —
flagged in the 2026-07-09 design memo to Arch.

Relationship to the connector-binding rail (ADR-070): this is the general
hosted store; each connector's #1232-contract port migrates its grant onto the
binding rail as it lands, shrinking this store's connector share naturally.
"""

from __future__ import annotations

import threading
import time
from typing import Dict, List, Optional, Tuple

import structlog
from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool

logger = structlog.get_logger(__name__)

_CONTEXT_PREFIX = "secure_credentials."

# #2101 (alpha stalls, 2026-10-19): every read here is a SYNCHRONOUS psycopg2
# connect on the event loop (NullPool: a fresh connection per op), and the chat
# path reads several credentials per turn (integration status, GitHub config,
# the calendar adapter). When the proxy is slow the loop freezes for the connect
# duration; PA's log window showed a 33 s silence with no DB-side error. Three
# bounds, none of them the architectural fix (that is Arch's: move the reads
# off the loop or onto the async engine):
#   - a connect timeout, so one hung connect costs at most this many seconds;
#   - a short in-process read cache, so a turn pays one connect per name per
#     TTL instead of one per read (writes and deletes invalidate their name);
#   - a WARNING when a read takes longer than SLOW_READ_SECONDS, so the next
#     stall's log names the call.
CONNECT_TIMEOUT_SECONDS = 5
READ_CACHE_TTL_SECONDS = 60.0
SLOW_READ_SECONDS = 1.0

# The store's clock, patchable in tests WITHOUT touching time.monotonic itself
# (asyncio's event loop reads time.monotonic; patching it globally stopped the
# loop in every later async test of the same run, the 4 errors of 1a38f0d775).
_clock = time.monotonic

# Arch (#2101 ruling, comment 6280164505): the read cache is PROCESS-WIDE, not
# per instance. KeychainService() builds a fresh store on every construction
# (43 sites), so a per-instance cache barely bounded the chat path and let a
# long-lived instance serve a deleted credential for up to 60 s. One dict,
# keyed by name: a write or delete through any instance is seen by every other.
_READ_CACHE: Dict[str, Tuple[Optional[str], float]] = {}
_READ_CACHE_LOCK = threading.Lock()
# #2101 (Arch): a per-name generation. ``_forget`` bumps it; a read that started under an
# older generation does not store its value, so a delete or write that lands while a read
# is in flight can never be overwritten by that read's stale answer. One-process
# assumption: the cache and its generations live in this process only; a second app
# process would not see this one's invalidations (alpha runs one machine; see the
# module docstring).
_READ_GENERATION: Dict[str, int] = {}


class EncryptedDBCredentialStore:
    """Encrypted credential storage in Postgres, keyed by composed name."""

    def __init__(self, encryptor=None, engine=None):
        if encryptor is None:
            from services.security.field_encryption import FieldEncryptionService

            encryptor = FieldEncryptionService.from_env()
        if encryptor is None:
            # Fail closed: no master key means no secure place to put a secret.
            raise RuntimeError(
                "EncryptedDBCredentialStore requires ENCRYPTION_MASTER_KEY — "
                "refusing to store credentials without encryption (#1382)."
            )
        self._encryptor = encryptor
        self._engine = engine
        self._engine_lock = threading.Lock()

    def _get_engine(self):
        if self._engine is None:
            with self._engine_lock:
                if self._engine is None:
                    from services.database.session_factory import get_sync_migration_url

                    # NullPool per the Arch concur's build-note (2026-07-09):
                    # "short-lived = actually short-lived." Ops are rare
                    # (connect/settings-time), so every op opens and truly
                    # closes its connection — no idle sync connection parked
                    # against Postgres for the process lifetime.
                    self._engine = create_engine(
                        get_sync_migration_url(),
                        poolclass=NullPool,
                        connect_args={"connect_timeout": CONNECT_TIMEOUT_SECONDS},
                    )
        return self._engine

    def store(self, name: str, value: str) -> None:
        encrypted = self._encryptor.encrypt(value, _CONTEXT_PREFIX + name)
        with self._get_engine().begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO secure_credentials (name, encrypted_value) "
                    "VALUES (:name, :val) "
                    "ON CONFLICT (name) DO UPDATE SET "
                    "encrypted_value = EXCLUDED.encrypted_value, updated_at = now()"
                ),
                {"name": name, "val": encrypted},
            )
        self._forget(name)
        logger.info("credential_stored_db", name=name)

    @staticmethod
    def _forget(name: str) -> None:
        with _READ_CACHE_LOCK:
            _READ_CACHE.pop(name, None)
            _READ_GENERATION[name] = _READ_GENERATION.get(name, 0) + 1

    @staticmethod
    def _generation(name: str) -> int:
        with _READ_CACHE_LOCK:
            return _READ_GENERATION.get(name, 0)

    @staticmethod
    def _cached(name: str) -> Tuple[bool, Optional[str]]:
        with _READ_CACHE_LOCK:
            hit = _READ_CACHE.get(name)
            if hit is None:
                return False, None
            value, expires = hit
            if _clock() >= expires:
                _READ_CACHE.pop(name, None)
                return False, None
            return True, value

    def get(self, name: str) -> Optional[str]:
        found, value = self._cached(name)
        if found:
            return value
        generation = self._generation(name)
        started = _clock()
        with self._get_engine().connect() as conn:
            row = conn.execute(
                text("SELECT encrypted_value FROM secure_credentials WHERE name = :name"),
                {"name": name},
            ).first()
        elapsed = _clock() - started
        if elapsed >= SLOW_READ_SECONDS:
            # #2101: this read ran on the event loop; a slow one is the stall.
            logger.warning("credential_store_slow_read", name=name, elapsed_s=round(elapsed, 2))
        value = None if row is None else self._encryptor.decrypt(row[0], _CONTEXT_PREFIX + name)
        with _READ_CACHE_LOCK:
            if _READ_GENERATION.get(name, 0) == generation:
                _READ_CACHE[name] = (value, _clock() + READ_CACHE_TTL_SECONDS)
        return value

    def delete(self, name: str) -> bool:
        with self._get_engine().begin() as conn:
            result = conn.execute(
                text("DELETE FROM secure_credentials WHERE name = :name"), {"name": name}
            )
        deleted = result.rowcount > 0
        self._forget(name)
        if deleted:
            logger.info("credential_deleted_db", name=name)
        return deleted

    def list_names(self) -> List[str]:
        with self._get_engine().connect() as conn:
            rows = conn.execute(text("SELECT name FROM secure_credentials ORDER BY name")).all()
        return [r[0] for r in rows]
