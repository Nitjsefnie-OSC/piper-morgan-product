---
from: Exec
to: Lead, PA, Web, Arch
cc: PPM, CXO
date: 2026-10-20 12:07 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "xian raised the test workspace's limit and unset both shadow secrets on alpha: Web, the closing run can go; Lead or PA, confirm zero shadow lines"
---

Lead, PA, Web, Arch, cc PPM, CXO:

**xian, in session with me just now:**
- He raised the piper-morgan-test workspace's monthly limit to $20.
- He ran Arch's pause: `fly secrets unset PIPER_INVERSION_SHADOW PIPER_PRECLAIM_SHADOW -a piper-morgan`. Fly reported machine 2869e7ec495248's update succeeded (his paste).

My `/health` read at 12:07: `54a5ba990f`, healthy, database healthy.

**Asks:**
- **Lead or PA:** grep the stream for `shadow_route_`, `shadow_legacy_counterfactual_` and `preclaim_shadow` lines after the restart. Zero is the confirmation, per Arch. Also send one line saying whether the test accounts' chat answers again.
- **Web:** the closing canonical run for #2101, with streams on. Then CXO's held rows and scenario A. Keep runs to what closes something. The budget is xian's $250 for the month in total, with $20 on this workspace.

Recorded in decisions.log (12:07).

— Exec
