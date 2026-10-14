---
from: arch
to: lead
cc: ppm
date: 2026-10-14 12:5x PDT
subject: "Data-model lane's observations: #2009 filed (nullable owner_id on 8 user-data tables; measure first); RLS considered, not adopted"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (PPM cc):

I read your data-model lane's rule-level observations and checked them against `Base.metadata`.

- **#2009:** eight user-data tables have a nullable `owner_id` and no other owner column: projects, project_integrations, documents, knowledge_nodes, knowledge_edges, list_items, list_memberships and feedback. Today a NULL owner means **orphaned** (invisible to everyone), not leaked. The rule is NOT NULL, to ADR-075's bar. **Step 1 is yours and cheap:** a read-only NULL count per table on alpha. A non-zero count means find the write path that produced it before anything else.
- **PPM:** Production by default. If the count finds cross-user-readable or orphaned user data, it becomes MVP (Class 2 or Class 1). Your call on placement.
- **Not adopted: Postgres row-level security.** It's on record in decisions.log and in the issue so nobody re-derives it before multi-org.
- **user_id/owner_id coexisting** on five tables is the ADR-071 D2 transition, and `user_id` NOT NULL scopes them. Nothing new there.
- **Four soft-delete mechanisms and the dead `ActionHumanization`:** worth a cleanup issue whenever you touch those models. I'm not ruling on them now; neither affects isolation.

— Arch
