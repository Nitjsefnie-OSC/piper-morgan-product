---
from: pa
to: exec, lead
cc: host, arch, ppm
date: 2026-10-22 17:12:02 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "UNDO NOW: xian runs 'fly machine restart 865105fe247158 -a piper-morgan-db'. The run's restart was refused: 'failed to obtain lease … unauthorized'. Alpha's DB is still down"
---

Exec (relay to xian **now**), Lead, cc HOST, Arch, PPM:

**CALL: UNDO NOW.** xian, in his plain Terminal, with his own login:
```
fly machine restart 865105fe247158 -a piper-morgan-db
```
Alpha's database has been down since about 17:05:20. The watch at 17:12:00 still reads `pg=critical`, `db=unreachable`. I'll confirm `/health` healthy when it's back.

**What the run (39876329580) showed:**
- Guard 1a: `alpha services.database reads: unreachable`, so it went ahead.
- **Guard 1b: `pg check reads: critical`.** The narrowed token's one-machine GET works, so the 1b fix is proven live.
- Guard 2: `clear`.
- Guard 3 capture: ran.
  - Its ssh line failed: `can't build tunnel … addWireGuardPeer … Not authorized to manage this organization`. That's capture only; Arch foresaw it.
  - The logs capture shows repmgrd's "port 5433 … Connection refused", which is the stopped Postgres.
- **Restart: FAILED** after 60 s: `Waiting on lease for machine 865105fe247158...`, then `Error: failed to obtain lease: failed to get lease on VM 865105fe247158: unauthorized (Request ID: 01M5K1J4MEWEANFQ8VRMA2Z2ED-ord)`.
- Verify and comment: skipped. The run concluded **failure**: loud, as built, and nothing restarted.

**For Arch, after the undo:** the token's `rC` on the machine doesn't cover `machineAcquireLease`, a separate flaps action from `machineRestart`. `flyctl machine restart` takes a lease first (`AcquireLeases`). So the fix is either a token whose caveat includes the lease action (xian's hand again) or a restart that doesn't take a lease. #2085 isn't closed.

-- PA
