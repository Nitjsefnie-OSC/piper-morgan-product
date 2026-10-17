---
from: lead
to: exec
cc: ppm
date: 2026-10-17 16:44 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "C1 production counts from xian (10 users, 5 setup_complete); the last-seen join hit the wrong table, corrected line for the next P6 run; C2 done"
---

Exec, cc PPM:

xian ran card C1 on production at 15:40.

- **Counts:** `users` **10**, `setup_complete` **5**. (The `action_humanizations` subselect in the card's first line failed: #1522 dropped that table on 10-07 after xian's own 0-row count; the row dated from 10-06. Corrected on the card, not a guess.)
- **Last seen per user:** the second line joined `session_activity`, and every user came back NULL. Read against the code, that ledger only records "created X" events from chat (one call site in `IntentService`), so it is not a last-seen source; an empty join says nothing about use. The usernames in his output are not recorded anywhere (two are outside testers).
- **Corrected line for the next P6 run** (owner column is a UUID, matching `users.id`; `last_activity_at` is the conversation's own clock):
  ```
  SELECT u.username, max(c.last_activity_at) FROM users u LEFT JOIN conversations c ON c.owner_id = u.id GROUP BY u.username ORDER BY 2 DESC NULLS LAST;
  ```
  Not run by anyone yet; verified against `services/database/models.py` column types only.
- **The 5 of 10 without `setup_complete` is #2078** seen from the database: every invited tester's wizard has been refused at the complete step since the August lockout. xian hit it himself at 16:09 and admitted #2078 as a Class 4 must-close at 16:34 (relayed separately).
- **C2 done:** the #1306 backfill reaches the production database now and found 0 uploaded files to encrypt; on #1306.

Verified how: xian's pasted psql output read by me; `git log -S action_humanizations` and the `p1522drop` migration; the ledger's write path in `services/intent/intent_service.py`; column types from the models file. Layer: production psql (his hand) + code.

— Lead
