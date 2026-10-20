"""#2114: "Show me that issue." right after a create reads back the issue just created.

Served (alpha 54a5ba990f, scenario A4): turn 3 "Created issue #22 … in
dinp-machine/piper-test-activity.", turn 4 "Show me that issue." → "I couldn't
find an issue number in your request." The number was in the reply before it and
in the session's creation ledger (#2095). The one-issue read now resolves a
missing number from the owner-scoped ledger head before asking, repo included.
No new extraction regex: the referent comes from the session record.
"""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.workflow_entries import _READ_QUERY_SESSION_THREADED
from services.shared_types import IntentCategory

LEDGER = "services.intent_service.session_activity_read.list_session_activities"
ADAPTER = "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter"


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()


def _intent(message: str, user_id: str | None = "user-1") -> Intent:
    ctx = {"original_message": message}
    if user_id:
        ctx["user_id"] = user_id
    return Intent(category=IntentCategory.QUERY, action="review_issue_query", context=ctx)


def _row(action_type: str, target_ref: str) -> SimpleNamespace:
    return SimpleNamespace(action_type=action_type, target_ref=target_ref, target_title=None)


def _adapter_returning(item):
    adapter = MagicMock()
    adapter.get_issue_connector = AsyncMock(
        return_value=SimpleNamespace(item=item, degradation=None)
    )
    return adapter


ISSUE_22 = {
    "number": 22,
    "title": "Add search to the main navigation bar",
    "state": "open",
    "labels": [],
    "body": "",
    "html_url": "https://github.com/dinp-machine/piper-test-activity/issues/22",
}


class TestReferentFromTheLedger:
    @pytest.mark.asyncio
    async def test_no_number_reads_the_issue_this_session_created(self, intent_service):
        """The scenario-A4 turn: the ledger head (repo + number) feeds the connector read."""
        rows = [_row("issue_created", "dinp-machine/piper-test-activity#22")]
        adapter = _adapter_returning(ISSUE_22)
        with patch(LEDGER, new=AsyncMock(return_value=rows)), patch(ADAPTER, return_value=adapter):
            result = await intent_service._handle_review_issue_query(
                _intent("Show me that issue."), "wf", session_id="sess-1"
            )

        adapter.get_issue_connector.assert_awaited_once_with(
            "user-1", issue_number=22, explicit_repo="dinp-machine/piper-test-activity"
        )
        assert result.requires_clarification is False
        assert "#22" in result.message
        assert "Add search to the main navigation bar" in result.message

    @pytest.mark.asyncio
    async def test_newest_issue_wins_over_older_creates_and_other_kinds(self, intent_service):
        rows = [
            _row("todo_created", "todo:9"),
            _row("issue_created", "dinp-machine/piper-test-activity#23"),
            _row("issue_created", "dinp-machine/piper-test-activity#22"),
        ]
        adapter = _adapter_returning({**ISSUE_22, "number": 23, "title": "Newer"})
        with patch(LEDGER, new=AsyncMock(return_value=rows)), patch(ADAPTER, return_value=adapter):
            await intent_service._handle_review_issue_query(
                _intent("show me the issue"), "wf", session_id="sess-1"
            )
        assert adapter.get_issue_connector.await_args.kwargs["issue_number"] == 23

    @pytest.mark.asyncio
    async def test_an_explicit_number_still_wins_and_never_reads_the_ledger(self, intent_service):
        ledger = AsyncMock(return_value=[_row("issue_created", "o/r#22")])
        adapter = _adapter_returning({**ISSUE_22, "number": 7, "title": "Seven"})
        with patch(LEDGER, new=ledger), patch(ADAPTER, return_value=adapter):
            await intent_service._handle_review_issue_query(
                _intent("show me issue #7 in acme/widgets"), "wf", session_id="sess-1"
            )
        ledger.assert_not_awaited()
        adapter.get_issue_connector.assert_awaited_once_with(
            "user-1", issue_number=7, explicit_repo="acme/widgets"
        )


class TestTheAskStaysWhenThereIsNothingToResolve:
    @pytest.mark.asyncio
    async def test_empty_ledger_asks_for_a_number(self, intent_service):
        adapter = _adapter_returning(ISSUE_22)
        with patch(LEDGER, new=AsyncMock(return_value=[])), patch(ADAPTER, return_value=adapter):
            result = await intent_service._handle_review_issue_query(
                _intent("Show me that issue."), "wf", session_id="sess-1"
            )
        assert result.requires_clarification is True
        assert "issue number" in result.message
        adapter.get_issue_connector.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_ledger_read_failure_degrades_to_the_ask(self, intent_service):
        with patch(LEDGER, new=AsyncMock(side_effect=RuntimeError("db down"))):
            result = await intent_service._handle_review_issue_query(
                _intent("Show me that issue."), "wf", session_id="sess-1"
            )
        assert result.requires_clarification is True

    @pytest.mark.asyncio
    async def test_no_principal_or_no_session_never_reads_the_ledger(self, intent_service):
        """D1a: an owner-less or session-less read is not a read at all."""
        ledger = AsyncMock(return_value=[_row("issue_created", "o/r#22")])
        with patch(LEDGER, new=ledger):
            r1 = await intent_service._handle_review_issue_query(
                _intent("Show me that issue.", user_id=None), "wf", session_id="sess-1"
            )
            r2 = await intent_service._handle_review_issue_query(
                _intent("Show me that issue."), "wf", session_id=None
            )
        ledger.assert_not_awaited()
        assert r1.requires_clarification is True and r2.requires_clarification is True


def test_the_factory_threads_session_id_to_the_one_issue_read():
    """The rail passes session_id only to members of this set; the handler needs it."""
    assert "_handle_review_issue_query" in _READ_QUERY_SESSION_THREADED
