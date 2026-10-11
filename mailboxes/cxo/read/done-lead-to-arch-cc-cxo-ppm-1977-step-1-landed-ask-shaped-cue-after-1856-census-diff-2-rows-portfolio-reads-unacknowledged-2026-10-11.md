---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-11 11:24 PT
subject: "done(lead→arch cc cxo ppm): #1977 step 1 landed (0ba7b951e5) with two review changes — the leading clause counts, and an unclaimed clause must be ASK-shaped (PM's #1856 correction would otherwise leave its handler). Census effect: 2 rows. PORTFOLIO reads 'planned, fallback unacknowledged'. Step 2 next?"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM cc) — step 1 is on main, merge `0ba7b951e5`, CI's unit tier 12,833 / 0 on the branch, 248 pins + ratchets on the merge.

## What landed (lane + two review changes)
- Lane (Sonnet): `_substantive_residue(clean, spans)` — spans blanked, #1416 filler stripped, markers `and/also/then/plus/;` (no comma),
  ≥2 content words; a clause counts as unclaimed only if **no claim span touches it** (spans are keyword-level; plain blanking over-declined
  26 real two-claim splits). Multi-entry decline (`multi_intent_residue_declined`) + single-entry parity. No literal moved. 9 pins; the
  WRITE-with-marker phrasing claims nothing at surface 1 either way (no todo/reminder literal is left to claim it) — pinned as such.
- **Review 1 (mine):** the helper only read clauses AFTER a marker, so a dropped half that comes FIRST was never seen and the gate on the
  branch still read "fallback claims STATUS only". Fixed: every clause the markers cut, the leading one included.
- **Review 2 (mine), from the full unit tier:** PM's #1856 turn 2 — "we're going in circles now and no that is not the name of the new
  project" — has an aside as its leading clause; the rule declined it, and the add-project handler would never see the correction (router
  ×6: NONE, the floor). **Narrowed:** an unclaimed clause counts only when **ask-shaped** — verb-first (list/show/tell/check/summarize/
  connect/delete/…), a wh-word, can/could/would you, or "please". Statements and asides stay with the claim beside them. **The trade, named:**
  a declarative second ask ("summarize my current work and I need the archived list too") stays with STATUS — the old drop. I would rather
  carry that trade than pull mid-flow corrections off their handlers; your call if you want the cue widened.

## The measurement for a change that does not touch the router
The scorer scores the router, and the router is byte-identical before and after, so a full run would re-measure the same 592 answers. What
changes is which turns reach it. Census claim diff, main vs branch, over 592 rows: **2 rows change claim**, both two-topic, both with router
evidence already on file — "what time is it? also connect my github" (REVIEW; router get_current_time @0.9) and the #1606 clear-reminders +
default-repo row (plan; router PLAN[clear_todos→get_capabilities] MATCH). Router ×6 on the phrasings the converted tests now decline:
"summarize my current work and delete my hydrate reminder" → PLAN[session_activity_query→delete_todo] 6/6; "connect my slack and check my
schedule" → PLAN[get_contextual_guidance→week_calendar] 6/6; "… and tell me a joke about cats" → REFUSED 6/6 (a plan with NONE/CLARIFY
can't validate → legacy → LLM classifier, one intent: the step-2 case, same user outcome as the deterministic drop it replaces). **I did not
spend the ~590-call full run; say so if you want it anyway and I will run it.**

## Gate today
`--list PORTFOLIO_PATTERNS`: NO-GO (rule 11) — "planned, fallback unacknowledged: … fallback unclaimed — the legacy LLM classifier returns
ONE intent … OK once #1977 step 2 lands". PPM: **121**, as before.

## Step 2
Reply assembly: carry the residue clause from the step-1 decline in `context["unclaimed_residue"]` and append CXO's one line when the served
category does not cover it; the "Want me to?" arms a pending offer. Bar: a served-reply check on CXO's example. It flips
`STEP2_ACKNOWLEDGEMENT_LANDED` and the pin, and PORTFOLIO's last literal then reads "planned" → 120. **Shall I start it today, or does
it wait for PM's admit via Exec?** Nothing else is unblocked on my side.

Verified how: lane's and my tiers as quoted (tests/unit full on the branch; 248 pins + ratchets on the merge, rc 0); census diff by the gate's
own `build_census` on both trees; router controls in `dev/2026/10/11/controls/`. Layer: surface 1 + gate on file + router shadow; no served
chat reply. Denominator: 592 rows diffed; 7 phrasings sampled ×6.
