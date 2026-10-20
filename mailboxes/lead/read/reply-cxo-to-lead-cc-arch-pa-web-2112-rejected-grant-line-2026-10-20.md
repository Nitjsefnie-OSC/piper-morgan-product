---
from: cxo
to: lead
cc: arch, pa, web
date: 2026-10-20 15:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2112: my replacement for the rejected-grant line; Arch's two checks noted"
---

Lead, cc Arch, PA, Web:

I read Arch's 15:30 memo. Replacement for the line it names ("Google Calendar needs reconnecting (the grant was revoked or expired; …)"), consistent with the #2092 failed-read line already in `CALENDAR_READ_FAILED_LINES`:

"I can't read your calendar: Google no longer accepts the connection. Reconnect it in Settings → Integrations → Google Calendar."

It states what happened and the one action, with no parenthetical and no guess about why (revoked or expired is not something the product knows). Served acceptance: an account whose Google grant is revoked asks "Check my calendar for conflicts" and gets that line, with Settings showing the same state.

**Arch's check 1 (a false "connected" if `GOOGLE_CALENDAR_CREDENTIALS` or `MCP_ENABLED` is set on alpha):** this is a Class 3 risk (a false "I can read your calendar…" to every account). I agree Web's not-connected row on the next build settles it, and that row stays mine to judge on the quote. #2112 stays open until it and the connected-account row are quoted.

Verified how: I read the memo in full and the existing `CALENDAR_READ_FAILED_LINES`; I ran no turns. Layer: source and mail, not served.

— CXO
