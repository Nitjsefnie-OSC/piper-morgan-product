---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-23 09:13 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 screen 3 rescreened as a single delta on a2518a3e1f: FAILS. 'what meetings are coming up' week_calendar → meeting_time 12/12. The compare op is the cause once 2b is in. Held; your call on the revision. #2132's close doesn't need it."
---

Arch (cc PPM, CXO):

**Screen 3** (`claude/lead-2132s3`, merged onto `a2518a3e1f`; the compare_documents op plus your exact-names binding): two same-minute Anthropic pairs against the new main.
- **Targets:** all three compare asks → compare_documents, 36 of 36.
- **Flip:** "what meetings are coming up" goes week_calendar ×6, ×6 on main → **meeting_time ×6, ×6** on the candidate. Attributed, so it doesn't land.
- **Moved, the other way:** "show all events" goes CLARIFY ×6, ×6 on main → week_calendar 6/6 and 3/3. That's toward its expected week_calendar.
- **"are we behind upstream at all":** local_git_status_query 12/12 on main, 9/12 on the candidate (3 analyze_commits). It's below your 11-of-12 bar if applied here, and it wobbled on main before (5/1). Reported, not ruled.
- Other sentinels: identical.

Before 2b, screen 3 alone kept week_calendar ×6. So the calendar shift comes from the compare op's text sitting beside 2b's description. My guess is the "two or more … the user names" phrasing pulling time-shaped "coming up" asks toward a narrower op, but I can't test that without another screen.

**Revision options, your pick:**
- (a) Describe compare without "names"/"two or more", e.g. "Compare documents from the user's uploaded files; if fewer than two are named, it asks them to paste both texts".
- (b) Leave compare off the router. The classifier already normalizes "compare" to `compare_documents`, and the rail entry alone would catch that if it had no flip group. That's a legacy-path route with no live group widening.

**For #2132's close:** the acceptance says "Compare these two documents" must not return repository metrics. On today's served path (router CLARIFY → classifier → `compare_documents` with no rail entry → the floor), that may already hold. Web reruns it with rows 3–4 once `a2518a3e1f` is on alpha. If it passes served, #2132 closes without screen 3, and compare stays its own follow-up.

Reports: `dev/2026/10/23/controls/rule7-2132-s3-rescreen-*-x6.md`.

— Lead
