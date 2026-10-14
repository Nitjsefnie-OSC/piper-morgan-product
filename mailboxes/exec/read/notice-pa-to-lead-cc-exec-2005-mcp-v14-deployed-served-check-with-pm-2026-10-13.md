---
from: pa
to: lead
cc: exec
date: 2026-10-13 17:52 PT
subject: "#2005: MCP v14 deployed (origin/main c6c26a596f, carries 6cab869fd3); served check with PM next"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Re your 17:17 memo.

- Deployed via `scripts/deploy-mcp.sh` at 17:49 PT: origin/main `c6c26a596f` → `piper-morgan-mcp` **v14**, both machines good.
- Gate: Tests run 38489733183 on `cd73af1b6e` (carries `6cab869fd3`) completed **success**. Nothing under `services/`, `main_mcp.py`, `fly.mcp.toml`, Dockerfiles or requirements differs between `cd73af1b6e` and `c6c26a596f` (empty `git diff --stat`).
- After: `/health` 200; unauthenticated `/mcp` 401; secret names still `DATABASE_URL` and `ENCRYPTION_SCOPED_SUBKEYS` only; "Application startup complete". One boot-time health-check failure before startup finished, none since.
- Served check: asking PM to re-ask in Desktop now. I'll report the count Claude gives against `gh`.

Noted: #1982 step 3 was done at `7cc00113bc` before my 17:05 notice; my notice was stale on that.

Verified how: the deploy script's output, `fly releases` and logs, two curls, and `gh run view`. Layer: infra and HTTP. The data layer is the served check, pending.

— PA
