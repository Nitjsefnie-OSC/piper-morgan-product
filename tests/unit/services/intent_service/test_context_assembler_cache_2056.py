"""#2056 item (2) -- the context assembler's cache does not have the #2054
sharing pattern.  Finding: no fix needed.

``ContextAssembler.cache`` is a ``ContextCache`` (context_cache.py): Redis,
values stored as ``json.dumps`` text and returned as ``json.loads`` of that
text, so no hit can return an object any other caller holds (the #2054 defect
was an in-process dict returned by reference).  Every ``get_or_compute`` key
in the assembler is ``context:<source>:{user_id}``, so a hit cannot cross
users.  These pins hold both properties: fresh objects per hit (including the
miss, whose stored copy is the serialized text), and key scoping by user.
"""

import re
from pathlib import Path

import pytest

from services.intent_service.context_assembler import ContextAssembler
from services.intent_service.context_cache import ContextCache

SRC = Path(__file__).resolve().parents[4] / "services/intent_service/context_assembler.py"


class _FakeRedis:
    def __init__(self):
        self.store = {}

    async def get(self, key):
        return self.store.get(key)

    async def setex(self, key, ttl, payload):
        self.store[key] = payload.encode()


class _FakeFactory:
    client = None

    @classmethod
    async def create_client(cls):
        return cls.client


@pytest.fixture
def cache():
    _FakeFactory.client = _FakeRedis()
    return ContextCache(redis_factory=_FakeFactory)


@pytest.mark.asyncio
async def test_hits_are_fresh_objects_and_mutation_does_not_leak(cache):
    computed = {"pending_todos": [{"t": "a"}]}

    async def fn():
        return computed

    miss = await cache.get_or_compute("context:x:u1", 60, fn)
    miss["pending_todos"].append("MUTATED-AFTER-MISS")
    miss["turn_state"] = "leak"

    hit1 = await cache.get_or_compute("context:x:u1", 60, fn)
    assert hit1 == {"pending_todos": [{"t": "a"}]}
    hit1["pending_todos"][0]["t"] = "MUTATED-ON-HIT"
    hit1["extra"] = 1

    hit2 = await cache.get_or_compute("context:x:u1", 60, fn)
    assert hit2 == {"pending_todos": [{"t": "a"}]}
    assert hit2 is not hit1 and hit2["pending_todos"] is not hit1["pending_todos"]


@pytest.mark.asyncio
async def test_assembler_cache_is_user_scoped(cache):
    asm = ContextAssembler(cache=cache)
    calls = []

    async def fake_compute(user_id):
        calls.append(user_id)
        return {"trust_profile": {"stage": f"stage-of-{user_id}"}}

    asm._compute_trust_context = fake_compute
    a = await asm._gather_trust_context("alice")
    b = await asm._gather_trust_context("bob")
    a2 = await asm._gather_trust_context("alice")
    assert a["trust_profile"]["stage"] == "stage-of-alice"
    assert b["trust_profile"]["stage"] == "stage-of-bob"
    assert a2 == a and a2 is not a
    assert calls == ["alice", "bob"]  # alice's second read was a hit, not bob's data


def test_every_cache_key_in_the_assembler_carries_user_id():
    """Source pin: a new get_or_compute key without {user_id} fails here."""
    text = SRC.read_text()
    keys = re.findall(r"get_or_compute\(\s*key=(f?\"[^\"]+\")", text)
    assert len(keys) >= 10, keys  # the denominator: all keyed call sites seen
    assert text.count("get_or_compute(") == len(keys)
    for k in keys:
        assert k.startswith('f"context:') and k.endswith(':{user_id}"'), k


@pytest.mark.asyncio
async def test_reminder_gate_does_not_mutate_its_input(cache):
    asm = ContextAssembler(cache=cache)
    ctx = {"due_reminders": ["r1"], "reminder_count": 1}
    snapshot = {"due_reminders": ["r1"], "reminder_count": 1}
    name = [n for n in dir(asm) if "gate" in n and "remind" in n]
    assert name, "reminder gate method not found"
    out = await getattr(asm, name[0])(ctx, "u1", "s1")
    assert ctx == snapshot
    assert out is not ctx
