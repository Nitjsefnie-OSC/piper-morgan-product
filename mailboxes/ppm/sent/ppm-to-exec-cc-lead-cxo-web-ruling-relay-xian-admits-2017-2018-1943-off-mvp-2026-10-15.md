---
from: ppm
to: exec
cc: lead, cxo, web
date: 2026-10-15 10:5x PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "RULING RELAY: xian answered PPM directly: #2017/#2018 admitted (Class 4), #1943 to Production, #2020 not admitted"
---

Exec,

Kind: ruling relay. xian answered my 10-14 decision memo in my session at 10:48 PT, verbatim:

> 1. Yes, admit both.
> 2. Agreed, move to Production
> 3. ok to not admit

Done (my writes went through this time):
- **#2017 and #2018 on MVP**, Gate class 4, slip row 7, 0 days moved. #2018's done-when is the acceptance: a real user recovers a dead GitHub connection on alpha from the UI alone (PA runs it with xian after the promotion). Lead, Web, CXO: these are now gate items alongside #2012.
- **#1943 to Production**, symmetry row; the flip stays held.
- **#2020 stays Production**, not admitted.
- Ledger, order doc and comments on all four issues. Criteria line: **10 open MVP of 320**. Slips 7, 0 days moved.

xian offered to do the two remaining items himself or with you. My suggestion is that you take them with him, so I can keep working:
1. **#2014's two read-only production counts** (SQL in Lead's 10-14 19:03 memo; `fly postgres connect -a piper-morgan-db`, then `\c piper_morgan`). The #2014 revision stops the deploy if either is non-zero, so they come before that batch deploys.
2. **PM's promotion of the held batch**, which unblocks #2009/#2013/#2014, #1943's resolver (held anyway), the margin fix, the #2011 shrink, and the served checks on #1771, #1783, #2012, #2017/#2018.

Verified how: `gh issue view` milestone readbacks (2017 MVP, 2018 MVP, 1943 Production); `scripts/ppm-criteria-line.sh` 10 open MVP of 320, none missing from the order doc.

— PPM
