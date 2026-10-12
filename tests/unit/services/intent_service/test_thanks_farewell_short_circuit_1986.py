"""#1986 — pure thanks/farewell take the canned path (Arch's 2026-10-12 ruling,
reversing #1754 for these two pairs only; six conditions).

Alpha c613beabf5 served a todo briefing for a cold "thank you!": the
pre-classifier claimed it as CONVERSATION/thanks, but only greeting had the
canned short-circuit, so the turn floored with the user's context. These pins
hold the gate's new contract and the conditions that bound it:

1. no interpretation growth — the patterns are byte-identical and compound
   forms still floor (#1416);
3. an ARMED turn does not short-circuit thanks/farewell (greeting unchanged,
   reported to Arch rather than widened);
4. one string, one place — the keyless gate and the keyed path share the
   constants;
5. dispositions CANONICAL.
"""

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.action_registry import ACTION_REGISTRY, ActionDisposition
from services.intent_service.pre_classifier import PreClassifier
from services.shared_types import IntentCategory
from services.ui_messages.keyless_pleasantry import (
    FAREWELL_LINE,
    KEYLESS_KIND_PREFIXES,
    THANKS_AFTER_DELIVERY,
    THANKS_NOTHING_DONE_THIS_SESSION,
)


def _conv(action: str, message: str, armed: str | None = None) -> Intent:
    ctx = {"original_message": message}
    if armed is not None:
        ctx["armed_offer_rail"] = armed
    return Intent(category=IntentCategory.CONVERSATION, action=action, context=ctx)


@pytest.fixture
def gate():
    svc = IntentService.__new__(IntentService)
    return svc._requires_canonical_handler


# --- the gate ---------------------------------------------------------------


@pytest.mark.parametrize(
    "action,message",
    [
        ("thanks", "thank you!"),
        ("thanks", "thanks!"),
        ("thanks", "thank you so much"),
        ("farewell", "goodbye"),
        ("farewell", "bye"),
        ("greeting", "hello"),
    ],
)
def test_pure_pleasantries_take_the_canned_path(gate, action, message):
    assert gate(_conv(action, message)) is True


@pytest.mark.parametrize(
    "action,message",
    [
        ("thanks", "thanks, now show my todos"),
        ("thanks", "no thanks"),
        ("farewell", "bye, but first list my projects"),
        ("greeting", "Hi, I just got access to this. How do I address you?"),
    ],
)
def test_compound_or_declining_forms_still_floor(gate, action, message):
    """#1416 unchanged: residue floors even when the classifier labels the turn."""
    assert gate(_conv(action, message)) is False


@pytest.mark.parametrize("message", ["thanks, now show my todos", "no thanks"])
def test_surface_one_does_not_claim_the_two_named_forms(message):
    """Condition 1: no interpretation growth — the pre-classifier never claimed these."""
    assert PreClassifier._is_pleasantry_only(message.lower()) is False
    assert PreClassifier.pre_classify(message) is None


@pytest.mark.parametrize("rail", ["workflow_offer", "last_offer", "interview_offer"])
@pytest.mark.parametrize("action,message", [("thanks", "thanks!"), ("farewell", "bye")])
def test_armed_turn_does_not_short_circuit_thanks_or_farewell(gate, rail, action, message):
    """Condition 3: 'thanks' to 'Want me to…?' may be an answer — today's path."""
    assert gate(_conv(action, message, armed=rail)) is False


def test_greeting_is_not_widened_to_the_armed_check(gate):
    """Deliberate: a pure 'hi' on an armed turn still takes the canned greeting
    (the offer survives via the #1739 §5a re-arm). Reported to Arch, not changed."""
    assert gate(_conv("greeting", "hello", armed="workflow_offer")) is True


# --- metadata and copy --------------------------------------------------------


def test_dispositions_are_canonical_again():
    assert ACTION_REGISTRY[("CONVERSATION", "thanks")] is ActionDisposition.CANONICAL
    assert ACTION_REGISTRY[("CONVERSATION", "farewell")] is ActionDisposition.CANONICAL
    assert ACTION_REGISTRY[("CONVERSATION", "greeting")] is ActionDisposition.CANONICAL


def test_one_string_one_place():
    """Condition 4 + CXO's copy ruling: the keyless gate and the keyed path serve
    the same constants; thanks never claims a service when nothing was done."""
    assert KEYLESS_KIND_PREFIXES["thanks"] == THANKS_NOTHING_DONE_THIS_SESSION
    assert KEYLESS_KIND_PREFIXES["farewell"] == FAREWELL_LINE
    assert THANKS_NOTHING_DONE_THIS_SESSION == (
        "That's kind — though I haven't done anything this session yet."
    )
    assert THANKS_AFTER_DELIVERY == "You're welcome."
    assert FAREWELL_LINE == "Goodbye for now."
    for line in (THANKS_NOTHING_DONE_THIS_SESSION, THANKS_AFTER_DELIVERY, FAREWELL_LINE):
        assert "?" not in line and "todo" not in line.lower()


def test_patterns_byte_identical_to_the_ruled_floor():
    """Condition 1: THANKS/FAREWELL/filler lists are the #1974 permanent floor."""
    assert [p.pattern if hasattr(p, "pattern") else p for p in PreClassifier.THANKS_PATTERNS] == [
        r"\bthanks\b",
        r"\bthank you\b",
        r"\bthx\b",
        r"\bty\b",
        r"\bmuch appreciated\b",
    ]
    assert len(PreClassifier.FAREWELL_PATTERNS) == 5
    assert len(PreClassifier._PLEASANTRY_FILLER_PATTERNS) == 10


# --- the durable reader (condition 2, tightened) ------------------------------


class TestCountDeliveredTurns:
    """`count_delivered_turns` is the POSITIVE proof behind the honest-empty
    form: it reads the durable `conversation_turns` table, owner-checked, and
    raises on anything that is not a successful read."""

    @staticmethod
    def _scope(row, count):
        from unittest.mock import AsyncMock, MagicMock

        session = AsyncMock()
        session.get = AsyncMock(return_value=row)
        result = MagicMock()
        result.scalar.return_value = count
        session.execute = AsyncMock(return_value=result)
        scope = MagicMock()
        scope.__aenter__ = AsyncMock(return_value=session)
        scope.__aexit__ = AsyncMock(return_value=False)
        return scope

    @pytest.mark.asyncio
    async def test_owner_mismatch_raises_not_zero(self):
        from unittest.mock import MagicMock, patch

        from services.intent_service.conversation_context import count_delivered_turns

        row = MagicMock()
        row.user_id = "someone-else"
        with patch(
            "services.database.session_factory.AsyncSessionFactory.session_scope",
            return_value=self._scope(row, 3),
        ):
            with pytest.raises(PermissionError):
                await count_delivered_turns("s-1986", "f13937fb-182b-44db-a9fd-0d722a3a223e")

    @pytest.mark.asyncio
    async def test_missing_conversation_row_reads_as_zero(self):
        from unittest.mock import patch

        from services.intent_service.conversation_context import count_delivered_turns

        with patch(
            "services.database.session_factory.AsyncSessionFactory.session_scope",
            return_value=self._scope(None, 0),
        ):
            assert await count_delivered_turns("s-1986", "u") == 0

    @pytest.mark.asyncio
    async def test_owned_conversation_counts_delivered_turns(self):
        from unittest.mock import MagicMock, patch

        from services.intent_service.conversation_context import count_delivered_turns

        row = MagicMock()
        row.user_id = "u"
        with patch(
            "services.database.session_factory.AsyncSessionFactory.session_scope",
            return_value=self._scope(row, 2),
        ):
            assert await count_delivered_turns("s-1986", "u") == 2
