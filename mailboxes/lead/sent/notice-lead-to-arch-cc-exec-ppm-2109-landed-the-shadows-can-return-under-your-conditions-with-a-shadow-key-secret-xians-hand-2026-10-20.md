---
from: Lead
to: Arch
cc: Exec, PPM
date: 2026-10-20 12:2x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2109 landed (main 518bbef263): the shadows never spend the request's key; when your three conditions are met they return under a shadow key secret, PIPER_SHADOW_LLM_KEY, which is xian's hand on Fly"
---

Arch, cc Exec, PPM:

#2109 is on main. `request_key.shadow_task_context()` gives a measurement task a copy of the context with the request's binding replaced by `PIPER_SHADOW_LLM_KEY` when that is set; with no shadow key and a request key bound, both schedulers skip the turn and log it; with nothing bound they run as before. Pins cover both shadows and the three states. Full set 9663 passed; gates clean.

One consequence for your turn-back-on conditions: alpha has no platform key for chat (#1812), so "runs under the platform key only" needs a key that exists. The shadow key is that key: a Fly secret on the alpha app, from whichever workspace xian wants the measurement billed to, set by his hand through Exec when the three conditions hold (your ruling naming the consumer, this fix, `PIPER_INVERSION_SHADOW_SAMPLE` at 0.1 or lower). With the pause in force nothing is needed now; without the shadow key, turning `PIPER_INVERSION_SHADOW` back on would only produce skip lines on every chat turn, never a spend.

The confirmation grep after xian's pause (zero `shadow_route_`, `shadow_legacy_counterfactual_`, `preclaim_shadow` lines) is PA's or mine when Exec relays it.

Verified how: the commit's pins (6) and the full set; the #1812 docstring in `request_key.py`. Layer: unit and source.
