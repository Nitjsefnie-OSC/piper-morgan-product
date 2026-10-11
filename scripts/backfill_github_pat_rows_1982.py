#!/usr/bin/env python3
"""backfill_github_pat_rows_1982.py — copy PATs saved before the #1982 dual write into
``user_api_keys`` (provider ``github``, GitHub-only HKDF context), gated like the
re-encrypt (HOST's condition 2). Runs on a machine that holds ENCRYPTION_MASTER_KEY
(an alpha machine, via ``fly ssh console -a piper-morgan -C "python scripts/…"``).

Source rows: ``secure_credentials`` names of the form ``<uid>_github_token_api_key``
(the KeychainService name Settings → GitHub writes), each encrypted under its own
per-user context ``secure_credentials.<name>``. The keychain copy is NOT deleted:
alpha's sync readers use it.

    (no flags)                  DRY RUN: counts (source rows, already present, to write,
                                unparseable, undecryptable, no such user), writes nothing.
    --apply --snapshot "<id>"   writes each missing row through
                                UserAPIKeyService.store_user_key(validate=False), then
                                reads every written row back and checks it equals the
                                keychain value (never printed). Refuses without --snapshot
                                and refuses if any source row is undecryptable.

Exit: 0 clean, 1 a row failed, 2 refused. Prints counts and user ids only.
"""

from __future__ import annotations

import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # prod_db, next to this file

_UUID = r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
NAME_RE = re.compile(rf"^(?P<uid>{_UUID})_github_token_api_key$")


def parse_name(name: str) -> str | None:
    """``<uid>_github_token_api_key`` → uid, else None (not a user PAT row)."""
    m = NAME_RE.match(name)
    return m.group("uid") if m else None


async def _run_async(*, apply: bool, snapshot: str | None) -> int:
    from prod_db import _database_url, _redacted  # noqa: PLC0415
    from sqlalchemy import create_engine, text  # noqa: PLC0415

    from services.security.field_encryption import (  # noqa: PLC0415
        ENV_MASTER_KEY,
        DecryptionError,
        FieldEncryptionService,
    )

    enc = FieldEncryptionService.from_env()
    if enc is None or enc.is_scoped:
        print(f"!!! {ENV_MASTER_KEY} is required (master mode); refusing", file=sys.stderr)
        return 2
    if apply and not snapshot:
        print("!!! --apply requires --snapshot '<id or note>' (HOST condition 2); refusing")
        return 2

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== #1982 GitHub PAT backfill {mode} ===")
    url, source = _database_url()
    print(f"--- target: {_redacted(url)}  (resolved via {source})")
    if snapshot:
        print(f"--- operator-asserted DB snapshot: {snapshot}")

    eng = create_engine(url)
    with eng.connect() as c:
        names = [
            r[0]
            for r in c.execute(
                text("SELECT name FROM secure_credentials WHERE name LIKE :pat ORDER BY name"),
                {"pat": r"%\_github\_token\_api\_key"},
            ).all()
        ]
        present = {
            str(r[0])
            for r in c.execute(
                text(
                    "SELECT user_id FROM user_api_keys WHERE provider = 'github' "
                    "AND encrypted_secret IS NOT NULL AND is_active"
                )
            ).all()
        }
        users = {str(r[0]) for r in c.execute(text("SELECT id FROM users")).all()}

    todo: list[tuple[str, str]] = []  # (uid, name)
    unparseable = already = no_user = 0
    undecryptable: list[str] = []
    for name in names:
        uid = parse_name(name)
        if uid is None:
            unparseable += 1
            continue
        if uid not in users:
            no_user += 1
            continue
        if uid in present:
            already += 1
            continue
        todo.append((uid, name))

    # Dry-run phase: every candidate must decrypt under its own keychain context.
    plain: dict[str, str] = {}
    with eng.connect() as c:
        for uid, name in todo:
            row = c.execute(
                text("SELECT encrypted_value FROM secure_credentials WHERE name = :n"), {"n": name}
            ).first()
            try:
                plain[uid] = enc.decrypt(row[0], "secure_credentials." + name)
            except DecryptionError:
                undecryptable.append(uid)
    print(
        f"--- before: source={len(names)} unparseable={unparseable} no_user={no_user} "
        f"already_present={already} to_write={len(todo)} undecryptable={len(undecryptable)} "
        f"{undecryptable if undecryptable else ''}"
    )
    if undecryptable:
        print("!!! a source row cannot be decrypted; nothing written")
        return 1
    if not apply:
        print(
            f"DRY-RUN complete — no writes. Re-run with --apply --snapshot '<id>' to write {len(todo)} row(s)."
        )
        return 0
    if not todo:
        print("--- nothing to write")
        return 0

    from services.database.session_factory import AsyncSessionFactory  # noqa: PLC0415
    from services.security.user_api_key_service import UserAPIKeyService  # noqa: PLC0415

    svc = UserAPIKeyService()
    written: list[str] = []
    failed: list[str] = []
    for uid, _name in todo:
        try:
            async with AsyncSessionFactory.session_scope_fresh() as session:
                await svc.store_user_key(
                    session, uid, "github", plain[uid], validate=False, security_check=False
                )
            written.append(uid)
        except Exception as exc:  # noqa: BLE001 — report per row, keep going
            print(f"!!! write failed for user {uid}: {type(exc).__name__}")
            failed.append(uid)
    verified = 0
    for uid in written:
        async with AsyncSessionFactory.session_scope_fresh() as session:
            back = await svc.retrieve_user_key(session, uid, "github")
        if back == plain[uid]:
            verified += 1
        else:
            failed.append(uid)
    plain.clear()
    print(f"--- after: written={len(written)} verified={verified} failed={failed if failed else 0}")
    if failed:
        print("!!! at least one row did not round-trip; see the ids above")
        return 1
    print("APPLY complete — every backfilled PAT reads back under the GitHub context.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--apply", action="store_true", help="write the missing rows (default: dry run)"
    )
    ap.add_argument(
        "--snapshot", default=None, help="id or note of the DB snapshot taken before --apply"
    )
    args = ap.parse_args(argv)
    return asyncio.run(_run_async(apply=args.apply, snapshot=args.snapshot))


if __name__ == "__main__":
    raise SystemExit(main())
