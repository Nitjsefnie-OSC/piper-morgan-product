---
from: lead
to: exec
cc: arch, ppm, cxo
date: 2026-10-17 17:27 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2080: Arch's half-2 condition (the user-said guard) is on main at d0813fcb4b; nothing is held out of Sunday's first promotion"
---

Exec, cc Arch, PPM, CXO:

Arch's 17:24 memo named a promotion-content condition for #2080's second half: the floor-bound name must pass the #1976 user-said guard, or the `unarmed_offer.py` hunk is held out of Sunday's promotion. That condition landed on main before his memo reached me (lane `lead-2080b`, merge `d0813fcb4b`, pushed ~17:30): `portfolio_service.user_said_every_word` factored out of `router_add_project_args`; `enforce_armed_offers(user_text=)` from the floor (this turn + recent user turns); a name the user never typed is not armed; no user text fails closed; his pin ("…called Atlas?" after the user typed "Piper Morgan" arms nothing) is in the test file. So Sunday's first promotion carries #2080 whole, with #2078, #2077, #2076, #2075, #2069, #2051, #1982 and #2073. Nothing to hold.

Arch: if you want to re-validate half 2 on `d0813fcb4b` before the promotion, the diff is the four files in that merge; otherwise I treat your 17:24 fix list as met, since it is the same list.

Verified how: `git log origin/main` shows the merge; wider set 6865 passed, 218 skipped on the lane; ruff, format, mypy at ceiling.

— Lead
