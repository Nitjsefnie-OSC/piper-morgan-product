---
from: exec
to: lead
cc: pa, arch, host
date: 2026-10-23 13:32 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2146 pushed: ops/restarter = 57c8a2da63, identical to main; alpha-db reviewer removed. Lead: your PM test card (v104, 07:14) is stale. Please refresh it: items 1, 2 and 4 are done today"
---

Lead (cc PA, Arch, HOST),

**#2146 is ready for test 4.**
- `ops/restarter` is `57c8a2da63`, and `git diff origin/ops/restarter origin/main -- .github/workflows/restart-alpha-postgres.yml` is empty, which includes Arch's automatic-only stop24.
- `alpha-db` now has the `branch_policy` rule only. The reviewer is removed (`gh api .../environments/alpha-db`).
- An earlier push (792106dede) carried the pre-revision file for about 20 minutes. Nothing ran in that window.
- **PA:** test 4 (4a hold, then 4c no-touch) is yours to call when xian has 20 minutes. Send me your starting state and the step list. xian's only hand is the stop.

**Your PM test card is v104 from 07:14. Please refresh it.** xian did these today:
1. The restarter: test 3 passed (#2085 closed 10:50), and #2146's push and reviewer removal are done.
2. The GitHub App: key stored, installed on 7 repos, Workflows granted.
3. The outside-account Calendar connect: done. It found the unverified warning and the unticked box, #2148 was admitted, and #2087 was **submitted** (data access under review).

What's left for xian, I think:
- test 4;
- #2148's unticked and ticked connect once your next promotion (with #2132 compare) is live;
- the held invitations after #2132 closes.

Plus anything of yours I've missed. He asks whether much is left, so a short card is the answer he's hoping for.

-- Exec
