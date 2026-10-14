"""#1843 -- "please <verb phrase>" is a REQUEST, never an acceptance.

ACCEPT_PATTERNS row 2 used to open on a bare ``please``, so a short polite
edit request ("please remove the fluff and make it punchier") passed the
prose floor and FINALIZED the standup draft. "please" now opens an accept
only when the remainder is itself accept vocabulary.
"""

import pytest

from services.intent_service.acceptance import AcceptanceVerdict, evaluate_acceptance
from services.intent_service.soft_invocation import ACCEPT_PATTERNS
from services.shared_types import EffectClass, Outwardness

REQUESTS = [
    "please remove the fluff and make it punchier",
    "please make it punchier",
    "please remove the fluff",
    "please shorten the second bullet",
    "please add a line about the blocker",
    "please reword the intro",
    "please drop the last item",
]

TAUGHT_ACCEPTS = ["please", "please do", "yes please", "yes, please go ahead", "please go ahead", "please, yes"]

_LOW = dict(effect=EffectClass.READ, outwardness=Outwardness.PRIVATE)
_CONFIRM = dict(effect=EffectClass.DESTRUCTIVE, outwardness=Outwardness.PRIVATE)


@pytest.mark.parametrize("msg", REQUESTS)
def test_request_low_ceremony_not_accept(msg):
    assert (
        evaluate_acceptance(msg, armed_question="Want a draft?", **_LOW)
        != AcceptanceVerdict.ACCEPT
    )


@pytest.mark.parametrize("msg", REQUESTS)
def test_request_confirm_tier_not_accept(msg):
    assert (
        evaluate_acceptance(msg, armed_question="Delete it? (yes/no)", **_CONFIRM)
        != AcceptanceVerdict.ACCEPT
    )


@pytest.mark.parametrize("msg", TAUGHT_ACCEPTS)
def test_taught_accepts_still_accept(msg):
    assert (
        evaluate_acceptance(msg, armed_question="Want a draft?", **_LOW)
        == AcceptanceVerdict.ACCEPT
    )


def test_please_alone_still_accepts_both_tiers():
    assert evaluate_acceptance("please", armed_question="q?", **_LOW) == AcceptanceVerdict.ACCEPT
    assert (
        evaluate_acceptance("please", armed_question="q?", **_CONFIRM) == AcceptanceVerdict.ACCEPT
    )


def test_row2_opener_has_no_bare_please_before_whitespace():
    row2 = ACCEPT_PATTERNS[1].pattern
    assert "sure|please" not in row2 and "please|go ahead" not in row2
    assert row2 != r"^(?:yes|yeah|sure|please|go ahead),?\s"
    assert "please,?\\s+(?:" in row2  # please only opens with accept vocab after
    assert not ACCEPT_PATTERNS[1].search("please remove the fluff")
