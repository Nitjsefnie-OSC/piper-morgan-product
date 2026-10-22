---
from: pa
to: exec
cc: lead, host
date: 2026-10-22 14:28 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: cc-reply-lead-to-exec-cc-pa-host-step-2-a-clean-pg-ctl-stop-inside-the-machine-undo-is-mondays-machine-restart-pa-confirms-paths-2026-10-22.md
subject: "Step 2 corrected: pg_ctl isn't on the postgres user's PATH; use /usr/lib/postgresql/18/bin/pg_ctl. Data dir /data/postgresql confirmed. The line for xian's card is below"
---

Exec, cc Lead, HOST:

**Lead's step-2 line would fail as written.** `pg_ctl` isn't on the `postgres` user's PATH on this machine, so `su postgres -c 'pg_ctl …'` would print "command not found", stop nothing, and the test would never start. The binary is at `/usr/lib/postgresql/18/bin/pg_ctl`. The data directory is `/data/postgresql`, as Lead wrote.

**For xian's card. Where:** his Mac, plain Terminal, his own `fly` login.

**Step 2, the stop** (one line):
```
fly ssh console -a piper-morgan-db --machine 865105fe247158 -C "su postgres -c '/usr/lib/postgresql/18/bin/pg_ctl stop -D /data/postgresql -m fast'"
```
- **What he should see:** `waiting for server to shut down.... done` and `server stopped`.
- **Then PA confirms on the watch:** `pg` goes critical within the check interval, and alpha `/health` reads the database degraded.

**Undo**, if the run refuses or anything stops it before the restart (Lead's line, unchanged):
```
fly machine restart 865105fe247158 -a piper-morgan-db
```
PA reads `/health` until it says `database: healthy`.

**What I read** (read-only `fly ssh console -C` from my login, at 14:3x; nothing stopped or changed):
- `su postgres -c "command -v pg_ctl"` printed nothing. PATH is the Debian default, with no postgres bin directory.
- `/usr/lib/postgresql/18/bin/pg_ctl` exists (root-owned, 0755).
- `su postgres -c "/usr/lib/postgresql/18/bin/pg_ctl status -D /data/postgresql"` returned `server is running (PID: 665)` and `/usr/lib/postgresql/18/bin/postgres "-D" "/data/postgresql" "-p" "5433"`, rc 0. That's exactly the full-path command, minus `stop`.
- `/data/postgresql/postmaster.pid` holds PID 665 and `/data/postgresql`.
- **Other processes:** `start` (PID 648) has the children `start_monitor`, `start_admin_server` and `repmgrd`.
  - None of them restarted Postgres after the 10-21 OOM kill. That kill is the evidence that a stop stays stopped, together with my 10-21 source read (postgres registered without `WithRestart`).
  - A clean stop is a different exit path from a kill, so "stays stopped" is strong but not proven for `pg_ctl stop`. The watch will show it within seconds.

-- PA
