"""2013: knowledge-graph nodes and edges are written with the signed-in owner.

Before this change ``KnowledgeNodeDB.from_domain`` / ``KnowledgeEdgeDB.from_domain``
never set ``owner_id`` and every owner-filtered read (``WHERE owner_id = :me``) skipped
the rows, so a user's own writes were invisible to them. These tests drive the real
route handlers, service and repository against in-memory SQLite (the 2009 pattern) and
read the rows back through the owner-filtered repository reads:

- POST /nodes and POST /edges, called as a signed-in user, round-trip for that user
  and are invisible to another user.
- ``TodoKnowledgeService`` writes the todo's owner onto its node and edges.
- The DB constructors, repository and service refuse a missing owner.
- The column is NOT NULL on the model.
"""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest
import pytest_asyncio

aiosqlite = pytest.importorskip("aiosqlite")

from sqlalchemy import JSON, MetaData, String, func, select  # noqa: E402
from sqlalchemy.dialects import postgresql  # noqa: E402
from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

import services.domain.models as domain  # noqa: E402
from services.database.models import (  # noqa: E402
    KnowledgeEdgeDB,
    KnowledgeNodeDB,
    User,
)
from services.database.repositories import KnowledgeGraphRepository  # noqa: E402
from services.knowledge.knowledge_graph_service import KnowledgeGraphService  # noqa: E402
from services.shared_types import EdgeType, NodeType  # noqa: E402
from services.todo.todo_knowledge_service import TodoKnowledgeService  # noqa: E402
from web.api.routes import knowledge_graph as routes  # noqa: E402

ALICE = str(uuid.uuid4())
BOB = str(uuid.uuid4())

_TABLES = [User, KnowledgeNodeDB, KnowledgeEdgeDB]


def _sqlite_schema() -> MetaData:
    md = MetaData()
    for model in _TABLES:
        table = model.__table__.to_metadata(md)
        for col in table.columns:
            if isinstance(col.type, postgresql.UUID):
                col.type = String(36)
            elif isinstance(col.type, (postgresql.JSONB, postgresql.ARRAY)):
                col.type = JSON()
            col.server_default = None
        table.indexes.clear()
    return md


@pytest_asyncio.fixture
async def session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(_sqlite_schema().create_all)
    SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with SessionLocal() as s:
        yield s
    await engine.dispose()


@pytest.fixture
def service(session) -> KnowledgeGraphService:
    enforcer = MagicMock()
    enforcer.check_harassment_patterns = AsyncMock(return_value=False)
    enforcer.check_inappropriate_content = AsyncMock(return_value=False)
    return KnowledgeGraphService(
        knowledge_graph_repository=KnowledgeGraphRepository(session),
        ethics_boundary_enforcer=enforcer,
    )


def _user(sub: str) -> SimpleNamespace:
    return SimpleNamespace(sub=sub)


class TestRoutesWriteTheSignedInOwner:
    @pytest.mark.asyncio
    async def test_node_and_edge_round_trip_for_the_creator(self, session, service):
        a = await routes.create_node(
            name="alpha",
            node_type="concept",
            current_user=_user(ALICE),
            kg_service=service,
        )
        b = await routes.create_node(
            name="beta",
            node_type="concept",
            current_user=_user(ALICE),
            kg_service=service,
        )
        edge = await routes.create_edge(
            source_node_id=a["id"],
            target_node_id=b["id"],
            edge_type="references",
            current_user=_user(ALICE),
            kg_service=service,
        )
        await session.commit()

        repo = KnowledgeGraphRepository(session)
        # Owner-filtered reads: by id, and the WHERE owner_id = :me list reads.
        assert (await repo.get_node_by_id(a["id"], ALICE)) is not None
        assert (await repo.get_edge_by_id(edge["id"], ALICE)) is not None
        mine = await repo.get_nodes_by_session(ALICE)
        assert {n.id for n in mine} == {a["id"], b["id"]}
        assert [e.id for e in await repo.get_edges_by_session(ALICE)] == [edge["id"]]

    @pytest.mark.asyncio
    async def test_another_user_cannot_see_them(self, session, service):
        a = await routes.create_node(
            name="alpha", node_type="concept", current_user=_user(ALICE), kg_service=service
        )
        await session.commit()
        repo = KnowledgeGraphRepository(session)
        assert await repo.get_node_by_id(a["id"], BOB) is None
        assert await repo.get_nodes_by_session(BOB) == []

    @pytest.mark.asyncio
    async def test_owner_column_is_the_user_not_the_session_tag(self, session, service):
        a = await routes.create_node(
            name="alpha", node_type="concept", current_user=_user(ALICE), kg_service=service
        )
        await session.commit()
        row = await session.get(KnowledgeNodeDB, a["id"])
        assert row.owner_id == ALICE


class TestTodoKnowledgeServiceWritesTheTodosOwner:
    @pytest.mark.asyncio
    async def test_node_and_edge_carry_the_todo_owner(self, session, service):
        todo_svc = TodoKnowledgeService(service)

        def _todo(tid: str):
            from datetime import datetime, timezone

            return SimpleNamespace(
                id=tid,
                title=tid,
                description="",
                status="pending",
                priority="medium",
                tags=[],
                context="",
                creation_intent="",
                intent_confidence=0.0,
                estimated_minutes=None,
                project_id=None,
                owner_id=ALICE,
                created_at=datetime.now(timezone.utc),
                knowledge_node_id=None,
            )

        t1, t2 = _todo("t1"), _todo("t2")
        n1 = await todo_svc.create_todo_knowledge_node(t1, user_id="session-ish-not-owner")
        n2 = await todo_svc.create_todo_knowledge_node(t2, user_id="session-ish-not-owner")
        assert n1 is not None and n2 is not None
        await session.commit()

        repo = KnowledgeGraphRepository(session)
        assert {n.id for n in await repo.get_nodes_by_session(ALICE)} == {n1.id, n2.id}

        # Edge path: pass the relationship as the enum the service requires.
        await service.create_edge(
            source_node_id=n1.id,
            target_node_id=n2.id,
            edge_type=EdgeType.REFERENCES,
            owner_id=t1.owner_id,
        )
        await session.commit()
        assert len(await repo.get_edges_by_session(ALICE)) == 1


class TestMissingOwnerIsRefused:
    @pytest.mark.asyncio
    async def test_todo_with_no_owner_writes_no_node(self, session, service):
        todo = SimpleNamespace(id="t0", owner_id=None, knowledge_node_id=None)
        result = await TodoKnowledgeService(service).create_todo_knowledge_node(
            todo, user_id="a-session-or-user"
        )
        assert result is None
        assert (
            await session.execute(select(func.count()).select_from(KnowledgeNodeDB))
        ).scalar() == 0

    def test_node_constructor_refuses_missing_owner(self):
        node = domain.KnowledgeNode(name="n", node_type=NodeType.CONCEPT)
        for bad in (None, ""):
            with pytest.raises(ValueError, match="explicit owner_id"):
                KnowledgeNodeDB.from_domain(node, bad)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            KnowledgeNodeDB.from_domain(node)  # type: ignore[call-arg]

    def test_edge_constructor_refuses_missing_owner(self):
        edge = domain.KnowledgeEdge(
            source_node_id="a", target_node_id="b", edge_type=EdgeType.REFERENCES
        )
        for bad in (None, ""):
            with pytest.raises(ValueError, match="explicit owner_id"):
                KnowledgeEdgeDB.from_domain(edge, bad)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            KnowledgeEdgeDB.from_domain(edge)  # type: ignore[call-arg]

    def test_constructors_write_the_owner_they_are_given(self):
        node = domain.KnowledgeNode(name="n", node_type=NodeType.CONCEPT)
        assert KnowledgeNodeDB.from_domain(node, ALICE).owner_id == ALICE
        edge = domain.KnowledgeEdge(
            source_node_id="a", target_node_id="b", edge_type=EdgeType.REFERENCES
        )
        assert KnowledgeEdgeDB.from_domain(edge, ALICE).owner_id == ALICE

    @pytest.mark.asyncio
    async def test_service_and_repo_refuse_missing_owner(self, session, service):
        with pytest.raises(TypeError):
            await service.create_node(name="n", node_type=NodeType.CONCEPT)  # type: ignore[call-arg]
        with pytest.raises(ValueError, match="explicit owner_id"):
            await service.create_node(name="n", node_type=NodeType.CONCEPT, owner_id="")
        node = domain.KnowledgeNode(name="n", node_type=NodeType.CONCEPT)
        with pytest.raises(ValueError, match="explicit owner_id"):
            await KnowledgeGraphRepository(session).create_node(node, "")

    @pytest.mark.asyncio
    async def test_bulk_methods_write_the_owner(self, session, service):
        nodes = await service.create_nodes_bulk(
            [{"name": "a"}, {"name": "b"}], session_id="s", owner_id=ALICE
        )
        await session.commit()
        repo = KnowledgeGraphRepository(session)
        assert {n.id for n in await repo.get_nodes_by_session(ALICE)} == {n.id for n in nodes}
        with pytest.raises(TypeError):
            await service.create_nodes_bulk([{"name": "c"}])  # type: ignore[call-arg]

    def test_columns_are_not_null(self):
        assert KnowledgeNodeDB.__table__.c.owner_id.nullable is False
        assert KnowledgeEdgeDB.__table__.c.owner_id.nullable is False
