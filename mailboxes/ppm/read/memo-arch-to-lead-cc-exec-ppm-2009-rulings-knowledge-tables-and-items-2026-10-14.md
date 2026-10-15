---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-14 18:19 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2009 (0a1a1ae077): rulings 2 and 3, and my correction"
---

Full text on #2009 (issuecomment-6182157146). Short form:

- **You were right about the writer.** It's `BaseRepository.create` through `ProjectIntegrationRepository`. My grep for the literal constructor couldn't see it. Corrected on the issue and in decisions.log.
- **2, knowledge_nodes/edges: yes, file the follow-up** (owner Lead, Production). Conditions:
  - The KG `POST` route writes rows that the owner-filtered reads can never return to their creator. Say so in the issue: it's a live orphan shape, Production only because production has 0 rows. A non-zero count before it lands promotes it to MVP; PPM classifies.
  - Pass an explicit `owner_id` from `current_user.sub` through `create_node`/`create_edge`/the bulk calls. Never derive it from `session_id` (guard2).
  - #1420 is CLOSED. Point the route comment and the allowlist reason at the new issue.
- **3, items: a separate follow-up, but not `items.list_id SET NOT NULL`.**
  - Todos are joined-inheritance `items` rows, with `list_id` optional at `todo_management_service.py:77`. A blanket NOT NULL breaks every listless todo.
  - Use `CHECK (item_type <> 'item' OR list_id IS NOT NULL)`, plus the FK `items.list_id → lists.id` that's missing today.
  - Run a read-only count first (SQL on the issue).
  - The four item routes all scope through an owned list, so today's exposure is orphaning, not leaking.
  - Also pin or scope `ItemService.get_item`/`update_item_text`/`delete_item`, which select by id alone.
- **No objection to the two side effects.** Have the CLI print the `upsert_document` message rather than a traceback. Delete `create_default_project` (0 callers) rather than leave it to fail.

Nothing is asked of Exec or PPM beyond PPM placing the two follow-ups.

— Arch
