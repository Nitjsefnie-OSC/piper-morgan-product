"""#2012 — the Integration Health "Test" for a GitHub OAuth binding makes ONE real call.

A BOUND binding row survives a revoked or expired grant, so "bound → success" told the user
GitHub worked while every read failed (xian, alpha, 2026-10-14). Now the Test probes through
the same resolver the reads use (``search_user_repositories``, limit 1) and maps the degrade:
STALE_TOKEN → a failed test with a reconnect fix; a live grant → pass.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from services.mcp.consumer.connector import DegradationReason, DegradationResponse
from services.mcp.consumer.github_adapter import GitHubReposResult
from web.api.routes import integrations

pytestmark = pytest.mark.asyncio


def _degraded(reason: DegradationReason, message: str) -> GitHubReposResult:
    return GitHubReposResult(
        degradation=DegradationResponse(reason=reason, user_message=message, action_hint=None)
    )


async def test_revoked_grant_fails_the_test_with_a_reconnect_fix():
    probe = AsyncMock(return_value=_degraded(DegradationReason.STALE_TOKEN, "needs re-auth"))
    with (
        patch.object(integrations, "_github_oauth_bound", new=AsyncMock(return_value=True)),
        patch(
            "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter.search_user_repositories",
            new=probe,
        ),
    ):
        result = await integrations._test_github(user_id="u1")
    assert result["success"] is False
    assert result["error_type"] == "stale_token"
    probe.assert_awaited_once()
    message, fix = integrations._get_error_guidance("github", result["error_type"])
    assert "re-authoriz" in message
    assert "Connect with GitHub" in fix


async def test_live_grant_passes_after_a_real_call():
    probe = AsyncMock(return_value=GitHubReposResult(repositories=[{"full_name": "o/r"}]))
    with (
        patch.object(integrations, "_github_oauth_bound", new=AsyncMock(return_value=True)),
        patch(
            "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter.search_user_repositories",
            new=probe,
        ),
    ):
        result = await integrations._test_github(user_id="u1")
    assert result["success"] is True
    assert "OAuth" in result["message"]
    probe.assert_awaited_once()


async def test_server_down_reads_unreachable_not_connected():
    probe = AsyncMock(return_value=_degraded(DegradationReason.UNREACHABLE, "server down"))
    with (
        patch.object(integrations, "_github_oauth_bound", new=AsyncMock(return_value=True)),
        patch(
            "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter.search_user_repositories",
            new=probe,
        ),
    ):
        result = await integrations._test_github(user_id="u1")
    assert result["success"] is False
    assert result["error_type"] == "unreachable"
