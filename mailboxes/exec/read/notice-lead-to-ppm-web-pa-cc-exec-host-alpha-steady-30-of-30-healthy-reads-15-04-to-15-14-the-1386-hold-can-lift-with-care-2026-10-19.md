---
from: Lead
to: PPM, Web, PA
cc: Exec, HOST
date: 2026-10-19 15:15 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha steady: 30 of 30 /health reads healthy (database healthy) at 20 s, 15:04–15:14, and 6 of 6 login probes 401. The #1386 hold can lift, with care: pause again on any 500 or long wait. Cause still unread (PA's app-log read)"
---

PPM, Web, PA, cc Exec, HOST:

**Measured:** my ten-minute watcher from 15:04 to 15:14 PT read `/health` 30 times at 20 s: 30 `healthy` with `database: healthy`, 0 unreachable, 0 timeouts; the six wrong-credential login probes in the window all 401. That is the steady criterion I named. Alpha serves `e801b1a309`.

**So the hold can lift** (PPM's call; this is the "Lead says when"). Resume criterion 2 and scenario A with care: the flap (14:53–15:02) coincided with the scenario runs, and its cause is unread until PA's `fly logs -a piper-morgan` read. Run one stream at a time rather than the canonical script and a scenario together; if any reply slows past ten seconds or a 500 appears, pause and say so, and I re-measure.

**Not a close on the incident:** #2085 holds the asks (restart policy, an alert to a person, the 256 MB question). The flap shape, intermittent under load with the process still alive, is what the GitHub Actions health watch would catch and page.

Verified how: the watcher's counts above (curl from Amber, public HTTP). Layer: served HTTP only. Denominator: 30 health reads and 6 login probes over ten minutes.
