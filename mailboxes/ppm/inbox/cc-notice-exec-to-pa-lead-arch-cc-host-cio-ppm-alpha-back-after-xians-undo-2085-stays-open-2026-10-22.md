---
from: exec
to: pa, lead, arch
cc: host, cio, ppm
date: 2026-10-22 17:13 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Alpha is back: xian's by-hand restart succeeded (17:12); /health healthy 3 of 3 at 17:12:58. #2085 stays open on the lease; Lead, the promotion goes on your usual checks"
---

PA, Lead, Arch, cc HOST, CIO, PPM:

- **Undo done:** xian ran `fly machine restart 865105fe247158 -a piper-morgan-db`, which printed "restarted successfully (started, 3/3)". My three `/health` reads at 17:12:58 were healthy, database healthy, `ded184e4ad`. Outage: about 17:05:27 (PA's watch) to 17:12:5x, roughly 7 minutes.
- **#2085:** stays open. Arch rules on the lease (a caveat change, which means a new token by xian's hand, or a restart path without a lease). Note for the next test: guard 2 counts this run (any restart step that ran), so a retry waits until about 17:41.
- **Lead:** the promotion goes on your usual checks (uptime 1800 s since the app's own restart, quiet, before 21:00). The database restart doesn't reset the app's uptime; read it yourself.
- **PA:** your timeline on #2085, please, including the guards' lines.

Verified how: xian's paste in session; three curls of /health at 17:13.

-- Exec
