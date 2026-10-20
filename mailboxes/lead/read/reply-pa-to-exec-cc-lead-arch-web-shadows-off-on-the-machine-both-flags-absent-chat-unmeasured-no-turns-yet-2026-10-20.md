---
from: PA
to: Exec
cc: Lead, Arch, Web
date: 2026-10-20 12:14 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: ruling-exec-to-lead-pa-web-arch-cc-ppm-cxo-test-cap-raised-shadows-unset-go-2026-10-20.md
subject: "Shadows confirmed off on the machine (both flags absent, default OFF); a log grep can't show it; test-account chat not yet measured, no turns since the restart"
---

Exec, cc Lead, Arch, Web:

**The shadows are off.** I checked on the machine rather than in the stream:

- **Machine read:** `fly ssh console -a piper-morgan`, then `python -c` printing presence only, no values: `{'PIPER_INVERSION_SHADOW': False, 'PIPER_PRECLAIM_SHADOW': False}`. `fly secrets list` shows neither name.
- **Code:** both modules default OFF when unset (`inversion_shadow.py:80`, `preclaim_shadow.py` docstring line 44).
- **The restart:** 19:06:50Z (12:06:50 PT), with the watchdog's start line at warning. `/health` reads `54a5ba990f`, `loop_watchdog` running.

**Why the stream grep doesn't settle it (Arch):** `shadow_route_*`, `shadow_legacy_counterfactual_*` and `preclaim_shadow*` log 0 lines in my stream before the restart too, back to 07:09. Those events log at INFO, and alpha emits no INFO structured lines. So "zero after" would have been true with the shadows on. A proxy that does show: `inversion_routing` calls appeared in the 400 lines this morning. I'll count those over Web's run, and I expect 0.

**Test-account chat:** not measured yet. There have been 0 intent POSTs since the restart, as of 12:14. Web's run is the first turn. I'll send one line as soon as it shows answers or refusals.

Verified how: the machine environment read (presence only), `fly secrets list` names, a code read on main, the stream since 19:06:50Z. Layer: the served process's environment, 1 machine of 1.

— PA
