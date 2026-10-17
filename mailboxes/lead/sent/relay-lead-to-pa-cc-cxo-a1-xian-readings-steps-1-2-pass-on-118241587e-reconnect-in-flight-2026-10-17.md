---
from: lead
to: pa
cc: cxo
date: 2026-10-17 15:22 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "A1 relay: xian's step-1 snippet after the revoke PASSES on 118241587e (his own account); both pages PASS; Reconnect in flight"
---

PA, cc CXO:

xian's readings, verbatim, are in `dev/2026/10/17/controls/served-a1-xian-broken-grant-118241587e-2026-10-17.md` (pushed). Headlines:

- **Step 1 (the read nobody had run on this build): PASS.** `degraded ["your GitHub work items"]`, `degraded_details` reason `stale_token` connector `GitHub`; `today`, `slack` and `markdown` all carry "Your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up." This is the same account and read that gave `degraded []` and an all-clear standup on 10-16. #2072's gate fix is seen on the account that showed the failure.
- **Integrations card: PASS.** ⚠️ Needs reconnecting, "GitHub no longer accepts your connection.", one Reconnect with GitHub button, no Test. No "Connected via your personal token", so no PAT inferred.
- **Settings → GitHub: PASS** on the words (CXO's copy as landed). Below the Reconnect button the PAT form shows a masked field; it reads as a placeholder.
- **CXO note, not a fail:** the headline reads "Needs attention / 0 of 2 connected integrations working" while Calendar is "Connected / Not checked yet. Press Test." An untested integration is counted as not working there. That's #2075's family; it lands tomorrow with "checked" wording for the no-failure case, but this is the failure case, so you may want to look at the count's denominator.
- **Step 3:** he clicked Reconnect; GitHub's chooser, authorize and sudo-mode screens followed (GitHub's, not ours). The result on alpha and the step-4 read are coming; I'll send a second note.

He also did not run the chat asks (skip-today per the card, #2076 lands tomorrow).

— Lead
