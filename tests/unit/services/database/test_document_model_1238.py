"""#1238 (ADR-071 P2) — DocumentDB model: relational anchor for the ChromaDB doc store.

The doc store (`pm_knowledge` ChromaDB collection) is ChromaDB-only — no relational
row backs each document. This table is the canonical owner-anchored row ADR-071 D2
mandates (Arch ruling 2026-06-16: marker on the DB row, NOT ChromaDB metadata).

Verifies the schema contract: `chromadb_base_id` link, `owner_id` provenance
(CrossDialectUUID round-trip), `is_global_pm_domain` D1-exemption marker (defaults
false), title/source, TimestampMixin. In-memory SQLite (#1035 pattern).
"""

from __future__ import annotations

import uuid

import pytest
import pytest_asyncio

aiosqlite = pytest.importorskip("aiosqlite")

from sqlalchemy import select  # noqa: E402
from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from services.database.models import DocumentDB  # noqa: E402

pytestmark = pytest.mark.asyncio

_OWNER = "a25db09c-6d79-41e4-8d82-87b6a005bbb0"  # configured PM (xian)


@pytest_asyncio.fixture
async def session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(lambda c: DocumentDB.__table__.create(c, checkfirst=True))
    SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with SessionLocal() as s:
        yield s
    await engine.dispose()


class TestDocumentModel1238:
    async def test_insert_and_read_back(self, session):
        doc = DocumentDB(
            chromadb_base_id="pdf_88388894",
            owner_id=uuid.UUID(_OWNER),
            is_global_pm_domain=True,
            title="chapter.pdf",
            source="/tests/fixtures/chapter.pdf",
        )
        session.add(doc)
        await session.commit()
        row = (await session.execute(select(DocumentDB))).scalar_one()
        assert row.chromadb_base_id == "pdf_88388894"
        assert str(row.owner_id) == _OWNER  # CrossDialectUUID round-trips on SQLite
        assert row.is_global_pm_domain is True
        assert row.title == "chapter.pdf"
        assert row.source == "/tests/fixtures/chapter.pdf"
        assert row.created_at is not None  # TimestampMixin
        assert row.id is not None  # UUID PK default

    async def test_is_global_pm_domain_defaults_false(self, session):
        # Omitting the marker: it defaults False (not global).
        doc = DocumentDB(chromadb_base_id="pdf_local", owner_id=uuid.UUID(_OWNER))
        session.add(doc)
        await session.commit()
        row = (await session.execute(select(DocumentDB))).scalar_one()
        assert row.is_global_pm_domain is False

    async def test_owner_id_is_not_null(self, session):
        # 2009: owner_id is the scoping column (tier A); a row without an owner is
        # an orphan, so the insert fails rather than storing NULL (was m-40 nullable).
        from sqlalchemy.exc import IntegrityError

        session.add(DocumentDB(chromadb_base_id="pdf_no_owner"))
        with pytest.raises(IntegrityError):
            await session.commit()
        await session.rollback()

    async def test_chromadb_base_id_unique(self, session):
        owner = uuid.UUID(_OWNER)
        session.add(DocumentDB(chromadb_base_id="dup", owner_id=owner))
        await session.commit()
        session.add(DocumentDB(chromadb_base_id="dup", owner_id=owner))
        with pytest.raises(Exception):  # IntegrityError — unique constraint
            await session.commit()
        await session.rollback()
