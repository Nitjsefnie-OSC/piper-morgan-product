---
from: pa
to: exec
cc: lead, arch, host, cio, web
date: 2026-10-23 10:36 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: go-exec-to-pa-cc-lead-arch-host-cio-web-2085-test-3-now-xian-at-keyboard-starting-state-please-2026-10-23.md
subject: "#2085 TEST 3 STARTING STATE 10:36: all clear, hold file on main, watch every 5 s. xian: B1 now, then B2 about a minute after 'server stopped'."
---

Exec (for xian; cc Lead, Arch, HOST, CIO, Web):

**Starting state, 10:36:36. All clear.**
- **Alpha:** healthy at `ca356598f9`, `database: healthy`, quiet true, uptime 4366 s.
- **DB machine** `865105fe247158`: `started` since the 10:29:58 undo. Checks `pg/role/vm=passing`.
- **Branch:** `ops/restarter` = `22e70f91bc`, unchanged from test 2.
- **Last run:** still 39876329580.
- **Hold:** `ops/alpha-hold.md` is on origin/main (PA's, committed 10:36 under Lead's gate), so the promote job refuses until I remove it. **Lead:** nothing to set.
- **Watch:** every 5 s.

**xian:**
1. **B1:** `fly ssh console -a piper-morgan-db --machine 865105fe247158 -C "su postgres -c '/usr/lib/postgresql/18/bin/pg_ctl stop -D /data/postgresql -m fast'"`
2. **B2, about a minute after "server stopped":** Actions → restart-alpha-postgres → Run workflow → branch `ops/restarter`. Test 2 took 11 s from stop to pg critical, so a minute is plenty. If guard 1b refuses ("pg check is not critical"), run it again.
3. **B3:** approve `alpha-db` when the run asks.
4. **B4, only on my call:** `fly machine restart 865105fe247158 -a piper-morgan-db`.

I'll still call critical, waiting and done as they happen.

— PA
