"""#2127 — selection never leaves the request's binding.

Served on alpha (ded184e4ad, 2026-10-22): an account holding only an OpenAI key
asked "What should I focus on today?" and was told to add a key. Alpha's log
(PA, read-only): "Default provider openai not available, using anthropic", then
``request_spend_key('anthropic')`` refused. Two causes, both needed:

1. ``get_configured_providers`` counted the server's env ``ANTHROPIC_API_KEY``
   (``get_api_key`` step 2), which no turn can spend since #1812.
2. With no per-user consent list, the user inherited the server/global list.

Arch's ruling (15:28 and 15:30): availability is the providers THIS request bound,
intersected with consent; an authenticated user's consent never comes from the
global slot. These are Arch's four pins.
"""

from typing import Dict, Optional, Tuple

import pytest

from services.config.llm_config_service import LLMConfigService
from services.llm.provider_selection import CONSENT_SLOT, DEFAULT_SLOT, resolve_authorized_providers
from services.llm.request_key import (
    ConsentUnreadableError,
    UnboundLLMKeyError,
    request_api_key,
    request_spend_key,
)

USER = "user-openai-only"


class _DictKeychain:
    """Primitive-path stand-in: a ``(slot, username)`` dict. ``fail_user`` raises
    on that user's consent read, the shape a broken store presents."""

    def __init__(self, slots: Dict[Tuple[str, Optional[str]], str], fail_user=None):
        self.slots = slots
        self.fail_user = fail_user
        self.reads = []

    def get_api_key(self, name, username=None):
        self.reads.append((name, username))
        if name == CONSENT_SLOT and username is not None and username == self.fail_user:
            raise RuntimeError("keyring backend unavailable")
        return self.slots.get((name, username))


@pytest.fixture
def server_env(monkeypatch):
    # Alpha's shape: one server provider variable, anthropic. The env default is
    # set to anthropic too, so a server preference cannot win either.
    for var in ("OPENAI_API_KEY", "GEMINI_API_KEY", "PERPLEXITY_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-server-env-not-spendable")
    monkeypatch.setenv("PIPER_DEFAULT_PROVIDER", "anthropic")
    monkeypatch.delenv("PIPER_EXCLUDED_PROVIDERS", raising=False)


def _global(consent="anthropic", default="anthropic"):
    return {(CONSENT_SLOT, None): consent, (DEFAULT_SLOT, None): default}


def test_openai_only_user_with_no_list_gets_openai_despite_env_and_global(server_env):
    kc = _DictKeychain(_global(consent="anthropic"))
    svc = LLMConfigService(keychain_service=kc)
    with request_api_key({"openai": "sk-user-openai"}):
        assert svc.get_available_providers(USER) == ["openai"]
        assert svc.get_default_provider(USER) == "openai"
        assert request_spend_key("openai") == "sk-user-openai"
    # The global consent slot was never consulted for this authenticated user.
    assert (CONSENT_SLOT, None) not in kc.reads


def test_per_user_list_naming_both_still_selects_only_the_bound_provider(server_env):
    slots = _global(consent="anthropic")
    slots[(CONSENT_SLOT, USER)] = "anthropic,openai"
    svc = LLMConfigService(keychain_service=_DictKeychain(slots))
    with request_api_key({"openai": "sk-user-openai"}):
        assert svc.get_available_providers(USER) == ["openai"]
        assert svc.get_default_provider(USER) == "openai"


def test_failed_per_user_consent_read_refuses_and_never_falls_to_global(server_env):
    kc = _DictKeychain(_global(consent="anthropic,openai"), fail_user=USER)
    svc = LLMConfigService(keychain_service=kc)
    with request_api_key({"openai": "sk-user-openai"}):
        with pytest.raises(ConsentUnreadableError):
            svc.get_available_providers(USER)
    assert (CONSENT_SLOT, None) not in kc.reads


def test_no_principal_reads_the_global_slot_and_spend_still_refuses(server_env):
    kc = _DictKeychain(_global(consent="anthropic"))
    assert resolve_authorized_providers(None, ["anthropic", "openai"], keychain=kc) == ["anthropic"]
    assert (CONSENT_SLOT, None) in kc.reads
    # Nothing bound: availability is empty and spend refuses, env key or not.
    svc = LLMConfigService(keychain_service=kc)
    assert svc.get_available_providers(None) == []
    with pytest.raises(ValueError):
        svc.get_default_provider(None)
    with pytest.raises(UnboundLLMKeyError):
        request_spend_key("anthropic")


def test_server_key_listing_is_operator_only(server_env):
    # The CLI listing and startup validation describe the server's own keys.
    svc = LLMConfigService(keychain_service=_DictKeychain({}))
    assert svc.get_configured_providers(include_server_keys=True) == ["anthropic"]
    assert svc.get_configured_providers() == []
