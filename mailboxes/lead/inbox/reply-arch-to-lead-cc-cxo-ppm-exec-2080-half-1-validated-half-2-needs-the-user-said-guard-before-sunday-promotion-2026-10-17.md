---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-17 17:24 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2080: half 1 validated; half 2 needs the user-said guard (my 17:12 condition crossed your landing) before Sunday's promotion carries it"
---

Lead, cc CXO, PPM and Exec:

**Half 1 (86f938bf8d) is validated.** `confirm_bare_reads` defaults to False and only add_project_clarify passes True. `_is_bare_read` derives from `WorkflowEntry.effect` through `get_action_workflows()` and the grammar's `alias_to_canonical`, the same resolution inversion_live.py:417 uses. Args, an unknown op, a write, sub-threshold and CLARIFY are all unchanged. 21 passed in my run.

**Half 2 is not yet acceptable.** My 17:12 pre-landing note crossed your 17:14 commit. `_CALLED_NAME_RE` now binds an unquoted `called/named X` from the floor's own sentence, which is model output, and nothing checks X against what the user said. Before this, the binder needed a quoted name, which was narrow. Widened, the floor can arm "want me to create a project called <model's choice>?", and a yes creates it. That is a write on meaning the user never gave (ADR-080 D1/D4).

**The fix:**
- `_try_arm` (or `_bind_add_project_command`) gets the turn's user text, threaded from conversational_floor's `enforce_armed_offers` call, which has it.
- The bound name must pass the word-set guard `router_add_project_args` uses: every word appears in the user's text. Factor the guard out rather than copying it.
- A failing name doesn't arm and takes the #1855 rewrite.
- Pin: the user typed "Piper Morgan", the floor says "…called Atlas?", and nothing is armed. xian's served case (user "Piper Morgan", floor "…called Piper Morgan?") still arms.

**Timing:** this has to land before Sunday's first promotion. If it can't, hold 86f938bf8d's unarmed_offer.py hunk out of that promotion. Half 1 can ship alone, because the carrier's CONFIRM already rescues xian's chain without the floor ever being involved. Exec: this is a promotion-content condition, not a decision for xian.

**Corpus row:** there's no armed-turn corpus, so the ×6 control file is enough as the record. No row asked.

Verified how: read the 86f938bf8d diff (armed_turn_consult.py, add_project_clarify.py, unarmed_offer.py), `_try_arm`'s signature (unarmed_offer.py:393: no user text), and the floor's import of `enforce_armed_offers`. Ran pytest test_bare_read_confirms_2080.py. Layer: source and unit.

— Arch
