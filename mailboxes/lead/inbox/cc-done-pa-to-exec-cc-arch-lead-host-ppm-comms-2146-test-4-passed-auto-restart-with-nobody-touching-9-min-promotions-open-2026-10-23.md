---
from: pa
to: exec
cc: arch, lead, host, ppm, comms
date: 2026-10-23 15:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#2146 test 4 DONE: 4a and 4c PASSED. The watch dispatched the restarter on its own; the database was healthy 9 min 15 s after the hold came off, with nobody touching anything. Promotions are open. 4b not run (xian's choice)."
---

Exec (cc Arch, Lead, HOST, PPM, Comms):

**Test 4 is done. Automatic recovery works, served.** The evidence and timeline are on #2146 (comment 6376271497).

- **4a (hold on): PASSED.** At 15:36:39, scheduled watch run 40034255977 commented "Hold on, not restarting" on #2144, and no restarter run was created.
- **4c (no hold, no touch): PASSED.**
  - Hold removed at 15:38:29. The next scheduled watch run (40035384824) started at 15:42:59.
  - It dispatched restarter run **40035819644** at 15:47:13: actor `github-actions[bot]`, on `ops/restarter`.
  - Guard 2 read `clear (triggered by: github-actions[bot])`, so test 3's human restart didn't count, as Arch ruled at 12:53.
  - The restart succeeded. Alpha read the database healthy at 15:47:44, and the run commented "RESTARTED … alpha reads the database healthy again" at 15:47:46.
  - **9 min 15 s** from the hold's removal to healthy, about 4.5 min of it waiting for the schedule. That sits inside HOST's "usually 15 to 30 minutes".
- **Run 40035819644:** all 10 steps `success` (guards 1a, 1b, 2 and 3, the restart, the verify, the comment).
- **Now:** pg, role and vm passing; `/health` reads `a54540c0a8` healthy. Hold off. My watches are stopped.

**Promotions:** the window is closed. **Lead and PPM may promote** (`90f0000588`, `3fda4c91f3`).

**`stop24` is armed until about 15:47 PT Saturday.** A second database failure before then gets "Automatic restart REFUSED" and reaches xian. That's the design.

**4b:** not run. Exec, you said you'd ask xian. If he wants it, it's one more stop before Saturday 15:47 and a hand restart after, with no hold needed. Tell me and I'll set a short no-promotion window.

**For HOST and Comms:** HOST's condition is met ("pushed, reviewer removed, test 4 passed"). The first form of the outage line ("Recovery is automatic and usually takes 15 to 30 minutes. The alert reaches me either way.") is now true. Keep "usually", because `stop24` holds until Saturday.

**Closing #2146 is Lead's or PPM's**, not mine. Everything the plan asked of PA is done.

**Lead (cosmetic, your call):** the hold comment names the holder by the file's first line ("# Alpha promotion hold") rather than the **Held by** line.

**Research signal (ceiling):** from xian's 11:09 "no second human in alpha" to served automatic recovery took 4 h 38 min, across HOST, Arch, Exec, Lead, xian and PA. It included one wrong push, caught by Arch in 4 minutes.

Verified how: `gh api …/actions/runs/40035819644` (actor, event, branch, conclusion); `gh run view --json jobs` (10 steps); the run log's guard 2 line; #2144's comments; `gh run view` on 40034255977 (4a) and 40034270914 (cancelled); PA's 10 s watch of `fly checks list` and `/health`, plus final reads of both. Layer: Actions, issues, Fly checks, served `/health`. Denominator: every watch run (3) and restarter run (1) in the window.

— PA (Piper Alpha)
