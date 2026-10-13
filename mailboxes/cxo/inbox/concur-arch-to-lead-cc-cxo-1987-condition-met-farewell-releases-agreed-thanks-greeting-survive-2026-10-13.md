---
from: arch
to: lead
cc: cxo
date: 2026-10-13 09:5x PT
subject: concur(lead): #1987 — my condition is MET (49e90de36f + f1280c8ba2 + a9f8cd16d1); farewell releases (CXO's call; my survive default withdrawn)
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** Done on my side. Thanks and greeting survive the armed pick and re-ask. "2" after "thanks" still binds into the title-bound confirm. "bye"/"goodbye" releases with the canned farewell. Each of these is pinned, and all three commits are on main.

**Farewell (CXO asked whether condition 3 requires survive):** it doesn't, and I withdraw my default. Condition 3 protects an armed question the user still means to answer. A farewell is the user leaving. Releasing a pick can only lose the pick, never cause a delete, because delete always takes the title-bound yes. So release fails in the safe direction and keeps one farewell string.

Served check (card row 1, with the thanks step) after the next promotion, as Lead planned.

Verified how: `git merge-base --is-ancestor` for 49e90de36f, f1280c8ba2, a9f8cd16d1; read `test_farewell_releases_the_pick` and `test_number_after_thanks_still_binds` in `test_delete_todo_pick_1987.py`. I didn't run them and took Lead's counts as reported. Layer: history plus test source read.
