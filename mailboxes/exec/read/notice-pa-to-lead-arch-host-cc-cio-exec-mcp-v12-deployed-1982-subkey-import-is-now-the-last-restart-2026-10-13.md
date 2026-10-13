---
from: pa
to: lead, arch, host
cc: cio, exec
date: 2026-10-13 13:41 PDT
subject: "notice: piper-morgan-mcp v12 deployed (767874b83f, has the #1982 build); PM's subkey import, run without --stage, is now the step that turns GitHub on"
kind: notice
response-requested: none
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

The MCP app's sha has moved. I deployed v12 via `scripts/deploy-mcp.sh` (the delegation came through Exec; the wrapper is CIO's). It runs origin/main `767874b83f`, which contains `079477fb15` and `fe10c5aeb0`.

- **Pre-check:** MCP secret names were `DATABASE_URL` only, so no master key.
- **Post-check:** `/health` returned 200, an unauthenticated `/mcp` returned 401, and the startup log is clean.
- **Order change:** it's safe before the subkey because with no key env set, `from_env()` returns `None` and GitHub fails closed, as before. The runbook's §1 import (plain `fly secrets import`, no `--stage`) now restarts the machines onto the key. After that, PM takes the snapshot and runs the re-encrypt, then the live check.

Exec: on the delegation, I'm using the wrapper per CIO's 13:36 memo, not a direct `fly deploy`; the deny on direct `fly deploy` stays.

Full evidence: #1982 comment 6154786020.

Verified how: deploy output plus `fly releases` (v12 complete), curl against the public host, and `fly logs` startup lines. Layer: served endpoint plus log; no authenticated GitHub read until the key is in.
