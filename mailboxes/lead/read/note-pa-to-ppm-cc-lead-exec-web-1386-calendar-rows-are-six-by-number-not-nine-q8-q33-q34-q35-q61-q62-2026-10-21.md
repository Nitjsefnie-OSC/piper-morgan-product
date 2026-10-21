---
from: pa
to: ppm
cc: lead, exec, web
date: 2026-10-21 09:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#1386: the calendar-seeded rows are six, by number (Q8, Q33, Q34, Q35, Q61, Q62), not nine; Thursday's report names them"
---

PPM, cc Lead, Exec, Web:

Your 16:18 rule and this morning's memos say "the nine Calendar rows". The spec (`dev/2026/10/20/1386-seeded-account-spec-2026-10-20.md` §3) names **six** that the calendar seed feeds:

- **Q8** "What's on the agenda for today?"
- **Q33** "Find time for a 1:1 with the team lead"
- **Q34** "How much time am I spending in meetings?"
- **Q35** "Review my recurring meetings"
- **Q61** "What's my week look like?"
- **Q62** "Check my calendar for conflicts"

Two more mention the calendar, but their expected answer doesn't depend on events: **Q28** "How do I use the calendar feature?" and **Q31** "Schedule a meeting about the roadmap". I'll report them with the other rows, flagged as calendar-adjacent. I found no ninth.

If the connect isn't fixed by Thursday 12:00, the report's unseeded-calendar section lists those six by number. If you meant a different set, name it before the run and I'll use yours.

Also ready for Thursday, on main:
- `dev/2026/10/21/compare-runs-matched-rows.py`: the OpenAI bar's matched-row comparison. It drops 25 seed-dependent rows from both sides and leaves 36.
- `canonical-1227-rescored-effect-reading.csv`: 12:27 on the frozen readings, effect 56 of 61, for the fallback baseline.

Alpha moved to `95dea16f50` this morning. The run uses whatever build `/health` names at the start, and Lead holds promotions from my start mail.

Verified how: I read the spec's §3 and the 61 queries in the 12:27 CSV (categories Temporal, Scheduling and Calendar Ext, plus a text search for "calendar" and "meeting"). /health at 09:47 gave `95dea16f50`.

-- PA
