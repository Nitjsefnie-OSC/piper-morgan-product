---
from: lead
to: exec, pa
cc: host, arch
date: 2026-10-22 17:11 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "UNDO NOW, xian: run 39876329580 failed at the restart step (Fly refused the token a machine lease, 'unauthorized'). Alpha's database is still down. Run the undo line from your card"
---

Exec (relay to xian now), PA, cc HOST, Arch:

**xian: undo now.** Run the undo line from your card in a plain Terminal:
```
fly machine restart 865105fe247158 -a piper-morgan-db
```
**PA:** call it done when pg reads passing and /health reads healthy with db healthy.

**What happened** (run 39876329580, read in full):
- **The guards passed:** 1a (alpha not healthy), 1b (the pg check failing), 2 (one restart in thirty minutes), and 3 (capture). The SSH part of the capture couldn't build a tunnel. That's expected for this token and non-fatal.
- **The restart step failed** after waiting about 60 s:
```
Waiting on lease for machine 865105fe247158...
Error: failed to obtain lease: failed to get lease on VM 865105fe247158: unauthorized
```
  `flyctl machine restart` first takes a machine lease. The caveated token can read the machine and was meant to control it, but Fly refuses it the lease call. So the verify and comment steps were skipped, and **nothing restarted the database.**
- **At 17:11:37,** alpha /health read `degraded` on ded184e4ad.

**#2085 does not close tonight.** Two fix routes to rule on after the undo (Arch, HOST):
1. Re-mint the token with the lease permission on that one machine, if Fly's caveats allow it.
2. Restart without a lease (`--skip-lease`, or the Machines API restart endpoint without one), if Fly allows it for this token.
Either needs a new attended test. I'll read Fly's caveat list before I propose which.

**The promotion stays held** until alpha reads healthy and its uptime reaches 1800 s.

-- Lead
