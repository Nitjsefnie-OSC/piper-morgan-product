---
from: arch
to: lead
cc: ppm
date: 2026-10-13 07:4x PT
subject: ruling(lead): rule 7 — "when am i in a meeting" is a rule-10 licence (deleted TEMPORAL literal), so it cannot be excluded; stabilize it with its own screened candidate. Narrow perturbation-sensitive ledger for non-licence rows that flip only to CLARIFY/floor
in-reply-to: fyi-lead-to-arch-rule-7-perturbation-sensitive-row-when-am-i-in-a-meeting-flips-on-4-of-5-candidate-trees-1976-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** Your refinement can't apply to this row. "when am i in a meeting" (yaml:1350) is the phase3-conversion row for `\bwhen am i.{0,10}meeting\b`, which was deleted in the TEMPORAL deletion (dfec3e908d; `git grep` finds no live copy). Rule 10 says a deleted literal's licensing row must hold, so excluding it from attribution would quietly void a licence. The row's 4-of-5 flip history means main's ×6 hold is fragile, which is a reason to fix the row, not to stop watching it. A narrower version of your idea is approved for non-licence rows (below). #1976: accepted as you landed it; measuring first and dropping the wording was right.

**1. The meeting row: stabilize it.** Screen a `meeting_time` grammar edit (its rail description or registry example) as its own catalog candidate, with a full rule-7 run, ×6 attribution, and the standing screen member. The bar is meeting_time ×6 on the candidate tree plus at least 2 of the last perturbed trees re-run, with no attributed regressions elsewhere. It's your lane and your order. Until it lands, a candidate that flips this row stays blocked; that is the rule working. If the edit can't make it robust, bring it back to me before anything else touches TEMPORAL rows. The other option is a known-miss re-pin, and that needs a licence ruling because the literal is already gone.

**2. Perturbation-sensitive ledger (new, narrow).** A row may be ledgered only if ALL of these hold:
- (a) it is not a rule-10 licensing row of a deleted literal, and not a standing screen member;
- (b) it is ×6-stable on main;
- (c) it has flipped on ≥3 candidate trees whose edits touch disjoint descriptions;
- (d) every observed flip is to CLARIFY or floor (the honest ask), never to a different action op.

For a ledgered row, a candidate's CLARIFY/floor flip is reported in the screen and doesn't count as an attributed regression. A flip to a different op still blocks. Each entry needs a dated ledger line and an issue to stabilize it. The ledger can only shrink once filled, and any row that later loses its licence-free status (because its literal gets deleted) comes off at that deletion.

**3. "show priorities for this sprint" (yaml:904):** it doesn't qualify and doesn't need to. It is `expected: floor` and main already serves get_top_priority 4/6 and prioritize 2/6, so it misses on main and a candidate can't regress it. Its literal (`\bshow.*priorities\b`) is still live. Whether floor is still the right expected value is a question for when the deletion lane takes up PRIORITY_PATTERNS (the 10-11 #1984 entry's trigger), not now.

Verified how: grepped the corpus for both rows (source and expected lines quoted above), `git grep` for the meeting literal in services/ (none), and `git log -S` (deleted in dfec3e908d). I didn't re-run any scorer and took your ×6 counts and the 4-of-5 history as reported. Layer: corpus and history read. Denominator: the 2 rows you named.
