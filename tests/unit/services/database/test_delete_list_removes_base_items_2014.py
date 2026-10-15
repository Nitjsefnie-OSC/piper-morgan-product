"""2014: ``UniversalListRepository.delete_list`` removes the list's base items first.

CI-pinning unit test. SQLite cannot build ``lists`` (JSONB) and there is no async SQLite
driver, so the session is a thin fake: the DELETE on ``items`` runs for real against an
in-memory SQLite ``items`` table; the list lookup and ``session.delete`` are stubbed.
The Postgres end-to-end counterpart is
tests/integration/test_delete_list_base_items_e2e_2014.py.
"""

from types import SimpleNamespace

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.sql.dml import Delete

from services.database.models import Base
from services.repositories.universal_list_repository import UniversalListRepository


class _FakeSession:
    def __init__(self, conn, db_list):
        self.conn, self.db_list, self.calls = conn, db_list, []

    async def execute(self, stmt):
        if isinstance(stmt, Delete):
            self.calls.append("delete_items")
            return self.conn.execute(stmt)
        self.calls.append("select_list")
        return SimpleNamespace(scalar_one_or_none=lambda: self.db_list)

    async def delete(self, obj):
        self.calls.append("delete_list")


@pytest.fixture
def conn():
    engine = create_engine("sqlite://")
    Base.metadata.tables["items"].create(engine)
    with engine.begin() as c:
        for i, (lid, typ) in enumerate(
            [("L1", "item"), ("L1", "item"), ("L1", "todo"), ("L2", "item")]
        ):
            c.execute(
                text(
                    "INSERT INTO items (id,text,position,list_id,item_type,created_at,updated_at)"
                    " VALUES (:i,'x',0,:l,:t,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)"
                ),
                {"i": f"r{i}", "l": lid, "t": typ},
            )
        yield c


@pytest.mark.asyncio
async def test_delete_list_removes_only_that_lists_base_items_before_the_list(conn):
    session = _FakeSession(conn, SimpleNamespace(id="L1"))
    repo = UniversalListRepository(session)

    assert await repo.delete_list("L1", owner_id="u1") is True

    assert session.calls == ["select_list", "delete_items", "delete_list"]
    left = {r[0] for r in conn.execute(text("SELECT id FROM items"))}
    # r0, r1: L1 base items gone. r2: L1 todo kept (FK SET NULL's job). r3: other list kept.
    assert left == {"r2", "r3"}


@pytest.mark.asyncio
async def test_delete_list_not_owned_removes_nothing(conn):
    session = _FakeSession(conn, None)
    assert await UniversalListRepository(session).delete_list("L1", owner_id="u2") is False
    assert session.calls == ["select_list"]
    assert conn.execute(text("SELECT count(*) FROM items")).scalar() == 4
