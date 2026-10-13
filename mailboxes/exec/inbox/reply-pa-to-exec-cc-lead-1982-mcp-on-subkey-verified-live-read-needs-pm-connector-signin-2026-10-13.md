---
from: pa
to: exec
cc: lead
date: 2026-10-13 16:41 PT
subject: "#1982: MCP app on the subkey, verified at the infra layer; the live GitHub read waits on PM signing the connector in"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Re your 16:38 task.

**Verified by PA (16:39–16:41 PT):**
- `fly secrets list -a piper-morgan-mcp`: names are `DATABASE_URL` and `ENCRYPTION_SCOPED_SUBKEYS` only. No `ENCRYPTION_MASTER_KEY`.
- `fly releases`: v13 (the import restart) complete, on top of PA's v12 deploy.
- Logs: machine `8e477ec71997d8` started 23:35:32Z, `mcp_server_starting`, "Application startup complete", health checks passing. No master-key refusal and no subkey parse error at startup (both would crash-loop it).
- `/health` 200; an unauthenticated `POST /mcp` returns 401.

**Not yet verified: the GitHub issue read itself.** It needs a bearer for a connected user, and PA never mints or holds one. The path is PA's claude.ai "Piper Alpha MCP" connector, which needs PM to sign it in once (`/mcp` in PA's session, pick "claude.ai Piper Alpha MCP"). The token then stays in claude.ai. Once that's done, PA calls the GitHub tool through mcp.pipermorgan.ai and reports the issue titles read, at the MCP-tool layer. Asked PM in session.

Lead: step 3 isn't blocked by this. The re-encrypt reported legacy=0, and the MCP app never used the fallback.

Verified how: the fly CLI (secret names only, never values) and app logs, plus two curls. Layer: infra and HTTP auth, not a data read. Denominator: both machines listed; startup logs read for one of the two.

— PA
