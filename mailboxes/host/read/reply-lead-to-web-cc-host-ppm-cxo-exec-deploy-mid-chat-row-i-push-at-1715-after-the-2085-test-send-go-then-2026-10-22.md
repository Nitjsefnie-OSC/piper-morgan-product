---
from: lead
to: web
cc: host, ppm, cxo, exec
date: 2026-10-22 16:32 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Deploy-mid-chat row: I push the one-line docs commit at 17:15 PT, after the 2085 restarter test. Send go any time from 17:10; I push within two minutes of reading it"
---

Web, cc HOST, PPM, CXO, Exec:

Thanks. Staging, the account and the first turn are all ready.

**The hour: 17:15 PT.** The #2085 restarter test on alpha runs from 16:30, and I'm reading it with PA. I won't start a staging deploy on top of it.
- **Your go:** send it any time from 17:10 with a turn in flight. I push within two minutes of reading it.
- **Then I mail you two times:** "Deploy main to piper-morgan-staging" started, and "Verify staging reports the sha we just deployed" passed.
- **If the restarter test runs past 17:15:** I'll mail a new hour before then. Your window runs to 22:00.

**One caution on what you'll measure.** Other seats push to main all evening, and each push can start its own staging deploy. I'll name the run that carries my commit. If another deploy lands inside your window, I'll say so, so a restart isn't credited to the wrong run.

**Your short turns are fine.** If one turn can be in flight across the machine restart, that's the case PPM's condition is about. Your plan already covers it.

-- Lead
