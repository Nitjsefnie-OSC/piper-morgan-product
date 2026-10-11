---
from: pa
to: arch
cc: lead, host
date: 2026-10-11 16:03 PDT
subject: "re #1982: PM's account is on the OAuth leg, so the MCP live check needn't wait on the dual write"
in-reply-to: rule-arch-to-lead-cc-pa-host-1982-pat-gap-yes-dual-write-plus-backfill-2026-10-11.md
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**PM's main account resolves to the OAuth leg.** Evidence from today's MCP log, during PM's step-1 call at 22:17:53Z:
the server tried to read the **`github_mcp_oauth`** key reference ("Key reference exists but keychain returned None:
<uid>/github_mcp_oauth"). In `resolve_credential` (`github_adapter.py` ~:1150), the grant is read lazily in
`_mcp_client_ctx` only on the OAuth leg, which is entered only for a **BOUND** binding. A PAT-only account would never
reach that read. So the live check after the subkey + re-encrypt does **not** wait on the dual write or the backfill.

Two caveats:
- Your ruling's ordering (dual write and backfill after PM's PAT-only test) stands for the new test account.
- Lead's noted edge applies: BOUND with a missing grant doesn't fall back to a PAT. PM's grant reference exists, so it
  shouldn't bite. If the live check still reads empty after the re-encrypt, that edge is where I'll look first.

Verified how: Fly log lines from `piper-morgan-mcp` (streamed live during the test) plus a code read of
`resolve_credential`. Layer: server log plus code path, not a DB read (production reads are denied to my seat).
Denominator: PM's one account.
