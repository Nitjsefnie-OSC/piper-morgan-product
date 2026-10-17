"""#2066: the OAuth-leg GitHub card carries last_check once a real check is recorded.

Web's served round on d741214b6c: an OAuth-connected account's card had ``last_check: null``
after a passed Test, so the #2045 time line never rendered. The card builder (#2031) returned
the OAuth leg without the health monitor's timestamp; it now carries it the way the generic
path does, and never the startup UNKNOWN stamp (#2044).
"""

from __future__ import annotations

import time
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest

from services.health.integration_health_monitor import ComponentStatus
from web.api.routes import integrations as integrations_routes


def _oauth_credential():
    return SimpleNamespace(leg="oauth", stale_oauth_reason=None)


def _monitor(status, last_check):
    health = SimpleNamespace(status=status, last_check=last_check, last_error=None)
    return SimpleNamespace(get_component_health=lambda _id: health)


METADATA = {"display_name": "GitHub", "configure_url": "/settings/integrations/github"}


@pytest.mark.asyncio
async def test_oauth_card_carries_last_check_after_a_recorded_check():
    checked_at = time.time() - 30
    with (
        patch.object(
            _adapter_cls(),
            "resolve_credential",
            AsyncMock(return_value=_oauth_credential()),
        ),
        patch.object(
            integrations_routes,
            "_get_health_monitor",
            lambda: _monitor(ComponentStatus.HEALTHY, checked_at),
        ),
    ):
        card = await integrations_routes._github_card(METADATA, "user-1")
    assert card is not None
    assert card.status == "healthy"
    assert card.status_message == "Connected with your GitHub account."
    assert card.last_check is not None
    assert card.last_check.startswith("20")  # ISO 8601, UTC


@pytest.mark.asyncio
async def test_oauth_card_has_no_last_check_before_any_real_check():
    with (
        patch.object(
            _adapter_cls(), "resolve_credential", AsyncMock(return_value=_oauth_credential())
        ),
        patch.object(
            integrations_routes,
            "_get_health_monitor",
            lambda: _monitor(ComponentStatus.UNKNOWN, time.time()),
        ),
    ):
        card = await integrations_routes._github_card(METADATA, "user-1")
    assert card is not None
    assert card.status == "healthy"
    assert card.last_check is None


def _adapter_cls():
    from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter

    return GitHubMCPSpatialAdapter
