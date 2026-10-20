"""CXO's served words after the 3b7fbb46fb checks (2026-10-20 14:24 memo).

- #2113: the update with no field named asks a question, not an error.
- #2111: a positive not-found names the issue and the repo the read looked in.
- #2112: the floor's calendar sentences (connected: reads with their limits;
  not connected: say so and offer the connection), in the #2100 slot.
- #2118: a chat create applies no default label unless the config names one.
"""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.config.github_config import GitHubConfiguration
from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service import capability_legibility as cl
from services.intent_service.conversational_floor import ConversationalFloor
from services.mcp.consumer.connector import DegradationReason, DegradationResponse
from services.mcp.consumer.github_adapter import GitHubIssueResult
from services.shared_types import IntentCategory

ROUTER = "services.integrations.github.github_integration_router.GitHubIntegrationRouter"
RESOLVER = "services.integrations.github.repo_resolver"
ADAPTER = "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter"
_USER = "3f7b8a52-2113-4b00-9e00-000000002113"


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()


class TestUpdateIssueAsksAQuestion2113:
    @pytest.mark.asyncio
    async def test_no_field_named_asks_what_to_change(self, intent_service):
        intent = Intent(
            category=IntentCategory.QUERY,
            action="update_issue",
            original_message="Update issue #123",
            context={
                "original_message": "Update issue #123",
                "issue_number": 123,
                "repository": "dinp-machine/piper-test-activity",
                "user_id": _USER,
            },
        )
        resolved = SimpleNamespace(full_name="dinp-machine/piper-test-activity")
        with (
            patch(f"{ROUTER}.initialize", new=AsyncMock()),
            patch(f"{ROUTER}.is_available", new=AsyncMock(return_value=True)),
            patch(f"{RESOLVER}.resolve_repo", new=AsyncMock(return_value=resolved)),
        ):
            result = await intent_service._handle_update_issue(intent, "wf-2113", user_id=_USER)
        assert result.clarification_type == "update_fields_required"
        assert result.message == (
            "What would you like to change on #123? I can update the title, the body, "
            "the state, the labels or the assignees."
        )
        assert "Cannot update" not in result.message


class TestNotFoundNamesTheIssueAndRepo2111:
    @pytest.mark.asyncio
    async def test_positive_not_found_line(self, intent_service):
        adapter = MagicMock()
        adapter.get_issue_connector = AsyncMock(
            return_value=GitHubIssueResult(
                degradation=DegradationResponse(
                    reason=DegradationReason.RESOURCE_NOT_FOUND,
                    user_message="That GitHub resource wasn't found.",
                ),
                resolved_repo="dinp-machine/piper-test-activity",
            )
        )
        intent = Intent(
            category=IntentCategory.QUERY,
            action="review_issue_query",
            context={"original_message": "show me issue 999999", "user_id": _USER},
        )
        with patch(ADAPTER, return_value=adapter):
            result = await intent_service._handle_review_issue_query(intent, "wf", session_id="s")
        assert (
            result.message == "I couldn't find issue #999999 in dinp-machine/piper-test-activity."
        )
        assert result.intent_data["degraded"] == "resource_not_found"

    @pytest.mark.asyncio
    async def test_other_degrades_keep_the_connector_line(self, intent_service):
        adapter = MagicMock()
        adapter.get_issue_connector = AsyncMock(
            return_value=GitHubIssueResult(
                degradation=DegradationResponse(
                    reason=DegradationReason.UNREACHABLE,
                    user_message="GitHub's MCP server is unreachable right now.",
                ),
                resolved_repo="o/r",
            )
        )
        intent = Intent(
            category=IntentCategory.QUERY,
            action="review_issue_query",
            context={"original_message": "show me issue 7", "user_id": _USER},
        )
        with patch(ADAPTER, return_value=adapter):
            result = await intent_service._handle_review_issue_query(intent, "wf", session_id="s")
        assert result.message == "GitHub's MCP server is unreachable right now."


class TestCalendarFloorWords2112:
    def test_connected_calendar_renders_reads_with_their_limits(self):
        assert cl.chat_reads_line("calendar") == (
            "I can read your calendar for today, tomorrow or this week, including your "
            "free time. I can't check for conflicts or find a time that works for other "
            "people yet."
        )
        # The claim rests on declared readers that resolve (the #2100 pin's check).
        assert all(cl.reader_symbol_resolves(r.reader) for r in cl.CHAT_READS["calendar"])
        assert cl.chat_reads_line("github").startswith("chat reads ")  # unchanged

    def test_not_connected_calendar_says_so_and_offers_the_connection(self):
        out = ConversationalFloor(llm_client=MagicMock())._format_domain_context(
            {"integrations": [{"name": "calendar", "status": "not_connected"}]}
        )
        assert "- Not connected (available in Settings): Google Calendar" in out
        assert (
            "Your calendar isn't connected, so I can't look at it. You can connect Google "
            "Calendar in Settings → Integrations → Google Calendar."
        ) in out

    def test_connected_calendar_does_not_say_not_connected(self):
        out = ConversationalFloor(llm_client=MagicMock())._format_domain_context(
            {"integrations": [{"name": "calendar", "status": "active"}]}
        )
        assert "isn't connected" not in out
        assert "I can't check for conflicts" in out


class TestNoDefaultLabel2118:
    def test_the_code_default_names_no_label(self):
        assert GitHubConfiguration.create_default().default_labels == []

    def test_the_loader_default_names_no_label(self):
        import importlib
        from pathlib import Path

        mod = importlib.import_module("services.configuration.piper_config_loader")
        src = Path(mod.__file__).read_text()
        assert 'github_section.get("default_labels", [])' in src
        assert '["enhancement"]' not in src
