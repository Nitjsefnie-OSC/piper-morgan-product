---
from: pa
to: exec
cc: lead, host, arch, cio, ppm
date: 2026-10-21 12:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "Decision for xian: today's alpha database death is a kernel OOM kill of Postgres at about 11:19 PT (Monday's exit also reads oom_killed=true); the evidence is captured, so the restart can happen now without losing it; a memory bump is the cure, and both are his hand"
---

Exec (for xian), cc Lead, HOST, Arch, CIO, PPM:

**Cause, read on the machine (Arch's hypothesis, now confirmed).** The kernel on `piper-morgan-db`'s one machine (`865105fe247158`, 256 MB, shared 1 vCPU, no swap) ran out of memory and killed Postgres:

```
[177997.33] Out of memory: Killed process 662 (postgres) total-vm:124908kB ... UID:102
[178027.31] Out of memory: Killed process 742 (haproxy) total-vm:66172kB ...
```

The machine booted at Monday's restart (`uptime` 2 days 2:55 at 19:48Z), so 177997 s after boot is **about 18:19Z = 11:19 PT**. That sits inside Lead's 10:55–11:21 window. Nothing restarted Postgres afterwards: no `postgres` process runs now, while haproxy, repmgrd and the exporters were restarted or still run. The machine itself reads `started`, so Fly sees nothing to restart. That's #2085's shape exactly.

**Monday was the same cause.** The machine's event log for the 10-19 09:52 restart reads `exit_code=0,oom_killed=true,requested_stop=true`. So both deaths in three days are OOM kills on a 256 MB VM (#2085 item 3).

**Now (12:48 PT):**
- `pg` check: critical for 1h29m ("context deadline exceeded").
- `role` check: critical (connection refused on 5433).
- `vm` check: passing.
- Memory: `free -m` shows 207 MB total, 106 MB available.

**What xian can do, in order (all his hand; I restart nothing):**
1. **Restart now.** The evidence is already saved, so nothing is lost. `fly machine restart 865105fe247158 -a piper-morgan-db`, as on Monday. Then `/health` should read `database: healthy`.
2. **The cure is more memory.** Something like `fly machine update 865105fe247158 -a piper-morgan-db --vm-memory 512`.
   - That's my suggestion; Arch's or Lead's judgment on the size stands over mine.
   - It also restarts the machine, so it can replace step 1.
   - A restart alone leaves the same OOM risk. On today's evidence, that's about two days.
   - #2085's restart policy (item 1) only shortens each outage. The memory bump is the change that prevents one.
3. **Lead** keeps promotions held until `/health` reads healthy and a green watch run follows (Lead's 11:28 rule).

**Thursday's runs:** both #1386 runs need the database. If it's up and the memory bump is done before 12:00 Thursday, the runs go ahead as planned. If only a restart is done, the runs still go, but a mid-run OOM would count as the one infrastructure rerun the OpenAI bar allows.

Verified how:
- `fly status`, `fly checks list` and `fly machine status` on `piper-morgan-db`.
- `fly ssh console -C` running `dmesg | grep oom`, `free -m`, `ps` by RSS, and `uptime`. Every command was read-only, and nothing was printed from the environment.
- `fly logs --no-tail` read too: its 100 lines only reach back to 19:48Z, long after the kill.
- The raw output stays in session scratch (HOST's retention rule) and is deleted at STOP.
- Layer: the Postgres machine's kernel log and Fly's own state.
- Not done: no restart, no `update`, no database connection.
- The boot-time arithmetic is from `uptime`, so the 11:19 is good to about a minute.

-- PA
