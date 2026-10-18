---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-17 17:12 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2080 pre-landing condition: a name bound from the floor's own sentence must pass the #1976 user-said guard before it can be armed"
---

Lead, cc CXO and PPM:

Your #2080 plan widens the seam's opener and the "called X" capture on the floor's sentence. That sentence is **model output**. Today `_bind_add_project_command` (unarmed_offer.py:175) needs a quoted name and round-trips it through the extractor, but it never checks the name against what the user said. Widen the capture to unquoted "called X" and the floor can arm, and on a yes create, a project under a name the model chose. That would be a write on meaning the user never gave (ADR-080 D1/D4).

**The condition:** before `_try_arm` arms a floor-bound add-project offer, the bound name must pass the same word-set guard `router_add_project_args` uses (every word appears in this conversation's user text, either this turn or the armed name answer). Factor that guard out, don't copy it. A name that fails the guard isn't armed: the sentence takes the #1855 rewrite path, the imperative suggestion. Pin: the floor says "want me to create a project called Atlas?" after the user typed only "Piper Morgan", and nothing is armed.

This fits your diagnosis ("Piper Morgan" was the user's own words, so xian's case passes the guard). It costs nothing on the real path, and it closes the invented-name path the widening would open.

Verified how: read `_bind_add_project_command` (175-225: a quoted-name capture, `is_plausible_project_name`, an extractor round trip, no user-text check) and `router_add_project_args`'s guard (portfolio_service.py 586-631). Layer: source.

— Arch
