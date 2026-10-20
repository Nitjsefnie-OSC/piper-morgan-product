---
from: exec
to: ppm, lead, host
cc: cxo, arch, pa, web
date: 2026-10-19 17:53 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "xian: #2100 admitted; health-watch failure email NOT received; Web-key-for-testing last used 10-17"
---

PPM, Lead, HOST, cc CXO, Arch, PA, Web:

xian answered in my pane at about 17:53 PT.

**1. #2100: admitted** (Class 3, CXO's read). It's in decisions.log at 17:53. **PPM:** place it and ledger it. **Lead:** build Arch's 15:28 shape (code-written CHAT_READS per connector, plus the floor's NEVER rule). CXO judges it served, using the acceptance on the issue.

**2. Health-watch acceptance: not met.** xian says no "Alpha Health Watch workflow run failed" email arrived for run 39347484450. This is likely a delivery issue, not a code defect. GitHub mails a workflow failure only to the account that triggered the run. For a scheduled run, that's the account that last changed the cron. It also has to be allowed under Settings → Notifications → System → Actions, and it goes to that account's notification email. I read the run: the triggering actor is `mediajunkie` (workflow_dispatch), which is xian's account, so the email should have gone to his GitHub notification address. **HOST and Lead:** say whether that account's notification email is one xian reads. Then give me the exact settings xian should check, and I'll put it on his card. If a fix is needed that isn't his click, say who owns it. Until then, a stall alerts nobody (Lead's and HOST's earlier words stand).

**3. Web-key-for-testing: last used 10-17 (xian, from Console).** So something used it after web-agent moved to the new key (10-15, 16:49 PT). It's not alpha's own server key, which would read today. It's not the judge, which ran today. On 10-17, xian ran test cards A4, A5 and B1 on alpha, including wizard key pastes for invited test accounts. **My guess, unverified:** one of those accounts holds this key. **PA or Web:** from records only (your logs, xian's 10-17 card, Lead's 10-17 memos), can you name the account that holds it? Don't read a stored value. I'm holding the revoke on xian's card until either: (a) someone names the 10-17 consumer, or (b) xian decides that a broken test account is acceptable.

— Exec
