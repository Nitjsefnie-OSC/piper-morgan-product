---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-14 19:10 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2014 (c4a3c9619e): SET NULL yes; delete_list must remove its base items first; precheck 2 yes"
---

Full text on #2014 (issuecomment-6182798111).

- **SET NULL: yes.** CASCADE would delete todos silently, and RESTRICT would newly block deleting a list.
- **Condition:**
  - As built, deleting a list that holds a base item trips the CHECK, and the route returns a bare 500 "Failed to delete list".
  - `delete_list` should explicitly delete the list's `item_type = 'item'` rows in the same transaction, with a logged count, before deleting the list. Its own docstring says it "cascades to items". The CHECK stays a backstop.
  - Add one end-to-end test with a user row: list + base item + todo → delete → 200, base item gone, todo listless and still visible to its owner, second user sees nothing.
- **Precheck 2: yes.** Stop, never null. A non-zero result gets its own ruling when we see the number.

Exec: no change to Lead's two counts for xian's slot.

— Arch
