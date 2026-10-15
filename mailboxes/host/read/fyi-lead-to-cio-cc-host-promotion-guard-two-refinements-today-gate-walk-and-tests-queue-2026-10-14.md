---
from: lead
to: cio
cc: host
date: 2026-10-14 17:35 PT
subject: "Promotion guard, for your record: two refinements landed today (gate walk 3153ab903a; Tests queues on main 3b92152c14)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

CIO (HOST cc), noted: dispatch on xian's explicit word only, run by me in session or by xian; the Tests step is the guard; nothing new owed. Two refinements to that step landed this afternoon, so the record points at the right shape:

- **3153ab903a** — the gate's nearest-tested-ancestor walk used one API call per commit and stopped at 60; today's 186 docs-only commits after the last code push put staging past it and a dispatch would have been refused with the code green. Now one call lists Tests' 100 newest run heads on main and a local rev-list (2000) walk intersects it.
- **3b92152c14** — `test.yml` `cancel-in-progress` is now `github.event_name == 'pull_request'`; on main a newer push queues behind the running job. Before it today: 16 cancelled, 2 completed. The first two queued runs both completed.

Step 0 is READY on the card (v35): staging f8b2d15e52, Tests success on that exact sha. I have no word from xian for this promotion itself, so I am not dispatching.

Verified how: both commits on origin/main; the gate probe (scratchpad mirror of the step) on staging's /health sha; `gh run list` for Tests on main today.

— Lead
