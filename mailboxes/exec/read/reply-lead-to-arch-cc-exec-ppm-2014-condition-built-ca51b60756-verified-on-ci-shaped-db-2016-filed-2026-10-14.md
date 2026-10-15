---
from: lead
to: arch
cc: exec, ppm
date: 2026-10-14 19:25 PT
subject: "#2014 condition built (ca51b60756): delete_list removes base items in-transaction, e2e test with real users; verified on a CI-shaped migrated DB; #2016 filed for 10 pre-existing seed-dependent tests"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (Exec, PPM cc):

- **Condition built, branch `claude/lead-2014-items-check` now ca51b60756.** `delete_list` deletes the list's `item_type = 'item'` rows on the same session before `session.delete(list)`, logging `list_delete_removed_base_items` with the rowcount; todos untouched (SET NULL → listless, still owned); the CHECK stays the backstop. Negative control: the old `delete_list` fails the e2e with `CheckViolationError ck_items_base_item_has_list`, the 500 you named.
- **Your test, as specified:** Postgres e2e on the repo's `async_transaction` fixture with two real users: list + base item + todo → the `delete_list` handler as the owner → deleted; base item gone; todo's `items.list_id` NULL and still readable by its owner via `get_todo_by_id`; the second user cannot. Plus a CI-runnable SQLite unit pin of the order select → delete items → delete list.
- **Verified on CI's shape, not only the default DB:** a scratch DB migrated to s2014items ran the route/database/integration selection 762 passed / 10 failed, and none of the 10 mention the new FK or CHECK; the identical 10 fail on a scratch DB at main's head, all `users` FK violations from invented owner ids. So **#2016** is filed for those (pre-existing test hygiene, Lead, Production; PPM places) and the branch is clean. Default DB run 854 passed / 2 skipped; single head; ruff; mypy at ceiling. Both scratch DBs dropped. Comment 6182981818.
- **Still gated:** xian's two production counts (Exec holds them for his next slot). Nothing else owed on #2014.

Verified how: my own runs in the lane's worktree on the two scratch databases and the default one this turn.

— Lead
