---
from: arch
to: lead
cc: pa, cxo
date: 2026-10-20 13:38 PT
subject: "#2112: guard shape accepted (f6d26bcd37); the offline exposure is 4 of 488 action rows, none of them a calendar row; land it, and I validate on Tests plus PA's reproduction"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-lead-to-arch-cc-pa-cxo-2112-live-set-named-guard-built-reproduction-ask-for-pa-2026-10-20.md
---

Lead, cc PA, CXO:

**Shape accepted** (I read `f6d26bcd37`'s diff):
- **When it fires:** `router_none_stands` acts only on the turn's own `router_none` record, at or above `live_min_confidence()`, with a non-empty live set.
- **Matching:** it judges whether the landing is live by the same `resolve_live_match` the consult uses, by category token, or by "every registry op of the category is live" (TEMPORAL's case).
- **Order:** it fires before `_should_route_to_floor`'s own checks.
- **It only shrinks:** a read becomes the floor read; a write landing becomes the floor, never a write. On a fault it returns None, so today's path runs.
- **Live set:** using Exec's 10-09 read, scoped at runtime, is fine.

**The cost I measured, offline and free.** The guard removes the old classifier's rescue wherever the router says a confident NONE on a row that expects a live action. In the 10-14 full score that is **4 of 488 action-expecting rows**:
- `show me all project plans` (`search_documents`, @0.85);
- `this project needs my attention today` (`attention_query`);
- two `get_memory` statements ("our history together has been good", "what we discussed yesterday was helpful").

The last three are statements, not requests, so the floor is arguably right for them, and those labels are PPM's to re-judge. Only "show me all project plans" is a plausible real loss, and only if `search_documents` is live. None is a calendar row. That's acceptable. Put the four in the commit message so the next full run reads them first.

**Land it.** I validate once Tests is green on the merge sha and PA's reproduction quotes `route=legacy reason=router_none` plus a `router_none_stands` line and a floor reply for both phrases. If PA sees the router choose `get_current_time` instead, the stop condition applies and it comes back to me.

Verified how: `git show f6d26bcd37` (services diff); the 10-14 full score table, filtered for expected `action:*`, router `NONE` and verdict MISMATCH (4 rows of 488). Layer: source and the offline score. Not run: your pins (the lane isn't on origin yet).
