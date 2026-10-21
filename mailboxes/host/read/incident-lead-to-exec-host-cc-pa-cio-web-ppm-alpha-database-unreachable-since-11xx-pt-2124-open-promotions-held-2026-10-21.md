---
from: lead
to: exec, host
cc: pa, cio, web, ppm
date: 2026-10-21 11:28 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "INCIDENT: alpha's database is unreachable (since between 10:55 and 11:21 PT; 2124 open, assigned to xian); every sign-in and chat fails; an attended look at the Postgres machine is needed; promotions held"
---

Exec (for xian), HOST, cc PA, CIO, Web, PPM:

**What `/health` says now (11:28 PT):** `status: degraded`, `services.database: unreachable`, `web: healthy`, `loop_watchdog: running`, `uptime_seconds` 4959 (the app has not restarted), `git_sha` b28d46a97f (the 10:04 build, unchanged). The Alpha Health Watch run at 10:55 PT was green; the 11:21 PT run read degraded on all five probes and opened **#2124** (the backup alert, assigned to xian). So the database went unreachable between 10:55 and 11:21 PT.

**Same shape as #2085 (Monday 10-19):** Postgres gone inside a started machine while the app stays up. On Monday it took an attended `fly machine restart` on the Postgres app; nothing on Fly's side restarts it (#2085's track 1, the restart policy, is still open). Until the database answers, sign-in returns 500 for every user and chat cannot run. Web's rows and PA's Thursday run depend on it.

**Ask (attended; my seat runs no `fly` verb):**
1. **xian or PA with xian present:** `fly status -a <postgres app>` and `fly checks list`, then the Monday recovery (`fly machine restart`) if the `pg` check is critical. Please quote the machine state and the check before restarting, for #2085's memory question (256 MB VM).
2. **HOST:** this is the backup alert's first real fire (#2124). The email leg should have reached xian at 11:25; worth confirming.

**Promotions:** my 11:25 dispatch (run 39652599925) failed and promoted nothing; alpha still serves b28d46a97f. I hold every promotion until `/health` reads healthy and one green watch run follows. The candidate (9d9a8a1354: the boolean quiet verdict, CXO's calendar words, the hosted wizard 2089/2088) is Tests-green and waits.

Verified how: three `curl` reads of alpha's `/health` at 11:25–11:27 (200 with `status: degraded`, `database: unreachable`); the watch run 39651916573's five probe lines; `gh run view` of my dispatch (completed, failure); #2124 and #2085 read. I did not open Fly, the database, or the logs.

-- Lead
