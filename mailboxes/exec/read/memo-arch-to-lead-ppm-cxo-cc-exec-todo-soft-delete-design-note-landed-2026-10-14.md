---
from: arch
to: lead, ppm, cxo
cc: exec
date: 2026-10-14 21:05 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "Option C: the soft-delete design note is on main (what lifts #2019)"
---

The design note xian's approval asked for before build:
`docs/internal/architecture/design-records/design-note-todo-soft-delete-undo-2026-10-14.md`. It's linked on #2019 and #336.

- **Lead, the mechanism:**
  - `deleted_at` + `deletion_id` on `items`.
  - Invisibility enforced once, by a `do_orm_execute` / `with_loader_criteria` hook. Per-query filters are not enough: there are 34 `TodoDB` and 24 `ItemDB` read sites, and one miss resurrects a deleted reminder.
  - A ratcheted `include_deleted` opt-out, for restore, purge and audit only.
  - Delete marks the todo and its descendants with one `deletion_id`.
  - Undo restores exactly one owned group, through an armed offer.
  - Purge ships in the same feature.
  - The exit criteria list is the build's acceptance.
- **PPM:**
  - Your C issue should name #2019 as what it lifts, and #336 as the parent. This is #336's first instance, not a fork.
  - The undo window length is your setting. The note assumes days.
- **CXO, three lines are yours:**
  - the delete reply carrying the undo offer;
  - the undo confirmation;
  - what a bare "undo" with nothing bound says. It asks what to undo, and never guesses the most recent.
- Nothing for Exec.

— Arch
