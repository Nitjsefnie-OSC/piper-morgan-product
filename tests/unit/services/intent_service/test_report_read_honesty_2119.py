"""#2119: 'Generate a status report' answered 'Generated commit_analysis report … 0 commits'.

CXO's words (16:05): with a read, "I looked at <repo> for <window> and found N
commits"; with none, say so. Never an internal type name. The adapter marks a
failed read (`read_failed`) so the handler can tell it from an empty window.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.shared_types import IntentCategory

EMPTY = {"commits": [], "prs": [], "issues_created": [], "issues_closed": []}


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()


def _intent() -> Intent:
    return Intent(
        category=IntentCategory.ANALYSIS,
        action="generate_report",
        original_message="Generate a status report",
        context={"original_message": "Generate a status report", "user_id": "u-2119"},
    )


async def _run(intent_service, activity):
    domain = MagicMock()
    domain._github_agent.get_recent_activity = AsyncMock(return_value=activity)
    with (
        patch("services.domain.github_domain_service.GitHubDomainService", return_value=domain),
        patch.object(
            intent_service,
            "_resolve_analysis_repository",
            new=AsyncMock(return_value=("dinp-machine/piper-test-activity", None)),
        ),
    ):
        return await intent_service._handle_generate_report(_intent(), "wf-2119")


@pytest.mark.asyncio
async def test_the_read_carries_the_principal(intent_service):
    """#2121: the handler threads the principal so an OAuth-only account reads with its grant."""
    domain = MagicMock()
    domain._github_agent.get_recent_activity = AsyncMock(return_value=dict(EMPTY))
    with (
        patch("services.domain.github_domain_service.GitHubDomainService", return_value=domain),
        patch.object(
            intent_service,
            "_resolve_analysis_repository",
            new=AsyncMock(return_value=("dinp-machine/piper-test-activity", None)),
        ),
    ):
        await intent_service._handle_generate_report(_intent(), "wf-2121")
    assert domain._github_agent.get_recent_activity.await_args.kwargs["user_id"] == "u-2119"


@pytest.mark.asyncio
async def test_a_real_empty_window_says_it_looked_and_found_none(intent_service):
    result = await _run(intent_service, dict(EMPTY))
    # CXO 10-22 (Q19): say what it did and didn't do
    assert result.message == (
        "I can't write a full status report yet. What I found: 0 commits in the last 7 days "
        "in dinp-machine/piper-test-activity."
    )
    assert "commit_analysis" not in result.message
    assert "Generated" not in result.message


@pytest.mark.asyncio
async def test_a_failed_read_never_claims_a_count(intent_service):
    failed = dict(EMPTY, read_failed=[{"error": "RuntimeError"}])
    result = await _run(intent_service, failed)
    assert "found 0 commits" not in result.message
    assert (
        "I couldn't read dinp-machine/piper-test-activity with this account's GitHub connection"
        in result.message
    )


@pytest.mark.asyncio
async def test_a_none_rest_answer_is_a_failed_read_not_zero_commits(intent_service):
    """Web, 71b4b15eed: an OAuth-only account (no native PAT for the REST path) got
    "found 0 commits" while GitHub had five. The adapter's None now marks the read."""
    failed = dict(EMPTY, read_failed=[{"error": "no_response"}])
    result = await _run(intent_service, failed)
    assert "0 commits" not in result.message
