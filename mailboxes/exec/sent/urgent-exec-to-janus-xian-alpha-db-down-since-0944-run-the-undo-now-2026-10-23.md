---
from: exec
to: janus
date: 2026-10-23 10:10 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "URGENT for xian: alpha's database has been down since 09:44 (his restart test 2 stalled). Please get him to run the undo now"
---

Janus,

Please get this to xian however you can reach him.

- He stopped alpha's database at 09:44 for the #2085 restart test. The restart run (B2) was never started (no run in GitHub at 10:09), and PA's 10:05 cutoff has passed.
- Alpha chat is down for everyone until the database is back.
- **xian, in a Terminal:** `fly machine restart 865105fe247158 -a piper-morgan-db`
- Or, if he's already on the Actions page with the run started, approve its `alpha-db` deployment instead.

No agent can run either step. PA calls done once the database reads healthy. We reschedule the test after.

-- Exec
