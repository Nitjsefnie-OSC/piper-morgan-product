"""2009: owner_id NOT NULL on the user-data tables that have no other owner column.

Spec: Arch's ruling on issue 2009 (comment 6181823415) and the 13:0x tier ruling.
Production step-1 count (xian, 2026-10-14 ~17:49 PT, read-only):

    projects              A   0 / 4
    documents             A   0 / 0
    project_integrations  B   3 / 3   (write path never set it; fixed in this change)
    list_items            B   0 / 0
    list_memberships      B   0 / 0
    feedback (user_id)    C   0 / 0

Each table is a separate step, in this order: backfill where the owner is
derivable from a NOT NULL parent, assert zero NULLs remain (raise with the
table and count; rows are never deleted), then ``SET NOT NULL``.

Tier B backfills: ``project_integrations`` from ``projects.owner_id`` (Arch's
ruling), ``list_items`` and ``list_memberships`` from ``lists.owner_id``
(``list_id`` is a NOT NULL FK to ``lists``, whose ``owner_id`` is NOT NULL).

Held out (not in this revision): ``knowledge_nodes`` and ``knowledge_edges``.
Their writers (``KnowledgeNodeDB.from_domain`` / ``KnowledgeEdgeDB.from_domain``,
reached from the mounted POST knowledge-graph routes and the todo knowledge
service) never set ``owner_id``; the owner rides ``session_id`` (the tracked
1420 residual). NOT NULL before those writers are fixed would fail every new
node and edge insert, which is the hard ordering constraint Arch set for
project_integrations. They stay in the nullable allowlist pinned in
tests/test_architecture_enforcement.py until a writer fix lands.

Downgrade drops NOT NULL on each column. It never un-backfills.

Revision ID: q2009nn
Revises: p1522drop
Create Date: 2026-10-14
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "q2009nn"
down_revision = "p1522drop"
branch_labels = None
depends_on = None


# (table, column, backfill SQL or None), in the order Arch listed them.
_STEPS = [
    ("projects", "owner_id", None),
    (
        "project_integrations",
        "owner_id",
        "UPDATE project_integrations pi SET owner_id = p.owner_id "
        "FROM projects p WHERE pi.project_id = p.id AND pi.owner_id IS NULL",
    ),
    ("documents", "owner_id", None),
    (
        "list_items",
        "owner_id",
        "UPDATE list_items li SET owner_id = l.owner_id "
        "FROM lists l WHERE li.list_id = l.id AND li.owner_id IS NULL",
    ),
    (
        "list_memberships",
        "owner_id",
        "UPDATE list_memberships lm SET owner_id = l.owner_id "
        "FROM lists l WHERE lm.list_id = l.id AND lm.owner_id IS NULL",
    ),
    ("feedback", "user_id", None),
]


def _assert_no_nulls(table: str, column: str) -> None:
    bind = op.get_bind()
    count = bind.execute(sa.text(f"SELECT count(*) FROM {table} WHERE {column} IS NULL")).scalar()
    if count:
        raise RuntimeError(
            f"2009: {table}.{column} still has {count} NULL row(s) after backfill; "
            f"refusing to SET NOT NULL. Report these rows (do not delete them) and "
            f"rerun once they have an owner."
        )


def upgrade() -> None:
    for table, column, backfill in _STEPS:
        if backfill:
            op.execute(backfill)
        _assert_no_nulls(table, column)
        op.execute(f"ALTER TABLE {table} ALTER COLUMN {column} SET NOT NULL")


def downgrade() -> None:
    for table, column, _backfill in reversed(_STEPS):
        op.execute(f"ALTER TABLE {table} ALTER COLUMN {column} DROP NOT NULL")
