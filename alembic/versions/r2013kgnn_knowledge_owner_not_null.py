"""2013: owner_id NOT NULL on knowledge_nodes and knowledge_edges.

Follows q2009nn, which held these two tables out because their writers
(``KnowledgeNodeDB.from_domain`` / ``KnowledgeEdgeDB.from_domain``) never set
``owner_id``. 2013 threads an explicit owner (``current_user.sub`` on the routes, the
todo's owner in ``TodoKnowledgeService``) down to both constructors, which now refuse a
missing owner, so NOT NULL is safe here.

No backfill: there is no derivable owner (the domain objects carry none, and
``session_id`` is never an owner). The upgrade asserts zero NULL rows and raises,
naming the table and count, if any remain; rows are never deleted. Production read
0 / 0 on 2026-10-14.

Downgrade drops NOT NULL on both columns.

Revision ID: r2013kgnn
Revises: q2009nn
Create Date: 2026-10-14
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "r2013kgnn"
down_revision = "q2009nn"
branch_labels = None
depends_on = None

_TABLES = ["knowledge_nodes", "knowledge_edges"]


def _assert_no_nulls(table: str) -> None:
    bind = op.get_bind()
    count = bind.execute(sa.text(f"SELECT count(*) FROM {table} WHERE owner_id IS NULL")).scalar()
    if count:
        raise RuntimeError(
            f"2013: {table}.owner_id has {count} NULL row(s); refusing to SET NOT NULL. "
            f"Report these rows (do not delete them) and rerun once they have an owner."
        )


def upgrade() -> None:
    for table in _TABLES:
        _assert_no_nulls(table)
        op.execute(f"ALTER TABLE {table} ALTER COLUMN owner_id SET NOT NULL")


def downgrade() -> None:
    for table in reversed(_TABLES):
        op.execute(f"ALTER TABLE {table} ALTER COLUMN owner_id DROP NOT NULL")
