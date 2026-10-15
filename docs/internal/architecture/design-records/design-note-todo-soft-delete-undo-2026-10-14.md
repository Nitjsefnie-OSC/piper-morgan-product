---
type: design-note
title: "Todo soft delete with an undo window: design note (Arch)"
valid_from: "2026-10-14"
last_updated: "2026-10-14"
---

# Todo soft delete with an undo window

**Status:** design note, written before build, as xian's 10-14 approval of PPM's recommendation asks
(option C: "soft delete with an undo window for todos is the real fix; Arch writes the design note
before build"). Lead builds. PPM places the issue. CXO owns every user-facing line.
**What it lifts:** #2019, the interim cap of one bulk todo delete per request, lifts when the exit
criteria at the end of this note are met.
**Relation to #336** (DATA-SOFT-DELETE across domain models, open since 2025-11): this is #336's
first instance, built as the general mechanism and applied to one model. It is not a todo-only
fork.

## Why a mechanism and not a filter

Today a todo delete is a hard delete. `TodoRepository.delete_todo` (`todo_repository.py:380`) calls
`session.delete(db_todo)`, and the ORM cascades it to subtodos (`TodoDB.children`,
`cascade="all, delete-orphan"`).

A soft delete has to hide a row from every read. Counted on main 10-14 (`git grep`, services/ and
web/, tests excluded):
- **34 read sites** name `TodoDB`: 22 in the repository, 5 in `todo_service.py`, 4 in
  `intent_service.py`, 2 in `canonical_handlers.py`, 1 in the domain.
- **24 more** select `ItemDB`. A todo *is* an `items` row (joined inheritance, `TodoDB(ItemDB)`),
  and `item_service`'s list reads load every subclass with `selectin_polymorphic`.

The two existing precedents both filter per query:
- **`insights`:** an `is_deleted` boolean (#1031), with `InsightDB.is_deleted == False` written out
  at 5 sites in `repositories.py`.
- **`conversations`:** a `deleted_at` timestamp.

That works at 5 sites. At 58, one missed filter brings deleted todos back into a standup, a count or
a list. Nothing would fail; the user would just see a reminder they deleted. This is the same shape
as the #2009 rule that rests on every query keeping the filter. ADR-075's bar is "can't be
expressed", not "is avoided".

## Decisions

**D1. One column pair: `deleted_at` (timestamptz, nullable) and `deletion_id` (uuid, nullable).**
- **On `items`, not `todo_items`.** Every todo is an `items` row, and the polymorphic list reads
  start there. A later #336 extension to base items then costs nothing.
- **`deleted_at` gives the window its clock**, so a timestamp, not a boolean. That follows the
  `conversations` precedent, not the `insights` one.
- **`deletion_id` groups one user action.** It ties together the bulk set and the subtodo cascade, so
  undo restores exactly what that action removed: never more, never a re-resolve.
- **Don't reuse `lifecycle_state`.** It carries the MUX lifecycle (ARCHIVED, COMPOSTED). Putting
  "deleted" in it would make one column hold two facts.

**D2. Invisibility is enforced centrally, once.**
- **The hook:** a SQLAlchemy `do_orm_execute` session event adds
  `with_loader_criteria(ItemDB, ItemDB.deleted_at.is_(None), include_aliases=True)` to every ORM
  select. That covers `TodoDB`, `ItemDB` and the polymorphic loads.
- **Opting out takes a named execution option** (for example `include_deleted=True`), and only
  restore, purge and the deletion audit may use it.
- **A ratchet pins the opt-out:** an enumeration test lists every `include_deleted` call site against
  an allowlist.
- **Raw SQL is outside the ORM hook.** The ratchet also fails on any `text(...)` query naming
  `items` or `todo_items` that lacks the filter. Today's count is 0 (see Verified how), so the
  ratchet holds it there.

**D3. Delete becomes a mark, with the same scoping.**
- `delete_todo` keeps its owner filter and sets `deleted_at = now()` and one fresh `deletion_id` on
  the todo and all its descendants.
- A bulk delete (once #2019 lifts) uses one `deletion_id` for the whole confirmed set: the exact ids
  bound on the confirm carrier, as today.
- `list_memberships` rows are left in place. D2 hides the todo they point at, and undo then needs no
  rebuild.
- `items.list_id` is untouched. The #2014 `ON DELETE SET NULL` concerns list deletion, not todo
  deletion.

**D4. Undo is a write, so it gets a permission rule (ADR-080 D3).**
- **What `restore_todos(deletion_id, owner_id)` checks:** that every row in the group is owned by the
  caller, and that `deleted_at` is inside the window. It clears both columns for exactly that group
  and reports the count.
- **Partial restores are refused,** because they would mean Piper choosing which rows to bring back.
- **How the offer reaches the user:** the delete reply carries the undo offer as an armed offer bound
  to the `deletion_id` (the #1766 rule: a reply that needs binding must be armed).
- **The live router needs it allowlisted.** If the router is to dispatch it, `restore_todos` needs a
  `FLIP_WRITE_ALLOWLIST` entry, with the bound-offer path first. A bare "undo" with nothing bound
  asks what to undo. It never restores the most recent group on a guess (D4: uncertainty never
  writes).

**D5. Purge is part of the feature, not a follow-up.**
- **Why:** a user who is told "deleted" must eventually be right. So a scheduled hard delete removes
  rows whose `deleted_at` is older than the window, in `deletion_id` groups.
- **Mechanics:** it runs the existing ORM cascade, logs a count per run, and refuses to run if the
  window setting is missing.
- **Shipping rule:** soft delete with no purge is a privacy regression from today, so it doesn't
  ship.
- **Knowledge-graph rows (#2013):** a purge also removes a todo's knowledge-graph node, if one
  exists.

**D6. The window length is a product setting, not a constant in code.** PPM sets it; CXO says it.
The note assumes days, not seconds. "Undo" means a later turn can still restore, not only the next
reply.

## Exit criteria (what lifts #2019)

1. **Migration and model:** D1's columns on `items`, plus a partial index on `owner_id` for the live
   rows.
2. **D2's hook and ratchet,** with a test that a soft-deleted todo is absent from each public read:
   - list;
   - get by id;
   - search;
   - counts and stats (`get_completion_stats`);
   - the polymorphic list-items read;
   - standup's todo source.

   Plus the opt-out census.
3. **D3–D4 end to end:** delete two todos (one with a subtodo) → both and the subtodo are gone from
   every read → undo through the armed offer → exactly those three are back. A second user's undo
   of that `deletion_id` restores nothing.
4. **D5 purge,** run against a scratch DB with an expired group: it removes exactly that group and
   reports the count.
5. **A served run on alpha** of delete → undo, with CXO's lines.

Then #2019's cap lifts. Bulk delete comes back under the existing enumerating confirm, with undo
behind it.

## Not decided here

- **Extending to other models (#336's remainder).** This note makes the mechanism reusable but
  applies it only to `items`.
- **Migrating `insights`' `is_deleted` onto D1's pair.** Worth doing when #336 resumes, so the
  codebase ends with one convention, not three.

**Verified how:** read on origin/main 10-14:
- `TodoRepository.delete_todo` and `TodoDB`'s relationships;
- `ItemDB`/`TodoDB` inheritance;
- the `insights` and `conversations` soft-delete columns and their filters;
- `services/mux/lifecycle.py`.

Read sites counted with `git grep` (34 `TodoDB`, 24 `ItemDB`; services/ and web/, tests excluded). Raw SQL:
a case-insensitive `git grep` for `from`/`join`/`update` on `items` or `todo_items` in services/
and web/ found 0 hits, so D2's raw-SQL ratchet starts from zero. #336 read on GitHub.
Layer: source and design; nothing built or run.
