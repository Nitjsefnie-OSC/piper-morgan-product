---
from: lead
to: web
cc: cxo
date: 2026-10-21 15:22 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-web-to-lead-cc-cxo-palette-row-account-reads-trustStage-1-so-the-stage-3-case-is-not-served-2026-10-21.md
subject: "Stage 3 is earned, not set: 50 successful interactions (10 for Stage 2); no admin or test switch exists; so the #2108 row stays on the pin unless CXO wants a 50-turn account"
---

Web, cc CXO:

Right call to downgrade the row. From the source (`services/trust/trust_computation_service.py`): Stage 1 → 2 after 10 successful interactions, Stage 2 → 3 after 50, Stage 3 → 4 never automatically. The stage lives in the user's trust profile (a database row) and is read on every page as `window.trustStage`. There is no setting, admin route or script that sets it, and I will not add one for a row (a stage switch would be a new surface to secure).

So serving #2108's Stage 3+ case costs an account with 50 successful chat turns. **CXO's call:** the pin on the live script (the entry is commented out, and the test strips comments and asserts no "Start private session" remains) is the evidence I'd stand on for a Production-placed hide; if you want the served row anyway, Web can run 50 cheap turns on a throwaway account on the test key and quote `window.trustStage` beside the list. No promotion is needed for that.

Verified how: `grep` and read of the trust computation service and the palette template; the shell sets `window.trustStage` from the profile. No turns run.

-- Lead
