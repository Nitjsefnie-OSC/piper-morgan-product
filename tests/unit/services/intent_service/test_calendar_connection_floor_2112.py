"""#2112: a TEMPORAL floor turn knows whether the calendar is connected.

Served (86ee0bbfa1, Web 15:10): "Check my calendar for conflicts" on an account
with no calendar reached the floor, but the floor's context carried no calendar
fact (the temporal summary is {} whether the calendar is empty or absent), so
the model wrote its own guess and never offered the connection. The assembler
now states the connection with CXO's sentence; the floor renders it.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.intent_service import capability_legibility as cl
from services.intent_service.context_assembler import ContextAssembler
from services.intent_service.conversational_floor import ConversationalFloor

STATUS = "services.integrations.integration_status_service.IntegrationStatusService.get_status"


@pytest.mark.asyncio
async def test_not_connected_carries_cxo_sentence():
    with patch(STATUS, new=AsyncMock(return_value={"configured": False, "via": None})):
        conn = await ContextAssembler()._gather_calendar_connection("user-1")
    assert conn["status"] == "not_connected"
    assert conn["line"] == cl.not_connected_line("calendar")
    out = ConversationalFloor(llm_client=MagicMock())._format_domain_context(
        {"calendar_connection": conn}
    )
    assert "Google Calendar is not connected: say \"Your calendar isn't connected" in out
    assert "Settings → Integrations → Google Calendar" in out
    # Arch (16:08): the #2100 never-promise rule needs the reads line on this turn too.
    assert conn["reads"] == cl.chat_reads_line("calendar")
    assert (
        "What chat reads from Google Calendar once it is connected: I can read your calendar" in out
    )
    assert "Never promise more than that." in out


@pytest.mark.asyncio
async def test_connected_carries_reads_with_limits_and_never_says_not_connected():
    with patch(
        STATUS, new=AsyncMock(return_value={"configured": True, "via": "oauth", "healthy": True})
    ):
        conn = await ContextAssembler()._gather_calendar_connection("user-1")
    assert conn["status"] == "active"
    out = ConversationalFloor(llm_client=MagicMock())._format_domain_context(
        {"calendar_connection": conn}
    )
    assert "Google Calendar is connected: I can read your calendar for today" in out
    assert "I can't check for conflicts" in out
    assert "once it is connected" not in out  # the reads line rides only the non-active states
    assert "isn't connected" not in out


@pytest.mark.asyncio
async def test_rejected_grant_renders_needs_reconnecting_not_connected():
    with (
        patch(
            "services.integrations.integration_status_service.needs_reconnecting",
            return_value=True,
        ),
        patch(
            STATUS, new=AsyncMock(return_value={"configured": True, "via": "oauth_binding_stale"})
        ),
    ):
        conn = await ContextAssembler()._gather_calendar_connection("user-1")
    assert conn["status"] == "needs_reconnecting"
    out = ConversationalFloor(llm_client=MagicMock())._format_domain_context(
        {"calendar_connection": conn}
    )
    assert "Google no longer accepts the connection" in out
    assert "Reconnect it in Settings → Integrations → Google Calendar" in out
    assert "Google Calendar is connected:" not in out


@pytest.mark.asyncio
async def test_a_deployment_wide_env_credential_is_not_this_persons_calendar():
    """Arch's check: via "env" (GOOGLE_CALENDAR_CREDENTIALS / MCP_ENABLED set) must not
    render "I can read your calendar…" for every account."""
    with patch(STATUS, new=AsyncMock(return_value={"configured": True, "via": "env"})):
        conn = await ContextAssembler()._gather_calendar_connection("user-1")
    assert conn["status"] == "not_connected"


@pytest.mark.asyncio
async def test_no_principal_or_service_failure_states_nothing():
    assert await ContextAssembler()._gather_calendar_connection(None) == {}
    with patch(STATUS, new=AsyncMock(side_effect=RuntimeError("down"))):
        assert await ContextAssembler()._gather_calendar_connection("user-1") == {}


@pytest.mark.asyncio
async def test_temporal_context_includes_the_connection():
    """The TEMPORAL gather (the path a floored calendar ask takes) carries it."""
    assembler = ContextAssembler()
    with (
        patch.object(assembler, "_gather_calendar_context", new=AsyncMock(return_value={})),
        patch.object(assembler, "_get_pending_todos_cached", new=AsyncMock(return_value={})),
        patch.object(assembler, "_get_completed_todos_cached", new=AsyncMock(return_value={})),
        patch.object(assembler, "_get_projects_cached", new=AsyncMock(return_value={})),
        patch.object(
            assembler, "_gather_active_milestones_context", new=AsyncMock(return_value={})
        ),
        patch.object(assembler, "_gather_recent_activity_context", new=AsyncMock(return_value={})),
        patch(STATUS, new=AsyncMock(return_value={"configured": False})),
    ):
        ctx = await assembler._gather_temporal_context("user-1", None)
    assert ctx["calendar_connection"]["status"] == "not_connected"
