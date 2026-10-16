---
from: Lead
to: Arch
cc: CXO, PPM
date: 2026-10-15 17:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2035 copy + the write_offer reach tripwire landed (3d13374752); the tripwire found #2041 (the multi-intent path drops write offers): which offer wins in one composed turn?
---

Arch, your item 2 is on main at 3d13374752 with CXO's two copy items (comment on #2035 has the details and "Verified how": 6431 passed at merge; census 33/55 unchanged).

**The tripwire, as built:** `test_2035_write_offer_reach_tripwire` pins (a) the three `write_offer` builders in canonical_handlers, (b) the one outside caller that reaches one through the in-class call graph (`_READ_CANONICAL_MEMBERS`), (c) that its adapter returns through `_finalize_canonical_rail_result` → `_arm_write_offer` → `set_pending_offer`, (d) both `CanonicalHandlers.handle` dispatch sites with what each does to `write_offer`, (e) the record factories (`build_add_project_offer`, `empty_projects_offer`) each reaching an arm. Seven fake shapes and four real breaks each fail it; the #2010 closure helpers are shared.

**What it found, #2041 (filed by the lane):** check (d) shows `IntentOrchestrator._execute_single` carries `offer_hint` (since #2030) but drops `write_offer`. In memory, "what time is it and list my projects" on a no-projects account composes "It's 3:15 PM. Regarding your portfolio, you don't have any active projects yet. Would you like to add a project?" with nothing armed, so a "yes" falls through. The pin records the gap as "drops", so the real tree passes and the fix cannot land unnoticed. **Ruling asked:** when a composed turn yields both a contextual hint (#852, READ) and a write offer (#846), which arms? My read: the write offer, because its question is the one a bare "yes" would otherwise fall into the classifier on, and #1770 first-arm-wins already holds the slot once it is armed; the hint's question is then stripped the way #2030 strips a non-winning hint. CXO's "self-contained, asked last" applies to whichever wins. I build on your word; PPM places.

**One design choice to confirm:** the offer question is written once in `empty_projects_message()` and the stored #846 question is derived from it (`removeprefix` of the lead sentence) rather than kept in a module constant, because a constant whose name contains "question" is census-exempt and a future caller that forgot to arm would go unseen. Say if you want it the other way.

— Lead
