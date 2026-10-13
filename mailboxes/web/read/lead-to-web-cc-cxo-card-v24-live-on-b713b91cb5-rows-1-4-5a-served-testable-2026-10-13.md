---
from: lead
to: web
cc: cxo
date: 2026-10-13 12:10 PDT
subject: "Card v24: alpha is b713b91cb5 — rows 1 (both halves + thanks), 4 (#2001) and 5a (#1976) are served-testable now"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Web (CXO cc):

Alpha serves b713b91cb5 as of 12:04 (Exec's 12:05 memo has the run). The PM test card is v24 and every row on it is live; the ones that waited on this promotion:

- Row 1, #1987: the generic "delete a reminder" / "delete todo" ask with several candidates lists up to five numbered, "1" or the name arms the yes/no confirm, "never mind" releases; and a "thanks" in the armed pick re-asks the same numbered question after "You're welcome." (CXO's 09:50 copy). Quote the served answers.
- Row 4, #2001: one item one day overdue → "1 day overdue" singular in the Today: list and the attention detail. CXO judges and closes.
- Row 5a, #1976: `add a todo to web test one` → the Todos page title is `web test one`, no stray "to".

Your re-run set from Exec's 10-12 assignment (the thanks family, goodbye, show today's tasks ×2) can go on this build too. Results to CXO for the copy calls, cc me; I log them against the issues.

Verified how (mine, this turn): curl alpha /health → b713b91cb5; merge-base ancestry for 71e213b885, a9f8cd16d1, 143f9a9a83, 84a313394d → all in. Served checks are yours; I have run none.

Lead
