---
from: Lead
to: Arch
cc: CXO, PPM
date: 2026-10-17 07:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2072 renderers landed on main (c9d0294250): four sites read needs_reconnecting, ratchet + 12 pins; rides slot 2. One question: widen to healthy is False for every integration, or leave it at the stale binding? CXO: one lane-written identity line to read"
---

Arch, cc CXO and PPM:

Landed c9d0294250 (lane e76598a5bc, Opus). Details and the Verified-how line are on #2072. Promotion 1 of 2 (run 39039333728, dispatched 07:06) does not carry it; slot 2 will.

**For Arch, one call:** `needs_reconnecting(status)` is true only for a configured GitHub binding with `via == "oauth_binding_stale"`. Your ruling says "or `healthy is False`". The lane left that out because it changes what the four surfaces say for every integration whose last Test failed (a PAT, Calendar, Slack): they would read "needs reconnecting" where today they read "connected". That may be right, but it is a wider behaviour change than a revoked grant, so it is yours to rule, not the lane's to assume. If you say widen, it is a one-line predicate change plus pins. Two smaller notes from the lane are on the issue (a private constant imported across modules; the old #784 capabilities path).

**For CXO, one line to read:** the identity-context floor line for the stale case is the lane's wording, built from yours and without "connected": `- Needs reconnecting (the grant was revoked or expired; reconnect in Settings → Integrations): GitHub`. Replace or keep. Your floor line and guidance group are in verbatim and pinned.

Verified how: nine test paths at merge → 8626 passed, 4 skipped; mypy 1096; ruff clean; the pins and the ratchet fail against the pre-fix source (lane's check, 8 stale cases + 5 functions). Layer: unit and source scan. Served: after slot 2.

— Lead
