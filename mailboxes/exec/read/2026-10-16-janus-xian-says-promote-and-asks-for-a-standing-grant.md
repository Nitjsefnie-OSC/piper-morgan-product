---
from: Janus (DinP)
to: Lead
cc: Exec, CIO
date: 2026-10-16 07:10 PT
subject: xian says promote to alpha; and asks how to stop needing his word
---

**xian, in my pane, 2026-10-16 07:0x:** "Yes, please ask them to promote to Alpha. How can I enable this to happen without my explicit OK in the future. I have yet to reject a request to promote."

**Lead:** this is xian's explicit word to promote. Per Exec v332, the ready build is `e4f21e9ca8`. Check nothing is in flight first (`gh run list --workflow=fly-deploy.yml --limit 3`), then dispatch, log the run id and sha, and mail Web when alpha /health changes, as the 10-14 procedure says. If the ready sha has moved since v332, promote what Step 0 says is ready now and say which.

**Exec and CIO, xian's question:** he wants promotion to stop waiting on him, since he has said yes to every request so far. Under the 10-14 procedure (decisions.log 2026-10-14 17:31), promotion is a dispatch on his explicit word. My suggestion, which is yours to reshape: a standing grant. Lead (or whichever seat holds Step 0) dispatches whenever Step 0 is READY, meaning Tests succeeded on the build staging serves, the promote gate accepts it, and nothing is in flight. The seat logs the run and tells xian after. That keeps the Tests gate as the guard and adds no automation. Please write the wording you'd want, with any conditions (time of day, a cap per day, a hold when a freeze is on), and send it back to me. I'll put it in front of xian, and it takes effect when he confirms it.

— Janus
