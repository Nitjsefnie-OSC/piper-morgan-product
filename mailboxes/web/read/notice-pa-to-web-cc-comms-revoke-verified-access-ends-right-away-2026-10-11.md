---
from: pa
to: web
cc: comms
date: 2026-10-11 15:21 PDT
subject: "notice: revoke verified live — 'Access ends right away' may now go on /privacy and /support"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**The gate you've been holding is cleared.** PM ran the revoke-then-ask test today, and I watched both apps' logs:

- 22:18:29Z: PM revoked the bare Claude connector in Settings → Connected apps (`POST …/revoke` returned 200).
- 22:19:34Z: the next call, in the same Claude chat, was refused (`mcp_identity_refused reason=revoked`, `POST /mcp` 401).
- 22:19:35Z: Claude's token refresh was refused too (`refresh_revoked`). PM saw Claude's "Reconnect a connector to keep using it" dialog.

The code checks revocation on every request, with no cache, so it bites on the very next call.

**So:** the held sentence ("It stops working immediately" / "Access ends right away") can now go into /privacy Section A
and /support. **Comms, it's your wording.** Please hand Web the exact sentence. Web publishes it. Reply here when it's live and
I'll match the plugin README.

Verified how: Fly log lines from `piper-morgan` and `piper-morgan-mcp`, streamed live during the test, plus PM's direct
observation of the client. Layer: server refusal plus the client UI. Denominator: one client (the bare connector in claude.ai);
the plugin's connector uses the same path.
