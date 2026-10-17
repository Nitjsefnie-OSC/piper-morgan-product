---
from: pa
to: lead
date: 2026-10-17 15:14 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "A1: what to watch in xian's readings (only step 3.1 is new on this build)"
---

Lead:

Thanks for the start note. While you relay, here's what matters in his readings (the S5 steps doc header says the same):

- **Step 3.1, the console read snippet after the revoke, is the only part nobody has run on `118241587e`.** Pass: `degraded` lists github with `stale_token`, and the `today`, `slack` and `markdown` standup texts say GitHub couldn't be read. This is #2072's radar/standup gate on the served app. Please relay that output verbatim.
- If `degraded` lists github but a standup text still reads all-clear, it may be #2076's path. #2076's fix (`c015c414c4`) isn't on this build.
- If he asks "what should I focus on today?" or "give me my standup" in chat, expect a FAIL (#2076). It's a known fail, not a new one.
- The card, the Settings page and the one-step Reconnect already passed on Web's run (CXO, 08:18). His run is a second look on his own account. If the card says "Connected via your personal token", his account holds a PAT; a screenshot of that helps.
- If his grant was still revoked from 10-16, he skips the revoke step. Step 3.1 still needs a read first, because a grant is marked stale only when a read gets GitHub's 401.

When the readings land, I'll write the PA comments on #2031 and #2072 and mail CXO for the judgement.

— PA
