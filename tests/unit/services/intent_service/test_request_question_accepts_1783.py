"""#1783 - request-questions naming the remainder accept an opted-in READ offer.

Arch's ruling (2026-10-14), three conditions, CXO yes:
(a) declared per offer, READ / LOW_CEREMONY only; (b) the question must NAME the
offered remainder (rest / others / remaining / more) - a modal opener plus any
verb is too broad; (c) never at a completion or NAMED_OBJECT seam.
"""

import pytest

from services.intent_service.acceptance import (
    AcceptanceVerdict,
    evaluate_acceptance,
    is_remainder_request_question,
)
from services.shared_types import EffectClass, Outwardness
from tests.unit.services.intent_service.test_cashable_list_remainder_1762 import (
    _USER,
    _arm_a_capped_list,
    _inert_registry,
    _store,
    _stub_fallthrough_routing,
    live_service,  # noqa: F401  (fixture)
)

OFFER = "That's 5 of 340 — say the word and I'll pull the rest."
ISSUE_PHRASINGS = ["can I see the rest?", "could you show me the rest?", "what are the others?"]


def _eval(msg, *, opt_in, effect=EffectClass.READ, outwardness=Outwardness.PRIVATE):
    return evaluate_acceptance(
        msg,
        effect=effect,
        outwardness=outwardness,
        armed_question=OFFER,
        accepts_request_questions=opt_in,
    )


class TestOptedInSeam:
    @pytest.mark.parametrize("msg", ISSUE_PHRASINGS)
    def test_the_three_issue_phrasings_accept(self, msg):
        assert _eval(msg, opt_in=True) is AcceptanceVerdict.ACCEPT

    @pytest.mark.parametrize("msg", ["can you show me the remaining ones?", "will you pull more?"])
    def test_other_remainder_words_accept(self, msg):
        assert _eval(msg, opt_in=True) is AcceptanceVerdict.ACCEPT

    def test_a_modal_plus_any_verb_that_does_not_name_the_remainder_does_not_accept(self):
        assert (
            _eval("can you delete the first one?", opt_in=True) is AcceptanceVerdict.STATE_QUESTION
        )

    def test_completion_question_stays_state_question(self):
        assert (
            _eval("are we done with that standup?", opt_in=True) is AcceptanceVerdict.STATE_QUESTION
        )

    def test_a_what_question_not_naming_the_remainder_stays_state_question(self):
        assert _eval("what are the labels?", opt_in=True) is AcceptanceVerdict.STATE_QUESTION

    def test_helper_is_shape_only(self):
        assert is_remainder_request_question("could you show me the rest?")
        assert not is_remainder_request_question("is the rest done?")
        assert not is_remainder_request_question("")


class TestNoOptIn:
    @pytest.mark.parametrize("msg", ISSUE_PHRASINGS)
    def test_without_the_declaration_the_phrasings_stay_state_question(self, msg):
        assert _eval(msg, opt_in=False) is AcceptanceVerdict.STATE_QUESTION

    def test_default_is_no_opt_in(self):
        v = evaluate_acceptance(
            "can I see the rest?",
            effect=EffectClass.READ,
            outwardness=Outwardness.PRIVATE,
            armed_question=OFFER,
        )
        assert v is AcceptanceVerdict.STATE_QUESTION

    @pytest.mark.parametrize(
        "effect,outw",
        [
            (EffectClass.WRITE, Outwardness.PRIVATE),  # LOW_CEREMONY but not READ
            (EffectClass.WRITE, Outwardness.OUTWARD),
            (EffectClass.DESTRUCTIVE, Outwardness.PRIVATE),
            (None, None),
        ],
    )
    def test_a_declaration_on_a_non_read_or_non_low_ceremony_seam_fails(self, effect, outw):
        with pytest.raises(ValueError):
            _eval("can I see the rest?", opt_in=True, effect=effect, outwardness=outw)

    @pytest.mark.parametrize(
        "effect,outw",
        [(EffectClass.DESTRUCTIVE, Outwardness.PRIVATE), (EffectClass.WRITE, Outwardness.OUTWARD)],
    )
    def test_named_object_seams_keep_the_completion_question_a_state_question(self, effect, outw):
        v = _eval("are we done with that standup?", opt_in=False, effect=effect, outwardness=outw)
        assert v is AcceptanceVerdict.STATE_QUESTION


@pytest.mark.asyncio
class TestCappedListSeamEndToEnd:
    async def test_could_you_show_me_the_rest_pulls_the_rest(self, live_service):  # noqa: F811
        sid = "1783-e2e-accept"
        _arm_a_capped_list(sid, held=50)
        q = "could you show me the rest?"
        p_registry, mock_registry = _inert_registry()
        p_classify, p_floor, p_floor2 = _stub_fallthrough_routing(live_service, q)
        with p_registry as registry_fn, p_classify, p_floor, p_floor2:
            registry_fn.return_value = mock_registry
            result = await live_service.process_intent(message=q, session_id=sid, user_id=_USER)
        assert result.intent_data["action"] == "list_remainder_cash"
        assert result.intent_data["context"]["returned"] == 45
        assert _store(sid) is None

    async def test_a_modal_verb_that_does_not_name_the_rest_does_not_cash(self, live_service):  # noqa: F811
        sid = "1783-e2e-too-broad"
        _arm_a_capped_list(sid)
        q = "can you delete the first one?"
        p_registry, mock_registry = _inert_registry()
        p_classify, p_floor, p_floor2 = _stub_fallthrough_routing(live_service, q)
        with p_registry as registry_fn, p_classify, p_floor, p_floor2:
            registry_fn.return_value = mock_registry
            result = await live_service.process_intent(message=q, session_id=sid, user_id=_USER)
        assert result.intent_data.get("action") != "list_remainder_cash"
        assert _store(sid) is not None
