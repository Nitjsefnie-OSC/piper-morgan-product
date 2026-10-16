"""#2054 (Arch, 2026-10-16; ADR-071 D5, ADR-080 D3) — the intent cache holds
classification only, and every hit returns FRESH objects.

Before the fix, ``IntentCache.set`` stored, and ``get`` handed back, the very
dict the returned ``Intent`` held as its ``context``. IntentService then wrote
per-turn state into that dict (the principal ``user_id``, ``secondary_intents``,
``multi_intent_greeting``, ``armed_offer_rail``, ``unclaimed_residue``,
``declined_claims``), so every turn with the same text, from any user, for up
to an hour, shared one mutable object: two interleaved users could read each
other's principal, a caller with no ``user_id`` inherited the last one, and
routing keys rode into later turns.

The pins below drive the real ``IntentClassifier.classify`` /
``classify_multiple`` (LLM stubbed, no network) and then do what
``IntentService.process_intent`` does with the result: stamp the principal
``if user_id`` (intent_service.py, "Added user_id to intent context") and read
it back through the sanctioned ``_principal_from_intent`` accessor.
"""

import asyncio
import json
from typing import Any, Dict, Optional

import pytest

from services.intent.intent_service import _principal_from_intent
from services.intent_service.cache import IntentCache
from services.intent_service.classifier import IntentClassifier

# Not claimed by the pre-classifier (probed 2026-10-16), not a B3 referent,
# not vague: reaches the LLM leg and is cache-eligible.
_LLM_TEXT = "what is the weather on the moon zorbly"
# Claimed by the pre-classifier (greeting) — the other cache writer.
_PRE_TEXT = "good morning"

_PER_TURN_KEYS = (
    "user_id",
    "secondary_intents",
    "multi_intent_greeting",
    "armed_offer_rail",
    "unclaimed_residue",
    "declined_claims",
)


class _StubLLM:
    """Returns one fixed classification; yields to the loop on every call so
    the classification path has a real ``await`` to interleave at."""

    def __init__(self) -> None:
        self.calls = 0

    async def complete(self, **_kwargs: Any) -> str:
        self.calls += 1
        await asyncio.sleep(0)
        return json.dumps(
            {
                "category": "query",
                "action": "search_documents",
                "confidence": 0.9,
                "reasoning": "stub",
            }
        )


@pytest.fixture
def classifier(monkeypatch) -> IntentClassifier:
    from services.configuration import personalization_service as ps_mod

    async def _no_prompt(_user_id: Optional[str]) -> str:
        return ""

    monkeypatch.setattr(
        ps_mod.personalization_service, "resolve_system_prompt_standalone", _no_prompt
    )
    return IntentClassifier(llm_service=_StubLLM())


def _stamp_principal(intent, user_id: Optional[str]) -> None:
    """IntentService.process_intent's host-boundary stamp, verbatim shape."""
    if user_id:
        if intent.context is None:
            intent.context = {}
        intent.context["user_id"] = user_id


def _stamp_routing_state(intent) -> None:
    """The per-turn routing keys IntentService writes after classification."""
    intent.context["multi_intent_greeting"] = True
    intent.context["secondary_intents"] = [{"category": "conversation", "action": "greeting"}]
    intent.context["armed_offer_rail"] = "create_todo"
    intent.context["unclaimed_residue"] = "and also the other thing"
    intent.context["declined_claims"] = ["portfolio_list"]


# ── (1) interleaved same-text turns for different principals ────────────────


class TestInterleavedPrincipals:
    @pytest.mark.parametrize("text", [_LLM_TEXT, _PRE_TEXT])
    async def test_two_users_same_text_each_read_their_own_principal(self, classifier, text):
        """A classifies (miss: the cache is written), stamps A, then awaits;
        B classifies the same text (hit), stamps B; A then reads its
        principal. Pre-fix A read B's id — they shared one context dict."""
        a_stamped = asyncio.Event()
        b_stamped = asyncio.Event()
        seen: Dict[str, Optional[str]] = {}

        async def turn_a() -> None:
            intent = await classifier.classify(text, user_id="user-A", session_id="s-A")
            _stamp_principal(intent, "user-A")
            a_stamped.set()
            await b_stamped.wait()  # the await B's turn interleaves at
            seen["A"] = _principal_from_intent(intent)

        async def turn_b() -> None:
            await a_stamped.wait()
            intent = await classifier.classify(text, user_id="user-B", session_id="s-B")
            _stamp_principal(intent, "user-B")
            b_stamped.set()
            await asyncio.sleep(0)
            seen["B"] = _principal_from_intent(intent)

        await asyncio.wait_for(asyncio.gather(turn_a(), turn_b()), timeout=5)
        assert classifier.cache.hits == 1  # B really was served from the cache
        assert seen == {"A": "user-A", "B": "user-B"}

    async def test_two_users_both_cache_hits_interleaved(self, classifier):
        """Both turns are hits (warm cache) and interleave at an await
        between stamp and read: still each reads its own principal."""
        await classifier.classify(_LLM_TEXT)  # warm
        a_stamped = asyncio.Event()
        b_stamped = asyncio.Event()
        seen: Dict[str, Optional[str]] = {}

        async def turn(uid: str, mine: asyncio.Event, other: asyncio.Event) -> None:
            intent = await classifier.classify(_LLM_TEXT, user_id=uid)
            _stamp_principal(intent, uid)
            mine.set()
            await other.wait()
            seen[uid] = _principal_from_intent(intent)

        await asyncio.wait_for(
            asyncio.gather(
                turn("user-A", a_stamped, b_stamped), turn("user-B", b_stamped, a_stamped)
            ),
            timeout=5,
        )
        assert classifier.cache.hits == 2
        assert seen == {"user-A": "user-A", "user-B": "user-B"}


# ── (2) a hit's context is never the cached object ──────────────────────────


class TestHitReturnsFreshObjects:
    @pytest.mark.parametrize("text", [_LLM_TEXT, _PRE_TEXT])
    async def test_miss_and_hits_hold_distinct_contexts(self, classifier, text):
        first = await classifier.classify(text)  # miss → cache written
        second = await classifier.classify(text)  # hit
        third = await classifier.classify(text)  # hit
        assert classifier.cache.hits == 2
        assert first.context is not second.context
        assert second.context is not third.context
        assert first.context is not third.context

    @pytest.mark.parametrize("text", [_LLM_TEXT, _PRE_TEXT])
    async def test_mutating_a_hit_does_not_change_the_next_hit(self, classifier, text):
        await classifier.classify(text)
        hit = await classifier.classify(text)
        baseline = dict(hit.context)
        hit.context["mutated"] = "yes"
        hit.context["original_message"] = "something else"
        nxt = await classifier.classify(text)
        assert nxt.context == baseline
        assert "mutated" not in nxt.context

    async def test_mutating_the_miss_result_does_not_change_the_cache(self, classifier):
        """The miss path cached the dict the returned Intent still held."""
        first = await classifier.classify(_LLM_TEXT)
        first.context["mutated"] = "yes"
        hit = await classifier.classify(_LLM_TEXT)
        assert "mutated" not in hit.context

    async def test_nested_objects_are_fresh_too(self, classifier):
        """Deep copy: entities / learning_signals / nested context values."""
        await classifier.classify(_LLM_TEXT)
        hit = await classifier.classify(_LLM_TEXT)
        hit.context.setdefault("knowledge_used", []).append("leak")
        hit.learning_signals["leak"] = True  # a dict on the LLM leg
        hit.entities["leak"] = True
        nxt = await classifier.classify(_LLM_TEXT)
        assert "leak" not in nxt.context.get("knowledge_used", [])
        assert "leak" not in nxt.learning_signals
        assert "leak" not in nxt.entities

    def test_intent_cache_set_and_get_copy(self):
        cache = IntentCache(ttl=3600)
        payload = {"category": "query", "action": "x", "context": {"k": [1]}}
        cache.set("hi there", payload)
        payload["context"]["k"].append(2)  # caller mutates after set
        got = cache.get("hi there")
        assert got is not None
        assert got["context"] == {"k": [1]}
        got["context"]["k"].append(3)  # caller mutates after get
        again = cache.get("hi there")
        assert again is not None
        assert again["context"] == {"k": [1]}
        assert got is not again and got["context"] is not again["context"]


# ── (3) per-turn routing keys never ride into the next hit ──────────────────


class TestRoutingStateDoesNotRide:
    @pytest.mark.parametrize("text", [_LLM_TEXT, _PRE_TEXT])
    async def test_routing_keys_from_one_turn_absent_on_next_hit(self, classifier, text):
        first = await classifier.classify(text, user_id="user-A")
        _stamp_principal(first, "user-A")
        _stamp_routing_state(first)
        hit = await classifier.classify(text, user_id="user-B")
        _stamp_principal(hit, "user-B")
        _stamp_routing_state(hit)
        nxt = await classifier.classify(text)
        assert classifier.cache.hits == 2
        for key in _PER_TURN_KEYS:
            assert key not in nxt.context, key

    async def test_classify_multiple_fallback_path_is_fresh(self, classifier):
        """classify_multiple's single-intent fallback goes through classify
        (the production call shape: context=None, user_id/session_id kwargs)."""
        r1 = await classifier.classify_multiple(_LLM_TEXT, user_id="user-A", session_id="s-A")
        i1 = r1.intents[0]
        _stamp_principal(i1, "user-A")
        _stamp_routing_state(i1)
        r2 = await classifier.classify_multiple(_LLM_TEXT, user_id="user-B", session_id="s-B")
        i2 = r2.intents[0]
        assert classifier.cache.hits == 1
        assert i2.context is not i1.context
        for key in _PER_TURN_KEYS:
            assert key not in i2.context, key


# ── (4) no user_id → no inherited principal ─────────────────────────────────


class TestNoInheritedPrincipal:
    @pytest.mark.parametrize("text", [_LLM_TEXT, _PRE_TEXT])
    async def test_caller_without_user_id_reads_no_principal(self, classifier, text):
        first = await classifier.classify(text, user_id="user-A")
        _stamp_principal(first, "user-A")
        anon = await classifier.classify(text)  # hit, no principal on the request
        _stamp_principal(anon, None)  # the stamp runs only `if user_id`
        assert classifier.cache.hits == 1
        assert _principal_from_intent(anon) is None
        assert _principal_from_intent(first) == "user-A"
