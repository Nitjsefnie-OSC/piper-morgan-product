"""#2072: a STALE GitHub binding is configured-and-broken, never "not configured".

xian's A1 run on alpha d741214b6c (2026-10-16 18:55 PT): with the OAuth app revoked, the
radar returned ``degraded []`` and the standups read all-clear. #2029 had written STALE
to the binding on GitHub's 401, and ``IntegrationStatusService.get_status`` counted only a
BOUND binding as configured, so ``WorkItemProvider.gather_for_user`` returned
VERIFIED_EMPTY without reading. The same steps passed on 6f2916d10f (#1965) before the
STALE write existed.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import services.integrations.integration_status_service as iss_mod
from services.integrations.integration_status_service import IntegrationStatusService
from services.mcp.consumer.connector import DegradationReason, DegradationResponse
from services.mcp.consumer.github_adapter import GitHubIssuesResult
from services.radar.feed_factory import WorkItemProvider, WorkItemReadKind

STATE = "services.integrations.integration_status_service.github_oauth_binding_state"
CONFIG = "services.integrations.integration_status_service.get_config_status"
HANDLE_READER = "services.integrations.github.repo_resolver.read_user_github_handle"


@pytest.mark.asyncio
@pytest.mark.parametrize("state", ["stale", "unreachable"])
async def test_broken_binding_is_configured_and_unhealthy(state):
    with (
        patch(STATE, AsyncMock(return_value=state)),
        patch(CONFIG, AsyncMock(return_value=("not_configured", None))),
    ):
        status = await IntegrationStatusService().get_status("u1", "github")
    assert status["configured"] is True
    assert status["via"] == "oauth_binding_stale"
    assert status["healthy"] is False
    assert status["last_check"] is None


@pytest.mark.asyncio
async def test_is_configured_true_for_a_stale_binding_so_the_read_is_attempted():
    with (
        patch(STATE, AsyncMock(return_value="stale")),
        patch(CONFIG, AsyncMock(return_value=("not_configured", None))),
    ):
        assert await IntegrationStatusService().is_configured("u1", "github") is True


@pytest.mark.asyncio
async def test_bound_binding_unchanged():
    with patch(STATE, AsyncMock(return_value="bound")):
        status = await IntegrationStatusService().get_status("u1", "github")
    assert (status["configured"], status["via"], status["healthy"]) == (True, "oauth_binding", True)


@pytest.mark.asyncio
async def test_no_binding_falls_through_to_the_credential_paths():
    with (
        patch(STATE, AsyncMock(return_value=None)),
        patch(CONFIG, AsyncMock(return_value=("not_configured", None))),
    ):
        status = await IntegrationStatusService().get_status("u1", "github")
    assert status["configured"] is False and status["via"] is None


@pytest.mark.asyncio
async def test_github_oauth_bound_is_true_only_for_bound():
    with patch(STATE, AsyncMock(return_value="stale")):
        assert await iss_mod.github_oauth_bound("u1") is False
    with patch(STATE, AsyncMock(return_value="bound")):
        assert await iss_mod.github_oauth_bound("u1") is True


@pytest.mark.asyncio
async def test_radar_gather_with_a_stale_binding_is_source_failed_with_stale_token():
    """The served shape: real ``is_configured`` (not patched), binding STALE, the
    router's strict read fails with the resolver's STALE_TOKEN degrade. The outcome
    must be SOURCE_FAILED carrying STALE_TOKEN, never VERIFIED_EMPTY."""
    from services.integrations.github.github_integration_router import GitHubIntegrationRouter
    from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter

    adapter = GitHubMCPSpatialAdapter.__new__(GitHubMCPSpatialAdapter)
    adapter.token_counter = MagicMock()
    adapter._store_github_context = AsyncMock()
    adapter.list_open_issues = AsyncMock(
        return_value=GitHubIssuesResult(
            degradation=DegradationResponse(
                reason=DegradationReason.STALE_TOKEN, user_message="re-authorize"
            )
        )
    )
    router = GitHubIntegrationRouter.__new__(GitHubIntegrationRouter)
    router._initialized = True
    router._user_id = "u1"
    router.mcp_adapter = adapter
    router.spatial_github = None
    router._resolve_default_repo = AsyncMock(return_value=("o", "r"))
    router.initialize = AsyncMock()
    router.close = AsyncMock()
    with (
        patch(STATE, AsyncMock(return_value="stale")),
        patch(CONFIG, AsyncMock(return_value=("not_configured", None))),
        patch(
            "services.integrations.github.github_integration_router.GitHubIntegrationRouter",
            return_value=router,
        ),
        patch(HANDLE_READER, AsyncMock(return_value=None)),
    ):
        outcome = await WorkItemProvider().gather_for_user("u1")
    assert outcome.kind is WorkItemReadKind.SOURCE_FAILED
    assert outcome.reason is DegradationReason.STALE_TOKEN
