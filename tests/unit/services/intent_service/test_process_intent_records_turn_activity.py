"""Every chat turn through IntentService.process_intent is recorded name-free for the
quiet count; the recorder never blocks a turn."""

from unittest.mock import AsyncMock, patch

import pytest

from services.infrastructure import turn_activity
from services.intent.intent_service import IntentProcessingResult, IntentService


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService()


@pytest.mark.asyncio
async def test_a_turn_is_recorded_for_its_principal(intent_service, monkeypatch):
    fresh = turn_activity.TurnActivity()
    monkeypatch.setattr(turn_activity, "TURN_ACTIVITY", fresh)
    with patch.object(
        intent_service,
        "_process_intent_internal",
        new=AsyncMock(
            return_value=IntentProcessingResult(success=True, message="ok", intent_data={})
        ),
    ):
        await intent_service.process_intent("hello", session_id="s-1", user_id="user-q")
    assert fresh.snapshot()["accounts"] == 1
    assert "user-q" not in str(fresh._last_turn_by_account)


@pytest.mark.asyncio
async def test_a_failing_recorder_never_blocks_the_turn(intent_service, monkeypatch):
    class _Broken:
        def record(self, *_a, **_k):
            raise RuntimeError("counter down")

    monkeypatch.setattr(turn_activity, "TURN_ACTIVITY", _Broken())
    with patch.object(
        intent_service,
        "_process_intent_internal",
        new=AsyncMock(
            return_value=IntentProcessingResult(success=True, message="ok", intent_data={})
        ),
    ):
        result = await intent_service.process_intent("hello", session_id="s-2", user_id="user-q")
    assert result.success is True
