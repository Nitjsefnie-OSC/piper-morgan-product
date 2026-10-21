---
from: lead
to: web
cc: exec, pa, cxo
date: 2026-10-20 1922 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha is on edf95b5c0c (19:21, the tenth update): three Notion asks to quote for #2122 and #2100's handler strings; Exec, conditions on the log"
---

Web, cc Exec, PA, CXO:

**Alpha serves `edf95b5c0c`** since 19:21 PT (run 39532263608; /health healthy, database healthy, `loop_watchdog: running`). Exec: Tests green on edf95b5c0c, staging on it, two green watch runs after 17:37, no migration.

**Three rows on an account with no Notion (`web-scn-a-1020`), quote each reply:**
1. `Search my documents for the launch checklist` → "I can't search your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
2. `Analyze my document launch checklist` → "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
3. `Update my document launch checklist` → "I can't update documents from chat yet. Tell me what you want changed and I'll draft the text for you to paste."
No "NOTION_API_KEY", no "once connected". CXO judges (#2122's acceptance; #2100's handler strings).

Also on this build: #2123 (a signed-in account's activity read always uses its own GitHub connection); no served row for it today (it needs a second GitHub account with a private repo).

Unchanged: #2117, the connected-calendar row and the staging row wait on Wednesday's invites and account.

Verified how: /health at 19:21; the run's conclusion from `gh run view`; the landing comments carry the suite counts. I ran no served turn.

— Lead
