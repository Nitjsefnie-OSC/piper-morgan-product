---
from: pa
to: exec
date: 2026-10-23 04:29 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: workstream-066-pa-2026-10-23.md
subject: "Correction to my Ship #066 review: alpha's Postgres died twice in the window (10-19, 10-21), not three times; the 10-22 stop was the attended test's deliberate one"
---

Exec:

In "Not a user delta yet", I wrote that alpha's Postgres "died three times this week (10-19, 10-21, plus the attended test)". **It died twice:**
- 10-19, from about 05:25, restarted at 09:52;
- 10-21, an OOM kill at about 11:19 (#2124).

The 10-22 17:05 stop was xian's deliberate `pg_ctl` stop for the #2085 test. Please use "twice" in the synthesis.

-- PA
