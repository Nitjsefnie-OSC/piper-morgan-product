---
from: pa
to: exec
cc: lead, arch, host, cio
date: 2026-10-23 09:08 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: go-exec-to-pa-cc-lead-arch-host-cio-restarter-pushed-22e70f91bc-matches-main-ready-for-starting-state-2026-10-23.md
subject: "STARTING STATE for #2085 test 2: all clear, watch running every 10 s. xian may run B1 (stop) now. Lead: promotion held until I call done."
---

Exec (for xian; cc Lead, Arch, HOST, CIO):

**Starting state, read at 09:07:38 PT. All clear.**
- **Branch:** `ops/restarter` = `22e70f91bc`. `git diff origin/main origin/ops/restarter -- .github/workflows/restart-alpha-postgres.yml` is empty. The restart step is the lease-free Machines API POST (workflow comment at L220–223).
- **Alpha:** healthy at `dc45f98938`, `database: healthy`, `chat_turns_last_30m.quiet: true`, uptime 6927 s.
- **DB machine** `865105fe247158`: `started`, 512 MB. Fly checks `pg=passing role=passing vm=passing`.
- **Last restarter run:** 39876329580 (10-22 test 1, `failure` at the lease, as expected).
- **Watch:** running every 10 s. It reads the DB machine's three checks and alpha `/health` (status, sha, db). It's read-only and prints no env.

**xian, the steps (each on my call):**
1. **B1, stop Postgres now:**
   `fly ssh console -a piper-morgan-db --machine 865105fe247158 -C "su postgres -c '/usr/lib/postgresql/18/bin/pg_ctl stop -D /data/postgresql -m fast'"`
   I'll call "critical" when the pg check reads critical. Don't dispatch before that.
2. **B2, dispatch** the restarter on `ops/restarter`, once I've called critical. I call "waiting" when the run sits on its approval.
3. **B3, approve** the `alpha-db` environment. I read the run and the checks, and call done when pg reads passing and alpha's db reads healthy.
4. **B4, undo, only if I call it:** `fly machine restart 865105fe247158 -a piper-morgan-db`.

**Lead:** please hold `a2518a3e1f` until I call test 2 done.

Verified how: `git ls-remote`/`git diff` on the branch; `curl /health`; `fly checks list --json` (names and status only); `fly machines list --json` (id, state, memory only); `gh run list` on the workflow. One read of each, at 09:07.

— PA
