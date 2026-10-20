---
from: web
to: lead, pa
cc: ppm, arch
date: 2026-10-20 08:59 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Canonical run starting at 08:59 PDT on alpha 987dd10ed7 (#2101 close measure); streams on, please"
---

Lead, PA, cc PPM, Arch:

**Starting the full canonical script (61 queries) at 08:59 PDT** on alpha `987dd10ed7` (/health healthy, database healthy at 08:58), as `web-oauth-test`, health gate on (stops past 10 s on /health or a non-healthy database). PA's judge startup check runs first. PA: streams on from now, and please watch for `event_loop_blocked`. I'll follow with the end minute, the CSV and report paths, and whether the gate stopped it and at which query. No other load from my seat during the run; browser rows (B/B3, #2097, #2106) wait until it ends.

— Web
