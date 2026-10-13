#!/usr/bin/env python3
"""reencrypt_github_secrets_1982.py — move GitHub credential rows to their own HKDF
context, gated the way HOST's condition 2 on #1982 requires.

Runs on a machine that holds ENCRYPTION_MASTER_KEY (an alpha machine, via
``fly ssh console -a piper-morgan -C "python scripts/reencrypt_github_secrets_1982.py"``).
It never prints a secret, a token, or a key: only counts and row ids.

Rows in scope: ``user_api_keys`` where ``provider`` is one of GITHUB_PROVIDERS and
``encrypted_secret`` is not NULL.

    (no flags)         DRY RUN. Counts rows under the legacy context and the new
                       context, decrypts every legacy row and re-encrypts it to a
                       scratch value (round-tripped), writes nothing.
    --apply --snapshot vs_<id>
                       Re-encrypts the legacy rows in one transaction, then re-reads
                       every GitHub row and decrypt-round-trips it under the new
                       context. Refuses without --snapshot (the operator asserts a DB
                       snapshot exists; the value is echoed into the report so the
                       claim is on the record), refuses a value that is not shaped
                       like a Fly volume snapshot id (``vs_`` + alphanumerics: on
                       2026-10-13 the literal placeholder ``<snapshot-id>`` was
                       accepted, so the "snapshot exists" claim was empty), and
                       refuses if the dry-run phase finds any row it cannot decrypt.
                       Existence is not checked here: this runs inside the app
                       machine, which has no flyctl. The operator's ``fly volumes
                       snapshots list`` output is the existence evidence.

Exit status: 0 on a clean run (including a dry run), 1 if any row is undecryptable,
2 on a refused --apply. When the final report reads ``legacy=0``, flip
``GITHUB_LEGACY_CONTEXT_FALLBACK`` to False in services/security/user_api_key_service.py
in the same commit that records the count.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # prod_db, next to this file


@dataclass
class Report:
    total: int = 0
    new_ctx: int = 0
    legacy: int = 0
    undecryptable: list[int] = field(default_factory=list)
    rewritten: int = 0
    verified_after: int = 0
    failed_after: list[int] = field(default_factory=list)


def classify(enc, token: str, new_ctx: str, legacy_ctx: str) -> str:
    """'new' | 'legacy' | 'undecryptable' for one stored token. Plaintext never leaves."""
    from services.security.field_encryption import DecryptionError  # noqa: PLC0415

    try:
        enc.decrypt(token, new_ctx)
        return "new"
    except DecryptionError:
        pass
    try:
        enc.decrypt(token, legacy_ctx)
        return "legacy"
    except DecryptionError:
        return "undecryptable"


# A Fly volume snapshot id: ``vs_`` then alphanumerics (observed: 24 characters after
# the prefix). Anything else is a placeholder or a note, which is not a snapshot.
SNAPSHOT_ID_RE = re.compile(r"^vs_[A-Za-z0-9]{8,}$")


def is_snapshot_id(value: str | None) -> bool:
    """True when ``value`` is shaped like a Fly volume snapshot id (not its existence)."""
    return bool(value) and SNAPSHOT_ID_RE.match(value or "") is not None


def run(*, apply: bool, snapshot: str | None) -> int:
    from prod_db import _database_url, _redacted  # noqa: PLC0415
    from sqlalchemy import create_engine, text  # noqa: PLC0415

    from services.security.field_encryption import (  # noqa: PLC0415
        ENV_MASTER_KEY,
        FieldEncryptionService,
    )
    from services.security.user_api_key_service import (  # noqa: PLC0415
        GITHUB_PROVIDERS,
        GITHUB_SECRET_CONTEXT,
        USER_SECRET_CONTEXT,
    )

    enc = FieldEncryptionService.from_env()
    if enc is None or enc.is_scoped:
        print(f"!!! {ENV_MASTER_KEY} is required (master mode); refusing", file=sys.stderr)
        return 2
    if apply and not snapshot:
        print("!!! --apply requires --snapshot vs_<id> (HOST condition 2); refusing")
        return 2
    if apply and not is_snapshot_id(snapshot):
        print(
            f"!!! --snapshot {snapshot!r} is not a Fly volume snapshot id (vs_ + alphanumerics); "
            "a placeholder or a note is not a snapshot. Run `fly volumes snapshots list "
            "<vol-id> -a piper-morgan-db` and pass the newest id; refusing"
        )
        return 2

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== #1982 GitHub secret re-encrypt {mode} ===")
    url, source = _database_url()
    print(f"--- target: {_redacted(url)}  (resolved via {source})")
    print(f"--- contexts: legacy={USER_SECRET_CONTEXT!r} new={GITHUB_SECRET_CONTEXT!r}")
    print(f"--- providers: {sorted(GITHUB_PROVIDERS)}")
    if snapshot:
        print(f"--- operator-asserted DB snapshot: {snapshot}")

    rep = Report()
    select_rows = text(
        "SELECT id, encrypted_secret FROM user_api_keys "
        "WHERE provider = ANY(:providers) AND encrypted_secret IS NOT NULL ORDER BY id"
    )
    params = {"providers": sorted(GITHUB_PROVIDERS)}
    eng = create_engine(url)

    # Phase 1 — census + no-write dry run (always).
    scratch: dict[int, str] = {}
    with eng.connect() as c:
        rows = c.execute(select_rows, params).all()
    rep.total = len(rows)
    for row_id, token in rows:
        kind = classify(enc, token, GITHUB_SECRET_CONTEXT, USER_SECRET_CONTEXT)
        if kind == "new":
            rep.new_ctx += 1
        elif kind == "legacy":
            rep.legacy += 1
            plain = enc.decrypt(token, USER_SECRET_CONTEXT)
            new_token = enc.encrypt(plain, GITHUB_SECRET_CONTEXT)
            if enc.decrypt(new_token, GITHUB_SECRET_CONTEXT) != plain:
                rep.undecryptable.append(row_id)  # round-trip failed; treat as unsafe
            else:
                scratch[row_id] = new_token
            del plain
        else:
            rep.undecryptable.append(row_id)
    print(
        f"--- before: total={rep.total} new={rep.new_ctx} legacy={rep.legacy} "
        f"undecryptable={len(rep.undecryptable)} {rep.undecryptable if rep.undecryptable else ''}"
    )
    if rep.undecryptable:
        print("!!! at least one row cannot be decrypted under either context; nothing written")
        return 1
    if not apply:
        print(
            "DRY-RUN complete — no writes. Re-run with --apply --snapshot vs_<id> to rewrite "
            f"the {rep.legacy} legacy row(s)."
        )
        return 0
    if rep.legacy == 0:
        print("--- nothing to rewrite (legacy=0); no transaction opened")
        return 0

    # Phase 2 — one transaction, then a full re-read verification.
    with eng.begin() as c:
        for row_id, new_token in scratch.items():
            res = c.execute(
                text("UPDATE user_api_keys SET encrypted_secret = :tok WHERE id = :id"),
                {"tok": new_token, "id": row_id},
            )
            rep.rewritten += res.rowcount
    with eng.connect() as c:
        after = c.execute(select_rows, params).all()
    legacy_after = 0
    for row_id, token in after:
        kind = classify(enc, token, GITHUB_SECRET_CONTEXT, USER_SECRET_CONTEXT)
        if kind == "new":
            rep.verified_after += 1
        elif kind == "legacy":
            legacy_after += 1
        else:
            rep.failed_after.append(row_id)
    print(
        f"--- after: total={len(after)} rewritten={rep.rewritten} verified_new={rep.verified_after} "
        f"legacy={legacy_after} failed={rep.failed_after if rep.failed_after else 0}"
    )
    if rep.failed_after or legacy_after:
        print(
            "!!! post-write verification did not read clean; restore from the snapshot named above"
        )
        return 1
    print(
        "APPLY complete — every GitHub row decrypts under the new context; legacy=0. "
        "Now flip GITHUB_LEGACY_CONTEXT_FALLBACK to False and record this count."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="rewrite legacy rows (default: dry run)")
    ap.add_argument(
        "--snapshot",
        default=None,
        help="id (vs_…) of the DB volume snapshot taken before --apply; a note is refused",
    )
    args = ap.parse_args(argv)
    return run(apply=args.apply, snapshot=args.snapshot)


if __name__ == "__main__":
    raise SystemExit(main())
