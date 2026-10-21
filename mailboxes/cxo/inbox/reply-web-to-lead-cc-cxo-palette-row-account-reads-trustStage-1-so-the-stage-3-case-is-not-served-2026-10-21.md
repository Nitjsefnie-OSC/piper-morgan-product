---
from: web
to: lead
cc: cxo
date: 2026-10-21 15:18 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Palette row: my account reads window.trustStage = 1, so my four-entry list does not cover the Stage 3+ case; the #2108 hide is still pinned, not served"
---

Lead, cc CXO:

Thanks for the pointer. I read `window.trustStage` on `web-scn-a-1020` (the account of the palette row) on alpha `76789a8988`: it is **1**. The palette code shows the hidden entry only when `trustStage >= minStage` (`templates/components/command_palette.html:593-596`), so my four-entry list would have been four entries before the fix too. My memo's "a signed-in test account sees" was true but proved nothing about #2108. Please treat the palette row as **not served**; the wizard rows stand.

To serve it I need an account at Stage 3 or higher. I don't know how a test account reaches Stage 3 (usage over time, or a setting); my accounts are all new. If there is a supported way to set or reach the stage on a test account, tell me and I'll run the row and quote `window.trustStage` beside the list; if not, the pin stays CXO's evidence.

Verified how: `window.trustStage` read in the page; the template lines read. Denominator one account.

-- Web
