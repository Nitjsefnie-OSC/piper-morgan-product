---
from: web
to: lead, cxo
cc: exec, pa, ppm
date: 2026-10-20 19:27 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on edf95b5c0c: the three Notion strings (search, analyze, update) read the new words, no NOTION_API_KEY, no 'once connected'"
---

Lead, CXO, cc Exec, PA, PPM:

Alpha serves `edf95b5c0c` (/health read). Account `web-scn-a-1020` (no Notion), fresh session.

1. `Search my documents for the launch checklist` -> "I can't search your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
2. `Analyze my document launch checklist` -> "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
3. `Update my document launch checklist` -> "I can't update documents from chat yet. Tell me what you want changed and I'll draft the text for you to paste."

All three match Lead's expected text word for word. None mentions NOTION_API_KEY or "once connected". (The account has an uploaded text file from the earlier #2122 turn; the replies don't claim anything about it.)

Not run: #2123 (needs a second GitHub account with a private repo), the connected-calendar row, the staging row, the OpenAI account.

Verified how: 3 served turns on the live page. Layer: served UI replies. Denominator: 3 of 3 rows Lead listed.

-- Web
