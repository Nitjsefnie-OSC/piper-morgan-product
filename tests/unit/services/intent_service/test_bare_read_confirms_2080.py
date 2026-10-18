"""#2080: a bare name the router reads as a question must not kill the offer chain.

Served (xian, alpha 118241587e, 2026-10-17): "list my projects" → offer → "yes" →
"What would you like to call it?" → "Piper Morgan" → the router read the bare
reply as ``get_identity`` ×6 @0.95, the armed name turn RELEASED it as a
competing command, the offer was dropped, the floor improvised "Got it — want me
to create a project called Piper Morgan?" (nothing armed), and "Yes" created
nothing. Arch's ruling (2026-10-17), both halves:

1. **Carrier-local bare-read CONFIRM.** ``classify_armed_reply`` gains
   ``confirm_bare_reads`` (default False, byte-identical for every other
   caller). When True, an at-threshold operation whose registered
   ``WorkflowEntry.effect`` is READ and whose decision carries NO args CONFIRMs
   instead of RELEASEing. Derived from the registry, never a hand list. A READ
   with args, any WRITE, sub-threshold and CLARIFY are unchanged. Only
   ``add_project_clarify`` passes True.
2. **The #1855 seam catches the improvised offer.** Diagnosis: the sentence was
   never DETECTED (the opener was not sentence-initial behind "Got it — "), and
   even detected it could not BIND (no quoted name). The detector accepts a short
   acknowledging lead before a family opener; the binder reads "called/named X"
   off the floor's own sentence. A genuinely mid-sentence mention still does
   not match.

Layer: unit, router stubbed, registry stubbed where the effect must be known.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from services.intent_service import armed_turn_consult as atc
from services.intent_service.add_project_clarify import (
    ADD_PROJECT_CONFIRM_KIND,
    build_add_project_name_offer,
    handle_add_project_name_turn,
)
from services.intent_service.armed_turn_consult import (
    ArmedReplyOutcome,
    classify_armed_reply,
)
from services.intent_service.unarmed_offer import (
    bind_catalogued_command,
    detect_offer_questions,
    enforce_armed_offers,
)
from services.shared_types import EffectClass

pytestmark = pytest.mark.asyncio

_USER = "3f7b8a52-2080-4b00-9e00-000000002080"


def _stub_route(monkeypatch, *, outcome="operation", operation=None, confidence=None, args=None):
    from services.intent_service import inversion_router as ir
    from services.intent_service.inversion_router import RoutingDecision

    async def _route(message, session_state=None, **kwargs):
        return RoutingDecision(
            outcome=outcome,
            operation=operation if outcome == "operation" else None,
            confidence=confidence,
            args=dict(args or {}),
        )

    monkeypatch.setattr(ir, "route", _route)
    monkeypatch.setattr(
        ir, "derive_routing_grammar", lambda: SimpleNamespace(alias_to_canonical={})
    )


def _stub_rail(monkeypatch, **effects):
    """Registry stub: operation name -> an entry whose only relevant field is effect."""
    from services.intent_service import workflow_dispatcher as wd

    rail = {name: SimpleNamespace(effect=effect) for name, effect in effects.items()}
    monkeypatch.setattr(wd, "get_action_workflows", lambda: rail)


def _svc():
    return SimpleNamespace(intent_classifier=None)


# ---------------------------------------------------------------- half 1: the consult


class TestBareReadConfirms:
    async def test_bare_read_confirms_when_the_carrier_asks(self, monkeypatch):
        _stub_route(monkeypatch, operation="get_identity", confidence=0.95, args={})
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        d = await classify_armed_reply(
            "Piper Morgan", _USER, session_id="s", intent_service=_svc(), confirm_bare_reads=True
        )
        assert d.outcome is ArmedReplyOutcome.CONFIRM
        assert d.operation == "get_identity"
        assert d.reason == "bare_read"

    async def test_default_is_byte_identical_release(self, monkeypatch):
        """The clear-family and todo carriers never pass the flag: unchanged."""
        _stub_route(monkeypatch, operation="get_identity", confidence=0.95, args={})
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        d = await classify_armed_reply("Piper Morgan", _USER, session_id="s", intent_service=_svc())
        assert d.outcome is ArmedReplyOutcome.RELEASE

    async def test_read_with_args_still_releases(self, monkeypatch):
        _stub_route(monkeypatch, operation="list_projects", confidence=0.95, args={"filter": "x"})
        _stub_rail(monkeypatch, list_projects=EffectClass.READ)
        d = await classify_armed_reply(
            "list my archived projects",
            _USER,
            session_id="s",
            intent_service=_svc(),
            confirm_bare_reads=True,
        )
        assert d.outcome is ArmedReplyOutcome.RELEASE

    async def test_write_still_releases(self, monkeypatch):
        _stub_route(monkeypatch, operation="archive_project", confidence=0.95, args={})
        _stub_rail(monkeypatch, archive_project=EffectClass.WRITE)
        d = await classify_armed_reply(
            "archive the Test project",
            _USER,
            session_id="s",
            intent_service=_svc(),
            confirm_bare_reads=True,
        )
        assert d.outcome is ArmedReplyOutcome.RELEASE

    async def test_unknown_operation_is_not_a_bare_read(self, monkeypatch):
        _stub_route(monkeypatch, operation="not_on_the_rail", confidence=0.95, args={})
        _stub_rail(monkeypatch)
        d = await classify_armed_reply(
            "whatever", _USER, session_id="s", intent_service=_svc(), confirm_bare_reads=True
        )
        assert d.outcome is ArmedReplyOutcome.RELEASE

    async def test_alias_resolves_through_the_grammar(self, monkeypatch):
        from services.intent_service import inversion_router as ir

        _stub_route(monkeypatch, operation="who_am_i", confidence=0.95, args={})
        monkeypatch.setattr(
            ir,
            "derive_routing_grammar",
            lambda: SimpleNamespace(alias_to_canonical={"who_am_i": "get_identity"}),
        )
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        d = await classify_armed_reply(
            "Piper Morgan", _USER, session_id="s", intent_service=_svc(), confirm_bare_reads=True
        )
        assert d.outcome is ArmedReplyOutcome.CONFIRM

    async def test_clarify_and_sub_threshold_unchanged(self, monkeypatch):
        _stub_route(monkeypatch, outcome="clarify")
        _stub_rail(monkeypatch)
        d = await classify_armed_reply(
            "Atlas", _USER, session_id="s", intent_service=_svc(), confirm_bare_reads=True
        )
        assert d.outcome is ArmedReplyOutcome.CONFIRM
        _stub_route(monkeypatch, operation="get_identity", confidence=0.4, args={})
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        d = await classify_armed_reply(
            "Piper Morgan", _USER, session_id="s", intent_service=_svc(), confirm_bare_reads=True
        )
        assert d.outcome is ArmedReplyOutcome.CONFIRM
        assert d.reason == "sub_threshold"


# ---------------------------------------------------------------- half 1: the carrier


class _FakeOffers:
    def __init__(self):
        self.stored = None

    def set_pending_offer(self, session_id, offer, user_id=None):
        self.stored = offer
        return True


def _fake_service():
    return SimpleNamespace(
        intent_classifier=None,
        workflow_offer_service=_FakeOffers(),
        canonical_handlers=None,
    )


class TestNameCarrierPassesTheFlag:
    async def test_piper_morgan_as_a_name_confirms_instead_of_releasing(self, monkeypatch):
        """xian's served turn: the chain used to die here (RELEASE → None)."""
        _stub_route(monkeypatch, operation="get_identity", confidence=0.95, args={})
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        fake = _fake_service()
        offer = build_add_project_name_offer("add a project", _USER)
        result = await handle_add_project_name_turn(
            offer, "Piper Morgan", session_id="s-2080", user_id=_USER, intent_service=fake
        )
        assert result is not None, "RELEASE returned None and the offer chain died (#2080)"
        assert result["message"] == 'Add a project called "Piper Morgan"? (yes/no)'
        assert fake.workflow_offer_service.stored is not None
        assert (
            fake.workflow_offer_service.stored["pending_action"]["kind"] == ADD_PROJECT_CONFIRM_KIND
        )
        # CXO 2026-10-17 18:32: the confirm stays ONE yes/no question (no "or did
        # you mean to ask me something?"); a "no" answers with a statement that
        # leaves the door open instead.
        assert fake.workflow_offer_service.stored["decline_message"] == (
            "Okay, I won't add that project. If you meant to ask me something, go ahead."
        )
        assert fake.workflow_offer_service.stored["pending_action"]["bare_read"] is True

    async def test_an_ambiguous_reply_keeps_the_naming_decline(self, monkeypatch):
        """CXO 18:48: the #1886(b) arm (sub-threshold, no question implied)
        keeps the line that names the project; only the bare-read arm gets
        the open-door line."""
        _stub_route(monkeypatch, operation="get_identity", confidence=0.4, args={})
        _stub_rail(monkeypatch, get_identity=EffectClass.READ)
        fake = _fake_service()
        offer = build_add_project_name_offer("add a project", _USER)
        result = await handle_add_project_name_turn(
            offer, "Klatch", session_id="s-1886b", user_id=_USER, intent_service=fake
        )
        assert result is not None
        assert result["message"] == 'Add a project called "Klatch"? (yes/no)'
        stored = fake.workflow_offer_service.stored
        assert stored["pending_action"]["bare_read"] is False
        assert stored["decline_message"] == (
            'Okay — I won\'t add a project called "Klatch". Nothing has been changed.'
        )

    async def test_a_real_competing_command_still_releases(self, monkeypatch):
        _stub_route(monkeypatch, operation="show_my_todos", confidence=0.95, args={"scope": "all"})
        _stub_rail(monkeypatch, show_my_todos=EffectClass.READ)
        fake = _fake_service()
        offer = build_add_project_name_offer("add a project", _USER)
        result = await handle_add_project_name_turn(
            offer, "show all my todos", session_id="s-2080b", user_id=_USER, intent_service=fake
        )
        assert result is None  # released to normal routing, as before


# ---------------------------------------------------------------- half 2: the seam

SERVED_SENTENCE = "Got it — want me to create a project called Piper Morgan?"


class TestSeamCatchesTheImprovisedOffer:
    @pytest.mark.parametrize(
        "sentence",
        [
            SERVED_SENTENCE,
            "Sure, want me to create a project called Atlas?",
            "Okay: should I set up a project named Atlas?",
            "Got it - would you like me to add a project called Atlas?",
        ],
    )
    def test_lead_clause_before_a_family_opener_is_detected(self, sentence):
        found = detect_offer_questions(sentence)
        assert len(found) == 1, sentence
        assert found[0].sentence == sentence

    @pytest.mark.parametrize(
        "sentence",
        [
            "I can do that if you want me to look into it?",  # mid-sentence, not a lead
            "Tell me when you want me to start?",
            "What's the repo?",
            "Say: add project Atlas.",
        ],
    )
    def test_mid_sentence_mentions_still_do_not_match(self, sentence):
        assert detect_offer_questions(sentence) == []

    def test_called_name_binds_to_the_add_project_command(self):
        found = detect_offer_questions(SERVED_SENTENCE)
        bound = bind_catalogued_command(found[0].predicate)
        assert bound is not None
        assert bound[1] == "add project Piper Morgan"

    def test_called_name_with_repo_binds_both_slots(self):
        found = detect_offer_questions(
            "Sure, want me to create a project called Atlas with repo acme/atlas?"
        )
        bound = bind_catalogued_command(found[0].predicate)
        assert bound is not None
        assert bound[1] == "add project Atlas with repo acme/atlas"

    def test_unarmed_served_sentence_is_rewritten_not_left_standing(self):
        text, rewrites = enforce_armed_offers(SERVED_SENTENCE)
        assert rewrites == 1
        assert "?" not in text
        assert "add project Piper Morgan" in text

    def test_with_the_arming_callback_the_question_is_armed_and_stands(self):
        armed = []

        def arm(record):
            armed.append(record)
            return True

        text, rewrites = enforce_armed_offers(
            SERVED_SENTENCE, arm_offer=arm, session_id="s", user_text="Piper Morgan"
        )
        assert rewrites == 0
        assert len(armed) == 1
        assert armed[0]["pending_action"]["command"] == "add project Piper Morgan"
        assert "add project Piper Morgan" in text and text.endswith(
            "Say yes, or tell me otherwise."
        )


class TestFloorBoundNameMustBeTheUsersWords:
    """Arch's pre-landing condition (2026-10-17): the floor's sentence is model
    output, so a name read off it passes the #1976 user-said guard or is not
    armed. xian's case passes (he typed "Piper Morgan"); an invented name
    takes the rewrite path and nothing is armed."""

    def _arm(self):
        armed = []

        def arm(record):
            armed.append(record)
            return True

        return armed, arm

    def test_invented_name_is_not_armed(self):
        armed, arm = self._arm()
        text, rewrites = enforce_armed_offers(
            "Want me to create a project called Atlas?",
            arm_offer=arm,
            session_id="s",
            user_text="Piper Morgan",
        )
        assert armed == []
        assert rewrites == 1
        assert "?" not in text

    def test_no_user_text_fails_closed(self):
        armed, arm = self._arm()
        text, rewrites = enforce_armed_offers(SERVED_SENTENCE, arm_offer=arm, session_id="s")
        assert armed == []
        assert rewrites == 1

    def test_name_from_a_recent_user_turn_passes(self):
        armed, arm = self._arm()
        _, rewrites = enforce_armed_offers(
            SERVED_SENTENCE,
            arm_offer=arm,
            session_id="s",
            user_text="yes Piper Morgan",  # the floor joins this turn with recent user turns
        )
        assert rewrites == 0 and len(armed) == 1

    def test_guard_is_the_factored_1976_one(self):
        from services.onboarding.portfolio_service import (
            router_add_project_args,
            user_said_every_word,
        )

        assert user_said_every_word("Piper Morgan", "piper morgan!") == "Piper Morgan"
        assert user_said_every_word("Atlas", "Piper Morgan") is None
        assert user_said_every_word("  ", "anything") is None
        out = router_add_project_args({"name": "Atlas"}, "add a project called Piper Morgan")
        assert out["name"] is None
        out = router_add_project_args({"name": "Piper Morgan"}, "add a project called Piper Morgan")
        assert out["name"] == "Piper Morgan"
