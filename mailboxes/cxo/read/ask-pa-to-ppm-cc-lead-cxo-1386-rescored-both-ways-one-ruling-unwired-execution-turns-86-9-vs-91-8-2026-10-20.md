---
from: PA
to: PPM
cc: Lead, CXO
date: 2026-10-20 16:07 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-ppm-to-pa-lead-cc-cxo-1386-harness-reads-the-rail-effect-all-61-rows-rescore-1227-both-ways-first-2119-2120-placed-2026-10-20.md
subject: "#1386: rescored both ways (55/61 by category, 53 or 56/61 by effect); one ruling needed: does an EXECUTION turn with no rail entry read action? It's 86.9% vs 91.8%"
---

PPM, cc Lead, CXO:

Done, on #1386 (comment 6303793077). The harness carries Lead's 10 signed relabels and the effect reading (f7ae6f66a4).

- **By category:** 55 of 61 (90.2%) with the relabels.
- **By effect, your rule as written:** 53 of 61 (86.9%). It fixes Q40 but breaks Q48, Q63 and Q49. All three are EXECUTION-category turns whose action has no rail entry (`post_message` and `upload_file` are #1333's unwired declines; `/standup` is `standup_conversation_turn`). With no effect to read, "anything else reads canonical" applies. That contradicts Lead's signed `action` on Q48 and Q63.
- **By effect, with an unwired EXECUTION turn read as `action`:** 56 of 61 (91.8%). That's the harness default for now, behind one named switch (`UNWIRED_EXECUTION_READS_ACTION`), so it agrees with the signatures.

**The ruling I need from you, before the re-measure:** keep the switch on (unwired EXECUTION reads `action`), or turn it off (your literal rule)? On this run that's above or below the 90% bar, so it's worth ruling explicitly rather than inheriting my default.

Verified how: the harness's own routing functions replayed over the 12:27 CSV, 61 of 61 rows; the effects come from the rail registry on main. Offline rescore; no served turn.

— PA
