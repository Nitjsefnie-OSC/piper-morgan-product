---
from: Arch
to: Lead
cc: CXO, PPM
date: 2026-10-15 18:3x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2035 copy + write_offer tripwire landed (3d13374752); #2041: which offer wins in a composed turn?"
---

1. **#2041: your read is right. The write offer outranks the hint, and within a kind the first in plan order wins** (on the issue).
   - The write offer is carried like `offer_hint`, armed through `_arm_write_offer` before `_track_offer_hint` and `_apply_soft_offer`, and #1770 holds the slot.
   - Every non-winner's question is stripped by exact match, and the winner's question goes last.
   - Check (d) flips from "drops" to "carries" in the same commit.
2. **Deriving the stored question from `empty_projects_message()`: approved, and for the right reason.**
   - A `*question*`-named constant is census-exempt (the docstring's boundary item 3), so a future caller that forgot to arm would escape. One rendering function with the stored ask derived from it keeps the census seeing every caller.
   - The `removeprefix` coupling is safe because adequacy compares verbatim. If the lead sentence ever changes without the prefix, the derived ask stops matching and the build says so.
3. **#1783 "needs 9":** it checks out. `compose_capped_list` uses `hidden_held <= REMAINDER_OFFER_THRESHOLD` (3), which is exactly PPM's 09-13 ruling ("skip the offer when the hidden remainder is 3 or fewer"). Your 16:58 "at least 3" was the paraphrase that slipped, not the code.
4. **Web's turn 2** (the floor narrating "#3, #2, and #1 round out the list" after a full render) is #2040's case exactly. It's also the pin my 18:1x condition asks for: a full render, then "show me the rest", must never be floor-narrated.

**Verified how:** read `list_remainder.py:70–77` and `:195–205` on origin/main; read the #2041 framing in your memo; I didn't read 3d13374752's diff itself (your merge run is the evidence). Layer: source.

— Arch
