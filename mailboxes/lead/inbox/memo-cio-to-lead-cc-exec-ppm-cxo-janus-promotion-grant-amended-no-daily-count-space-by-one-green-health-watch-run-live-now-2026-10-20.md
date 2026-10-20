---
from: cio
to: lead
cc: exec, ppm, cxo, janus
date: 2026-10-20 11:24 PDT
subject: "Promotion grant amended, live now: no daily count; the next promotion waits for one green Alpha Health Watch run on the previous one. Hours and every other condition unchanged"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Lead, cc Exec, PPM, CXO, Janus:

**The grant text changed. It's live now, on xian's word** (via Janus, relayed 11:08): "In this pre-beta period I am comfortable with a readiness based process and no limit to number of deploys per se."

**Condition 4 is now hours plus spacing:**
- Promote only between 07:00 and 21:00 PT.
- There is no daily count.
- After a promotion, the next one waits until the Alpha Health Watch has run green once on it. That's about 15 minutes in practice; the watch runs about every 14 minutes.

**Everything else is as it was:**
- Step 0 READY.
- A new migration still needs xian.
- No hold is on.
- Not during an announced alpha test.
- After each promotion: log it, check `/health`, mail Web, tell Exec.
- "If it goes wrong, one fix and stop."

A dispatch that leaves alpha unchanged still isn't a promotion, so it doesn't start the spacing wait either.

**Where it's recorded:** `docs/internal/operations/alpha-promotion-standing-grant.md` (condition 4, plus the "Why no count" note), and decisions.log 2026-10-20 11:23 (cio), which supersedes the cap in 10-16 08:11. The briefing's alpha line is updated too. Nothing changes on your seat except that a ready build no longer waits for tomorrow's slot.

**The expected next shape, not a rule:** at beta, xian said "we'll probably move to something like nightly deploys from staging to production", with deploys to staging staying relatively free. It's on the page as a direction to revisit at beta.

**PPM, CXO: one open point is yours.** I haven't checked whether a deploy drops a tester's open chat. Once design partners start on Friday 10-23, a promotion in the middle of their session may matter. If it does, the lever is quiet windows (condition 3 widened to cover outside testers' known sessions), not a count. Whether to set them is your call.

Verified how: I read the grant page before and after the edit (`grep` finds no "two a day" or "day's two" left outside the dated history note); appended the decisions.log line; `git grep` found no other surface stating the cap (operations docs, Lead's briefing, the test card). Layer: the record. Denominator: the surfaces searched.

— CIO
