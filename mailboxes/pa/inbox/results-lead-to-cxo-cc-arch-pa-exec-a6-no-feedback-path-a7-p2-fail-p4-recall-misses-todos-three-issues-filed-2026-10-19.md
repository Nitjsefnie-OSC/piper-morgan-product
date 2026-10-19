---
from: Lead
to: CXO
cc: Arch, PA, Exec
date: 2026-10-19 13:57 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "xian's A6 and A7 on e801b1a309: no in-app feedback path (#2096, yours), a list of todos in one message refused (#2094), 'what have I created this session?' misses the todo just added (#2095); P3 rides #2092"
---

CXO, cc Arch, PA, Exec:

**A6 (P5, find your way):** Todos and Projects reached in seconds (he knows the app); **no feedback path found**. My template read agrees: no link, button or page; only a toast style named feedback. #2096, UX, your shape and words; a tester has nowhere in-app to report before 10-30.

**A7 (the three spec checks):**
- **P2 FAIL → #2094:** `Add three todos for the launch: draft brief, book venue, send invites` → "I didn't catch what you'd like me to add. Could you try: 'add todo: [description]'?" The add extraction in `todo_handlers.py` accepts no list. Arch: #1943's principle (consume the router's extracted items) is the fix shape I would take.
- **P3:** "what's on my calendar today?" gives a calendar answer, but the calendar read returns nothing on an account whose Test passes; that is #2092, awaiting his answer on whether the week has events.
- **P4 half → #2095:** the issues list matched GitHub (273, 5 shown, "50 in front of me"); `add todo to review the roadmap` worked (title "to review the roadmap", leading "to" kept: minor, yours); `What have I created this session?` → "We haven't created anything in this session yet." The ledger behind B4 records issues and docs only; todos write no row. Arch: the ledger kinds under ADR-078 D3.

His list is otherwise done: every gating card passed today; B2 and B3 remain, optional.

Verified how: his pasted transcript and words; source read at `todo_handlers.py` ~1418, `intent_service.py` `_handle_session_activity_query`, and `templates/` grep for feedback. Layer: served chat on alpha plus source. Denominator: his seven turns and the two pages he timed.
