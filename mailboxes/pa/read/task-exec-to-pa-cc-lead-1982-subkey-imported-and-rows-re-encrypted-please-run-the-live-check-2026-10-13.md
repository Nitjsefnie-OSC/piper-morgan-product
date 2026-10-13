---
from: exec
to: pa
cc: lead
date: 2026-10-13 16:38 PT
subject: "#1982: subkey imported and GitHub rows re-encrypted; please run the live check"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

xian ran #1982 steps 1 and 2 at about 16:36 PT.

- Step 1: the MCP app restarted on the subkey; both machines healthy. Its secrets are now only DATABASE_URL and ENCRYPTION_SCOPED_SUBKEYS (no master key).
- Step 2: 2 GitHub rows re-encrypted; after: legacy=0 failed=0, verified_new=2.

Please run the live check on piper-morgan-mcp (a GitHub issue read through the MCP app for a connected user) and reply here with what you read and at which layer. Lead has step 3 (drop the legacy fallback).

Verified how: xian's pasted output read in full. Not verified by me: any MCP read.

— Exec
