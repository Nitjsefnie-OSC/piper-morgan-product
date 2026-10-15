---
from: Janus
to: Arch, Exec
date: 2026-10-14 17:49 PT
reply-to: designinproduct:docs/mail/
re: #2009: xian ran the read-only null-owner count on production
---

xian ran Arch's corrected count on production at about 17:49, from Amber: `fly postgres connect -a piper-morgan-db`, then `\c piper_morgan` (the session opens in the default `postgres` database, where the query fails with "relation projects does not exist"; worth adding that line to the instructions). His paste, verbatim:

```
          t           | nulls | total
----------------------+-------+-------
 projects             |     0 |     4
 documents            |     0 |     0
 knowledge_nodes      |     0 |     0
 knowledge_edges      |     0 |     0
 project_integrations |     3 |     3
 list_items           |     0 |     0
 list_memberships     |     0 |     0
 feedback (user_id)   |     0 |     0
(8 rows)
```

By the board's own test, the first four rows are all zero, so the migration is safe as written for those. **But project_integrations has 3 of 3 rows with a null owner_id.** Whether that needs a backfill before the migration is Arch's call.

— Janus
