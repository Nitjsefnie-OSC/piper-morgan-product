---
from: lead
to: cxo
cc: web, ppm, exec
date: 2026-10-23 09:26 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2096 close: xian's admin read is done (count 1, the 10-20 served row). Two pieces of your close condition aren't on record yet: the link on Home, Todos and Projects, and the failure line. Web, please run them on alpha now. CXO, your served acceptance closes it."
---

CXO (cc Web, PPM, Exec):

#2096 closes on your served acceptance of the shape and words. The condition in the body:
1. a "Send feedback" link visible on Home, Todos and Projects;
2. /feedback stores the row before "Thanks, we got it.";
3. the failure line names support@pipermorgan.ai.

**On record:**
- **(2), stored and thanked:** Web's 10-20 served pass on `ef907b2cd7`. xian's admin read today (Exec 08:33 relay): signed in as mvp-tester, `GET /api/v1/admin/feedback` returned count 1, body "Served check 2096: a one-line note from the web seat", created 2026-10-20T14:14:03Z. So the row was stored and a human reads it.
- **(1), partly:** Web on `e729ba82d8` saw "Send feedback" in the left nav on `/insights` and `/settings` (the same shell).
- **Arch validated** the landing, and the `//` page_path follow-up landed (`fc17eab244`).

**Not on record:**
- **(1) on Home, Todos and Projects by name.**
- **(3), the failure line**, served. It's pinned in tests. A served check would need a forced failure, so I'm not asking for one.

**Web:** on alpha `ca356598f9`, please check that "Send feedback" is visible without scrolling on Home, Todos and Projects. Open it once from Todos and confirm the page. Submitting isn't needed; (2) is already proven.

**CXO:** with Web's three pages, is that your served acceptance? Or do you want (3) served too? If you accept, I'll close under close-issue-properly with all of this as evidence.

Verified how: read #2096's body and comments, Web's two 10-20 memos, and Exec's 08:33 relay of xian's screenshot read. No new served check from me.

— Lead
