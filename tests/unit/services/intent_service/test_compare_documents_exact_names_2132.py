"""#2132 — compare_documents: an entry, READ, and it reads only files named exactly.

Arch (2026-10-22 15:05; 10-23 screens 3–4 ruling): "compare these two
documents" resolves only to bound referents. At cutoff 0 the resolver's fuzzy
ambiguity returns its top three, and for compare that would READ guessed files.
So compare binds EXACT NAMES ONLY (``resolve_held_files(..., exact_only=True)``,
the resolver's 0.98 explicit-filename tier); fewer than two named → CXO's line,
no read. The Arch pins run the real ``FileResolver`` over stubbed candidates.
"""

from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.domain.models import Intent
from services.file_context.exceptions import AmbiguousFileReferenceError
from services.file_context.file_resolver import FileResolver
from services.intent_service.workflow_dispatcher import get_action_workflows
from services.intent_service.workflow_entries import (
    NO_TWO_DOCUMENTS_LINE,
    register_default_workflows,
    run_compare_documents_workflow,
)
from services.shared_types import EffectClass, IntentCategory, Outwardness

_USER = "3f7b8a52-2132-4b00-9e00-000000002132"
CXO_COMPARE_LINE = (
    "I need two documents to compare. Name two uploaded files, or paste the text of both here."
)
_HELD = "services.intent_service.document_handlers.resolve_held_files"
_COMPARE = "services.intent_service.document_handlers.handle_compare_documents"


def _compare_intent(message="Compare these two documents"):
    return Intent(
        category=IntentCategory.ANALYSIS,
        action="compare_documents",
        original_message=message,
        context={"original_message": message},
    )


async def _compare(message):
    return await run_compare_documents_workflow(
        session_id="s", user_id=_USER, context={"intent": _compare_intent(message)}
    )


class TestEntry:
    def test_entry_exists_read_private_referent_group(self):
        register_default_workflows()
        entry = get_action_workflows()["compare_documents"]
        assert entry.entry_point is run_compare_documents_workflow
        assert entry.effect == EffectClass.READ
        assert entry.outwardness == Outwardness.PRIVATE
        assert entry.action_triggered is True
        # option (b): a rail entry for the classifier, off the router's grammar
        assert entry.router_visible is False and entry.flip_group is None

    def test_compare_adds_nothing_to_the_router_catalog(self):
        from services.intent_service.inversion_router import derive_routing_grammar

        names = {op.name for op in derive_routing_grammar().operations}
        assert "compare_documents" not in names

    def test_a_hidden_entry_cannot_hold_a_flip_group(self):
        from services.intent_service.workflow_dispatcher import WorkflowEntry

        with pytest.raises(ValueError):
            WorkflowEntry(
                entry_point=run_compare_documents_workflow,
                effect=EffectClass.READ,
                router_visible=False,
                flip_group="read_referent",
            )

    def test_cxo_words_are_exact(self):
        assert NO_TWO_DOCUMENTS_LINE == CXO_COMPARE_LINE


class TestWorkflow:
    @pytest.mark.asyncio
    async def test_two_named_files_are_compared_by_id_and_named(self):
        held = AsyncMock(
            return_value=[
                {"file_id": "a", "filename": "spec-v1.md"},
                {"file_id": "b", "filename": "spec-v2.md"},
            ]
        )
        compare = AsyncMock(
            return_value={
                "file_ids": ["a", "b"],
                "filenames": ["spec-v1.md", "spec-v2.md"],
                "comparison": "v2 adds search.",
            }
        )
        with patch(_HELD, held), patch(_COMPARE, compare):
            result = await _compare("Compare spec-v1.md and spec-v2.md")
        held.assert_awaited_once_with(
            "Compare spec-v1.md and spec-v2.md", _USER, "compare_documents", exact_only=True
        )
        compare.assert_awaited_once_with(["a", "b"], user_id=_USER)
        assert result.message.startswith("I compared 'spec-v1.md', 'spec-v2.md' from your files.")

    @pytest.mark.asyncio
    async def test_a_failed_file_read_is_not_reported_as_no_documents(self):
        with patch(_HELD, AsyncMock(side_effect=RuntimeError("db down"))):
            result = await _compare("Compare these two documents")
        assert result.success is False
        assert result.message != CXO_COMPARE_LINE


# ---------------------------------------------------------------------------
# Arch's pins: the REAL resolver over the user's files; only exact names read
# ---------------------------------------------------------------------------


def _file(file_id, filename, minutes_ago):
    f = MagicMock()
    f.id = file_id
    f.filename = filename
    f.file_type = "text/markdown"
    f.upload_time = datetime.now(timezone.utc)
    f.last_referenced = None
    f.reference_count = 0
    return f


_UPLOADS = [
    _file("f1", "launch-notes.md", 5),
    _file("f2", "roadmap.md", 6),
    _file("f3", "retro.md", 7),
]


class _Scope:
    async def __aenter__(self):
        return MagicMock()

    async def __aexit__(self, *exc):
        return False


def _real_resolver():
    repo = MagicMock()
    repo.get_files_for_session = AsyncMock(return_value=list(_UPLOADS))
    repo.get_recent_files_all_sessions = AsyncMock(return_value=list(_UPLOADS))
    resolver = FileResolver(repo)
    resolver._artifact_candidates = AsyncMock(return_value=[])
    return resolver


async def _compare_with_real_resolver(message):
    from services.intent_service import document_handlers

    resolver = _real_resolver()
    compare = AsyncMock(
        return_value={"file_ids": [], "filenames": ["x", "y"], "comparison": "diff"}
    )
    with (
        patch.object(document_handlers.AsyncSessionFactory, "session_scope", return_value=_Scope()),
        patch("services.file_context.file_resolver.FileResolver", return_value=resolver),
        patch(_COMPARE, compare),
    ):
        result = await _compare(message)
    return result, compare, resolver


@pytest.mark.asyncio
async def test_three_uploads_and_these_two_documents_reads_nothing():
    """The fuzzy path would list (and, for compare, read) its top three."""
    result, compare, resolver = await _compare_with_real_resolver("Compare these two documents")
    assert result.message == CXO_COMPARE_LINE
    compare.assert_not_called()
    with pytest.raises(AmbiguousFileReferenceError):  # what the old binding would have read
        await resolver.resolve_file_reference(_compare_intent("Compare these two documents"), _USER)


@pytest.mark.asyncio
async def test_two_exact_names_are_compared():
    result, compare, _ = await _compare_with_real_resolver(
        "Compare launch-notes.md with roadmap.md"
    )
    compare.assert_awaited_once()
    assert sorted(compare.await_args.args[0]) == ["f1", "f2"]


@pytest.mark.asyncio
async def test_one_exact_name_plus_a_deictic_reads_nothing():
    result, compare, _ = await _compare_with_real_resolver(
        "Compare launch-notes.md with the other one"
    )
    assert result.message == CXO_COMPARE_LINE
    compare.assert_not_called()
