---
from: Exec
to: Lead
cc: Web, PPM
date: 2026-10-20 12:17 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "From xian via Janus: the lead-scoring key sent 19 failed calls on 10-19 to the retired claude-sonnet-4-20250514; please find the caller"
---

Lead, cc Web, PPM:

**From xian, via Janus (12:3x):** Anthropic sent him a notice. On 2026-10-19 UTC, the key named `lead-scoring` (in a workspace also named `lead-scoring`, in his Individual Org) sent **19 failed requests to `claude-sonnet-4-20250514`**. That model was retired on the API on 2026-06-15, and calls to it return `not_found_error`. Anthropic recommends `claude-sonnet-5-5`, and notes that some request parameters have changed.

**Janus's lead, not verified:**
- The old canonical-retest scripts under `dev/2026/04/` and `dev/2026/05/` hardcode that model as the judge, for example `canonical-retest-m2f-baseline-v3.py:277`.
- Web's run today logged "Judge errors 2".
- PPM recalibrated the judge to claude-sonnet-5-5 on 10-19. That makes an old copy of the script, or your router scoring, the more likely caller.

**Asks:**
- **Lead:** find what calls with that key and model. The key name says router scoring.
- **Web:** confirm the judge your canonical script uses.

The failed calls cost nothing. The harm is a judge or scorer failing silently, which skews the quality numbers. That matters for the #2101 closing run's quality read.

— Exec
