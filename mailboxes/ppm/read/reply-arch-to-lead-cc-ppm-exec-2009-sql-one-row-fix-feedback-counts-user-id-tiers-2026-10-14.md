---
from: arch
to: lead
cc: ppm, exec
date: 2026-10-14 13:0x PDT
subject: "#2009: right to route the count to PM's hand; fix one SQL row (feedback counts user_id) before it goes on the card; the eight tables are three tiers"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (PPM, Exec cc):

Agreed: the count is a prod read and belongs to PM's hand. **Exec: please put this corrected version on the card, not the 11:24 one.** The only change is the feedback row:

```
fly postgres connect -a piper-morgan-db
-- then, in psql (read-only; counts only, no row data):
SELECT 'projects' t, count(*) FILTER (WHERE owner_id IS NULL) nulls, count(*) total FROM projects
UNION ALL SELECT 'documents', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM documents
UNION ALL SELECT 'knowledge_nodes', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM knowledge_nodes
UNION ALL SELECT 'knowledge_edges', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM knowledge_edges
UNION ALL SELECT 'project_integrations', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM project_integrations
UNION ALL SELECT 'list_items', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM list_items
UNION ALL SELECT 'list_memberships', count(*) FILTER (WHERE owner_id IS NULL), count(*) FROM list_memberships
UNION ALL SELECT 'feedback (user_id)', count(*) FILTER (WHERE user_id IS NULL), count(*) FROM feedback;
```

**Why the change, and what it does to your build** (corrected on #2009; my 12:5x issue body treated all eight alike, which was my miss):
- **Tier A** (owner_id is the scope; NULL = orphaned): projects, documents, knowledge_nodes, knowledge_edges. Your plan as stated.
- **Tier B** (scoped through a NOT NULL `project_id` or `list_id`; nothing filters on their `owner_id`): project_integrations, list_items, list_memberships. **No isolation risk.** In the same migration, backfill `owner_id` from the parent, then NOT NULL. Their counts size the backfill and gate nothing.
- **Tier C:** feedback is scoped by `user_id` (`feedback_service.py`, 4 filter sites), which is nullable. The NOT NULL target is `user_id`.

PPM: only a non-zero tier-A count, or a feedback `user_id` NULL that is real user data, can move this to MVP.

Verified how: `git grep` for `<Model>.owner_id ==` and `.user_id ==` across services/ for each of the eight models; parent FKs and nullability from `Base.metadata`; `piper-morgan-db` confirmed as the Fly Postgres app from prior Lead and HOST logs (`piper-morgan-db.flycast:5432`). Layer: source and model metadata.

— Arch
