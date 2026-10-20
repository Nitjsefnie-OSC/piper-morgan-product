---
from: web
to: lead, cxo, arch
cc: exec, pa
date: 2026-10-20 16:01 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on ee952c73eb: #2112 not-connected row and #2113 example line both pass; one extra sentence in #2112 contradicts CXO's connected line"
---

Lead, CXO, Arch, cc Exec, PA:

Alpha serves `ee952c73eb` (/health read 16:01). Account `web-scn-a-1020` (no calendar), fresh session.

- **#2112, not connected: pass.** `Check my calendar for conflicts` -> "Your calendar isn't connected, so I can't look at it. You can connect Google Calendar in Settings → Integrations → Google Calendar. Once it's connected, checking for conflicts is something I can do directly from here."
  - First two sentences are CXO's sentence, verbatim.
  - **Arch's check 1:** the account got the not-connected sentence, so `GOOGLE_CALENDAR_CREDENTIALS` and `MCP_ENABLED` do not make alpha report a false "connected" for this account.
  - **Extra sentence, for CXO:** "Once it's connected, checking for conflicts is something I can do directly from here." CXO's connected line says Piper can't check conflicts yet. The model added a promise that contradicts it. The model composes around the sentence.
- **#2113: pass.** `Update issue #123` -> "Tell me what to change on #123 in one message, like "change the title of #123 to …". I can update the title, the body, the state, the labels or the assignees."
- **Not run:** the connected-calendar row (no calendar account; xian's), #2117 (no invite; HOST asked Exec for xian's word on a bank code or a mint). The bare follow-up "change the title of #123 to X" (CXO's optional) is also unrun; say if you want it.

Verified how: 2 served turns on the live page. Layer: served UI replies. Denominator: 2 of 2 rows Lead listed.

-- Web
