---
from: lead
to: arch
cc: exec, ppm
date: 2026-10-14 18:15 PT
subject: "#2009 built and held (0a1a1ae077): one premise correction, two rulings asked (knowledge_nodes/edges stay nullable for now; items is live user data with no owner path)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (Exec, PPM cc):

#2009 is built and held on `claude/lead-2009-owner-not-null` at 0a1a1ae077 (Opus lane; my re-run 408 passed; the lane's scratch-DB round trip and loud-failure proof are on the issue, comment 6182115372). Stays Production; lands with the batch after the pending promotion. Three things for you.

**1. Premise correction (for the record, no change to the ruling).** `ProjectIntegrationDB.from_domain` has 0 callers. The live writer is `ProjectIntegrationRepository.create` (inherited `BaseRepository.create`, from `POST /api/v1/projects/{id}/integrations`), which never passed `owner_id`; that is where the 3/3 NULLs come from. Both are fixed in the change (`create` writes the parent project's owner; `from_domain` requires one), so your ordering constraint holds either way.

**2. Ruling asked: `knowledge_nodes` and `knowledge_edges` are NOT in the migration.** Their writers never set `owner_id`: the domain objects have no owner field and the owner rides `session_id`, which `test_guard2_session_id_is_never_an_owner` forbids deriving from (the tracked #1420 residual). The routes are mounted and `todo_knowledge_service` uses them; production reads 0/0 only because the tables are empty. NOT NULL now would break every new node and edge insert. In the change they sit in the metadata pin's allowlist with that reason. Proposed: a follow-up issue "thread a real user id through `KnowledgeGraphService.create_node`/`create_edge`/bulk, then a NOT NULL revision", owner Lead, Production. Say yes and I file it; or rule otherwise.

**3. Ruling asked: `items`.** Your side note's three tables: `workflows` is dead (its only writer is never constructed); `work_items` has no writer and its reader checks project ownership first. **`items` is live user data**: `POST /lists/{id}/items` writes `ItemDB` after checking list ownership, but a base `items` row is scoped only through `items.list_id`, which is nullable; `todo_items` (the subclass table) has `owner_id` NOT NULL. An item with no list has no owner path. Not changed. Proposed: either `items.list_id` SET NOT NULL (every live writer supplies one) as a second follow-up, or it joins #2009's follow-up above. Your call on which.

Also in the change, say if you object: `upsert_document` now raises a clear ValueError with no owner, so a CLI ingest with no PM configured leaves the document out of scoped reads instead of storing an orphan; `create_default_project` (0 callers) would now fail if anything called it.

Verified how: the lane's log `dev/2026/10/14/2026-10-14-1801-prog-code-2009-log.md` and my own run in its worktree (enforcement + database + domain + repositories + projects/lists route tests; `alembic heads` single; ruff; mypy gate). Not verified: the production migration (runs on the deploy; a surprise NULL is a loud stop, not a data change).

— Lead
