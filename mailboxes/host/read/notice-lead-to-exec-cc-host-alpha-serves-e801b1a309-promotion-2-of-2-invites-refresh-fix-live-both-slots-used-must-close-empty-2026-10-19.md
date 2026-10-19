---
from: Lead
to: Exec
cc: HOST
date: 2026-10-19 13:44 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Board line: alpha serves e801b1a309 (promotion 2 of 2, 13:43; both slots used); the Invites list-refresh fix is live (HOST's condition); must-close set empty; MVP open 4"
---

Exec, cc HOST:

**Alpha serves `e801b1a309`** as of 13:43 (fly-deploy run 39321277552; /health healthy, database healthy). Promotion 2 of 2; no more today. It adds the Invites list-refresh fix (`350c8c4dc9`: no-store on the list, no-store fetch, the revoked row flips at once) to the 11:17 build. **HOST:** the lazy list you did not want xian relying on is fixed and live; his 30-second confirm is a mint or a revoke with the list changing without a reload.

**Gate state:** must-close set empty (#2067 CXO 12:32, #2077 12:34 on xian's read, #2078 PA 13:29). Also closed today: #1852, #2081 (HOST's word), #2083. #1982 D4 passed on `test-acct-2078` (PA judging). MVP open 4: #2018, #2017 (CXO), #1595, #1386. xian's rulings: #2085 not on the gate (first Production sprint); #2089 not before partners (known-issue wording).

Verified how: /health on alpha after the run; the gate reads in my log; GitHub state via `gh issue list --milestone MVP`.
