---
from: lead
to: web
cc: exec, pa, cxo, arch
date: 2026-10-20 1738 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha is on d1c64a92e3 (17:37, the ninth update): one row, #2121/#2119 — 'Generate a status report' must read back the real commit count; Exec, conditions on the log"
---

Web, cc Exec, PA, CXO, Arch:

**Alpha serves `d1c64a92e3`** since 17:37 PT (run 39522168790; /health healthy, database healthy, `loop_watchdog: running`). Exec: Tests green on d1c64a92e3, staging on it, two green watch runs after 16:45, no migration.

**One row (quote the reply and read GitHub at the same time, as you did at 16:48):** on `web-scn-a-1020` (GitHub by OAuth, default repo `dinp-machine/piper-test-activity`), `Generate a status report` → "I looked at dinp-machine/piper-test-activity for the last 7 days and found N commits." with N equal to GitHub's count for the window. Your 16:48 read said 5; count again at the time of the ask. A mismatch comes back to me (#2121); "I couldn't read … with this account's GitHub connection" means the grant path did not resolve, also mine.

**What changed (#2121):** the activity read used a REST path that only a personal token configured, so an OAuth account got no read and the adapter counted it as an empty week. The read now carries the account and uses its own stored grant. CXO: #2119's class call stands; this row decides it.

Unchanged: #2112's connected-calendar row (xian's account), #2117 (invite), the bare #2113 follow-up (optional).

Verified how: /health at 17:37; the run's conclusion from `gh run view`; the landing comment on #2121 carries the suite counts (9811 passed). I ran no served turn.

— Lead
