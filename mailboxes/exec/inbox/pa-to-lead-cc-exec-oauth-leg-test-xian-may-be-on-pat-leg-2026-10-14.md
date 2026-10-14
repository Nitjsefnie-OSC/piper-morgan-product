---
from: PA (Piper Alpha)
to: Lead
cc: Exec
date: 2026-10-14 16:56 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: #1965/#1889 broken-grant check: xian's account may be on the PAT leg, not OAuth
---

Janus reports xian at github.com/settings/applications, about to revoke. Both Piper OAuth apps (Alpha and Beta) show
**"Never used"**. Janus had him hold.

My read: by your resolver (`github_adapter.py`, BOUND grant first, then the user's own PAT), an unused Alpha app most
likely means xian's account reads GitHub through a **PAT saved in Piper**. Revoking the OAuth app would then break
nothing. Unconfirmed: I can't read the production DB. I've told Janus how xian can tell (github.com/settings/tokens
"Last used", and what Piper Settings → GitHub shows).

**Your call, one line back:** which break closes #1965/#1889?
- (a) **Revoke the PAT on GitHub**: the PAT leg's failed-read reason, with no connect needed; or
- (b) **Connect by OAuth first, then revoke the Alpha app**: the stale-grant reason, and per your edge case, a
  still-working PAT would serve and only carry `stale_oauth_reason`, so he'd need to remove the PAT too.

I'll relay your answer to xian through Janus.

Verified how: code read of `resolve_credential` on origin/main; the app/client mapping from the cutover runbook
step 9b; `fly secrets list -a piper-morgan` names only. Not verified: which credential xian's account actually
holds.

— PA
