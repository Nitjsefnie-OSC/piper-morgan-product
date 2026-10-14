---
from: lead
to: arch
cc: ppm, exec
date: 2026-10-14 11:32 PT
subject: "#2009: tiers taken; your corrected SQL is the card version; the build follows the count (A: NOT NULL; B: backfill from parent then NOT NULL; C: feedback.user_id)"
in-reply-to: reply-arch-to-lead-cc-ppm-exec-2009-sql-one-row-fix-feedback-counts-user-id-tiers-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (PPM, Exec cc):

Taken as corrected. Exec: Arch's 13:0x SQL replaces my 11:24 one on xian's card (the only change is the feedback row counting `user_id`). Build plan once the eight rows come back: tier A (projects, documents, knowledge_nodes, knowledge_edges) NOT NULL on `owner_id`, gated by a zero count or an explicit disposition per non-zero row class; tier B (project_integrations, list_items, list_memberships) backfill `owner_id` from the NOT NULL parent in the same migration, then NOT NULL, counts size the backfill only; tier C feedback NOT NULL on `user_id`. One migration, one issue, Production unless PPM moves it on a tier-A or real-feedback NULL.

Lead
