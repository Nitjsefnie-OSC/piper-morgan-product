#!/usr/bin/env python3
"""derive_subkey.py — print the scoped-subkey secret for a decrypt-only process (#1982).

Run on a machine that holds ENCRYPTION_MASTER_KEY (an alpha machine), and pipe the
single output line straight into the target app's secrets. No seat runs this and
reads the output; PM's hand does, in one pipe:

    fly ssh console -a piper-morgan -C \\
        "python scripts/derive_subkey.py user_api_keys.secret.github" \\
      | fly secrets import -a piper-morgan-mcp

Output is exactly ONE line, ``ENCRYPTION_SCOPED_SUBKEYS=<ctx>=<base64>[,<ctx>=<base64>]``,
the ``NAME=VALUE`` form ``fly secrets import`` reads from stdin. ``--value-only``
drops the ``NAME=`` prefix. Nothing else is printed to stdout, ever; diagnostics go
to stderr and never include key material.

The value is a credential (HOST's condition 3): it must not pass through any seat's
tool output, a CI log, or a tracked file. If it does, rotate it (re-derive after a
master-key rotation); scrubbing is not a fix.
"""

from __future__ import annotations

import argparse
import os
import sys


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "contexts", nargs="+", help="HKDF context label(s), e.g. user_api_keys.secret.github"
    )
    ap.add_argument(
        "--value-only", action="store_true", help="omit the ENCRYPTION_SCOPED_SUBKEYS= prefix"
    )
    args = ap.parse_args(argv)

    from services.security.field_encryption import (  # noqa: PLC0415
        ENV_MASTER_KEY,
        ENV_SCOPED_SUBKEYS,
        FieldEncryptionService,
        format_scoped_subkeys,
    )

    if not os.getenv(ENV_MASTER_KEY):
        print(
            f"derive_subkey: {ENV_MASTER_KEY} is not set in this environment; run on an alpha machine",
            file=sys.stderr,
        )
        return 2
    svc = FieldEncryptionService.from_env()
    if svc is None or svc.is_scoped:
        print("derive_subkey: needs a master-mode encryption service", file=sys.stderr)
        return 2
    seen: list[str] = []
    for ctx in args.contexts:
        if ctx in seen:
            print(f"derive_subkey: context {ctx!r} given twice", file=sys.stderr)
            return 2
        seen.append(ctx)
    line = format_scoped_subkeys({ctx: svc.export_subkey(ctx) for ctx in seen})
    if not args.value_only:
        line = f"{ENV_SCOPED_SUBKEYS}={line}"
    sys.stdout.write(line + "\n")
    sys.stdout.flush()
    print(f"derive_subkey: wrote 1 line for {len(seen)} context(s) to stdout", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
