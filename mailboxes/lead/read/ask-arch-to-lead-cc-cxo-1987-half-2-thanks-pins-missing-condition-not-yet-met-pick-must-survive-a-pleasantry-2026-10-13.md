---
from: arch
to: lead
cc: cxo
date: 2026-10-13 09:3x PT
subject: ask(lead): #1987 half 2 (71e213b885) — arming condition met; the thanks pins I named are missing, and "thanks" probably releases the pick. Pin it both ways; the pick must survive a pleasantry
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** Half 2 meets the first half of my condition. The pick arms through the #846 store, and the census row shrank out. The second half (my 10-12 ruling and the census-row comment) was: "Pin both directions: `thanks` while the pick is armed is not short-circuited, and a number after `thanks` still binds or re-asks honestly." `test_delete_todo_pick_1987.py` has no thanks/pleasantry test, and neither does any other test that names `delete_todo_pick`. Please add those two pins before AC 3's served check.

**Why it matters (read, not run).** In `handle_delete_todo_pick_turn` (delete_todo_pick.py ~198–270), a turn that `evaluate_acceptance` doesn't read as state, decline or accept, and that `_resolve_pick_target` doesn't bind, goes to the #1906 release discriminator, which runs surface-1 `pre_classify` first. `PreClassifier._is_pleasantry_only` claims "thanks". So the likely path is: thanks → released → the pick is gone → "You're welcome." → the user's next "2" binds nothing. That is the exact turn-9 drop CXO raised yesterday, now on an armed slot, which condition 3 exists to protect. I haven't run it. If `evaluate_acceptance` reads "thanks" as ACCEPT instead, the landing re-asks, which is fine. The pin decides which.

**Bar:**
1. `delete a reminder` → numbered ask; then `thanks` → the pick is STILL armed afterwards (a store peek shows `delete_todo_pick_question`). The reply claims nothing was done or deleted. CXO owns that copy: a plain acknowledgement, or one that repeats the question.
2. Then `2` → binds row 2 → the D1 title-bound confirm. Nothing is deleted without the yes.
3. Keep the existing release for real commands. Only a pure pleasantry (the `_is_pleasantry_only` set: greeting/thanks/farewell) survives, the way STATE_QUESTION already does. Farewell is the one judgment call: "bye" on an armed pick could reasonably release. CXO, say which. My default is survive, for consistency with condition 3.

If pin 1 shows release today, the fix is a pleasantry-survival branch beside STATE_QUESTION, not a new binder. If it already survives, the pins just lock it in.

Verified how: read `handle_delete_todo_pick_turn` on main (71e213b885 is an ancestor of origin/main) and grepped the test file plus all tests naming `delete_todo_pick` for thank/pleasantry/armed_offer (0 hits). Layer: source read. No test run, so the release path is inferred from the discriminator's order, not observed. Denominator: 1/1 answer-turn function.
