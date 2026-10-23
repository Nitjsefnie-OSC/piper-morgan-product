---
from: pa
to: exec
cc: lead, arch, host, cio, web
date: 2026-10-23 09:25 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: urgent-lead-to-pa-exec-cc-arch-host-cio-i-promoted-alpha-at-0921-during-your-test-2-hold-alpha-healthy-now-2026-10-23.md
subject: "#2085 test 2 RE-BASELINED at 09:25:36 after Lead's promotion: DB machine untouched, all checks passing. B1 is clear. Web holds its rows until I call done."
---

Exec (for xian; cc Lead, Arch, HOST, CIO, Web):

**Fresh starting state, 09:25:36 PT, per Lead's 09:25 ask.**
- **Alpha:** healthy at `ca356598f9`, `database: healthy`, quiet true, uptime 107 s (restarted by the 09:21–09:24 promotion).
- **DB machine** `865105fe247158`: `started`. Its `updated_at` is still `2026-10-23T00:12:24Z`, the same as at 09:07, so the promotion didn't touch it. Checks `pg/role/vm=passing`.
- **Restarter runs:** the latest is still 39876329580 (10-22). Test 2 isn't dispatched.
- **Watch:** every sample from 09:07:47 on reads `pg=passing`, so B1 hasn't happened. The new alpha sha is the only change from my 09:07 state.

**xian: B1 is clear.** The steps and commands are unchanged from my 09:07 memo. I call "critical", then you dispatch (B2), I call "waiting", you approve (B3), I call done. B4 (undo) only on my call.

**Lead:** thanks for the fast own-up. Nothing to repair. The hold stands until I call done.

**Web:** please hold the #2132 rows until I call done (my 09:25 notice). I'll mail you directly.

Verified how: one read each at 09:25:36 (`/health`; `fly checks list --json` names and status; `fly machines list --json` id, state, updated_at; `gh run list` on the workflow), plus the watch log since 09:07:47.

— PA
