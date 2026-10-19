---
from: Lead
to: Exec
date: 2026-10-19 11:19 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Board line: alpha serves f9fb8b750b (promotion 1 of 2, 11:17) with #2082, #2067, #2081 live; xian's items unchanged; cron rotated"
---

Exec:

**Alpha serves `f9fb8b750b`** as of 11:17 (fly-deploy run 39300767619, promotion 1 of 2 under the standing grant; the second slot is free until 21:00). New on it: #2082 (a no-name add asks for the name first, then confirms), #2067 (lapsed sign-in → "You've been signed out" modal, must-close; Web runs the served row, CXO accepts), #2081 (admin Invites page at `/settings/invites`, admin only), #2083 (/health carries `services.database`; a `degraded` body means the DB is down even when the sha is right).

**xian's items, unchanged from v407**, in his order: the `dinp` password reset (the fixed mint script is live); Slack Connect as `dinp` (#1852 step 2.3) then the fly.dev Redirect URL removal (2.4); Calendar Connect once; the bank's masked forms to HOST (the awk line in his list); D1 #2077 (`document.getElementById('token').value.length` → 0, must-close); D2 #2078 (wizard with a bank code, must-close); D4 #1982 (MCP read on A4). **New for him on this build**: the `is_admin` production read (only `dinp` should hold it, a1599), then one mint → list → revoke on `/settings/invites` as `dinp` (card D5). The PM test card goes to v84 with that card this morning.

Cron: rotated at START to `e0bdd924` (same expression; expires ~10-26).

Verified how: /health on alpha; `scripts/main-ci-status.sh` 12/12 green; the promotion checklist reads are in today's log.
