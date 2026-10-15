"""#2028 / #2027: the interview questions carry no suggestion lists.

The standup interview attached ``suggestions=["nothing", "skip"]`` (and
``["no blockers", "skip"]`` at blockers) to seven question responses. Nothing
renders ``ConversationResponse.suggestions`` on web (Web's served DOM read,
Arch's source read of ``chat.js``), so the lists claimed chips that do not
exist and made ``skip`` look offered and tested. CXO 2026-10-15: delete the
lists, do not render chips. Typed "nothing" / "skip" keep working as built
(pinned in ``tests/unit/services/intent_service/test_escape_end_vs_pause_888.py``).

CXO 2026-10-15 10:10: the TEN other lists go too (the opening "Yes, let's do
it" list, the REFINING "Looks good" lists, the error-path "Try again" lists),
so no ``ConversationResponse`` in the handler sets ``suggestions`` at all. Where
a list carried the only hint of the expected answer, the reply says it in
words as a statement: the REFINING draft now ends "Say 'looks good' to
finalize it." The generation-error reply already said "Say 'try again' and
I'll rebuild it."

The ``suggestions`` field itself stays on ``ConversationResponse``: it is read
generically (``intent_service`` copies it into the ``standup_started``
intent_data context); it is always empty now.

Layer: source (AST of the handler) plus one handler-driven turn per question.
"""

import ast
import pathlib

import pytest

from services.shared_types import StandupConversationState
from services.standup.conversation_handler import StandupConversationHandler
from tests.unit.services.standup._fake_conversation_manager import (
    FakeStandupConversationManager,
)

S = StandupConversationState
_HANDLER_SRC = (
    pathlib.Path(__file__).resolve().parents[4] / "services/standup/conversation_handler.py"
)


def _conversation_response_calls():
    tree = ast.parse(_HANDLER_SRC.read_text())
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "ConversationResponse"
        ):
            yield node


def _kw(call, name):
    return next((k.value for k in call.keywords if k.arg == name), None)


class TestNoSuggestionListsOnInterviewQuestions:
    def test_no_response_in_the_handler_sets_suggestions(self):
        """#2027/#2028: zero ``suggestions=`` anywhere in the handler (was:
        the seven GATHERING lists only, ten others kept)."""
        assert _HANDLER_SRC.read_text().count("suggestions=") == 0
        offenders = [
            f"line {call.lineno}"
            for call in _conversation_response_calls()
            if _kw(call, "suggestions") is not None
        ]
        assert offenders == []

    def test_no_gathering_response_sets_suggestions(self):
        offenders = []
        for call in _conversation_response_calls():
            state = _kw(call, "state")
            if (
                isinstance(state, ast.Attribute)
                and state.attr.startswith("GATHERING_")
                and _kw(call, "suggestions") is not None
            ):
                offenders.append(f"line {call.lineno}: {state.attr}")
        assert offenders == []

    def test_no_suggestion_list_offers_skip(self):
        offenders = []
        for call in _conversation_response_calls():
            value = _kw(call, "suggestions")
            if isinstance(value, ast.List) and any(
                isinstance(e, ast.Constant) and str(e.value).lower() == "skip" for e in value.elts
            ):
                offenders.append(f"line {call.lineno}")
        assert offenders == []


class TestInterviewQuestionsDriven:
    @pytest.mark.asyncio
    async def test_each_question_has_empty_suggestions_and_typed_skip_advances(self):
        manager = FakeStandupConversationManager()
        handler = StandupConversationHandler(conversation_manager=manager)
        conv = await manager.create_conversation("sess-2028", "user-2028")

        first = await handler.handle_turn(conv, "yes")
        assert first.state == S.GATHERING_YESTERDAY
        assert first.suggestions == []

        conv = await manager.get_conversation(conv.id)
        today = await handler.handle_turn(conv, "skip")
        assert today.state == S.GATHERING_TODAY
        assert today.suggestions == []

        conv = await manager.get_conversation(conv.id)
        blockers = await handler.handle_turn(conv, "nothing")
        assert blockers.state == S.GATHERING_BLOCKERS
        assert blockers.suggestions == []


class TestRepliesSayTheAnswerInWords:
    """CXO 10:10: where a deleted list carried the only hint of the expected
    answer, the reply says it in words, as a statement (no new ask)."""

    def test_the_refining_draft_names_looks_good(self):
        from services.standup.conversation_handler import (
            _REFINING_DEFAULT_ASK,
            _REFINING_FINALIZE_HINT,
        )

        assert _REFINING_FINALIZE_HINT == "Say 'looks good' to finalize it."
        assert "?" not in _REFINING_FINALIZE_HINT
        src = _HANDLER_SRC.read_text()
        # both "Here's your standup" arm sites carry the hint after the ask
        assert src.count("{_REFINING_DEFAULT_ASK} {_REFINING_FINALIZE_HINT}") == 2
        assert _REFINING_DEFAULT_ASK == "Would you like to make any changes?"

    def test_the_generation_error_names_try_again(self):
        assert "Say 'try again' and I'll rebuild it." in _HANDLER_SRC.read_text()
