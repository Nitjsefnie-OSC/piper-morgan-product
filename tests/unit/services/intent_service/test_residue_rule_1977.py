"""#1977 step 1: the residue rule at surface 1 (ADR-080 D6, declines MORE).

A claim set whose claimed spans leave a substantive second clause (a
coordination marker -- and/also/then/plus/; -- followed by >= 2 content
words) is declined, so nothing deterministic takes the turn and the whole
message reaches the router / LLM classifier. Generalizes the #1416/#1924
pleasantry-with-residue branch. Pure unit pins: no LLM, no network.
"""

from services.intent_service.pre_classifier import PreClassifier


def _sub(message, spans):
    return PreClassifier._substantive_residue(message.strip().lower(), spans)


class TestMultiIntentResidue:
    def test_two_claims_cover_both_clauses_not_declined(self):
        """Measured 2026-10-11 (after the twenty-seventh deletion took
        PORTFOLIO's show/list/view literal): PORTFOLIO claims via the ruled
        `update ... project` survivor (0,17) + STATUS `current work` (49,61);
        the leftover ' name to Atlas and summarize my ' is not ask-shaped ->
        not declined. Was "list my archived projects and summarize my current
        work" (PORTFOLIO (0,25) + STATUS (43,55)) until that literal went."""
        r = PreClassifier.detect_multiple_intents(
            "update my project name to Atlas and summarize my current work"
        )
        assert [i.action for i in r.intents] == ["manage_portfolio", "get_project_status"]
        assert r.is_multi_intent

    def test_single_claim_with_substantive_second_clause_declined(self):
        """Measured: one STATUS claim ('current work') + ' and tell me a joke
        about cats' unclaimed -> declined, no intents."""
        msg = "summarize my current work and tell me a joke about cats"
        r = PreClassifier.detect_multiple_intents(msg)
        assert r.intents == []
        assert not r.is_multi_intent
        clause = _sub(msg, [(13, 25)])
        assert clause is not None and clause.startswith("tell me a joke")

    def test_single_claim_no_marker_unchanged(self):
        r = PreClassifier.detect_multiple_intents("summarize my current work")
        assert [i.action for i in r.intents] == ["get_project_status"]

    def test_comma_is_not_a_marker(self):
        assert _sub("show status, tell me a joke about cats", [(0, 11)]) is None

    def test_one_content_word_after_marker_not_substantive(self):
        assert _sub("show my status and also the details", [(8, 14)]) is None

    def test_semicolon_marker(self):
        assert _sub("show my status; tell me a joke about cats", [(8, 14)]) is not None


class TestWriteSyntheticPin:
    """Arch's synthetic WRITE pin ("remind me to call mom and pick up milk").

    Measured: surface 1 claims NOTHING for this phrasing today (the
    reminder-create literals are gone), so the residue rule has no claim to
    decline -- outcome is identical before/after: no intents, (None, None).
    Direction-safe either way: a decline sends a create_reminder turn to the
    router and consent still decides; whether it serves the same answer is
    what Lead's rule-7 WRITE rows must show, not this unit pin.
    """

    def test_write_claim_with_and_in_object(self):
        msg = "remind me to call mom and pick up milk"
        assert PreClassifier.detect_multiple_intents(msg).intents == []
        assert PreClassifier.pre_classify_with_pattern_list(msg) == (None, None)


class TestSingleEntryParity:
    def test_declined_phrasing_through_single_entry(self):
        msg = "summarize my current work and tell me a joke about cats"
        # the underlying claim exists...
        assert PreClassifier._pre_classify_claim(msg)[1] == "STATUS_PATTERNS"
        # ...and the public single entry declines it.
        assert PreClassifier.pre_classify_with_pattern_list(msg) == (None, None)

    def test_single_claim_without_residue_still_claims(self):
        intent, name = PreClassifier.pre_classify_with_pattern_list("summarize my current work")
        assert name == "STATUS_PATTERNS" and intent is not None


# ---------------------------------------------------------------------------
# Widened ask cue (CXO + Arch, 2026-10-11): request-statements ("I need", "I want",
# "I'd like", "I'd love", "let me see", "give me", "can I get/see/have") are asks.
# Gated on the mid-flow-correction sentinels: a correction joined by a marker
# must not be pulled off its handler.
# ---------------------------------------------------------------------------
import pytest as _pytest

from services.intent_service.pre_classifier import PreClassifier as _PC


@_pytest.mark.parametrize(
    "message",
    [
        "summarize my current work and I need the archived list too",
        "summarize my current work and give me the archived list",
        "summarize my current work and I'd like the archived list as well",
    ],
)
def test_request_statement_second_ask_declines(message):
    """The declarative second ask was the named trade of the first cut; with the
    widened cue it declines like an imperative one (the list half is no longer
    dropped silently by the STATUS claim)."""
    assert _PC.detect_multiple_intents(message).intents == []
    assert _PC.pre_classify(message) is None


@_pytest.mark.parametrize(
    "message",
    [
        # #1856 turn 2 — an aside joined to the claim: stays claimed.
        "we're going in circles now and no that is not the name of the new project",
        # a marker-joined correction that CARRIES the claim: the trailing clause
        # is touched by the claim span, so it is not unclaimed.
        "we're going in circles and I want the new project called Atlas",
    ],
)
def test_mid_flow_corrections_stay_with_the_add_project_handler(message):
    intents = _PC.detect_multiple_intents(message).intents
    assert [(i.category.value, i.action) for i in intents] == [("portfolio", "manage_portfolio")]
    assert _PC.pre_classify(message) is not None


@_pytest.mark.parametrize(
    "message",
    [
        "we're going in circles and I want it called Atlas",
        "that's wrong, and I need the name to be Atlas",
        "no, I want it called Atlas",
    ],
)
def test_corrections_without_a_claim_were_never_surface_1_turns(message):
    """Arch's sentinel shapes: no surface-1 literal matches these at all, so
    surface 1 did not claim them before the cue and does not after — the
    active-process machinery, not surface 1, owns a mid-flow correction with
    no claim. Pinned so a future literal cannot quietly start claiming them."""
    assert _PC.detect_multiple_intents(message).intents == []
    assert _PC.pre_classify(message) is None
