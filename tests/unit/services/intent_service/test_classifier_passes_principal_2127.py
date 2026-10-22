"""#2127: the classifier's LLM call carries the acting principal, so the provider resolves
to the user's own key (#1415). Without it the client resolved the server default
(anthropic) and #1815/#1819 refused an OpenAI-only account's turn (PA's run, Q21:
"That needs an LLM key of your own").
"""

import json
from unittest.mock import AsyncMock, patch

import pytest

from services.intent_service.classifier import IntentClassifier


def _llm_json():
    return json.dumps(
        {"category": "synthesis", "action": "free_form_action", "confidence": 0.9, "reasoning": "r"}
    )


@pytest.mark.asyncio
async def test_the_classification_call_carries_the_acting_principal():
    clf = IntentClassifier()
    with (
        patch.object(clf, "_llm", create=True),
        patch(
            "services.configuration.personalization_service.personalization_service"
            ".resolve_system_prompt_standalone",
            new=AsyncMock(return_value="sys"),
        ),
    ):
        clf._llm = AsyncMock()
        clf._llm.complete = AsyncMock(return_value=_llm_json())
        complete = clf._llm.complete  # the patch restores _llm on exit; keep the mock
        await clf._classify_with_reasoning(
            "What should I focus on today?", user_id="user-openai-only"
        )
    kwargs = complete.await_args.kwargs
    assert kwargs["task_type"] == "intent_classification"
    assert kwargs["user_id"] == "user-openai-only"


@pytest.mark.asyncio
async def test_an_anonymous_turn_still_passes_none_not_a_made_up_principal():
    clf = IntentClassifier()
    with (
        patch.object(clf, "_llm", create=True),
        patch(
            "services.configuration.personalization_service.personalization_service"
            ".resolve_system_prompt_standalone",
            new=AsyncMock(return_value="sys"),
        ),
    ):
        clf._llm = AsyncMock()
        clf._llm.complete = AsyncMock(return_value=_llm_json())
        complete = clf._llm.complete
        await clf._classify_with_reasoning("hello")
    assert complete.await_args.kwargs["user_id"] is None
