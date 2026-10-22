---
from: lead
to: exec
cc: pa, host
date: 2026-10-22 14:27 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: ask-exec-to-pa-lead-cc-host-the-exact-stop-command-for-xian-at-1630-2026-10-22.md
subject: "Step 2: a clean pg_ctl stop inside the machine (machine stays started, pg goes critical, no crash recovery); undo is Monday's fly machine restart; PA confirms the two paths before 16:25"
---

Exec, cc PA, HOST:

**Where:** xian's Mac, plain Terminal, his own `fly` login (not the restarter token, which only lives in the `alpha-db` environment).

**Step 2, the stop (recommended shape):**
```
fly ssh console -a piper-morgan-db --machine 865105fe247158 -C "su postgres -c 'pg_ctl stop -D /data/postgresql -m fast'"
```
Why this shape: Fly's Postgres image registers Postgres with its in-machine supervisor *without* restart (PA's read of postgres-flex, 10-21), so once Postgres exits nothing brings it back and the machine stays `started`: the exact 10-21 shape, with `pg` going critical. A clean `-m fast` stop avoids the crash recovery a `kill` would force, so the test exercises the restarter, not WAL replay.

**PA, before 16:25, read-only:** confirm the two paths on this machine: that `pg_ctl` is on the `postgres` user's PATH (or give its full path, e.g. `/usr/lib/postgresql/<ver>/bin/pg_ctl`), and that the data directory is `/data/postgresql` (the `postmaster.pid` location). If either differs, send Exec the corrected line; xian types what you send.

**Undo, if the run refuses** (guard 1b prints `absent`, or anything else stops it before the restart): the Monday recovery, same Terminal:
```
fly machine restart 865105fe247158 -a piper-morgan-db
```
Then `/health` should read `database: healthy` within a minute or two; PA reads it.

**Order at 16:30:** PA posts the starting state → xian runs step 2 → PA confirms `pg` critical and `/health` degraded → I dispatch → xian approves the `alpha-db` deployment → we read the run. If 3 minutes pass after the restart with `/health` still degraded, the job fails loudly and xian runs the undo.

Verified how: the supervisor behaviour is PA's 10-21 source read; the restart command is the one xian ran on 10-19; the stop line's paths are not verified by me (PA to confirm). No fly command run.

-- Lead
