"""#2010 -- "list my projects" made two offers nothing was armed to keep.

Empty state: now the #852 manage_portfolio string + an armed offer, so a
"yes" starts the add-project flow ("import an existing project" is gone: no
chat path exists). Non-empty: the closing question is dropped (the list
stands on its own).

#2035 (Arch's rule, CXO's shape B, 2026-10-15): the offer's "yes" leads to a
WRITE, so it is armed on the #846 one-slot store with the offer_add_project
landing, no longer the #852 contextual hint. The full yes / decline / name
flow is pinned in tests/unit/services/intent_service/test_write_offers_846_2035.py.
"""

import ast
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

import pytest

from services.consciousness import files_consciousness as fc
from services.consciousness.files_consciousness import (
    empty_projects_message,
    empty_projects_offer,
    format_projects_conscious,
)
from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.classifier import IntentClassifier
from services.shared_types import IntentCategory

_USER = "3f7b8a52-1666-4b00-9e00-000000002010"
EXPECTED = "You don't have any active projects yet. Would you like to add a project?"


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


@pytest.fixture
def live_service():
    from services.intent_service.workflow_entries import register_default_workflows

    register_default_workflows()
    return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


def _stub_list_projects(monkeypatch, service, seen):
    intent = Intent(
        category=IntentCategory.QUERY,
        action="list_projects",
        original_message="list my projects",
        confidence=0.95,
        context={"original_message": "list my projects"},
    )

    async def _classify_multiple(msg, context=None, user_id=None, session_id=None):
        seen.append(context)
        return SimpleNamespace(
            intents=[intent],
            is_multi_intent=False,
            has_greeting=False,
            has_substantive_intent=True,
            primary_intent=intent,
            secondary_intents=[],
        )

    monkeypatch.setattr(service.intent_classifier, "classify_multiple", _classify_multiple)


def _stub_portfolio(monkeypatch, projects):
    from contextlib import asynccontextmanager

    from services.database.session_factory import AsyncSessionFactory
    from services.onboarding.portfolio_service import PortfolioService

    @asynccontextmanager
    async def _scope():
        yield object()

    async def _list_active(self, user_id):
        return projects

    monkeypatch.setattr(AsyncSessionFactory, "session_scope", staticmethod(_scope))
    monkeypatch.setattr(PortfolioService, "list_active_projects", _list_active)


class TestEmptyState:
    def test_returns_the_852_string(self):
        assert empty_projects_message() == EXPECTED

    def test_formatter_never_asks_on_empty(self):
        # The formatter cannot arm, so it must not render the empty-state
        # question; callers render empty_projects_message() and arm it.
        assert "?" not in format_projects_conscious([])

    def test_message_question_is_the_offer_text(self):
        # The acceptance judge reads the stored question as the held ask
        # (#1739 a / #1665).
        question = EXPECTED.split(". ", 1)[1]
        assert question == empty_projects_offer()["question"]
        assert empty_projects_message().endswith(empty_projects_offer()["question"])

    def test_offer_is_an_846_record_with_the_add_project_landing(self):
        # #2035 (was the #852 hint's keys/values: ruled away).
        offer = empty_projects_offer(_USER)
        assert offer["workflow_type"] == "offer_add_project"
        assert offer["question"] == "Would you like to add a project?"
        assert offer["pending_action"]["kind"] == "add_project_offer_question"
        assert offer["pending_action"]["user_id"] == _USER
        assert offer["decline_message"] == (
            "Okay, I'll leave it for now. Say 'add a project' any time."
        )
        assert "continuation_hint" not in offer

    def test_import_clause_is_gone(self):
        src = Path("services/consciousness/files_consciousness.py").read_text()
        assert "import an existing project" not in src
        assert "import an existing project" not in empty_projects_message()

    def test_both_renderers_read_the_one_source(self):
        canon = Path("services/intent_service/canonical_handlers.py").read_text()
        assert "response = empty_projects_message()" in canon
        assert "empty_projects_offer(user_id)" in canon
        assert '"Would you like to add a project?"' not in canon
        assert "Would you like to add a project?" in Path(fc.__file__).read_text()
        svc = Path("services/intent/intent_service.py").read_text()
        assert "message = empty_projects_message()" in svc
        assert "empty_projects_offer(user_id)" in svc
        assert "empty_projects_offer_hint" not in canon + svc

    def test_strings_are_functions_not_module_constants(self):
        # Arch 2026-10-15: a module constant cannot be consumer-armed under
        # the census's one-hop rule; the question lives only inside functions.
        tree = ast.parse(Path(fc.__file__).read_text())
        for node in tree.body:
            if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
                for sub in ast.walk(node.value):
                    assert not (
                        isinstance(sub, ast.Constant)
                        and isinstance(sub.value, str)
                        and "?" in sub.value
                    ), f"module-level question constant at line {node.lineno}"


@pytest.mark.asyncio
class TestArmedOffer:
    async def test_empty_list_arms_the_846_offer_not_the_852_hint(self, monkeypatch, live_service):
        # #2035: was "yes steers the classifier with the add-project hint"
        # (the #852 rail), the behaviour Arch ruled away. Now the offer holds
        # the #846 slot and "yes" never reaches the classifier.
        from services.intent_service.conversation_context import get_or_create_context

        seen: list = []
        _stub_list_projects(monkeypatch, live_service, seen)
        _stub_portfolio(monkeypatch, [])
        sid = str(uuid4())

        result = await live_service.process_intent(
            message="list my projects", session_id=sid, user_id=_USER
        )
        assert result.message == EXPECTED
        assert get_or_create_context(sid, user_id=_USER).last_offer is None
        offer = live_service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER)
        assert offer is not None
        assert offer["workflow_type"] == "offer_add_project"
        assert offer["question"] == "Would you like to add a project?"

        calls = len(seen)
        result = await live_service.process_intent(message="yes", session_id=sid, user_id=_USER)
        assert result.message == "What would you like to call it?"
        assert len(seen) == calls  # the classifier never saw the "yes"

    async def test_non_empty_reply_arms_nothing_and_ends_plainly(self, monkeypatch, live_service):
        from services.intent_service.conversation_context import get_or_create_context

        seen: list = []
        _stub_list_projects(monkeypatch, live_service, seen)
        _stub_portfolio(monkeypatch, [SimpleNamespace(name="Alpha", is_archived=False)])
        sid = str(uuid4())

        result = await live_service.process_intent(
            message="list my projects", session_id=sid, user_id=_USER
        )
        assert "Alpha" in result.message
        assert "?" not in result.message
        assert get_or_create_context(sid, user_id=_USER).last_offer is None
        assert live_service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER) is None


class TestNonEmptyRenderer:
    def test_no_closing_question(self):
        out = format_projects_conscious(
            [{"name": "A", "active": True}, {"name": "B", "active": False}]
        )
        assert "?" not in out
        assert out.rstrip().endswith("(inactive)")
        assert "show you the files" not in out
