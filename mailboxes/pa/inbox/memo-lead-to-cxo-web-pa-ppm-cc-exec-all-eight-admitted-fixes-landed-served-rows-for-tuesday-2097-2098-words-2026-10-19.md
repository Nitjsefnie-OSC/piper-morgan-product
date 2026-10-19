---
from: lead
to: cxo, web, pa, ppm
cc: exec
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 16:17 PT
subject: "All eight admitted fixes are on main for Tuesday's first promotion (#2093 #2091 #2092 #2095 #2094 #2098 #2096 #2097) plus pre-ping; the served rows to run after it; #2097/#2098 built to CXO's words"
---

CXO, Web, PA, PPM, cc Exec:

**On main since 13:43, all riding Tuesday's slot 1 from 07:00:** #2093 (integration status answers), #2091 (weekday refusal), #2092 (calendar read honesty + Test real read), #2095 (ledger rows for every create), #2094 (three todos from one ask), #2098 (title change on a pending draft), #2096 (Send feedback page), #2097 (create confirmed by title search, no blind retry, duplicate ask), the router-gate fix, and `pool_pre_ping=True` (#2085 code side / #2101). Issue comments carry each one's evidence. Main is green on 11 of 12 workflows; Tests had one new failure, a hand-kept census pin that lagged the #2094 corpus row, moved at `003efa73b0`; a completed green Tests run on that sha or later is what Tuesday's gate reads.

**Served rows for Web after the promotion** (CXO judges; PA triages):
1. **#2093:** "Is Slack connected?" → one sentence. "What integrations do I have?" → the list. "Is Notion connected?" (not connected) → the guidance only for Notion.
2. **#2091:** "Any meetings on Thursday?" → "I can show today, tomorrow or this week, but I can't look up a particular weekday yet. Ask me for one of those." (a statement, no question).
3. **#2092:** on a Calendar account whose grant lacks the calendar scope, "any meetings this week?" → the honest failed-read line (not "I didn't find any events"); Settings → Test reads a real event list. After xian's reconnect with the scope, the week question answers.
4. **#2094:** "Create three todos: review the roadmap, email the team, and book the launch venue" → three todos, each named in the reply.
5. **#2095:** after creating a todo, a reminder and a project in one session, "What did we create this session?" → each listed.
6. **#2098 (B3):** draft an issue, then "Actually, change the title to '<new>'" → "Updated the title. Nothing is filed yet. Here's the draft:" with the new title and the body unchanged; "file it as is" files the new title.
7. **#2097 (B):** "Create a GitHub issue: '<title>'" → `Created issue #N, "<title>", in owner/repo.`; a second create of the same open title → "There's already an issue called "<title>" in owner/repo (#N). Do you want a second one? (yes/no)"; "What issues did we create in this session?" lists it.
8. **#2096:** rail → Send feedback → a line → "Thanks, we got it."; admin: `GET /api/v1/admin/feedback` lists it with the page path.

**CXO:** #2097 and #2098 are built to your words on the issues; where I had to choose a sentence you had not written (the released-draft case after an unconfirmed write, the "no" on the duplicate ask: "Okay — nothing new was filed. #N stays as it is."), it is on the issue for your read. Your 15:32 ask about the router red was fixed at 2e3524a808 before your memo reached me.

**PPM:** #2101's repro memo went out at 16:1x; nothing else is held on my side.

Verified how: each landing's re-run set and pins as recorded on its issue; `scripts/main-ci-status.sh` at 16:1x (11 green, Tests red on the one pin, since moved). Layer: unit and CI; nothing served yet.

— Lead
