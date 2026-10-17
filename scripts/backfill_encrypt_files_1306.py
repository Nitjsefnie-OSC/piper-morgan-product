"""#1306 backfill — encrypt existing plaintext uploaded files on disk (zero-downtime).

Iterates uploaded_files rows' storage_paths (DB-known files only — orphans on
disk are unreachable through the product and are reported, not touched),
sniffs the marker, and encrypts unmarked files in place with the exact envelope
write_file_to_storage uses, so reads decrypt transparently mid-run.

Idempotent: marked files are skipped. REFUSES to run keyless.

    ENCRYPTION_MASTER_KEY=<base64-32B> POSTGRES_PORT=5433 \
        venv/bin/python -m scripts.backfill_encrypt_files_1306

Read-only first (Exec, 2026-10-16: the narrow step before a prod write):
    venv/bin/python -m scripts.backfill_encrypt_files_1306 --count
sniffs every DB-known file's marker and prints the same shape of counts
("plaintext" instead of "encrypted") without writing a byte; it needs no key.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from services.security.encrypted_types import MARKER
from services.security.field_encryption import FieldEncryptionService

_CONTEXT = "uploaded_files.content"
_MARKER_BYTES = MARKER.encode("ascii")


def require_encryptor() -> FieldEncryptionService:
    enc = FieldEncryptionService.from_env()
    if enc is None:
        print("ERROR: ENCRYPTION_MASTER_KEY unset — refusing to run.", file=sys.stderr)
        raise SystemExit(1)
    return enc


def _database_url() -> tuple[str, str]:
    """Resolve the DB URL the way the APP does: ``DATABASE_URL`` first (#1278, how
    alpha gets its database), then ``POSTGRES_*``. Returns ``(url, source)``.

    The old POSTGRES_*-only construction defaulted to localhost:5433, the dev
    database, so on alpha the count refused the connection before reading
    anything (Comms, 2026-10-17). The fallback is loud, never silent: a count
    against the wrong database looks identical to success.
    """
    try:
        from services.database.connection import db  # noqa: PLC0415

        return db._build_database_url(), "app config (services.database.connection)"
    except Exception as exc:  # noqa: BLE001 — fall back LOUDLY
        print(
            f"WARNING: app database config unavailable ({exc!r}); "
            "falling back to POSTGRES_* (dev defaults, localhost:5433)",
            file=sys.stderr,
        )
        user = os.getenv("POSTGRES_USER", "piper")
        password = os.getenv("POSTGRES_PASSWORD", "dev_changeme_in_production")
        host = os.getenv("POSTGRES_HOST", "localhost")
        port = os.getenv("POSTGRES_PORT", "5433")
        database = os.getenv("POSTGRES_DB", "piper_morgan")
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}", "POSTGRES_* env"


def classify_file(path: Path) -> str:
    """Read-only: 'plaintext' | 'already' | 'missing'. Never writes."""
    if not path.exists():
        return "missing"
    with path.open("rb") as fh:
        head = fh.read(len(_MARKER_BYTES))
    return "already" if head == _MARKER_BYTES else "plaintext"


def encrypt_file_in_place(path: Path, encryptor: FieldEncryptionService) -> str:
    """Returns 'encrypted' | 'already' | 'missing'."""
    state = classify_file(path)
    if state != "plaintext":
        return state
    data = path.read_bytes()
    path.write_bytes(_MARKER_BYTES + encryptor.encrypt_bytes(data, _CONTEXT))
    return "encrypted"


def run_over_paths(paths, encryptor, *, count_only: bool) -> dict:
    """The per-file loop, shared by --count and the write. With ``count_only``
    the encryptor is never consulted and no file changes."""
    if count_only:
        counts = {"plaintext": 0, "already": 0, "missing": 0}
        for p in paths:
            counts[classify_file(Path(p))] += 1
        return counts
    counts = {"encrypted": 0, "already": 0, "missing": 0}
    for p in paths:
        counts[encrypt_file_in_place(Path(p), encryptor)] += 1
    return counts


def format_counts(counts: dict, *, count_only: bool) -> str:
    if count_only:
        return (
            f"uploaded files: {counts['plaintext']} plaintext, {counts['already']} already encrypted, "
            f"{counts['missing']} missing-on-disk (count only, nothing written)"
        )
    return (
        f"uploaded files: {counts['encrypted']} encrypted, {counts['already']} already, "
        f"{counts['missing']} missing-on-disk"
    )


async def _fetch_storage_paths() -> list:
    url, source = _database_url()
    print(f"database: {source}", file=sys.stderr)
    engine = create_async_engine(url, pool_size=1, max_overflow=0)
    try:
        async with engine.connect() as conn:
            rows = (
                await conn.execute(
                    text("SELECT storage_path FROM uploaded_files WHERE storage_path IS NOT NULL")
                )
            ).fetchall()
    finally:
        await engine.dispose()
    return [storage_path for (storage_path,) in rows]


async def _main(count_only: bool) -> None:
    encryptor = None if count_only else require_encryptor()
    paths = await _fetch_storage_paths()
    counts = run_over_paths(paths, encryptor, count_only=count_only)
    print(format_counts(counts, count_only=count_only))


def _parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--count",
        action="store_true",
        help="read-only: sniff markers and print plaintext/already/missing counts; writes nothing; needs no key",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    asyncio.run(_main(count_only=_parse_args().count))
