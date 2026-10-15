"""2014 end to end (Postgres): deleting a list with a base item and a todo.

Uses the repo's ``async_transaction`` fixture (rolled back; same pattern as
test_cross_user_access.py). Needs a database migrated to s2014items (CHECK + FK
ON DELETE SET NULL); skipped otherwise.
"""

from datetime import datetime, timezone
from types import SimpleNamespace
from uuid import uuid4

import pytest
from sqlalchemy import text

from services.domain import models as domain
from services.repositories.todo_repository import TodoRepository
from services.repositories.universal_list_repository import UniversalListRepository
from tests.integration.test_cross_user_access import create_test_user_in_session


@pytest.mark.asyncio
async def test_delete_list_route_removes_base_item_and_listless_todo_survives(async_transaction):
    from web.api.routes.lists import delete_list as delete_list_route

    owner, other = str(uuid4()), str(uuid4())
    async with async_transaction as session:
        has_fk = await session.execute(
            text("SELECT 1 FROM pg_constraint WHERE conname = 'fk_items_list_id_lists'")
        )
        if has_fk.first() is None:
            pytest.skip("database is not migrated to s2014items")

        await create_test_user_in_session(session, owner)
        await create_test_user_in_session(session, other)
        lists = UniversalListRepository(session)
        todos = TodoRepository(session)

        lst = await lists.create_list(domain.List(name="L", owner_id=owner, item_type="todo"))
        todo = await todos.create_todo(
            domain.Todo(text="t", owner_id=owner, list_id=lst.id, position=0)
        )
        base_id = str(uuid4())
        now = datetime.now(timezone.utc)
        await session.execute(
            text(
                "INSERT INTO items (id,text,position,list_id,item_type,created_at,updated_at)"
                " VALUES (:i,'b',1,:l,'item',:n,:n)"
            ),
            {"i": base_id, "l": lst.id, "n": now},
        )

        resp = await delete_list_route(
            lst.id, current_user=SimpleNamespace(sub=owner), list_repo=lists
        )
        assert resp == {"status": "deleted", "list_id": lst.id}  # 200 path, no HTTPException

        # The route's dependency commits after the handler; flush stands in for that here.
        await session.flush()

        gone = await session.execute(text("SELECT count(*) FROM items WHERE id=:i"), {"i": base_id})
        assert gone.scalar() == 0, "base item must be removed with its list"
        row = await session.execute(text("SELECT list_id FROM items WHERE id=:i"), {"i": todo.id})
        assert row.one()[0] is None, "todo must survive, listless"

        mine = await todos.get_todo_by_id(todo.id, owner_id=owner)
        assert mine is not None and mine.text == "t"
        assert (await todos.get_todos_by_owner(other)) == []
        assert await todos.get_todo_by_id(todo.id, owner_id=other) is None
