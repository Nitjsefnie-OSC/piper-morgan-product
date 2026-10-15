"""2009: the tier-B owner_id copies are written from the parent row.

Arch's hard ordering constraint: ``project_integrations.owner_id`` goes NOT NULL
in the same change that makes the write path set it (production read 3 of 3
rows NULL: no writer ever set it). These tests drive the real write paths
against in-memory SQLite (the #1035 / #952 pattern) and read the row back:

- ``ProjectIntegrationRepository.create`` (the path POST
  /api/v1/projects/{id}/integrations uses) writes the parent project's owner.
- ``ProjectIntegrationDB.from_domain`` takes the owner explicitly and refuses None.
- ``UniversalListItemRepository.create_item`` writes the parent list's owner.
- ``DocumentRepository.upsert_document`` refuses a missing owner (tier A).
"""

from __future__ import annotations

import uuid

import pytest
import pytest_asyncio

aiosqlite = pytest.importorskip("aiosqlite")

from sqlalchemy import JSON, MetaData, String, select  # noqa: E402
from sqlalchemy.dialects import postgresql  # noqa: E402
from sqlalchemy.exc import IntegrityError  # noqa: E402
from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

import services.domain.models as domain  # noqa: E402
from services.database.models import (  # noqa: E402
    ListDB,
    ListItemDB,
    ProjectDB,
    ProjectIntegrationDB,
    User,
)
from services.database.repositories import ProjectIntegrationRepository  # noqa: E402
from services.repositories.universal_list_repository import (  # noqa: E402
    UniversalListItemRepository,
)
from services.shared_types import IntegrationType  # noqa: E402

OWNER = str(uuid.uuid4())

_TABLES = [User, ProjectDB, ProjectIntegrationDB, ListDB, ListItemDB]


def _sqlite_schema() -> MetaData:
    """A SQLite-renderable copy of the tables (DDL only). The Postgres-only column
    types (``postgresql.UUID``, ``JSONB``, ``ARRAY``) become String/JSON in the copy;
    nullability, the thing under test, is copied unchanged."""
    md = MetaData()
    for model in _TABLES:
        table = model.__table__.to_metadata(md)
        for col in table.columns:
            if isinstance(col.type, postgresql.UUID):
                col.type = String(36)
            elif isinstance(col.type, (postgresql.JSONB, postgresql.ARRAY)):
                col.type = JSON()
        # Postgres-only server defaults and index expressions don't matter here.
        for col in table.columns:
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


async def _project(session, owner=OWNER, pid="proj-1") -> str:
    session.add(ProjectDB(id=pid, owner_id=owner, name="Alpha", shared_with=[]))
    await session.flush()
    return pid


async def _owner_of_integration(session, iid: str):
    result = await session.execute(
        select(ProjectIntegrationDB.owner_id).where(ProjectIntegrationDB.id == iid)
    )
    return result.scalar_one()


class TestProjectIntegrationOwnerWrite:
    @pytest.mark.asyncio
    async def test_repository_create_writes_the_parent_projects_owner(self, session):
        pid = await _project(session)
        repo = ProjectIntegrationRepository(session)

        created = await repo.create(
            project_id=pid,
            type=IntegrationType.GITHUB,
            name="GitHub",
            config={"repository": "owner/repo"},
        )
        await session.commit()

        owner = await _owner_of_integration(session, created.id)
        assert owner is not None
        assert str(owner) == OWNER

    @pytest.mark.asyncio
    async def test_repository_create_refuses_a_project_with_no_row(self, session):
        repo = ProjectIntegrationRepository(session)
        with pytest.raises(ValueError, match="does not exist or has no owner"):
            await repo.create(
                project_id="missing",
                type=IntegrationType.GITHUB,
                name="GitHub",
                config={"repository": "owner/repo"},
            )

    @pytest.mark.asyncio
    async def test_repository_create_refuses_a_mismatched_owner(self, session):
        pid = await _project(session)
        repo = ProjectIntegrationRepository(session)
        with pytest.raises(ValueError, match="does not match"):
            await repo.create(
                project_id=pid,
                owner_id=str(uuid.uuid4()),
                type=IntegrationType.GITHUB,
                name="GitHub",
                config={"repository": "owner/repo"},
            )

    @pytest.mark.asyncio
    async def test_from_domain_writes_the_owner_it_is_given(self, session):
        pid = await _project(session)
        integration = domain.ProjectIntegration(
            type=IntegrationType.GITHUB, name="GitHub", config={"repository": "o/r"}
        )
        session.add(ProjectIntegrationDB.from_domain(integration, pid, owner_id=OWNER))
        await session.commit()

        assert str(await _owner_of_integration(session, integration.id)) == OWNER

    def test_from_domain_refuses_a_missing_owner(self):
        integration = domain.ProjectIntegration(type=IntegrationType.GITHUB, config={})
        with pytest.raises(ValueError, match="NOT NULL"):
            ProjectIntegrationDB.from_domain(integration, "proj-1", owner_id=None)

    @pytest.mark.asyncio
    async def test_the_model_column_rejects_null(self, session):
        """The model now matches the migrated schema: a NULL owner fails the insert."""
        pid = await _project(session)
        session.add(
            ProjectIntegrationDB(
                id="i-null",
                project_id=pid,
                type=IntegrationType.GITHUB,
                name="GitHub",
                config={},
            )
        )
        with pytest.raises(IntegrityError):
            await session.flush()


class TestListItemOwnerWrite:
    @pytest.mark.asyncio
    async def test_create_item_writes_the_parent_lists_owner(self, session):
        session.add(ListDB(id="list-1", name="Groceries", owner_id=OWNER, item_type="todo"))
        await session.flush()
        repo = UniversalListItemRepository(session)

        created = await repo.create_item(
            domain.ListItem(list_id="list-1", item_id="todo-1", item_type="todo", added_by=OWNER)
        )
        await session.commit()

        result = await session.execute(
            select(ListItemDB.owner_id).where(ListItemDB.id == created.id)
        )
        assert str(result.scalar_one()) == OWNER

    @pytest.mark.asyncio
    async def test_create_item_refuses_a_missing_list(self, session):
        repo = UniversalListItemRepository(session)
        with pytest.raises(ValueError, match="does not exist"):
            await repo.create_item(
                domain.ListItem(list_id="nope", item_id="t", item_type="todo", added_by=OWNER)
            )


class TestDocumentOwnerRequired:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("owner", [None, "not-a-uuid"])
    async def test_upsert_document_refuses_an_unresolvable_owner(self, owner):
        """documents.owner_id is NOT NULL (tier A): the repository names the problem
        before the insert instead of failing at flush."""
        from services.repositories.document_repository import DocumentRepository

        with pytest.raises(ValueError, match="NOT NULL"):
            await DocumentRepository(session=None).upsert_document("pdf_x", owner_id=owner)
