"""#1977 step 2: the legacy branch acknowledges the half it did not answer.

Step 1 (surface 1) declines a claim set that leaves a substantive second
clause, and hands the WHOLE message to the single-intent LLM classifier, which
serves ONE intent -- the other clause was dropped silently. Step 2 carries the
residue (``MultiIntentResult.unclaimed_residue`` / ``declined_claims``) onto the
served intent's context and appends CXO's one-line acknowledgement after the
answer (``IntentService._unanswered_half_line``), arming the existing #852
one-turn ``last_offer`` rail so a bare "yes" steers the classifier to the
clause. Pure unit pins: no LLM, no network.
"""

from uuid import uuid4

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentProcessingResult, IntentService
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import (
    LastOffer,
    get_or_create_context,
)
from services.intent_service.pre_classifier import PreClassifier
from services.shared_types import IntentCategory

_MSG = "summarize my current work and tell me a joke about cats"
_USER = "9c1e2d40-1977-4b00-9e00-000000001977"


def _intent(category, residue=None, declined=None):
    ctx = {}
    if residue is not None:
        ctx["unclaimed_residue"] = residue
    if declined is not None:
        ctx["declined_claims"] = declined
    return Intent(
        category=category,
        action="x",
        original_message=_MSG,
        confidence=0.9,
        context=ctx,
    )


class TestUnansweredHalfLine:
    def test_served_category_is_the_claimed_half(self):
        """(a) STATUS served, STATUS claim declined -> the residue is unanswered;
        the answered half's clause is known, so the line names both."""
        intent = _intent(
            IntentCategory.STATUS,
            "tell me a joke about cats",
            [("status", "get_project_status", "summarize my current work")],
        )
        line = IntentService._unanswered_half_line(intent)
        assert line == ('I haven\'t done "tell me a joke about cats" yet. Want me to?')

    def test_no_clause_text_for_declined_claim_names_only_the_unanswered(self):
        intent = _intent(
            IntentCategory.STATUS,
            "tell me a joke about cats",
            [("status", "get_project_status", None)],
        )
        assert (
            IntentService._unanswered_half_line(intent)
            == 'I haven\'t done "tell me a joke about cats" yet. Want me to?'
        )

    def test_served_category_differs_declined_clause_is_unanswered(self):
        """(b) the LLM answered the residue's side -> the declined clause is
        the unanswered one."""
        intent = _intent(
            IntentCategory.CONVERSATION,
            "tell me a joke about cats",
            [("status", "get_project_status", "summarize my current work")],
        )
        assert IntentService._unanswered_half_line(intent) == (
            'I haven\'t done "summarize my current work" yet. Want me to?'
        )

    def test_no_declined_claim_recorded_uses_the_residue(self):
        intent = _intent(IntentCategory.STATUS, "tell me a joke about cats", [])
        assert (
            IntentService._unanswered_half_line(intent)
            == 'I haven\'t done "tell me a joke about cats" yet. Want me to?'
        )

    def test_no_residue_in_context_is_none(self):
        """(c) never on a guess."""
        assert IntentService._unanswered_half_line(_intent(IntentCategory.STATUS)) is None
        stray = _intent(IntentCategory.STATUS, None, [("status", "a", "b")])
        assert IntentService._unanswered_half_line(stray) is None

    def test_context_none_is_none(self):
        intent = _intent(IntentCategory.STATUS)
        intent.context = None
        assert IntentService._unanswered_half_line(intent) is None

    def test_long_residue_trimmed_to_eight_words(self):
        """(d) CXO rule 4."""
        residue = "list all of my archived projects from the last two years please"
        assert len(residue.split()) == 12
        intent = _intent(IntentCategory.STATUS, residue, [])
        line = IntentService._unanswered_half_line(intent)
        assert (
            line == 'I haven\'t done "list all of my archived projects from the" yet. Want me to?'
        )
        assert len(line.split('"')[1].split()) == 8

    def test_blank_clause_after_trim_is_none(self):
        assert (
            IntentService._unanswered_half_line(_intent(IntentCategory.STATUS, " ;. ", [])) is None
        )

    def test_no_apology(self):
        line = IntentService._unanswered_half_line(
            _intent(IntentCategory.STATUS, "list my todos now", [])
        )
        assert "sorry" not in line.lower() and "wasn't able" not in line.lower()


class TestStepOneCarriesTheResidue:
    def test_detect_multiple_intents_carries_residue_and_declined_claim(self):
        r = PreClassifier.detect_multiple_intents(_MSG)
        assert r.intents == []
        assert r.unclaimed_residue is not None and r.unclaimed_residue.startswith("tell me a joke")
        assert r.declined_claims == [("status", "get_project_status", "summarize my current work")]

    def test_clean_message_carries_nothing(self):
        r = PreClassifier.detect_multiple_intents("summarize my current work")
        assert r.unclaimed_residue is None and r.declined_claims == []


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


class _Stop(Exception):
    pass


@pytest.mark.asyncio
class TestLegacyBranchThreadsTheContext:
    async def test_classify_multiple_wraps_the_single_intent_with_the_residue(self, monkeypatch):
        classifier = IntentClassifier(llm_service=_ExplosiveLLM())
        served = _intent(IntentCategory.STATUS)

        async def _classify(self, message, **kw):
            return served

        monkeypatch.setattr(IntentClassifier, "classify", _classify)
        r = await classifier.classify_multiple(_MSG)
        assert r.intents == [served]
        assert r.unclaimed_residue.startswith("tell me a joke")
        assert r.declined_claims[0][:2] == ("status", "get_project_status")

    async def test_process_intent_stamps_residue_on_the_served_intent(self, monkeypatch):
        service = IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))
        served = _intent(IntentCategory.STATUS)

        async def _classify(self, message, **kw):
            return served

        monkeypatch.setattr(IntentClassifier, "classify", _classify)
        seen = {}

        def _observe(intent, message):
            seen["context"] = dict(intent.context)
            raise _Stop()

        monkeypatch.setattr(service, "_observe_action_verb", _observe)
        with pytest.raises(Exception):
            await service.process_intent(_MSG, session_id=str(uuid4()), user_id=_USER)
        assert seen["context"]["unclaimed_residue"].startswith("tell me a joke")
        assert seen["context"]["declined_claims"][0] == (
            "status",
            "get_project_status",
            "summarize my current work",
        )

    async def test_plain_turn_gets_no_residue(self, monkeypatch):
        service = IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))
        served = _intent(IntentCategory.STATUS)

        async def _classify(self, message, **kw):
            return served

        monkeypatch.setattr(IntentClassifier, "classify", _classify)
        seen = {}

        def _observe(intent, message):
            seen["context"] = dict(intent.context)
            raise _Stop()

        monkeypatch.setattr(service, "_observe_action_verb", _observe)
        with pytest.raises(Exception):
            await service.process_intent(
                "summarize my current work", session_id=str(uuid4()), user_id=_USER
            )
        assert "unclaimed_residue" not in seen["context"]


class TestAppendAndArm:
    """The funnel half: the line rides after the answer; the question is kept
    only when a bare "yes" can cash it (the #852 contextual rail)."""

    LINE = 'I haven\'t done "tell me a joke about cats" yet. Want me to?'

    def _service(self):
        return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))

    def _result(self, intent_data=None):
        return IntentProcessingResult(
            success=True, message="Here is your status.", intent_data=intent_data or {}
        )

    def test_funnel_appends_after_the_answer_and_arms_the_rail(self):
        service, sid = self._service(), str(uuid4())
        out = service._apply_soft_offer(
            self._result(),
            "hi",
            sid,
            user_id=_USER,
            unanswered_half_suffix=self.LINE,
            unanswered_half_clause="tell me a joke about cats",
        )
        assert out.message == f"Here is your status.\n\n{self.LINE}"
        offer = get_or_create_context(sid, user_id=_USER).last_offer
        assert offer.offer_type == "contextual"
        assert offer.continuation_hint == "tell me a joke about cats"

    def test_live_arm_drops_the_question_and_does_not_clobber(self):
        service, sid = self._service(), str(uuid4())
        existing = LastOffer(offer_type="contextual", continuation_hint="keep me", offer_text="q")
        get_or_create_context(sid, user_id=_USER).last_offer = existing
        out = service._apply_soft_offer(
            self._result(),
            "hi",
            sid,
            user_id=_USER,
            unanswered_half_suffix=self.LINE,
            unanswered_half_clause="tell me a joke about cats",
        )
        assert out.message.endswith('I haven\'t done "tell me a joke about cats" yet.')
        assert "Want me to?" not in out.message
        assert get_or_create_context(sid, user_id=_USER).last_offer is existing

    def test_handler_pending_flag_drops_the_question(self):
        service, sid = self._service(), str(uuid4())
        out = service._apply_soft_offer(
            self._result(intent_data={"consent_check_pending": True}),
            "hi",
            sid,
            user_id=_USER,
            unanswered_half_suffix=self.LINE,
            unanswered_half_clause="tell me a joke about cats",
        )
        assert "Want me to?" not in out.message
        assert get_or_create_context(sid, user_id=_USER).last_offer is None

    def test_no_session_drops_the_question(self):
        out = self._service()._apply_soft_offer(
            self._result(),
            "hi",
            "",
            user_id=_USER,
            unanswered_half_suffix=self.LINE,
            unanswered_half_clause="tell me a joke about cats",
        )
        assert out.message.endswith('cats" yet.')

    def test_no_suffix_is_byte_identical(self):
        out = self._service()._apply_soft_offer(self._result(), "hi", str(uuid4()), user_id=_USER)
        assert "haven't" not in out.message
