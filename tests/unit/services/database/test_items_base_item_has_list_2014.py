"""2014: a base ``items`` row must have a list; a listless todo-shaped row is legal."""

import pytest
from sqlalchemy import create_engine, event, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from services.database.models import Base, ItemDB


@pytest.fixture
def session():
    """SQLite with FK enforcement on. Only ``items`` is created from the model (other
    tables carry Postgres UUID columns SQLite cannot render); ``lists`` is a stub."""
    engine = create_engine("sqlite://")

    @event.listens_for(engine, "connect")
    def _fk(dbapi_conn, _):
        dbapi_conn.execute("PRAGMA foreign_keys=ON")

    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE lists (id VARCHAR PRIMARY KEY)"))
    Base.metadata.tables["items"].create(engine)
    with Session(engine) as s:
        yield s


def test_base_item_without_list_is_refused(session):
    session.add(ItemDB(id="i1", text="x", list_id=None, item_type="item"))
    with pytest.raises(IntegrityError):
        session.commit()


def test_base_item_with_dangling_list_is_refused(session):
    session.add(ItemDB(id="i2", text="x", list_id="no-such-list", item_type="item"))
    with pytest.raises(IntegrityError):
        session.commit()


def test_listless_todo_shaped_row_still_inserts(session):
    # The CHECK lives on items; a todo's items row (item_type='todo') may be listless.
    session.execute(
        text(
            "INSERT INTO items (id, text, position, list_id, item_type, created_at, updated_at) "
            "VALUES ('t1', 'x', 0, NULL, 'todo', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        )
    )
    session.commit()
    assert session.execute(text("SELECT list_id FROM items WHERE id='t1'")).one()[0] is None


def test_base_item_with_real_list_inserts(session):
    session.execute(text("INSERT INTO lists (id) VALUES ('L1')"))
    session.add(ItemDB(id="i3", text="x", list_id="L1", item_type="item"))
    session.commit()


def test_constraints_present_on_model():
    names = {c.name for c in Base.metadata.tables["items"].constraints}
    assert "ck_items_base_item_has_list" in names
    fk = next(iter(Base.metadata.tables["items"].columns["list_id"].foreign_keys))
    assert fk.target_fullname == "lists.id" and fk.ondelete == "SET NULL"
