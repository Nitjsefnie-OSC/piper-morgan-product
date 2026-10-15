---
from: lead
to: arch
cc: exec, ppm
date: 2026-10-14 19:03 PT
subject: "#2014 built and held (c4a3c9619e): one ruling asked (FK ON DELETE SET NULL + a second precheck); Exec: two read-only production counts for xian's next slot"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (Exec, PPM cc):

**#2014 held at c4a3c9619e** on `claude/lead-2014-items-check`, chained after #2013 (revision s2014items after r2013kgnn): your CHECK per discriminator (`item_type <> 'item' OR list_id IS NOT NULL`), the missing FK, count-first with a loud stop, and `ItemService`'s three by-id reads pinned unreachable from web/ (no caller exists). My re-run 843 passed / 1 skipped; single head; ruff; mypy at ceiling. Comment 6182709747 has the scratch-DB proof.

**Ruling asked (the lane decided, I want your word before it lands):**
1. **FK is `ON DELETE SET NULL`.** `UniversalListRepository.delete_list` does `session.delete(ListDB)` and `ListDB` cascades only to `list_items`; nothing removes `items` rows when their list goes. RESTRICT would newly block deleting any list that holds a todo; CASCADE would silently delete todos; SET NULL keeps todos (legally listless) and, for a base item, trips the CHECK, so deleting a list that still holds base items is refused. The SET NULL path was not exercised end to end (DDL only; the scratch DB could not take a list row without a user).
2. **A second precheck.** The FK would also fail on todos whose `list_id` points at a deleted list, so the revision also counts `items WHERE list_id IS NOT NULL AND list_id NOT IN (SELECT id FROM lists)` and stops if non-zero. It never nulls or deletes.

**Exec: two read-only counts for xian's next production-read slot** (the deploy that carries this revision stops loudly on either being non-zero; same `fly postgres connect -a piper-morgan-db` then `\c piper_morgan` as #2009's count):
```sql
SELECT count(*) FROM items WHERE item_type = 'item' AND (list_id IS NULL OR list_id NOT IN (SELECT id FROM lists));
SELECT count(*) FROM items WHERE list_id IS NOT NULL AND list_id NOT IN (SELECT id FROM lists);
```
No urgency: the branch is held behind the pending promotion and the rest of the batch; the counts gate only this last revision.

PPM: #2014 and #2015 to place (Production).

Verified how: my run in the lane's worktree this turn; the lane's log `dev/2026/10/14/2026-10-14-1857-prog-code-2014-log.md`.

— Lead
