"""#2117 (CXO): the wizard's key check said "Valid (claude-3.5 access confirmed)".

The model name was a constant in the route, not anything the check reached, so
every invited partner read a confirmation of access that nobody had checked.
The reply now says only what happened: the key was accepted.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from web.api.routes.setup import KEY_ACCEPTED_MESSAGE, ApiKeyValidateRequest, validate_api_key


def _session_scope():
    cm = MagicMock()
    cm.__aenter__ = AsyncMock(return_value=MagicMock())
    cm.__aexit__ = AsyncMock(return_value=False)
    return cm


@pytest.mark.asyncio
@pytest.mark.parametrize("provider", ["anthropic", "openai"])
async def test_an_accepted_key_names_no_model(provider):
    service = MagicMock()
    service.store_user_key = AsyncMock(return_value=None)
    with (
        patch("web.api.routes.setup.UserAPIKeyService", return_value=service),
        patch(
            "web.api.routes.setup.AsyncSessionFactory.session_scope_fresh",
            return_value=_session_scope(),
        ),
    ):
        response = await validate_api_key(
            ApiKeyValidateRequest(provider=provider, api_key="sk-test-not-a-real-key")
        )

    assert response.valid is True
    assert response.message == KEY_ACCEPTED_MESSAGE == "Key accepted."
    assert "claude" not in response.message.lower()
    assert "gpt" not in response.message.lower()
    assert "confirmed" not in response.message.lower()


def test_the_route_module_no_longer_claims_model_access():
    import inspect

    import web.api.routes.setup as setup

    src = inspect.getsource(setup.validate_api_key)
    assert "access confirmed" not in src
