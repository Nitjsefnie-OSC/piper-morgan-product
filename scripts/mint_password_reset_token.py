"""Mint a password-reset token for a specific user (#441/#1261 beta recovery).

The beta auth model's answer to "email me a reset link" with no mailer in the
product: PM/HOST runs this against the target DB, hands the printed code to the
tester over the #1344 invite channel, and the tester uses it at /reset-password.

Unlike mint_invite_tokens.py, a reset token is BOUND to one account at mint
time (identified here by username or email) and EXPIRES (default 72h). The
token value is single-use, enforced atomically at consumption
(services/auth/password_reset_service.py).

Usage (run from the repo root; needs PYTHONPATH=. for the services.* imports):
    PYTHONPATH=. python scripts/mint_password_reset_token.py xian            # dry-run
    PYTHONPATH=. python scripts/mint_password_reset_token.py xian --apply    # insert
    PYTHONPATH=. python scripts/mint_password_reset_token.py xian@pobox.com --apply
    PYTHONPATH=. python scripts/mint_password_reset_token.py xian --apply --ttl-hours 24
"""

import argparse

# 2026-10-18 (#1261 follow-up, xian's run on alpha): this script used to build
# its DSN from POSTGRES_* defaults (localhost:5433, the DEV database) behind a
# hard-coded dotenv path, so inside the prod container it refused with
# "connection to server at localhost, port 5433 failed". It now resolves the
# URL the way every other ops payload does (prod_db: the app's own config,
# loud fallback, refuses localhost in production).
from prod_db import (  # noqa: F401 — shared, side-effect free
    _database_url,
    _redacted,
    _to_sync_url,
)
from sqlalchemy import create_engine, text

from services.auth.password_reset_service import generate_reset_token  # noqa: E402

_FIND_USER = text(
    "SELECT id, username, email FROM users " "WHERE username = :ident OR email = :ident"
)
_INSERT = text(
    "INSERT INTO password_reset_tokens (token, user_id, created_at, expires_at) "
    "VALUES (:token, :user_id, now(), now() + make_interval(hours => :ttl))"
)


def _engine():
    url, source = _database_url()
    print(f"--- target: {_redacted(url)}  (resolved via {source})")
    return create_engine(url)


def main():
    ap = argparse.ArgumentParser(description="#441/#1261 mint a password-reset token")
    ap.add_argument("identifier", help="username OR email of the account to reset")
    ap.add_argument("--apply", action="store_true", help="execute (default: dry-run)")
    ap.add_argument("--ttl-hours", type=int, default=72, help="token lifetime (default 72)")
    args = ap.parse_args()

    eng = _engine()
    with eng.connect() as c:
        rows = c.execute(_FIND_USER, {"ident": args.identifier}).fetchall()
    if not rows:
        raise SystemExit(f"No user found with username/email '{args.identifier}' — nothing minted.")
    if len(rows) > 1:
        # username-equals-someone-else's-email collision: refuse rather than guess.
        listing = ", ".join(f"{r.username} <{r.email}>" for r in rows)
        raise SystemExit(
            f"Identifier matches multiple accounts ({listing}) — use the exact username."
        )

    user = rows[0]
    token = generate_reset_token()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"=== #441/#1261 reset-token mint {mode} ===")
    print(f"Account: {user.username} <{user.email}> ({user.id})")
    print(f"TTL: {args.ttl_hours}h")
    if args.apply:
        with eng.begin() as c:
            c.execute(_INSERT, {"token": token, "user_id": user.id, "ttl": args.ttl_hours})
        print(f"Token (hand to the tester, single-use, expires in {args.ttl_hours}h):")
    else:
        print("Token (DRY-RUN — not inserted; re-run with --apply):")
    print(token)


if __name__ == "__main__":
    main()
