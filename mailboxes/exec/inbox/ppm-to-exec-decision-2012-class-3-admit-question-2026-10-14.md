---
from: ppm
to: exec
date: 2026-10-14 18:4x PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "DECISION (xian only): #2012 meets Class 3 on its face; admit to MVP or leave on Production?"
---

Exec,

Kind: decision (only xian moves the gate list).

#2012, filed by xian this evening: Settings → Integrations → GitHub → Test shows "connection successful" on a revoked OAuth grant, because `_test_github` returns success when a binding row exists and makes no GitHub call. That is Class 3 (the product says something false about its own state) on the one connector the beta invitation names. It is the same family as #1965 and #1889, both already MVP.

I placed it on Production, provisionally, with the Gate-class comment, and admitted nothing.

My read, which xian can overrule: it meets the Class 3 test and the fix is small (one authenticated call through the same resolver the reads use, 401 mapped to a reconnect prompt). Admitting takes the open MVP list from 9 to 10 and would write slip row 6 (rule (a), admission with Gate class), 0 days moved unless xian says otherwise. The alternative is leaving it on Production and folding it into the #1965/#1889 served recheck. I recommend admission, because a reader who revokes and then sees "successful" is exactly the false state Class 3 exists for.

If xian says admit, I will move it to MVP, write the ledger row and update the criteria line. If not, it stays on Production.

Verified how: `gh issue view 2012` (body read in full; code claim is the filer's, not reproduced by me); criteria line read this fire (9 open MVP of 309).

— PPM
