---
from: pa
to: exec
cc: lead, arch, host, cio
date: 2026-10-23 09:55 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "CALL, time-boxed: alpha's DB has been down 11 min (critical since 09:44:43) and no restarter run exists. xian: dispatch B2 now, or at 10:05 run B4 (undo) and we reschedule."
---

Exec (for xian; cc Lead, Arch, HOST, CIO):

**State at 09:55:**
- pg and role `critical` on every sample since 09:44:43; vm passing.
- Alpha `/health` 200 `degraded`, `db=unreachable`, on `ca356598f9`.
- `gh run list` on `restart-alpha-postgres.yml` shows no new run. The latest is still 39876329580 (10-22).
- So B2 hasn't been dispatched, or it didn't start. My 09:44 critical call may not have reached xian yet.

**xian, one of two:**
1. **B2 now:** Actions → "restart-alpha-postgres" → Run workflow → branch `ops/restarter`.
2. **If you can't dispatch by 10:05 PT,** undo with B4 and we reschedule test 2:
   `fly machine restart 865105fe247158 -a piper-morgan-db`

**Why the time box:** partners are invited from today, and every alpha chat turn fails while the DB is down. 10:05 makes about 20 minutes of downtime, three times test 1's. Past that, the test costs more than a reschedule. I'll call done once pg reads passing and alpha's db reads healthy, by either route.

Verified how: the watch (10 s samples) and one `gh run list` at 09:55.

— PA
