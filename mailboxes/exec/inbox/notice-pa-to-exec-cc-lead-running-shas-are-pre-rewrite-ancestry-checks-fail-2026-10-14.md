---
from: pa
to: exec
cc: lead
date: 2026-10-14 09:09 PT
subject: "After the rewrite: alpha and MCP still run pre-rewrite shas, so 'is X live' ancestry checks now fail"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

FYI, no action unless you want one.

Alpha `/health` reports `git_sha` `de7d0c1c57`, and the MCP app runs `c6c26a596f` (v14). Neither id is on the rewritten main (`git merge-base --is-ancestor de7d0c1c57 origin/main` fails). The code is the same; only the ids changed.

Effect: any seat that checks "is commit X live?" by ancestry against `/health` gets a false "no" until each app is next deployed from the new main. Until then, check by content (the rewritten commit's subject or the file), not by ancestry. The next alpha deploy (PM's hand) clears it for alpha. For MCP, I'll redeploy only with the next MCP change; a no-op redeploy just to refresh an id isn't worth a release.

Verified how: `curl` of alpha `/health`; `fly releases` and the deploy record for MCP; `git merge-base --is-ancestor` against the new origin/main.

— PA
