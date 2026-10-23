"""#2132 / #2133 — document asks bind only real referents; batch-from-meeting declines.

Arch (2026-10-22 15:05, 16:24): which handler owns an ask is meaning, routed by
corpus rows and entry descriptions; a handler checks state only. A document
ask resolves in order to (1) a file of the user's the turn binds, (2) a Notion
title the classifier extracted, with the page named, (3) CXO's line. Never the
top hit of a search on the bare message. compare_documents follows the same
rule with two files. Creating several issues from a meeting is a READ decline
in CXO's words; create stays single-issue.

There is no chat-session file list in the product (uploads and artifacts are
owner-scoped and carry no session id), so "bound" means an explicit id or a
name equal to one of the user's file names. These pins run with no LLM and no
database: the DB and analyzer boundaries are stubbed.
"""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import yaml

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service import workflow_entries
from services.intent_service.workflow_dispatcher import get_action_workflows
from services.intent_service.workflow_entries import (
    BATCH_FROM_MEETING_DECLINE,
    NO_TWO_DOCUMENTS_LINE,
    register_default_workflows,
    run_compare_documents_workflow,
    run_decline_batch_issues_from_meeting_workflow,
)
from services.shared_types import EffectClass, IntentCategory, Outwardness

_USER = "3f7b8a52-2132-4b00-9e00-000000002132"
NO_DOC_LINE = "I don't see a document in this chat. Paste the text here and I'll work with it."
CXO_COMPARE_LINE = (
    "I don't see two documents in this chat. Paste the text of both here and I'll compare them."
)
CXO_BATCH_LINE = (
    "I can't create several issues from a meeting yet. Tell me the first action item and "
    "I'll create it."
)
_CORPUS = Path(__file__).parents[4] / "tests" / "fixtures" / "inversion_corpus_phase0.yaml"


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()


def _notion_router():
    r = MagicMock()
    r.is_available.return_value = True
    r.connect_for_user = AsyncMock()
    r.search_notion = AsyncMock(return_value=[{"id": "page-x", "properties": {}}])
    r.get_page = AsyncMock(return_value={"title": "Some Page", "url": "u"})
    r.get_page_blocks = AsyncMock(return_value=[])
    return r


# ---------------------------------------------------------------------------
# 1. analyze_document: a held (bound) file comes before any Notion step
# ---------------------------------------------------------------------------


class TestHeldFileFirst:
    @pytest.mark.asyncio
    async def test_named_held_file_is_read_and_notion_is_not_searched(self, intent_service):
        intent = Intent(
            category=IntentCategory.ANALYSIS,
            action="analyze_document",
            context={
                "original_message": "Analyze q3-plan.pdf",
                "user_id": _USER,
                "filename": "q3-plan.pdf",
            },
        )
        router = _notion_router()
        resolve = AsyncMock(return_value=[{"file_id": "f-1", "filename": "q3-plan.pdf"}])
        analyze = AsyncMock(
            return_value={
                "file_id": "f-1",
                "filename": "q3-plan.pdf",
                "summary": "A plan for Q3.",
                "key_findings": ["Ship the beta"],
                "recommendations": [],
            }
        )
        with (
            patch(
                "services.integrations.notion.notion_integration_router.NotionIntegrationRouter",
                return_value=router,
            ),
            patch("services.intent_service.document_handlers.resolve_bound_files", resolve),
            patch("services.intent_service.document_handlers.handle_analyze_document", analyze),
        ):
            result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")

        router.search_notion.assert_not_called()
        router.get_page.assert_not_called()
        analyze.assert_awaited_once_with("f-1", _USER)
        assert resolve.await_args.kwargs["names"] == ["q3-plan.pdf"]
        assert result.message.startswith("I read 'q3-plan.pdf' from your files.")
        assert "A plan for Q3." in result.message
        assert "Notion" not in result.message

    @pytest.mark.asyncio
    async def test_held_file_wins_even_when_notion_is_not_connected(self, intent_service):
        intent = Intent(
            category=IntentCategory.ANALYSIS,
            action="analyze_document",
            context={"user_id": _USER, "file_id": "f-9"},
        )
        router = _notion_router()
        router.is_available.return_value = False
        with (
            patch(
                "services.integrations.notion.notion_integration_router.NotionIntegrationRouter",
                return_value=router,
            ),
            patch(
                "services.intent_service.document_handlers.resolve_bound_files",
                AsyncMock(return_value=[{"file_id": "f-9", "filename": "notes.md"}]),
            ),
            patch(
                "services.intent_service.document_handlers.handle_analyze_document",
                AsyncMock(return_value={"file_id": "f-9", "filename": "notes.md", "summary": "S"}),
            ),
        ):
            result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")
        assert result.message.startswith("I read 'notes.md' from your files.")
        router.is_available.assert_not_called()

    @pytest.mark.asyncio
    async def test_a_name_that_binds_no_held_file_still_goes_to_the_notion_title_search(
        self, intent_service
    ):
        intent = Intent(
            category=IntentCategory.ANALYSIS,
            action="analyze_document",
            context={"user_id": _USER, "document_title": "Q4 Roadmap"},
        )
        router = _notion_router()
        analyze = AsyncMock()
        with (
            patch(
                "services.integrations.notion.notion_integration_router.NotionIntegrationRouter",
                return_value=router,
            ),
            patch(
                "services.intent_service.document_handlers.resolve_bound_files",
                AsyncMock(return_value=[]),
            ),
            patch("services.intent_service.document_handlers.handle_analyze_document", analyze),
        ):
            result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")
        analyze.assert_not_called()
        assert router.search_notion.await_args.kwargs["query"] == "Q4 Roadmap"
        assert result.message.startswith("I read 'Some Page' in Notion.")

    @pytest.mark.asyncio
    async def test_two_held_files_bearing_the_name_are_listed_and_neither_is_read(
        self, intent_service
    ):
        intent = Intent(
            category=IntentCategory.ANALYSIS,
            action="analyze_document",
            context={"user_id": _USER, "filename": "notes.md"},
        )
        analyze = AsyncMock()
        with (
            patch(
                "services.intent_service.document_handlers.resolve_bound_files",
                AsyncMock(
                    return_value=[
                        {"file_id": "a", "filename": "notes.md"},
                        {"file_id": "b", "filename": "Notes.md"},
                    ]
                ),
            ),
            patch("services.intent_service.document_handlers.handle_analyze_document", analyze),
        ):
            result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")
        analyze.assert_not_called()
        assert "?" not in result.message  # stated, not asked (#1730)
        assert "- notes.md" in result.message and "- Notes.md" in result.message

    @pytest.mark.asyncio
    async def test_deictic_ask_with_nothing_bound_never_touches_the_file_store(
        self, intent_service
    ):
        """No session file list exists, so an unnamed 'this document' binds
        nothing: no file lookup runs, and with Notion connected the reply is
        CXO's line with no search (the 6d726c5221 pin, re-run with a principal)."""
        intent = Intent(
            category=IntentCategory.ANALYSIS,
            action="analyze_document",
            context={"original_message": "Analyze this document", "user_id": _USER},
        )
        router = _notion_router()
        resolve = AsyncMock(return_value=[])
        with (
            patch(
                "services.integrations.notion.notion_integration_router.NotionIntegrationRouter",
                return_value=router,
            ),
            patch("services.intent_service.document_handlers.resolve_bound_files", resolve),
        ):
            result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")
        resolve.assert_not_called()
        router.search_notion.assert_not_called()
        assert result.message == NO_DOC_LINE


# ---------------------------------------------------------------------------
# 1b. The live router's ``title`` arg is the Notion title (served fc183c41bc)
# ---------------------------------------------------------------------------


def _router_intent(message, args):
    ctx = {"original_message": message, "inversion_live": True}
    if args is not None:
        ctx["inversion_args"] = args
    return Intent(
        category=IntentCategory.ANALYSIS,
        action="analyze_document",
        original_message=message,
        context=ctx,
    )


async def _run_with_router(intent_service, intent):
    router = _notion_router()
    router.search_notion = AsyncMock(
        return_value=[
            {
                "id": "page-prd",
                "properties": {
                    "title": {"title": [{"text": {"content": "PRD Writing Guidelines"}}]}
                },
            }
        ]
    )
    router.get_page = AsyncMock(
        return_value={"title": "PRD Writing Guidelines", "url": "https://notion.so/prd"}
    )
    with patch(
        "services.integrations.notion.notion_integration_router.NotionIntegrationRouter",
        return_value=router,
    ):
        result = await intent_service._handle_analyze_document_notion(intent, "wf", "s")
    return router, result


class TestRouterTitleArg:
    @pytest.mark.asyncio
    async def test_router_title_is_searched_and_the_page_is_named(self, intent_service):
        intent = _router_intent(
            "Analyze the document called PRD Writing Guidelines",
            {"title": "PRD Writing Guidelines"},
        )
        router, result = await _run_with_router(intent_service, intent)
        assert router.search_notion.await_args.kwargs["query"] == "PRD Writing Guidelines"
        assert result.message.startswith("I read 'PRD Writing Guidelines' in Notion.")

    @pytest.mark.asyncio
    async def test_no_router_title_gets_cxos_line_and_no_search(self, intent_service):
        router, result = await _run_with_router(
            intent_service, _router_intent("Analyze this document", {})
        )
        router.search_notion.assert_not_called()
        assert result.message == NO_DOC_LINE

    @pytest.mark.asyncio
    @pytest.mark.parametrize("title", ["this document", "it", "the file", "this Notion page"])
    async def test_a_title_that_names_no_document_is_not_searched(self, intent_service, title):
        router, result = await _run_with_router(
            intent_service,
            _router_intent(f"Analyze {title} for me, this Notion page", {"title": title}),
        )
        router.search_notion.assert_not_called()
        assert result.message == NO_DOC_LINE

    @pytest.mark.asyncio
    async def test_a_title_with_words_the_user_did_not_say_is_not_searched(self, intent_service):
        router, result = await _run_with_router(
            intent_service,
            _router_intent("Analyze this document", {"title": "Q4 Roadmap"}),
        )
        router.search_notion.assert_not_called()
        assert result.message == NO_DOC_LINE

    @pytest.mark.asyncio
    async def test_non_string_title_is_ignored(self, intent_service):
        router, result = await _run_with_router(
            intent_service, _router_intent("Analyze this document", {"title": ["x"]})
        )
        router.search_notion.assert_not_called()
        assert result.message == NO_DOC_LINE

    @pytest.mark.asyncio
    async def test_router_title_naming_a_held_file_reads_the_file_not_notion(self, intent_service):
        intent = _router_intent("Analyze q3-plan.pdf", {"title": "q3-plan.pdf"})
        intent.context["user_id"] = _USER
        resolve = AsyncMock(return_value=[{"file_id": "f-1", "filename": "q3-plan.pdf"}])
        with (
            patch("services.intent_service.document_handlers.resolve_bound_files", resolve),
            patch(
                "services.intent_service.document_handlers.handle_analyze_document",
                AsyncMock(
                    return_value={"file_id": "f-1", "filename": "q3-plan.pdf", "summary": "S"}
                ),
            ),
        ):
            router, result = await _run_with_router(intent_service, intent)
        router.search_notion.assert_not_called()
        assert resolve.await_args.kwargs["names"] == ["q3-plan.pdf"]
        assert result.message.startswith("I read 'q3-plan.pdf' from your files.")


# ---------------------------------------------------------------------------
# 2. resolve_bound_files: state only, nothing guessed
# ---------------------------------------------------------------------------


class TestResolveBoundFiles:
    @pytest.mark.asyncio
    async def test_nothing_named_reads_nothing(self):
        from services.intent_service import document_handlers

        with patch.object(document_handlers, "AsyncSessionFactory") as factory:
            assert await document_handlers.resolve_bound_files(_USER) == []
            assert await document_handlers.resolve_bound_files(None, names=["a.md"]) == []
            factory.session_scope_fresh.assert_not_called()


# ---------------------------------------------------------------------------
# 3. compare_documents: an entry, READ, two bound files or CXO's line
# ---------------------------------------------------------------------------


def _compare_intent(**ctx):
    return Intent(
        category=IntentCategory.ANALYSIS,
        action="compare_documents",
        context={"original_message": "Compare these two documents", **ctx},
    )


class TestCompareDocuments:
    def test_entry_exists_read_private_referent_group(self):
        register_default_workflows()
        entry = get_action_workflows()["compare_documents"]
        assert entry.entry_point is run_compare_documents_workflow
        assert entry.effect == EffectClass.READ
        assert entry.outwardness == Outwardness.PRIVATE
        assert entry.action_triggered is True
        assert entry.flip_group == get_action_workflows()["analyze_document"].flip_group

    def test_cxo_words_are_exact(self):
        assert NO_TWO_DOCUMENTS_LINE == CXO_COMPARE_LINE

    @pytest.mark.asyncio
    async def test_nothing_bound_gets_cxos_line_and_no_compare(self):
        compare = AsyncMock()
        with patch("services.intent_service.document_handlers.handle_compare_documents", compare):
            result = await run_compare_documents_workflow(
                session_id="s", user_id=_USER, context={"intent": _compare_intent()}
            )
        assert result.message == CXO_COMPARE_LINE
        compare.assert_not_called()

    @pytest.mark.asyncio
    async def test_one_bound_file_is_fewer_than_two(self):
        compare = AsyncMock()
        with (
            patch(
                "services.intent_service.document_handlers.resolve_bound_files",
                AsyncMock(return_value=[{"file_id": "a", "filename": "a.md"}]),
            ),
            patch("services.intent_service.document_handlers.handle_compare_documents", compare),
        ):
            result = await run_compare_documents_workflow(
                session_id="s",
                user_id=_USER,
                context={"intent": _compare_intent(filenames=["a.md", "b.md"])},
            )
        assert result.message == CXO_COMPARE_LINE
        compare.assert_not_called()

    @pytest.mark.asyncio
    async def test_router_titles_bind_only_words_the_user_said(self):
        resolve = AsyncMock(return_value=[])
        intent = _compare_intent(
            original_message="Compare spec-v1.md with the other one",
            inversion_args={"titles": ["spec-v1.md", "invented.md"]},
        )
        with patch("services.intent_service.document_handlers.resolve_bound_files", resolve):
            result = await run_compare_documents_workflow(
                session_id="s", user_id=_USER, context={"intent": intent}
            )
        assert resolve.await_args.kwargs["names"] == ["spec-v1.md"]
        assert result.message == CXO_COMPARE_LINE

    @pytest.mark.asyncio
    async def test_two_bound_files_are_compared_by_id_and_named(self):
        resolve = AsyncMock(
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
        with (
            patch("services.intent_service.document_handlers.resolve_bound_files", resolve),
            patch("services.intent_service.document_handlers.handle_compare_documents", compare),
        ):
            result = await run_compare_documents_workflow(
                session_id="s",
                user_id=_USER,
                context={"intent": _compare_intent(file_ids=["a", "b"])},
            )
        compare.assert_awaited_once_with(["a", "b"], user_id=_USER)
        assert resolve.await_args.kwargs["uploads_only"] is True
        assert result.message.startswith("I compared 'spec-v1.md', 'spec-v2.md' from your files.")
        assert "v2 adds search." in result.message


# ---------------------------------------------------------------------------
# 4. #2133: the batch-from-meeting READ decline; create stays single-issue
# ---------------------------------------------------------------------------


class TestBatchFromMeetingDecline:
    def test_entry_exists_read_and_flips_only_by_its_own_token(self):
        register_default_workflows()
        entry = get_action_workflows()["decline_batch_issues_from_meeting"]
        assert entry.entry_point is run_decline_batch_issues_from_meeting_workflow
        assert entry.effect == EffectClass.READ
        assert entry.action_triggered is True
        assert entry.flip_group is None

    def test_cxo_words_are_exact(self):
        assert BATCH_FROM_MEETING_DECLINE == CXO_BATCH_LINE

    @pytest.mark.asyncio
    async def test_decline_returns_cxos_words_and_performs_no_write(self):
        svc = MagicMock()
        svc._handle_create_issue = AsyncMock()
        intent = Intent(
            category=IntentCategory.EXECUTION,
            action="decline_batch_issues_from_meeting",
            context={"original_message": "Create issues from this meeting's action items"},
        )
        result = await run_decline_batch_issues_from_meeting_workflow(
            session_id="s", user_id=_USER, context={"intent": intent, "intent_service": svc}
        )
        assert result.message == CXO_BATCH_LINE
        assert result.success is True
        svc._handle_create_issue.assert_not_called()
        # Nothing on the service was touched at all (no create, no router call).
        assert svc.method_calls == []

    def test_create_handler_is_unchanged_single_issue(self):
        """The decline is a separate key; create_ticket still aliases the one
        create_issue WRITE entry (#1412), whose handler takes one subject."""
        register_default_workflows()
        rail = get_action_workflows()
        assert rail["create_ticket"] is rail["create_issue"]
        assert rail["create_issue"].effect == EffectClass.WRITE
        assert rail["create_issue"] is not rail["decline_batch_issues_from_meeting"]
        assert (
            rail["create_issue"].entry_point
            is not workflow_entries.run_decline_batch_issues_from_meeting_workflow
        )


# ---------------------------------------------------------------------------
# 5. analyze_data's description is repository activity only
# ---------------------------------------------------------------------------


def test_analyze_data_description_names_repository_activity_not_documents():
    register_default_workflows()
    rail = get_action_workflows()
    desc = rail["analyze_data"].description
    assert "Repository activity" in desc
    assert "never a document or file" in desc
    assert rail["evaluate_metrics"] is rail["analyze_data"]


# ---------------------------------------------------------------------------
# 6. Corpus rows (the router is taught by rows, never by a handler phrase check)
# ---------------------------------------------------------------------------

_EXPECTED_ROWS = {
    "Analyze this document": "action:analyze_document",
    "Summarize this file": "action:summarize_document",
    "What does this document say?": "action:analyze_document",
    "Compare these two documents": "action:compare_documents",
    "Compare the two files I uploaded": "action:compare_documents",
    "Create issues for all the action items from today's meeting": (
        "action:decline_batch_issues_from_meeting"
    ),
    "Turn the meeting notes into GitHub issues": "action:decline_batch_issues_from_meeting",
    "Make tickets for each action item from the standup": "action:decline_batch_issues_from_meeting",
    "Create issues from this meeting's action items": "action:decline_batch_issues_from_meeting",
    "Create an issue about the login bug": "action:create_issue",
    "Analyze the document called PRD Writing Guidelines": "action:analyze_document",
    "Summarize my Q4 Roadmap doc in Notion": "action:analyze_document",
    "Analyze our repo activity this week": "action:analyze_data",
}
_EXPECTED_ARGS = {
    "Analyze the document called PRD Writing Guidelines": {"title": "PRD Writing Guidelines"},
    "Summarize my Q4 Roadmap doc in Notion": {"title": "Q4 Roadmap"},
}


def test_corpus_carries_the_2132_2133_rows():
    rows = {r["phrase"]: r for r in yaml.safe_load(_CORPUS.read_text())["corpus"]}
    for phrase, expected in _EXPECTED_ROWS.items():
        assert phrase in rows, f"missing corpus row: {phrase!r}"
        assert rows[phrase]["expected"] == expected, phrase
        assert "2132" in rows[phrase]["source"] or "2133" in rows[phrase]["source"], phrase
    for phrase, args in _EXPECTED_ARGS.items():
        assert rows[phrase].get("expected_args") == args, phrase


def test_the_scorer_compares_the_title_arg():
    import importlib.util
    import sys

    path = Path(__file__).parents[4] / "scripts" / "inversion_phase1_shadow_score.py"
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location("_score_2132", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok, _ = mod.args_match({"title": "Q4 Roadmap"}, {"title": "q4 roadmap."})
    assert ok
    ok, note = mod.args_match({"title": "Q4 Roadmap"}, {"title": "Q4 Roadmap doc"})
    assert not ok and note.startswith("title:")
