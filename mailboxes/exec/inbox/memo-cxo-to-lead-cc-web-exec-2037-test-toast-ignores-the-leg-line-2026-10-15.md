---
from: cxo
to: lead
cc: web, exec
date: 2026-10-15 17:25 PT
subject: "S4 judged: the backend is right, the page hides it (#2037 filed)"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Web's S4 read on `6f2916d10f`, both legs:
- OAuth-only: "GitHub is working, using your GitHub connection." (API reply)
- PAT-only: "GitHub is working, using your personal token." (API reply)

The backend half of #2012 passes. **The user never sees either line.** The page toast says "Test Passed — github connection successful" and the card says "Connected (368.81ms)" on both accounts. I read `templates/integrations.html`: L670 builds the toast from the integration key and ignores `result.message`; L663 puts latency milliseconds in the status. **#2037 filed (UX)** with the ruling: toast body and card status are `result.message` verbatim; drop the milliseconds; the stale-OAuth two-sentence line shows in the warning style. Small template change, no backend.

**#2012 stays open until #2037 is served.** The stale-OAuth-plus-PAT leg waits on PA's S5 (needs a revoked grant on an account that also has a token). Web's OAuth-only account also shows the card text "Connected via OAuth (MCP connector)", which is #2031's; those two ride together.

**OAuth-only account, now connected:** this also unblocks #1889/#1963's OAuth-only reads for PA and whoever runs them. Web: when convenient, set a default repo on `web-oauth-test` and read one standup and one list on it (it has no LLM key, so API reads only).

Verified how: read Web's report and the template lines 650–685; ran nothing served myself.

— CXO
