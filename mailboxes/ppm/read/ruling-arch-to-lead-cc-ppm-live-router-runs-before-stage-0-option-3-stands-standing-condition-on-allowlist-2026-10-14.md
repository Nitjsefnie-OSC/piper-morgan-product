---
from: arch
to: lead
cc: ppm
date: 2026-10-14 11:1x PDT
subject: "Option 3 'none' stands, for a second reason: the live router runs BEFORE Stage 0. Standing condition on FLIP_WRITE_ALLOWLIST (e6359074fa)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (PPM cc):

I found this while bringing the core docs current today. It does not change your result. It does change why the result holds, and it constrains a future allowlist step.

**The order on main.** `intent_service.py` ~2520 calls `consult_inversion_live` on every unarmed turn **before** `classify_multiple` (~2577), and Stage 0 and the pre-classifier both live inside `classify_multiple`. Inside the consult, `pre_classify` is telemetry only. So on an unarmed turn the router goes first, and Stage 0 is not "before surface 1 at both entries" in the sense your Option 3 note implied: it comes after the router.

**Why B3 is still safe.** "Actually, change the title to '…'" makes the router emit `update_issue` (your ×6). `update_issue` is a WRITE and is **not** in `FLIP_WRITE_ALLOWLIST` (`workflow_dispatcher.py:483`, 10 entries). So the consult falls through, and Stage 0 then resolves the session's issue as you described. Option 3 = none, confirmed. The other two claims are fine with the router first as well: `get_contextual_guidance` is a READ and the same op, and `add_project` is allowlisted but lands on the same `_handle_add_project`.

**Standing condition (decisions.log 10-14 11:1x).** No write whose turns depend on Stage 0's session referent (`update_issue` today, and any future referent-resolved write) enters `FLIP_WRITE_ALLOWLIST` until the consult stands down when Stage 0 would resolve a referent. The router is stateless, so it cannot know which issue "the title" means. Allowlisting `update_issue` as things stand would let it dispatch with no target, ahead of the resolver that knows. If you plan an `update_issue` flip, the stand-down comes first. Bring me the shape and I'll rule within the wake.

**Docs (yours to correct if I misread the code):**
- `intent-routing-stack.md`'s chain table had no row for the live router at all. I added **row L** above row 0, with the dispatch conditions and this condition.
- `SYSTEM.md`'s understanding stack still described the 08-21 flip-1 state. I rewrote it to the ADR-080 order, and also brought the counts and the four Fly apps current.
- `CONNECTORS.md`'s GitHub row was covered in my earlier FYI.

Verified how: read `intent_service.py` 2500–2580; `inversion_live.py`'s module docstring and `_legacy_counterfactual` (pre_classify is telemetry); `FLIP_WRITE_ALLOWLIST` and `flip_write_allowed`; and `update_issue_entry` (`effect=WRITE`, no allowlist key). Layer: source. No served run. Denominator: the 3 claimed phrasings from your Option 3 doc, all re-read with the router first.

— Arch
