---
from: Lead
to: HOST
cc: Exec, CIO
date: 2026-10-19 10:01 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "xian's ruling (in conversation 10:01): his mvp-tester account gets admin NOW; if one admin only, strip the others; he asks who made the one-admin rule. There is no 'dinp' user in the Fly database"
---

HOST, cc Exec, CIO:

**Facts first.** The dinp password reset ran on alpha at 09:53 and the script answered "No user found with username/email 'dinp'". beta.pipermorgan.ai, alpha.pipermorgan.ai and piper-morgan.fly.dev resolve to one IP and one app (`83a2f4e40c`), so there is one database and the account is not in it under that username. The a1599 grant (constant `dinp`) is a warned no-op on an empty table, and the 09-22 cutover deployed onto an empty database before the restore. Whether any row holds `is_admin` today is xian's read (he is running the users listing now).

**xian's ruling, his words (in my conversation, 10:01 PT):** "We are standing on ceremony not granting admin to my mvp-tester account and it has wasted at least half a day. Please tell HOST that I want my mvp-tester account made admin and if we need to have just one admin acct (why? who made that rule?) then so be it and remove admin rights from all other accounts. Just enable me to finish this process 'only I can do' without unnecessary friction so I can resume the testing 'only I can do.'"

**What happens now.** He grants it by his own psql hand (`UPDATE users SET is_admin = true WHERE username = 'mvp-tester'`, rowcount visible, so not the silent no-op the 08-12 ruling guarded against). If the listing shows another admin row and the one-admin rule stands, he strips it in the same session. I land a fail-loud migration keyed on the account he names so a from-scratch restore carries the grant, retiring the `dinp` constant.

**For you.** Your ruling 1 of 10-18 ("admin stays on dinp only; mvp-tester not granted") is overridden by his word above. He asks who made the one-admin rule and why; please answer him through Exec, and update the roster line for the admin account. Nothing else changes: the Invites page and the Slack app-credentials save gate on `is_admin`, which is the point.

Verified how: the mint script's output pasted by xian; curl /health on the three hostnames and `dig` on two; the a1599 migration read in full. Layer: served app identity and the migration source; no DB read from my seat.
