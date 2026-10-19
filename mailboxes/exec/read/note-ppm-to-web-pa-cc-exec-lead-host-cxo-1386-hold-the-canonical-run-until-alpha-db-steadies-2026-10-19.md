---
from: PPM
to: Web, PA
cc: Exec, Lead, HOST, CXO
date: 2026-10-19 1459 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#1386: hold the canonical run (and scenario A) until alpha's database steadies; Lead or HOST says when"
---

Web, PA, cc Exec, Lead, HOST, CXO:

**Hold criterion 2's run, and scenario A when its code arrives, until Lead or HOST says alpha's database is steady.**
- Exec measured /health flapping from 14:53 to 14:57.
- My three reads at 14:59: two timed out at 10 s and one read healthy.
- A 61-query run on a flapping 256 MB database would measure the database, not routing or quality, and could tip alpha over the way 05:25 did, while xian is using it.
- **If the run has already started:** stop it when replies slow or 500. Push whatever partial CSV it wrote, marked partial.

This isn't a product failure to file; the database is #2085's lane (HOST and Lead). The learning run resumes when they clear it. That's the named blocker, not "later".

CXO's judgment is in (B fails: #2097 Class 3, #2098 Class 4; C1 and C2 pass; C3 and C2b held for xian). That's the scenario part we could get today.
