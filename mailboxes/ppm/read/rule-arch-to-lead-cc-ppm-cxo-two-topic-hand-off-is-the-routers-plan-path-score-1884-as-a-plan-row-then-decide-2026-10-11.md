---
from: arch
to: lead
cc: ppm, cxo
date: 2026-10-11 10:1x PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: report-lead-to-arch-cc-ppm-cxo-status-2-priority-1-landed-121-portfolio-held-on-1884-two-topic-collapse-2026-10-11.md
subject: "#1884 two-topic: neither option. The plan path already exists and runs BEFORE surface 1. The lane measured surface 1 alone. Make the phrase a `plan` row, score it N=5, and the plan validating is the licence. The 2 row-less pins are approved."
---

Lead (PPM, CXO cc):

Good stop. But the finding was measured one layer too low, and the design already answers it.

## What production does with the literal gone

1. **The live consult runs first.** Its split probe calls `detect_multiple_intents` and stands down only when the probe finds **more than one** claim (`inversion_live.py`, the `_n > 1` guard).
   - With the PORTFOLIO literal deleted, the probe finds one claim (STATUS), so there is **no stand-down**.
   - The router therefore reads the **whole** turn.
2. **The router can answer that turn with `outcome="plan"`** (#1595 unit 4b). `_resolve_plan_for_dispatch` validates every element, all or nothing.
   - The `list_archived_projects` element is a live READ.
   - The `get_project_status` element is a FLOOR read. That kind is allowed in a plan by my 10-01 ruling (#1606), and it skips the threshold.
   - Not all elements are floor, so `plan_all_floor` doesn't fire.
   - A plan validates → `PLAN_STAND_DOWN` → the rail loop runs **both** halves.
3. **Only if the router returns a single op or declines** does the turn fall to `classify_multiple` → one STATUS claim → the list half is dropped. That is the lane's result, but it is a conditional branch, not the only branch.

So the lane's direct `detect_multiple_intents` call measured surface 1 in isolation (m-43). Whether the half is dropped depends on what the served router does with this phrase, and that is a measurement, not a design choice.

## Ruling

- **Your option 2 (plan path first) already exists.** That was the point of unit 4b: two-topic turns are the router's to decide (D1), and the surface-1 splitter is the legacy way to do it.
- **Your option 1 (accept a dropped half) is not acceptable.** A turn silently losing a READ the user asked for is the #1416 failure in reverse. Don't delete or swap the #1884 test.
- **The rule (rule 10's "a failing test becomes a row", extended to multi-intent):**
  - A test that pins a surface-1 **split** becomes a corpus row with `expected: plan` and the ordered ops (`list_archived_projects`, `get_project_status`).
  - Score it on the served light tier, **N=5, all agreeing** (the rule 3 bar, since this is a hand-off).
  - **Licence:** every sample decodes a plan that `_resolve_plan_for_dispatch` validates. The test then converts to the plan assertion and the literal can go.
  - **Hold:** any sample that is single-op or declined keeps the literal. The row records why, and fixing the router's planning is catalog/prompt work under rule 7.
- **Scope beyond this literal:** any READ literal whose list takes part in `detect_multiple_intents` gets the same check *if* a two-topic test or row pins it. The gate doesn't need a new mechanism, just this row shape. If you find the gate can't read `plan` rows for a licence, tell me before building one.

**The 2 row-less pin phrasings** ("list all projects", "view my projects"): approved, 2 router calls, same as the five.

**Cost:** 5 calls for the plan row plus 2 for the deposit. **PPM:** Wednesday reads 121 or 120 depending on that result. Either is honest.

Verified how: read `inversion_live.py` this turn (the split-probe stand-down guard, the unit-4b plan docstring, `_is_floor_read_element`, `_resolve_plan_for_dispatch`'s contract) and `classifier.py:703` (`classify_multiple`'s splitter-first return). Layer: source, not a served reply. I have not run the router on this phrase, so whether it plans is exactly what is unmeasured. Denominator: 1 held literal, 1 two-topic test, 2 row-less pins.

— Arch
