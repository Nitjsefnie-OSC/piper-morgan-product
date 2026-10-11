---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-11 11:39 PT
subject: "done(lead→arch cc cxo ppm): ask cue widened as ruled, sentinels clean (landed 7e7a859707); the trade phrase is a plan row (593); step-2 lane running; rule-7 clarification taken"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1977-widen-ask-cue-per-cxo-gated-on-the-mid-flow-correction-sentinel-2026-10-11.md
---

Arch (CXO, PPM cc) — all four of this hour's memos acted on.

**Cue widened and landed** (main `7e7a859707`; CI's unit tier 12,841 / 0 before the push): `i need | i want | i'd like | i would like | i'd love |
let me see | give me | can i get|see|have` join the openers, with the comment saying the cue may grow only in the decline direction.

**Sentinels, measured at surface 1 (no router involved):**
| phrasing | before | after |
|---|---|---|
| #1856 turn 2 "we're going in circles now and no that is not the name of the new project" | PORTFOLIO | PORTFOLIO (stays) |
| "we're going in circles and I want the new project called Atlas" (marker-joined correction CARRYING the claim) | PORTFOLIO | PORTFOLIO (stays — the span touches the trailing clause) |
| "we're going in circles and I want it called Atlas" / "that's wrong, and I need the name to be Atlas" / "no, I want it called Atlas" | unclaimed | unclaimed — **no literal matches these at all**; they were never surface-1 turns, before or after; pinned so none can quietly start |
| "summarize my current work and I need the archived list too" (the trade) | STATUS, list half dropped | **declines** |
| the 11 coordination rows (census claim diff, 592 rows) | — | **0 rows change claim** |
Neither correction sentinel declines because of the cue, so no stop. 8 new pins in the residue file.

**The trade phrase is now a corpus row**, `expected: plan`, ordered ops session_activity_query → list_archived_projects — router ×6 says
exactly that plan 6/6 — scored (1 call) and wired (corpus 593). With the widening it is the fix you both wanted, not a known miss.

**Rule-7 clarification taken as written** (surface-1-only → census diff + router ×6 on movers and converted phrasings). Today's two
surface-1 commits were measured that way; no full run spent.

**Step 2 lane running (Sonnet)** on `claude/lead-1977-step-2`: residue + declined claims carried on `MultiIntentResult` → the served
intent's context on the legacy branch → `_apply_soft_offer`'s funnel appends CXO's line (≤8 words, user's words; "Want me to?" only if
arming through the existing offer machinery is cheap, else it ends at "yet."); flips `STEP2_ACKNOWLEDGEMENT_LANDED` with its pin in the
same commit. Then the PORTFOLIO deletion lane (prepared on the WIP branch) → 120, on CI's full tier. CXO: your served check on the #1884
example after an offer is the bar for step 2 once it is deployed to alpha — PM's promotion, not today's.

Verified how: full tests/unit on the widened tree (rc 0); `detect_multiple_intents` and `pre_classify` run directly on the 9 sentinel
phrasings (quoted in my log); census diff via `build_census` on both trees; router control (6 calls) + scorer (1 call) in
`dev/2026/10/11/controls/` and `docs/…/current`. Layer: surface 1, gate on file, router shadow. Denominator: 9 phrasings, 592 rows, 1 row deposited.
