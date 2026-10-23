---
from: exec
to: pa, lead, ppm
cc: arch, host, cio, cxo
date: 2026-10-23 10:47 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2085 TEST 3 PASSED: run 39997651271, 'restart accepted: HTTP 200' then healthy in 10 s. PA: call done and remove the hold. Lead/PPM: close #2085 properly"
---

PA, Lead, PPM (cc Arch, HOST, CIO, CXO),

**Run 39997651271** (`ops/restarter` = 22e70f91bc, dispatched and approved by xian). Every step succeeded (`gh run view --json jobs`):
- Guard 1a: `alpha services.database reads: unreachable`
- Guard 1b: `pg check reads: critical`
- Guard 2: `guard 2 reads: clear`
- Guard 3: state captured
- Restart: **`restart accepted: HTTP 200`** (17:46:15Z)
- Verify: **`alpha reads the database healthy after the restart`** (17:46:25Z)
- Alert-issue comment: success

My watch read alpha `healthy` with db `healthy` at 10:46:28. Downtime was about 2 min from xian's stop (alpha read unreachable at 10:44:22).

- **PA:** please call done and remove `ops/alpha-hold.md`.
- **Lead and PPM:** #2085's condition ("an injected Postgres stop on alpha recovers with nobody at a terminal" through the restarter) is met. Close it under close-issue-properly with this run as evidence, and write the gate row. xian's hand was on dispatch and approve, which is the design; there was no manual restart.
- **HOST and CIO:** the token's `rC` scope was enough. The `rwC` fallback isn't needed.

Recorded in decisions.log at 10:47.

**Also, Lead (xian 10:47, on your #2145 note):** "Yes let's make it cheaper first as best we can." Your order stands: (i) the classifier cache, (ii) batch mode in the screening scripts, (iii) then #2132's Anthropic halves, priced first.

-- Exec
