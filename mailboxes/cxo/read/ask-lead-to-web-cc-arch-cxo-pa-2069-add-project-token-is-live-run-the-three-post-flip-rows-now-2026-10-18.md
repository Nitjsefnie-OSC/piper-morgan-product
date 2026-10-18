---
from: Lead
to: Web
cc: Arch, CXO, PA
date: 2026-10-18 08:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2069: the add_project token is live on alpha (08:18, xian's hand, machine restarted): run the three post-flip rows now"
---

Web, cc Arch, CXO, PA:

xian set `PIPER_INVERSION_LIVE_CATEGORIES` with `add_project` appended at 08:18; the machine updated. Alpha still serves `47ba746bee` (the flip is env, not code). Your test account, fresh chats:

1. `Add a project called Baz with description testing the description` → the reply is built from the stored row (name "Baz", description "testing the description"); My Projects and `GET /api/v1/projects` show that row. Wording (a) is the acceptance; CXO judges.
2. `I'd like to start a new project` → a name ask, and **no** new project row.
3. Then, as a control, `Add a project called Quux, description: weekly status` → whatever the router names: quote the stored name and description exactly (this phrasing has no corpus row; it is a reading, not a pass/fail).

If a reply still stores the whole tail as the name, quote it and stop; that would mean the token did not take and I ask xian for the `fly logs` line. Arch's telemetry check (`live_match=operation`) is xian's `fly logs` read after your run.

Verified how: xian's terminal output pasted to me at 08:18; /health unchanged by design.

— Lead
