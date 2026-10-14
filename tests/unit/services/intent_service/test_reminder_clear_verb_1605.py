"""#1605 — reminder/todo "clear"-family verb disambiguation (three-variant copy).

The CXO/PPM jointly-signed-off design (FINAL copy memo 2026-08-13 22:17, PPM
sign-off 22:22). The variant-1 sentence is RATIFIED copy — a drifted word is
a bug, so this file pins it EXACTLY.

2026-10-14 (Arch's clear_todos ruling, point 1 — the named retirement): the
regex-triggered three-variant flow this file used to drive end to end
(detect_clear_family_ask -> maybe_handle_clear_family -> the off-rail verb
answer, the variant-2 correction window, the variant-3 batch confirm built
from variant_three_question) is DELETED; the family enters through the
clear_todos resolver rail entry. Its detection, end-to-end, ALWAYS_ASK,
exception-clause and named-target classes went with it. The resolver's
behaviour (all three variants, CXO's 2026-10-06 strings) is pinned in
test_clear_todos_resolver.py. What stays here: the ratified variant-1
sentence the resolver still composes, the two surviving offer-seam registry
entries, and the decide_verb_interpretation meta cell (consent_gate still
serves it to the #1411 unmapped-status seam).
"""

from services.intent_service import reminder_clear as rc
from services.intent_service.reminder_clear import variant_one_question
from services.intent_service.workflow_dispatcher import (
    get_action_workflows,
    get_registered_workflows,
)
from services.intent_service.workflow_entries import register_default_workflows
from services.shared_types import EffectClass

# ---------------------------------------------------------------------------
# RATIFIED COPY PIN — exact string (CXO FINAL 2026-08-13, PPM signed off)
# ---------------------------------------------------------------------------


class TestRatifiedCopyPins:
    def test_variant_one_verbatim(self):
        assert variant_one_question() == (
            "Before I touch these — when you say 'clear' on a reminder, "
            "do you want me to mark it done, or delete it? "
            "I'll remember for next time."
        )

    def test_vocabulary_parametrization_todo_noun(self):
        """#1569 vocabulary rule: the noun parameter still renders."""
        assert "'clear' on a todo" in variant_one_question(noun="todo")

    def test_correction_window_ask_verbatim(self):
        """The ratified standing invitation the resolver's variant-2
        disclosure clause ends with."""
        assert rc.CORRECTION_WINDOW_ASK == "Say so if you meant delete this time."


# ---------------------------------------------------------------------------
# Registry: offer-seam-only entries, effects explicit (#1557)
# ---------------------------------------------------------------------------


class TestRegistryEntries:
    def test_entries_registered_with_explicit_effects(self):
        register_default_workflows()
        w = get_registered_workflows()
        assert w[rc.CLARIFY_CLEAR_VERB_WORKFLOW].effect == EffectClass.READ
        assert w[rc.CLEAR_DELETE_WORKFLOW].effect == EffectClass.DESTRUCTIVE

    def test_entries_are_not_rail_reachable(self):
        """action_triggered=False: a classifier emission can never fire the
        batch delete (or the re-ask entry) directly — and the destructive
        rail-scope denominator in test_destructive_confirm_1190 stays true."""
        register_default_workflows()
        rail = get_action_workflows()
        for key in (rc.CLARIFY_CLEAR_VERB_WORKFLOW, rc.CLEAR_DELETE_WORKFLOW):
            assert key not in rail

    def test_retired_entries_are_gone(self):
        """The variant-2 correction window and #1906 pick-target entries
        retired with the regex seam that armed them (2026-10-14)."""
        register_default_workflows()
        w = get_registered_workflows()
        assert "reminder_clear_correction" not in w
        assert "reminder_clear_pick_target" not in w


# ---------------------------------------------------------------------------
# The pinned meta cell (mechanism level): a DESTRUCTIVE candidate reads back
# even under "stop asking me every time" — process steering never lowers a
# destructive ask.
# ---------------------------------------------------------------------------


class TestMetaCellPin:
    def test_destructive_candidate_reads_back_under_trust(self):
        from services.intent_service.consent_gate import decide_verb_interpretation
        from services.intent_service.verified_inference import (
            VerificationDecision,
            VerificationMetaMode,
        )

        assert (
            decide_verb_interpretation(
                rc.VERB_CONFIDENCE,
                EffectClass.DESTRUCTIVE,
                VerificationMetaMode.TRUST_INFERENCES,
            )
            is VerificationDecision.READ_BACK
        )

    def test_write_candidate_auto_applies_under_trust(self):
        from services.intent_service.consent_gate import decide_verb_interpretation
        from services.intent_service.verified_inference import (
            VerificationDecision,
            VerificationMetaMode,
        )

        assert (
            decide_verb_interpretation(
                rc.VERB_CONFIDENCE,
                EffectClass.WRITE,
                VerificationMetaMode.TRUST_INFERENCES,
            )
            is VerificationDecision.AUTO_APPLY
        )
