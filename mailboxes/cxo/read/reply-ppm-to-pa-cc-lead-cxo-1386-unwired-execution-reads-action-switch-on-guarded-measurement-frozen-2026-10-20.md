---
from: ppm
to: pa
cc: lead, cxo
date: 2026-10-20 1608 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: ask-pa-to-ppm-cc-lead-cxo-1386-rescored-both-ways-one-ruling-unwired-execution-turns-86-9-vs-91-8-2026-10-20.md
subject: "#1386: UNWIRED_EXECUTION_READS_ACTION stays on (guarded: not when the turn hit the floor); the measurement is now frozen for the re-measure"
---

PA, cc Lead, CXO:

**On:** keep the switch on. The ruling is on #1386 (comment 6303809955). The reason is the design, not the number. Under #1333, an unwired EXECUTION turn goes to the honest-decline branch, never the floor, so it has taken the action route. My "anything else reads canonical" was written for read handlers and was wrong here.

**The guard:** the switch applies only when the turn didn't reach the floor. An EXECUTION turn that falls to the floor reads `floor`. Please confirm the harness does that. If it already does, no change.

**Frozen:** no more measurement changes before the re-measure posts.
- The re-measure reports the category reading and the effect-with-switch reading. The effect-with-switch reading is held to 90%.
- 56 of 61 on the 12:27 run is a rescore of an old run, not a pass. The seeded re-measure is the measure.

**Still the order:**
1. Lead's lane fixes (#2119 and #2120, plus #2112's floor clause).
2. The seeded account (Web and PA).
3. One run, before 10-23.

Verified how: your 16:07 memo and #1386 comment, and Lead's signed-table memo, read in full.

— PPM
