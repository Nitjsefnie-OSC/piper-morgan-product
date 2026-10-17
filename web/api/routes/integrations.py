"""
Integration Health Check API Routes
Issue #530: ALPHA-SETUP-VERIFY - Integration Health Check Dashboard

Provides API endpoints for checking and testing integration health status.
"""

import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import structlog
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from services.auth.auth_middleware import get_current_user
from services.auth.jwt_service import JWTClaims
from services.health.integration_health_monitor import ComponentStatus, IntegrationHealthMonitor

logger = structlog.get_logger()

# Router for integration health endpoints
router = APIRouter(prefix="/api/v1/integrations", tags=["integrations"])


class IntegrationStatus(BaseModel):
    """Status information for a single integration"""

    name: str
    display_name: str
    status: str  # healthy, degraded, failed, connected (#2044: configured, never tested), unknown, not_configured
    status_message: str
    last_check: Optional[str] = None
    error: Optional[str] = None
    fix_suggestion: Optional[str] = None
    configure_url: Optional[str] = None
    can_test: bool = True
    # #2031 (CXO's GitHub card states): a warning glyph before the status line, a
    # second line under it, whether the Test button shows at all, and a card action
    # that replaces the default buttons ("reconnect" → a Reconnect link to
    # ``configure_url``). All optional; other integrations leave them unset.
    status_icon: Optional[str] = None
    status_detail: Optional[str] = None
    show_test: bool = True
    action: Optional[str] = None


class IntegrationHealthResponse(BaseModel):
    """Response model for integration health check"""

    overall_status: str
    timestamp: str
    integrations: List[IntegrationStatus]
    healthy_count: int
    total_count: int


class ConnectionTestResponse(BaseModel):
    """Response model for testing a single connection"""

    integration: str
    success: bool
    message: str
    latency_ms: Optional[float] = None
    error: Optional[str] = None
    fix_suggestion: Optional[str] = None
    # #2037 (ADR-070 B4/B5): the resolver's serving leg ("oauth" | "pat") and, when a
    # personal token is covering for a stale OAuth grant, the degradation reason.
    # GitHub only; None for every other integration. Clients key state on these,
    # never on ``message`` copy.
    leg: Optional[str] = None
    stale_reason: Optional[str] = None


# Integration metadata and error guidance
INTEGRATION_REGISTRY = {
    "notion": {
        "display_name": "Notion",
        "icon": "📝",
        "configure_url": "/settings/integrations/notion",  # Issue #540: Dedicated settings page
        "errors": {
            "api_key_invalid": {
                "message": "Invalid Notion API key",
                "fix": "Check your Notion integration token in Settings → Integrations → Notion",
            },
            "connection_failed": {
                "message": "Cannot connect to Notion API",
                "fix": "Check your internet connection and Notion service status",
            },
            "permission_denied": {
                "message": "Integration lacks required permissions",
                "fix": "Ensure the integration has access to the required databases in Notion",
            },
        },
    },
    "slack": {
        "display_name": "Slack",
        "icon": "💬",
        "configure_url": "/settings/integrations/slack",  # Issue #528: Dedicated settings page
        "errors": {
            "token_expired": {
                "message": "Slack OAuth token has expired",
                "fix": "Re-authorize Slack in Settings → Integrations → Slack",
            },
            "token_invalid": {
                "message": "Invalid Slack token",
                "fix": "Re-connect your Slack workspace",
            },
            "scope_missing": {
                "message": "Missing required Slack permissions",
                "fix": "Re-authorize with updated permissions",
            },
        },
    },
    "github": {
        "display_name": "GitHub",
        "icon": "🐙",
        "configure_url": "/settings/integrations/github",
        "errors": {
            "token_invalid": {
                "message": "Invalid GitHub token",
                "fix": "Update your GitHub personal access token in Settings",
            },
            "rate_limited": {
                "message": "GitHub API rate limit exceeded",
                "fix": "Wait for rate limit reset or use authenticated requests",
            },
            "repo_not_found": {
                "message": "Repository not found or inaccessible",
                "fix": "Check repository permissions and token scope",
            },
            # #2012: the OAuth Test's live probe degrades with the connector taxonomy.
            # #2029: one step — the OAuth callback upserts the grant and sets the binding
            # BOUND over a STALE row, so no Disconnect is needed first.
            "stale_token": {
                "message": "Your GitHub connection needs re-authorizing",
                "fix": "In Settings → Integrations → GitHub, Reconnect with GitHub",
            },
            "connect_required": {
                "message": "GitHub is not connected for your account",
                "fix": "In Settings → Integrations → GitHub, Connect with GitHub",
            },
            "unreachable": {
                "message": "GitHub's MCP server is unreachable right now",
                "fix": "Try again in a few minutes",
            },
        },
    },
    "calendar": {
        "display_name": "Google Calendar",
        "icon": "📅",
        "configure_url": "/settings/integrations/calendar",  # Issue #537: Dedicated settings page
        "errors": {
            "auth_failed": {
                "message": "Calendar authentication failed",
                "fix": "Re-authorize Google Calendar access",
            },
            "mcp_not_running": {
                "message": "Calendar MCP server not running",
                "fix": "Start the Google Calendar MCP server",
            },
        },
    },
}


# #2044 (CXO, 2026-10-15): a card with a connection but no test result reads
# "Connected" with the health line "Not checked yet. Press Test." (a statement plus
# a plain instruction; nothing to arm). "unknown" is internal vocabulary and never
# reaches a configured card. One source for every provider's card; the healthy
# summary does not count an unchecked connection.
UNCHECKED_STATUS = "connected"
UNCHECKED_MESSAGE = "Connected"
UNCHECKED_DETAIL = "Not checked yet. Press Test."
# #2044 (CXO, 19:01): when the health CHECK itself throws, the card says so in plain
# words and offers the retry; the raw error goes to the log, never the card.
CHECK_FAILED_MESSAGE = "Couldn't check this just now. Press Test to try again."


def _unchecked_card(integration_id: str, metadata: Dict[str, Any]) -> "IntegrationStatus":
    """The configured-but-never-tested card (#2044). The health monitor registers
    every component as UNKNOWN with a real ``last_check`` at startup, so "never
    tested" is the UNKNOWN status, not a missing record."""
    return IntegrationStatus(
        name=integration_id,
        display_name=metadata["display_name"],
        status=UNCHECKED_STATUS,
        status_message=UNCHECKED_MESSAGE,
        status_detail=UNCHECKED_DETAIL,
        configure_url=metadata.get("configure_url"),
        can_test=True,
    )


def _get_health_monitor() -> IntegrationHealthMonitor:
    """The shared health monitor singleton.

    #1547: the singleton moved to services/integrations/integration_status_service.py
    (the canonical status source) so chat/floor/standup surfaces see the same cached
    active-test results the /test/* routes record. This delegate keeps the route's
    historical import surface working.
    """
    from services.integrations.integration_status_service import get_health_monitor

    return get_health_monitor()


def _get_error_guidance(integration: str, error_type: str) -> tuple[str, Optional[str]]:
    """Get user-friendly error message and fix suggestion"""
    registry = INTEGRATION_REGISTRY.get(integration, {})
    errors = registry.get("errors", {})
    error_info = errors.get(error_type, {})

    message = error_info.get("message", f"Error: {error_type}")
    fix = error_info.get("fix")

    return message, fix


@router.get("/health", response_model=IntegrationHealthResponse)
async def get_integrations_health(
    current_user: JWTClaims = Depends(get_current_user),
):
    """
    Get health status of all configured integrations.

    Returns status information for Notion, Slack, GitHub, Calendar, etc.
    Issue #530: ALPHA-SETUP-VERIFY

    2026-05-21: Added auth dependency to thread user_id down to per-integration
    config-status checks. Without it, user-scoped credentials in keychain
    (like Slack tokens stored under user_id per ADR-058) are invisible to the
    config-status check and integrations forever appear "Not configured" after
    successful OAuth.
    """
    try:
        integrations = []
        healthy_count = 0

        # Check each integration
        for integration_id, metadata in INTEGRATION_REGISTRY.items():
            integration_status = await _check_integration_health(
                integration_id, metadata, user_id=current_user.sub
            )
            integrations.append(integration_status)
            if integration_status.status == "healthy":
                healthy_count += 1

        # Determine overall status
        total = len(integrations)
        if healthy_count == total:
            overall = "healthy"
        elif healthy_count > 0:
            overall = "degraded"
        else:
            overall = "unhealthy"

        return IntegrationHealthResponse(
            overall_status=overall,
            timestamp=datetime.now(timezone.utc).isoformat(),
            integrations=integrations,
            healthy_count=healthy_count,
            total_count=total,
        )

    except Exception as e:
        logger.error("Failed to check integrations health", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Health check failed: {str(e)}",
        )


@router.post("/test/{integration_name}", response_model=ConnectionTestResponse)
async def check_integration_connection(
    integration_name: str, current_user: JWTClaims = Depends(get_current_user)
):
    """
    Test connection to a specific integration.

    Performs an active health check and returns detailed results.
    Issue #530: ALPHA-SETUP-VERIFY
    """
    if integration_name not in INTEGRATION_REGISTRY:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown integration: {integration_name}",
        )

    metadata = INTEGRATION_REGISTRY[integration_name]
    start_time = time.time()
    health_monitor = _get_health_monitor()

    try:
        result = await _test_integration(integration_name, user_id=current_user.sub)
        latency_ms = (time.time() - start_time) * 1000

        if result["success"]:
            # Record success in health monitor
            health_monitor.record_success(integration_name, latency_ms)
            # #2012: the GitHub Test names its serving leg (CXO's lines); other
            # integrations keep the generic line.
            message = f"{metadata['display_name']} connection successful"
            if integration_name == "github" and result.get("message"):
                message = result["message"]
            # #2037: the structured leg/stale flag rides beside the message (GitHub
            # only; other integrations' results carry neither key, so both stay None).
            return ConnectionTestResponse(
                integration=integration_name,
                success=True,
                message=message,
                latency_ms=round(latency_ms, 2),
                leg=result.get("leg"),
                stale_reason=result.get("stale_oauth_reason"),
            )
        else:
            # Record failure in health monitor
            error_msg = result.get("error", result.get("error_type", "Unknown error"))
            health_monitor.record_failure(integration_name, error_msg)
            message, fix = _get_error_guidance(
                integration_name, result.get("error_type", "unknown")
            )
            return ConnectionTestResponse(
                integration=integration_name,
                success=False,
                message=message,
                latency_ms=round(latency_ms, 2),
                error=result.get("error"),
                fix_suggestion=fix,
            )

    except Exception as e:
        latency_ms = (time.time() - start_time) * 1000
        # Record failure in health monitor
        health_monitor.record_failure(integration_name, str(e))
        logger.error(f"Integration test failed: {integration_name}", error=str(e))
        return ConnectionTestResponse(
            integration=integration_name,
            success=False,
            message=f"Test failed: {str(e)}",
            latency_ms=round(latency_ms, 2),
            error=str(e),
            fix_suggestion="Check logs for details or contact support",
        )


@router.post("/test-all", response_model=List[ConnectionTestResponse])
async def check_all_connections(current_user: JWTClaims = Depends(get_current_user)):
    """
    Test all configured integrations.

    Issue #530: ALPHA-SETUP-VERIFY
    """
    results = []
    for integration_name in INTEGRATION_REGISTRY.keys():
        try:
            result = await check_integration_connection(integration_name, current_user=current_user)
            results.append(result)
        except Exception as e:
            results.append(
                ConnectionTestResponse(
                    integration=integration_name,
                    success=False,
                    message=f"Test failed: {str(e)}",
                    error=str(e),
                )
            )
    return results


# #2031 — CXO's GitHub card words (2026-10-15), verbatim. The card is the third consumer
# of the one credential resolver (ADR-070 B4), after the #2012 Test and #2029's
# Settings → GitHub page; its state comes from ``resolve_credential``, never from
# whether a binding row is BOUND.
_GITHUB_CARD_CONNECTED = "Connected with your GitHub account."
_GITHUB_CARD_PAT_TITLE = "Connected via your personal token"
_GITHUB_CARD_PAT_DETAIL = (
    "Your GitHub connection needs re-authorizing, so I'm not using it right now."
)
_GITHUB_CARD_RECONNECT_TITLE = "Needs reconnecting"
_GITHUB_CARD_RECONNECT_DETAIL = "GitHub no longer accepts your connection."
_GITHUB_CARD_NOT_CONFIGURED = "Not configured"
_WARNING_ICON = "⚠️"


def _recorded_check_iso(integration_id: str) -> Optional[str]:
    """ISO timestamp of the last REAL health check for ``integration_id``, else None (#2066).

    ``register_component`` stamps ``last_check`` at startup with status UNKNOWN, so a
    timestamp alone is not evidence that a check ran; only a non-UNKNOWN status with a
    positive ``last_check`` counts (#2044, m-44).
    """
    component_health = _get_health_monitor().get_component_health(integration_id)
    if not component_health or component_health.last_check <= 0:
        return None
    if component_health.status == ComponentStatus.UNKNOWN:
        return None
    return datetime.fromtimestamp(component_health.last_check, tz=timezone.utc).isoformat()


async def _github_card(
    metadata: Dict[str, Any], user_id: Optional[str]
) -> Optional[IntegrationStatus]:
    """GitHub's Integrations card from the resolver's outcome (#2031, ADR-070 B4/B5).

    - OAuth leg serving → Connected.
    - PAT leg serving with a STALE OAuth grant, and the token answers one read (the
      #2012 Test's probe, the evidence #2029's page uses) → ⚠️ token-serving.
    - Nothing serving with a STALE grant (no token, or a token GitHub also refuses)
      → ⚠️ Needs reconnecting, a Reconnect action, Test hidden.
    - Nothing serving and no stale grant → Not configured.

    The words name the reason (B5), so they are used only where it is STALE_TOKEN.
    Any other resolver outcome (the user's own PAT with no stale grant; a non-stale
    degrade such as UNREACHABLE) returns ``None`` and the generic configured path
    (cached Test result, else "Click 'Test'") governs, as it did before.
    """
    from services.mcp.consumer.connector import DegradationReason, DegradationResponse
    from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter

    def card(**fields: Any) -> IntegrationStatus:
        return IntegrationStatus(
            name="github",
            display_name=metadata["display_name"],
            configure_url=metadata.get("configure_url"),
            **fields,
        )

    not_configured = card(
        status="not_configured", status_message=_GITHUB_CARD_NOT_CONFIGURED, can_test=False
    )
    needs_reconnecting = card(
        status="degraded",
        status_icon=_WARNING_ICON,
        status_message=_GITHUB_CARD_RECONNECT_TITLE,
        status_detail=_GITHUB_CARD_RECONNECT_DETAIL,
        can_test=False,
        show_test=False,
        action="reconnect",
    )
    if not user_id:
        return not_configured

    adapter = GitHubMCPSpatialAdapter()
    credential = await adapter.resolve_credential(user_id)
    if isinstance(credential, DegradationResponse):
        if credential.reason == DegradationReason.STALE_TOKEN:
            return needs_reconnecting
        if credential.reason in (
            DegradationReason.CONNECT_REQUIRED,
            DegradationReason.NOT_CONFIGURED,
        ):
            return not_configured
        return None
    if getattr(credential, "leg", None) == "oauth":
        # #2066: the OAuth-leg card carries the last recorded check like the generic
        # path below does, so the #2045 time line ("Healthy. Checked just now." /
        # "Last checked at …") can render. A real check only: UNKNOWN is the
        # registered-at-startup state (#2044), never a measurement.
        return card(
            status="healthy",
            status_message=_GITHUB_CARD_CONNECTED,
            can_test=True,
            last_check=_recorded_check_iso("github"),
        )
    if getattr(credential, "stale_oauth_reason", None) == DegradationReason.STALE_TOKEN:
        probe = await adapter.search_user_repositories(user_id, limit=1)
        if probe.degradation is not None:
            return needs_reconnecting
        return card(
            status="degraded",
            status_icon=_WARNING_ICON,
            status_message=_GITHUB_CARD_PAT_TITLE,
            status_detail=_GITHUB_CARD_PAT_DETAIL,
            can_test=True,
            # #2053 (CXO): Reconnect in every stale state, beside Test.
            action="reconnect",
        )
    return None


async def _check_integration_health(
    integration_id: str, metadata: Dict[str, Any], user_id: Optional[str] = None
) -> IntegrationStatus:
    """Check health of a specific integration without active testing.

    Args:
        integration_id: integration name (e.g. "slack", "calendar")
        metadata: registry entry from INTEGRATION_REGISTRY
        user_id: authenticated user id (used to look up user-scoped keychain
            credentials per ADR-058; if None, only env-var configuration is
            visible — fine for non-user-scoped integrations).
    """
    try:
        # #2031 (ADR-070 B4): GitHub's card derives from the one credential resolver.
        # A mapped outcome is the card; ``None`` means the user's own token serves with
        # nothing stale, so the configured path below (cached Test result) governs.
        if integration_id == "github":
            github_card = await _github_card(metadata, user_id)
            if github_card is not None:
                return github_card
            config_status = "configured"
        else:
            config_status = await _get_integration_config_status(integration_id, user_id=user_id)

        if config_status == "not_configured":
            return IntegrationStatus(
                name=integration_id,
                display_name=metadata["display_name"],
                status="not_configured",
                status_message="Not configured",
                configure_url=metadata.get("configure_url"),
                can_test=False,
            )

        # Get cached health status from IntegrationHealthMonitor
        health_monitor = _get_health_monitor()
        component_health = health_monitor.get_component_health(integration_id)

        if component_health and component_health.last_check > 0:
            # #2044: UNKNOWN is the registered-at-startup (or reset) state, i.e. no
            # test has ever recorded a result; that is the unchecked card, never
            # "Status: unknown".
            if component_health.status == ComponentStatus.UNKNOWN:
                return _unchecked_card(integration_id, metadata)

            # Map ComponentStatus to our status strings
            status_map = {
                ComponentStatus.HEALTHY: "healthy",
                ComponentStatus.DEGRADED: "degraded",
                ComponentStatus.FAILED: "failed",
                ComponentStatus.UNKNOWN: "unknown",
            }
            status_str = status_map.get(component_health.status, "unknown")

            # Convert timestamp to ISO string
            last_check_dt = datetime.fromtimestamp(component_health.last_check, tz=timezone.utc)
            last_check_str = last_check_dt.isoformat()

            # Build status message based on last check
            if status_str == "healthy":
                # #2049: the page renders the check time from last_check in the viewer's zone.
                status_message = "Healthy"
            elif status_str == "failed":
                status_message = component_health.last_error or "Connection failed"
            else:
                status_message = f"Status: {status_str}"

            return IntegrationStatus(
                name=integration_id,
                display_name=metadata["display_name"],
                status=status_str,
                status_message=status_message,
                last_check=last_check_str,
                error=component_health.last_error,
                configure_url=metadata.get("configure_url"),
                can_test=True,
            )

        # Configured but never tested, and no component registered (#2044).
        return _unchecked_card(integration_id, metadata)

    except Exception as e:
        # #2044: the raw error is logged here; the card carries CXO's line only
        # (``error`` unset, so the page does not redden a line that is not a failure
        # of the integration itself).
        logger.warning(f"Failed to check {integration_id} health", error=str(e))
        return IntegrationStatus(
            name=integration_id,
            display_name=metadata["display_name"],
            status="unknown",
            status_message=CHECK_FAILED_MESSAGE,
            configure_url=metadata.get("configure_url"),
            can_test=True,
        )


async def _get_integration_config_status(integration_id: str, user_id: Optional[str] = None) -> str:
    """Check if an integration is configured (user-scoped stores + env).

    #1547: canonical logic hoisted to
    services/integrations/integration_status_service.py — the #1513 (github
    keychain) / #1337 (notion user-secret store) / #839 (calendar user-scoped
    key) / ADR-058 (slack keychain) composition lives there now. This thin
    delegate preserves the route's historical name and status-string contract.
    """
    from services.integrations.integration_status_service import get_config_status

    status, _via = await get_config_status(integration_id, user_id=user_id)
    return status


async def _test_integration(integration_id: str, user_id: Optional[str] = None) -> Dict[str, Any]:
    """Perform active connection test for an integration"""
    try:
        if integration_id == "notion":
            return await _test_notion(user_id=user_id)
        elif integration_id == "slack":
            return await _test_slack(user_id=user_id)
        elif integration_id == "github":
            return await _test_github(user_id=user_id)
        elif integration_id == "calendar":
            return await _test_calendar(user_id=user_id)
        else:
            return {"success": False, "error": f"Unknown integration: {integration_id}"}

    except Exception as e:
        return {"success": False, "error": str(e), "error_type": "connection_failed"}


async def _test_notion(user_id: Optional[str] = None) -> Dict[str, Any]:
    """Test Notion API connection using stored API key (Issue #562).

    #1436 B16: get_config requires a principal — the acting user's key when
    present, the "system" marker otherwise (the router:157 convention), same
    as the sibling _test_slack/_test_github helpers.
    """
    try:
        import aiohttp

        from services.integrations.notion.config_service import NotionConfigService

        config_service = NotionConfigService()
        config = config_service.get_config(user_id or "system")
        api_key = config.api_key

        if not api_key:
            return {
                "success": False,
                "error": "Notion not connected. Please add your API key.",
                "error_type": "not_configured",
            }

        # Test with users/me endpoint using stored API key
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.notion.com/v1/users/me",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Notion-Version": "2022-06-28",
                },
            ) as response:
                if response.status == 200:
                    return {"success": True}
                else:
                    return {
                        "success": False,
                        "error": "API key invalid or expired",
                        "error_type": "api_key_invalid",
                    }

    except Exception as e:
        return {"success": False, "error": str(e), "error_type": "connection_failed"}


async def _test_slack(user_id: Optional[str] = None) -> Dict[str, Any]:
    """Test Slack API connection using stored OAuth token (Issue #562)"""
    try:
        import aiohttp

        from services.infrastructure.keychain_service import KeychainService

        keychain = KeychainService()
        token = (
            keychain.get_api_key("slack_bot", username=user_id)
            if user_id
            else keychain.get_api_key("slack_bot")
        )  # Issue #849: Correct key name + user-scoped

        if not token:
            return {
                "success": False,
                "error": "Slack not connected. Click Connect to authorize.",
                "error_type": "not_configured",
            }

        # Test with auth.test endpoint using stored OAuth token
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://slack.com/api/auth.test",
                headers={"Authorization": f"Bearer {token}"},
            ) as response:
                data = await response.json()

                if data.get("ok"):
                    return {"success": True}
                else:
                    return {
                        "success": False,
                        "error": data.get("error", "Token invalid or expired"),
                        "error_type": "token_invalid",
                    }

    except Exception as e:
        return {"success": False, "error": str(e), "error_type": "connection_failed"}


_GITHUB_WORKING_OAUTH = "GitHub is working, using your GitHub connection."
_GITHUB_WORKING_PAT = "GitHub is working, using your personal token."
_GITHUB_WORKING_PAT_STALE_OAUTH = (
    "GitHub is working, using your personal token. "
    "Your GitHub connection needs re-authorizing, so I'm not using it right now."
)


def _github_success_line(credential) -> str:
    """CXO's Test-button lines (2026-10-14): name the serving leg; never a plain green
    when only the fallback leg works and the OAuth grant is stale (B3)."""
    if getattr(credential, "leg", None) == "pat":
        if getattr(credential, "stale_oauth_reason", None) is not None:
            return _GITHUB_WORKING_PAT_STALE_OAUTH
        return _GITHUB_WORKING_PAT
    return _GITHUB_WORKING_OAUTH


def _github_failure(degradation) -> Dict[str, Any]:
    """A connector degrade → the Test result; ``error_type`` is the taxonomy value the
    registry's guidance table maps to a message and a fix."""
    from services.mcp.consumer.connector import DegradationReason

    reason = getattr(degradation, "reason", None)
    return {
        "success": False,
        "error": getattr(degradation, "user_message", "") or "GitHub is not reachable.",
        "error_type": reason.value
        if isinstance(reason, DegradationReason)
        else "connection_failed",
    }


async def _test_github(user_id: Optional[str] = None) -> Dict[str, Any]:
    """Test GitHub connection (Issue #562; reshaped for #2012, Arch's Amendment B).

    ONE probe through the adapter for both legs: ``resolve_credential`` picks the leg
    exactly as the reads do (a BOUND binding's grant, else the user's own PAT from
    ``user_api_keys`` then the keychain; never a global token), then one real
    authenticated read (``search_user_repositories``, limit 1) says whether GitHub
    answers. The result names the serving leg and surfaces a stale OAuth grant that a
    working PAT is covering for (B3). A BOUND row alone is not "connected" (a revoked
    grant leaves the row in place; xian, alpha, 2026-10-14), and a missing user is
    not-configured, never a fallback to a global key.
    """
    if not user_id:
        return {
            "success": False,
            "error": "GitHub not connected. Please add your token.",
            "error_type": "not_configured",
        }
    try:
        from services.mcp.consumer.connector import DegradationResponse
        from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter

        adapter = GitHubMCPSpatialAdapter()
        credential = await adapter.resolve_credential(user_id)
        if isinstance(credential, DegradationResponse):
            return _github_failure(credential)
        result = await adapter.search_user_repositories(user_id, limit=1)
        if result.degradation is not None:
            return _github_failure(result.degradation)
        stale = getattr(credential, "stale_oauth_reason", None)
        return {
            "success": True,
            "message": _github_success_line(credential),
            "leg": getattr(credential, "leg", None),
            "stale_oauth_reason": getattr(stale, "value", stale),
        }
    except Exception as e:
        return {"success": False, "error": str(e), "error_type": "connection_failed"}


async def _test_calendar(user_id: Optional[str] = None) -> Dict[str, Any]:
    """Test Google Calendar OAuth connection (Issue #539)"""
    try:
        from services.infrastructure.keychain_service import KeychainService
        from services.integrations.calendar.oauth_handler import GoogleCalendarOAuthHandler

        keychain = KeychainService()
        # Issue #839: Use user-scoped key when user_id available
        key_name = f"google_calendar_{user_id}" if user_id else "google_calendar"
        refresh_token = keychain.get_api_key(key_name)

        if not refresh_token:
            return {
                "success": False,
                "error": "Calendar not connected. Click Connect to authorize.",
                "error_type": "not_configured",
            }

        # Validate by attempting to refresh the token (Issue #539)
        handler = GoogleCalendarOAuthHandler()
        tokens = await handler.refresh_access_token(refresh_token)

        if tokens:
            return {"success": True}
        else:
            return {
                "success": False,
                "error": "Token expired or revoked. Please reconnect.",
                "error_type": "token_invalid",
            }

    except ImportError:
        return {"success": False, "error": "Calendar integration not available"}
    except Exception as e:
        return {"success": False, "error": str(e), "error_type": "connection_failed"}
