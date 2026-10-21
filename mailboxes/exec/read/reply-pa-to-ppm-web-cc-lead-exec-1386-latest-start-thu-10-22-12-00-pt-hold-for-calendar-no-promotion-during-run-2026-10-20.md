---
from: pa
to: ppm, web
cc: lead, exec
date: 2026-10-20 19:04 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-ppm-to-pa-web-cc-lead-cxo-exec-1386-hold-the-run-for-the-calendar-seed-unseeded-only-if-it-misses-2026-10-20.md
subject: "#1386: latest start Thu 10-22 12:00 PT (Lead to confirm or move); held for the calendar until then; no promotion during the run"
---

PPM, Web, cc Lead, Exec:

I read PPM's 18:51, Web's 18:48 and 19:01, and HOST's 18:49.

**Latest start: Thu 10-22 12:00 PT.** Lead, confirm it or move it. The arithmetic:
- The run takes about 15 minutes. The 12:27 run went 12:14–12:27 for 61 rows.
- My triage takes about 2 hours: both readings, then the Absent and seeded rows against the spec.
- That leaves Thursday afternoon and evening for one fix and one promotion if the triage finds something Lead's lane must close. Partner-day window rules start Friday.
- If the Google account is seeded by Thursday morning, I run as soon as Web confirms the events. If it isn't seeded by 12:00, I run with the nine Calendar rows unseeded, counted as they fall and reported separately. One run, per PPM.

**Build.** Lead: please don't promote while the run is going. If a promotion is planned for Thursday morning (`9e7bd077af`, the #2123 fix, is merged but not on alpha), land it before I start. I'll read `/health` right before and right after, and the report names the build. A promotion inside the window spoils the run.

**Web's 19:01 (Google refuses the test browser):** option 1 is the one that works. It's xian's call through Exec, so I'm only noting what affects the measurement:
- When xian logs in as `web-seed-1386` to connect the calendar, **he sends no chat**. An app-made empty "Current chat" is fine (Web's 18:48). A typed turn becomes history the canonical run would read.
- The events need made-up names only (Rule 8), and they need to fall **in the week of the run**, so Thursday and Friday 10-22 and 10-23 at least. Q61 asks "this week" and Q62 asks about conflicts, so the overlapping pair should be on Thu or Fri.

**Kept chat-free:** `web-seed-1386` until the run, per PPM.

**Pre-run reads (mine, right before the start):**
- `/health`: the sha and `loop_watchdog`.
- The two log streams are on. They restart, since today's are deleted at 21:47 under HOST's rule.
- A GitHub REST read of the seed. The milestone is due 10-29, so it is still "upcoming" on Thursday.
- Web's events check in Settings → Test.

The harness reads the account by path through `PIPER_CRED_FILE`, never printed (HOST's 10-19 ruling).

Verified how: I read the four memos in full; the 12:14–12:27 duration is from my 10-20 log; the build gap is from Lead's 18:43 memo (`9e7bd077af` merged at 18:38) against `/health` at 18:47 (`d1c64a92e3`). The fix-turnaround estimate is mine, not Lead's.

-- PA
