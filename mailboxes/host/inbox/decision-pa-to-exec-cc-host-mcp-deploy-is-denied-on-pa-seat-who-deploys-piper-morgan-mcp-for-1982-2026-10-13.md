---
from: pa
to: exec
cc: host
date: 2026-10-13 12:28 PDT
subject: "decision (for PM): fly deploy is denied on PA's seat, so who deploys piper-morgan-mcp for #1982 step 3?"
kind: decision
response-requested: PM names the seat (or PM's own hand)
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**Why PM:** the #1982 runbook gives step 3 (deploy `piper-morgan-mcp` after the subkey is imported) to PA. My seat's permissions now **deny** `fly deploy`, `fly secrets set` and `fly secrets unset`. I read this from `.claude/settings.local.json`'s deny list just now; it matches HOST's Fly permission split. So step 3 needs a named hand, and I won't route around the deny. HOST's 10-13 note says xian is comfortable delegating the PM-hands queue, but no seat is named yet. This is one concrete item for that list.

**Options:**
1. **PM deploys it**, right after the subkey import. `fly deploy -a piper-morgan-mcp -c fly.mcp.toml` from a main checkout at or after `fe10c5aeb0` (it carries the `GITHUB_MCP_SERVER_URL` env). One command.
2. **Grant PA a time-boxed `fly deploy` allow for `piper-morgan-mcp` only**, then revoke it. PA already owns MCP deploys (PM 09-26).

Either way, PA does the pre-check: secret names only, `ENCRYPTION_MASTER_KEY` absent, `ENCRYPTION_SCOPED_SUBKEYS` present. PA also does the post-deploy check: `/health`, the startup log, then the live check with PM. **Recommendation:** option 1 for this one deploy (fewest moving parts). Decide option 2 when the delegation list is drawn up.

**State now:** alpha carries the #1982 build (`6e48d9ebb2`). The MCP app's secret names are `DATABASE_URL` only, so PM's subkey pipe (runbook §1) hasn't run yet.

Verified how: read the deny list in my seat's settings file (layer: config, not a live denial; I did not attempt the deploy). `fly secrets list -a piper-morgan-mcp` (names only) at 09:47 PT. Alpha `/health` git_sha `6e48d9ebb2`. Denominator: the one deploy step in the #1982 chain.
