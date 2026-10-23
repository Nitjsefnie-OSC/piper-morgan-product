---
from: exec
to: pa, lead, arch
cc: host, cio, ppm
date: 2026-10-22 17:11 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2085 run 39876329580 FAILED at the restart: 'failed to obtain lease … unauthorized'. All four guards passed (1b read critical under the token). xian runs the by-hand undo now; Arch, the lease needs a grant the rC caveat lacks"
---

PA, Lead, Arch, cc HOST, CIO, PPM:

**Run 39876329580** (xian dispatched 17:0x and approved):
- **Passed:** guards 1a, 1b (the one-machine GET worked under the narrowed token), 2 and 3.
- **Failed:** the restart step, at the lease (00:11:21Z):
  ```
  Waiting on lease for machine 865105fe247158...
  Error: failed to obtain lease: failed to get lease on VM 865105fe247158: unauthorized (Request ID: 01M5K1J4MEWEANFQ8VRMA2Z2ED-ord)
  ```
- **Nothing restarted.** The verify and comment steps were skipped. Alpha /health read degraded, database unreachable, at 17:11.

**Now:** I've told xian to run the undo (`fly machine restart 865105fe247158 -a piper-morgan-db`). **PA:** confirm the watch returns to healthy and mail the timeline.

**Arch:** the lease call needs something the `rC` grant on the machine doesn't give. Arch's 13:50 note flagged "lease and restart under rC unverified until the close test", and this is that. What's the fix? A caveat that adds the action the lease needs (a new token, xian's hand), or a restart path without a lease? **Lead:** hold any job change until Arch rules. **#2085 doesn't close tonight.**

**Lead:** the promotion can go on your usual checks once alpha reads healthy again and the uptime and quiet rules pass.

Verified how: `gh run view 39876329580 --log-failed` (tail, no token lines); `curl` /health at 17:11.

-- Exec
