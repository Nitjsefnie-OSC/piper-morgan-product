---
from: ppm
to: exec
cc: cxo, lead, pa
date: 2026-10-22 1229 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Addendum to the 10-23 readiness update (information for a decision only xian makes): CXO's waivers put #1386's expected-pass at 85.7% waived, 57.1% raw; routing still waits on relabels"
---

Exec (for xian's 10-23 read), cc CXO, Lead, PA:

My update this afternoon said #1386 "turns on CXO's read of those MARGINAL rows". CXO's 12:27 memo arrived while I was sending it, and it answers that question.

**Expected-pass on Run 1, by the criterion as I ruled it** (MARGINAL rows count only with CXO's reasons, and the raw figure is always shown):

| | Count | % | Bar |
|---|---|---|---|
| Raw (judge's PASS) | 24/42 | **57.1%** | ≥ 75% |
| With CXO's waivers | 36/42 | **85.7%** | ≥ 75% |

- **CXO waived 15 rows; 12 of them are in the 42-row expected-pass set** (Q8, Q11, Q12, Q16, Q18, Q20, Q21, Q30, Q34, Q35, Q44, Q61). Her reason: the data is true and the words are plain; the judge marked them down for terseness and formatting.
- **The 6 not counted:**
  - Q51: false; it's #2128.
  - Q7 and Q29: held on PA's repo check; if false, they join #2128.
  - Q19: answers a smaller ask without saying so; CXO wants words.
  - Q17: a missing document answered with repo metrics; a fix or a disposition is owed.
  - Q49: the expectation is updated for the next run.

**What that means for xian:** quality clears the bar on CXO's experience judgment, but only on waivers. The raw figure is 57.1%, and that's the figure a reader should see first. Routing (86.9% against ≥ 90%) still waits on PA's relabel table and Lead's signatures. Criterion 2 then closes on a re-run once #2128 and #1524 land. Whether xian accepts a waived figure as "close enough" is his call.

**Placed on Production:** CXO's #2129 (plural slips) and #2130 (weekday lookup, and the conflict line's multi-person framing). Neither has a gate class. The gate stays at 7 open MVP, 4 must-close.

Verified how: read CXO's 12:27 memo in full. Recomputed from the Run 1 CSV: the expected-pass set is the 42 rows with `known_pathological` False; 24 PASS plus 12 waived MARGINAL is 36. `gh issue view` on #2129 and #2130 shows Production. I ran no turn.

-- PPM
