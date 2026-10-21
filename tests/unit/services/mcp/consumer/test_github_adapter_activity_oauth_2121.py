"""#2121: the activity read for an OAuth-only account (no native PAT session).

Web on 71b4b15eed: "found 0 commits" while GitHub had five. The REST path was
configured only by a native PAT, so an OAuth account's read answered None. With
the principal threaded, the adapter resolves the account's credential the way
every connector read does and reads with its grant.
"""

from unittest.mock import AsyncMock, patch

import pytest

from services.mcp.consumer.connector import DegradationReason, DegradationResponse
from services.mcp.consumer.github_adapter import GitHubCredential, GitHubMCPSpatialAdapter

GRANT = "services.mcp.consumer.github_adapter.ConnectorGrantStore.get"
SESSION = "services.mcp.consumer.github_adapter.AsyncSessionFactory.session_scope"


def _oauth_credential():
    return GitHubCredential(owner_id="u-1", mcp_server_ref="github", token=None, leg="oauth")


class _Scope:
    async def __aenter__(self):
        return object()

    async def __aexit__(self, *a):
        return False


@pytest.fixture
def adapter():
    a = GitHubMCPSpatialAdapter()
    a._call_github_api = AsyncMock(return_value=[])
    a._rest_configured = lambda: False  # no native PAT session (the OAuth-only account)
    return a


@pytest.mark.asyncio
async def test_oauth_account_reads_with_its_grant(adapter):
    adapter.resolve_credential = AsyncMock(return_value=_oauth_credential())
    with (
        patch(GRANT, new=AsyncMock(return_value="gho_test")),
        patch(SESSION, return_value=_Scope()),
    ):
        result = await adapter.get_recent_activity(7, repository="o/r", user_id="u-1")
    assert "read_failed" not in result
    calls = adapter._call_github_api.await_args_list
    assert len(calls) == 2
    for c in calls:
        assert c.kwargs["headers"] == {"Authorization": "Bearer gho_test"}
    assert calls[0].args[0] == "repos/o/r/commits"


@pytest.mark.asyncio
async def test_pat_leg_uses_the_users_own_token(adapter):
    adapter.resolve_credential = AsyncMock(
        return_value=GitHubCredential(
            owner_id="u-1", mcp_server_ref=None, token="ghp_own", leg="pat"
        )
    )
    result = await adapter.get_recent_activity(7, repository="o/r", user_id="u-1")
    assert "read_failed" not in result
    assert adapter._call_github_api.await_args_list[0].kwargs["headers"] == {
        "Authorization": "Bearer ghp_own"
    }


@pytest.mark.asyncio
async def test_no_credential_is_a_failed_read_never_zero_commits(adapter):
    adapter.resolve_credential = AsyncMock(
        return_value=DegradationResponse(
            reason=DegradationReason.CONNECT_REQUIRED, user_message="connect GitHub"
        )
    )
    result = await adapter.get_recent_activity(7, repository="o/r", user_id="u-1")
    assert result["read_failed"] == [{"error": "no_credential"}]
    adapter._call_github_api.assert_not_awaited()


@pytest.mark.asyncio
async def test_no_principal_keeps_the_pat_session_path(adapter):
    """Callers without a principal (the temporal last-activity read) are unchanged:
    an unconfigured session answers None → read_failed, never a grant lookup."""
    adapter.resolve_credential = AsyncMock()
    adapter._call_github_api = AsyncMock(return_value=None)
    result = await adapter.get_recent_activity(7, repository="o/r")
    adapter.resolve_credential.assert_not_awaited()
    assert result["read_failed"] == [{"error": "no_response"}]
