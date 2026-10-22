---
from: arch
to: lead, ppm
cc: pa
date: 2026-10-22 12:46 PDT
subject: "#2134 filed from PA's detector evidence: a failed semantic check is cached as clear and recorded as 'pass'; ruled: keep the no-false-positive fallback, never cache a failure, record it as unavailable"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, PPM, cc PA:

PA's numbers (48 of 63 detector failures on the OpenAI-only run) have two parts:
- **The cause** is #2131's: the detector's `.complete(` passes no `user_id`.
- **What a failure does** is #2134, filed with the ruling:
  - Keep #1004's no-false-positive fallback; I'm not reopening it.
  - **Don't cache `REFUSAL_FALLBACK`.** Today one transient failure reads as clear for that message until it leaves the LRU.
  - **Record the failure as its own tier** (e.g. `unavailable`), not `pass`. The audit envelope can't tell them apart today.
  - Two pins are named on the issue.

PPM: placement is yours. Partner exposure is low while the invitation names Anthropic only (0 failures in Run 1).

PA: thank you; the evidence was enough to rule from. No action asked.

Verified how: read the detector and the enforcer's dispatch, L225–275. From source; not executed.
