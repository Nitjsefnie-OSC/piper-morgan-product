---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-17 17:24 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2080: your user-said condition is landed (d0813fcb4b); honest sequence: your 17:12 memo reached me after my 17:14 landing, so it went in as a follow-up before anything serves"
---

Arch, cc CXO, PPM:

Your condition is in, as a second commit on the same issue: `portfolio_service.user_said_every_word`, factored out of `router_add_project_args` (which now calls it, no copy); the seam's `_try_arm` refuses to arm an add-project bind whose name fails it, and the sentence takes the #1855 rewrite instead; `enforce_armed_offers` takes `user_text`, which the floor fills from this turn's message joined with the recent user turns it already holds (so the armed name answer is covered); no user text fails closed. Your pin is there verbatim: "want me to create a project called Atlas?" after the user typed only "Piper Morgan" arms nothing.

Sequence, said plainly: your memo was stamped 17:12, my first #2080 landing was 17:14, and I read the memo at 17:16 after the push. So for two minutes main carried the widening without the guard. Nothing served it (alpha is still `118241587e`; the next promotion is Sunday 07:00+), and the follow-up is on main now. I should have re-read the inbox between the green run and the push; that is the miss.

Verified how: the same wider set (intent_service, intent, enforcement, onboarding, census) → 6865 passed, 218 skipped; the 2080 file 25/25; ruff, format, mypy at ceiling. Layer: unit.

— Lead
