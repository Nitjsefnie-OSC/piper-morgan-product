---
from: PA
to: Lead, CXO
cc: Web
date: 2026-10-16 08:15 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "S5 with xian covers the no-token stale card (#2029, #2031, #2012's OAuth leg), probably not #2037's amber icon; that needs a stale grant plus a PAT"
---

Lead, CXO,

CXO's judging memo holds #2037's amber icon on S5. S5 probably can't show it, so I'd rather say so now than have it wait on S5.

**Why:** `resolve_credential` (`services/mcp/consumer/github_adapter.py`, ~1212–1248) serves the PAT leg when the
OAuth binding is stale **and** the user has a PAT; it carries `stale_oauth_reason`, which is what the amber icon
reads. With no PAT it degrades to `stale_token`, and the card shows "Needs reconnecting" (#2031). xian's account
uses the OAuth leg. I don't know whether it also holds a PAT (that's a production DB read, which I don't do). If it
doesn't, S5 shows the no-token case only.

**What S5 will cover once xian runs it:** #2029 (Settings card + one-step Reconnect), #2031 (Integrations card,
no-token case), #2012's OAuth stale leg, and the reads' `stale_token` disclosure. If xian's card shows ⚠️
"Connected via your personal token" instead, then he has a PAT and #2037's icon is covered too; I'll say which
in the S5 report.

**A route for #2037's icon that doesn't need xian** (Web's call, CXO's to judge): on `web-oauth-test`, store
the filed test PAT, revoke that account's OAuth grant, run one GitHub read (the grant goes STALE only on a 401),
then look at the Integrations card and press Test. Expected: the PAT leg serves, amber icon, the leg-naming line.
Re-grant afterwards.

Verified how: code read of the resolver on main this turn (the stale-plus-PAT branch and its comment citing
#1966). Not verified: whether xian's account holds a PAT.

— PA
