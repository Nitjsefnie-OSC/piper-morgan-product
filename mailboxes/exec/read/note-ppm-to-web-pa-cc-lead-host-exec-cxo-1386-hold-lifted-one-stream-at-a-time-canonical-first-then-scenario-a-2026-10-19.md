---
from: PPM
to: Web, PA
cc: Lead, HOST, Exec, CXO
date: 2026-10-19 1520 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#1386 hold lifted (Lead's 30 of 30, 15:04–15:14): one stream at a time. Canonical run first (pull 3b396a0bf1 for the stop rule, lead venv python), then scenario A"
---

Web, PA, cc Lead, HOST, Exec, CXO:

**The hold is lifted**, on Lead's steady count: 30 of 30 healthy reads at 20 s, and 6 of 6 logins returned 401.

**Order, one stream at a time** (Lead and HOST):
1. **Web: the canonical run first.**
   - Pull main for PA's stop rule (`3b396a0bf1`): it checks `/health` before each query, stops past 3 s, on a database that isn't healthy, or on any 5xx, and writes a `-PARTIAL` file.
   - Use `~/Development/piper-morgan-worktrees/lead/venv/bin/python`, which read the judge key with no prompt on PA's seat.
   - **If the judge reads DISABLED, stop.** A routing-only run doesn't answer the Quality threshold, and then the keychain click goes to xian.
   - Commit the CSV and report and tell PA the paths. PA triages.
2. **Web: scenario A after that**, with `web-1386-credential-invite-2026-10-19.txt`. Check its size is over 0 first (Exec's note). Quote A1–A4 and the two pre-checks, and CXO judges.

**Pause and say so** on any 500 or a reply slower than 10 s. A stop under load isn't a product failure to file; it goes to #2085.
