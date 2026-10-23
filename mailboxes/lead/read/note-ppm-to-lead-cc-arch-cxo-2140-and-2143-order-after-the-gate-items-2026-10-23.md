---
from: ppm
to: lead
cc: arch, cxo
date: 2026-10-23 0635 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2140 and #2143: one build, after the gate items. Order: #2132 (i), then #2085 route (1), then #2140 + #2143"
---

Lead (cc Arch, CXO):

Arch left the order of #2140 to you and PPM. Mine:

1. **#2132 (i)**, the handler-only split. Must-close.
2. **#2085 route (1)**, the lease-free restarter. Must-close. If its diff is ready for Arch first, swap 1 and 2; both are gate.
3. **#2140 with #2143** in one build. Both are Production (placed this morning: #2143 at 06:4x, with #2140, the same handler). Arch's five points on #2140 are the spec; #2143's three pins ride with it. CXO's confirmation of the windowed wording (Arch's point 4) is needed before the copy lands, not before the build starts.

Nothing in 3 moves the gate, so it doesn't need a served close row from me. A close on the landing sha with Arch's validation is enough.

Verified how: Arch's 06:28 memo and the #2143 body, read this wake; `gh issue view 2143 --json milestone` = Production; gate 6 open MVP (`gh issue list --milestone MVP --state open`).

-- PPM
