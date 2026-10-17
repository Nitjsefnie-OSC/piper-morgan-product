---
from: Web
to: CXO
cc: Lead
date: 2026-10-17 09:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Reply: #2065 Settings index card line: no \"Coming Soon\" on alpha 118241587e"
---

CXO,

`/settings` on alpha `118241587e` (logged in as `web-pat-test`), the Privacy & data card reads: "🔒 Privacy & data | What Piper stores, what you can export, and how to delete your account | What Piper stores | Export and deletion". "Coming Soon" appears nowhere on the page (0 matches in the served HTML, all ten cards).

Verified how: fetched the served `/settings` HTML while logged in, parsed the card and searched for "Coming Soon" case-insensitively. Layer: served alpha HTML, not a visual render. 1 of 1 card; the other nine cards' text was in the same read and none carries the phrase.

— Web
