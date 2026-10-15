"""2014: a base ``items`` row must have a list; ``items.list_id`` gets a real foreign key.

Follows r2013kgnn. ``items.list_id`` was ``String, nullable=True`` with no foreign key, so a
base item (``item_type = 'item'``) with no list, or pointing at a deleted list, has no owner
path (ownership is derived from the list). Todos are joined-inheritance children
(``TodoDB(ItemDB)``, ``item_type = 'todo'``) whose owner is ``todo_items.owner_id``; they
legitimately have ``items.list_id`` NULL, so a blanket NOT NULL would be wrong. Instead:

* ``ck_items_base_item_has_list``: ``CHECK (item_type <> 'item' OR list_id IS NOT NULL)``
* ``fk_items_list_id_lists``: ``items.list_id -> lists.id``

ON DELETE SET NULL, chosen from how lists are deleted today: ``UniversalListRepository.
delete_list`` calls ``session.delete(ListDB)`` and ``ListDB`` only cascades to ``list_items``;
no code removes ``items`` rows when their list goes. So RESTRICT would newly make deleting any
list that holds a todo fail, and CASCADE would silently delete todos (user data). SET NULL
keeps todos (listless is legal for them, matching today's dangling behaviour minus the
dangling), and for a base item the SET NULL violates the CHECK, so deleting a list that still
holds base items is refused loudly rather than orphaning or deleting them.

The upgrade first counts offenders (read-only) and raises ``RuntimeError`` naming the count;
it never deletes or fixes up rows:

* base items with NULL or dangling ``list_id`` (the CHECK/FK would fail on them);
* any item (todos included) whose non-NULL ``list_id`` is not in ``lists`` (the FK would
  fail on them).

Downgrade drops both constraints.

Revision ID: s2014items
Revises: r2013kgnn
Create Date: 2026-10-14
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "s2014items"
down_revision = "r2013kgnn"
branch_labels = None
depends_on = None

_CHECK = "ck_items_base_item_has_list"
_FK = "fk_items_list_id_lists"


def _count(sql: str) -> int:
    return op.get_bind().execute(sa.text(sql)).scalar() or 0


def upgrade() -> None:
    base = _count(
        "SELECT count(*) FROM items WHERE item_type = 'item' "
        "AND (list_id IS NULL OR list_id NOT IN (SELECT id FROM lists))"
    )
    if base:
        raise RuntimeError(
            f"2014: {base} base item(s) (items.item_type = 'item') have a NULL or dangling "
            f"list_id; refusing to add {_CHECK} / {_FK}. Report these rows (do not delete "
            f"them) and rerun once they have a list."
        )
    dangling = _count(
        "SELECT count(*) FROM items WHERE list_id IS NOT NULL "
        "AND list_id NOT IN (SELECT id FROM lists)"
    )
    if dangling:
        raise RuntimeError(
            f"2014: {dangling} item row(s) have a non-NULL list_id that is not in lists; "
            f"refusing to add {_FK}. Report these rows (do not delete or null them) and "
            f"rerun once they are resolved."
        )
    op.create_foreign_key(_FK, "items", "lists", ["list_id"], ["id"], ondelete="SET NULL")
    op.create_check_constraint(_CHECK, "items", "item_type <> 'item' OR list_id IS NOT NULL")


def downgrade() -> None:
    op.drop_constraint(_CHECK, "items", type_="check")
    op.drop_constraint(_FK, "items", type_="foreignkey")
