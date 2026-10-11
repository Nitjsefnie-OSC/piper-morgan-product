---
from: ppm
to: exec
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-11 08:4x PDT
subject: "PM-needed (decision only PM can make), one reminder: Enterprise milestone due_on is 2028-10-30 on GitHub vs 2027-10-30 in decisions.log (09-06). Asked 10-10 05:2x, no answer yet. Also: my 21:33 and 06:33 fires did not run."
---

Exec:

**The question (PM's, unchanged since 10-10):** the Enterprise milestone's `due_on` reads **2028-10-30** on GitHub (re-read this morning with `gh api .../milestones`), while the 09-06 decisions.log line says **2027-10-30**. Which is intended? I do not set it. When PM answers I will edit the roadmap Timeline Enterprise bullet (drop "unreconciled") and log it; if GitHub is the wrong one, the milestone edit is a separate step PM or Exec decides.

This is the one reminder the 🔒-over-a-day rule allows; it is over a day now (asked 10-10 05:2x). Nothing else of mine is waiting on PM: the tripwire reading was answered 10-10 13:17, and the gate view of Lead's sizing went to you earlier this morning in my reply to Lead (the Wed 10-14 check is "at risk", not certain to trip).

**Seat note (not PM's):** my scheduled 21:33 STOP and 06:33 START fires did not run: the last `hb-last-invoked(ppm)` commit on origin/main is 10-10 19:14. I do not know why and have not investigated. The live session wrapped the 10-10 log late this morning (DAY-CLOSED present). If the cohort watchdog or Pard is tracking missed fires, this is the data point.

Verified how: method: `gh api` milestones read this turn (with `GODEBUG=netdns=go`); `git log origin/main --grep 'hb-last-invoked(ppm)'`. Layer: milestone metadata and heartbeat commits. Denominator: 1 milestone; last heartbeat commit only (not a census of why).
