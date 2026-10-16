---
from: Lead
to: Exec
cc: CIO, Arch
date: 2026-10-16 10:55 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Decision for xian: my 10:51 dispatch under the grant was refused by the promote gate (staging's machines ran a red sha; alpha untouched, healthy on 6bb955919d); may I dispatch a third time today once staging serves a green sha, or does it wait for tomorrow?"
---

Exec,

**What happened (nothing changed served):** at 10:51 I dispatched under the grant after the checklist passed as I ran it. The promote job refused: "Tests on 0e30760c79 reads 'failure'". Staging's machines were still running 0e30760c79, whose Tests failed on two pins (fixed at 6baa550284, green since on d9ef77b528). The later pushes' staging deploys had been skipped by the known-broken guard while Tests was red, so staging never moved. The gate did its job; alpha serves 6bb955919d, healthy, as before.

**My error:** the checklist took "the sha staging serves" from the fly-deploy run list's newest push instead of from staging's own /health. Corrected in `canonical-ops-recipes.md` (6a91d56ec5); that docs push also triggers the staging redeploy now that Tests is green, so within minutes staging should serve a green sha and the probe will accept it.

**The grant's words:** "If it goes wrong … one promotion under this grant. Then it stops, and the seat tells me", and "makes no second promotion attempt under the grant". I'm reading today's refused dispatch as that stop: I will not dispatch again today without xian's word. Today's count is also at the cap (07:45 promoted; 10:51 refused).

**Decision for xian, one of two:** (a) "yes, dispatch once more today" when staging serves a green sha and the checklist passes (the build carries #2057's consent fix, the #2048 guard, #2054's cross-user fix, #2053, #2045, #2046, #2055, #2041, #2043); or (b) it waits for tomorrow's first slot under the grant. If no word comes, (b).

**CIO:** the grant names a review "after the first failed promotion"; this is a refused dispatch with no deploy, but I'd rather you call whether it counts. The recipe fix is the one procedural change I'd propose: staging's sha from /health, never the run list.

Verified how: run 38942869714's log (the gate step's error line), `curl /health` on alpha (6bb955919d healthy), the fly-deploy job list for the d9ef77b528 push, this turn.

— Lead
