"""#2035 — a yes that leads to a write arms the #846 one-slot store with its
own landing, never the #852 contextual hint (Arch's rule, 2026-10-15; CXO
picked shape B the same day).

The served defect (Web, 6f2916d10f): on an account with no projects,
``list my projects`` -> "You don't have any active projects yet. Would you
like to add one?" -> ``yes`` -> the #1509 consent check ("Quick check before
I act: I'm reading that as asking me to add project…"), because the offer
armed the #852 contextual rail: "yes" steered the classifier into the
add_project WRITE, and that write passes consent (#1739).

Shape B (CXO, verbatim):
- the offer text stays;
- ``yes`` -> "What would you like to call it?" through a new accept landing
  (``offer_add_project``) that arms the existing add-project NAME question;
  no consent line, the router write path is never reached;
- only a name writes (the existing name rail, then its existing create);
- decline (``no``, ``not now``, ``later``) -> "Okay, I'll leave it for now.
  Say 'add a project' any time." (a statement; nothing armed);
- the same for "Are you ready to set up your first project?" and "Want to
  add another?"; the integration-setup offer (a READ) stays contextual.

Layer: the real ``IntentService.process_intent`` for every turn, with the
classifier stubbed per turn and the LLM boundary explosive (the #2010 pin's
seam); the name turn's armed-turn router consult is stubbed to "none" (the
#1886 pin's seam) and the create runs the REAL ``_create_or_report_project``
with the DB mocked.
"""

from __future__ import annotations

import contextlib
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.add_project_clarify import (
    ADD_PROJECT_NAME_QUESTION_KIND,
    ADD_PROJECT_OFFER_KIND,
    OFFER_ADD_PROJECT_WORKFLOW,
    build_add_project_offer,
    handle_add_project_offer_turn,
)
from services.intent_service.canonical_handlers import CanonicalHandlers
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.shared_types import IntentCategory

_USER = "3f7b8a52-2035-4b00-9e00-000000002035"
EMPTY = "You don't have any active projects yet. Would you like to add a project?"
NAME_Q = "What would you like to call it?"
DECLINE = "Okay, I'll leave it for now. Say 'add a project' any time."
CONSENT = "Quick check before I act"


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


@pytest.fixture(autouse=True)
def _router_consult_binds(monkeypatch):
    """The name answer turn runs the #1886(b) armed-turn router consult;
    "none" means BIND (the #1886 pin's default), with no router call."""
    from services.intent_service import inversion_router as ir
    from services.intent_service.inversion_router import RoutingDecision

    async def _route(message, session_state=None, **kwargs):
        return RoutingDecision(outcome="none")

    monkeypatch.setattr(ir, "route", _route)


@pytest.fixture
def svc():
    from services.intent_service.workflow_entries import register_default_workflows

    register_default_workflows()
    return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


class _Classify:
    """Per-turn classifier stub: records every message it sees and returns
    the intent queued for it. A turn the offer seam owns must never get
    here."""

    def __init__(self, monkeypatch, service):
        self.seen: list[str] = []
        self.next: Intent | None = None
        monkeypatch.setattr(service.intent_classifier, "classify_multiple", self._classify)

    async def _classify(self, msg, context=None, user_id=None, session_id=None):
        self.seen.append(msg)
        assert self.next is not None, f"classifier reached for {msg!r}"
        intent, self.next = self.next, None
        return SimpleNamespace(
            intents=[intent],
            is_multi_intent=False,
            has_greeting=False,
            has_substantive_intent=True,
            primary_intent=intent,
            secondary_intents=[],
        )


def _intent(message, category, action):
    return Intent(
        category=category,
        action=action,
        original_message=message,
        confidence=0.95,
        context={"original_message": message},
    )


class _FakeScope:
    async def __aenter__(self):
        return MagicMock()

    async def __aexit__(self, *exc):
        return False


class _Db:
    """The portfolio list read and the create write, both mocked; records
    every create so "nothing created" is measured, not assumed."""

    def __init__(self, monkeypatch, projects):
        from services.database.repositories import ProjectRepository
        from services.database.session_factory import AsyncSessionFactory
        from services.onboarding.portfolio_service import PortfolioService

        self.created: list[dict] = []
        created = MagicMock()
        created.id = "proj-2035"

        async def _list_active(_self, user_id):
            return projects

        async def _create(_self, **kwargs):
            self.created.append(kwargs)
            created.name = kwargs.get("name")
            return created

        async def _find_by_name(_self, **kwargs):
            return None

        monkeypatch.setattr(
            AsyncSessionFactory, "session_scope", staticmethod(lambda: _FakeScope())
        )
        monkeypatch.setattr(PortfolioService, "list_active_projects", _list_active)
        monkeypatch.setattr(ProjectRepository, "create", _create)
        monkeypatch.setattr(ProjectRepository, "find_by_name", _find_by_name)


@contextlib.contextmanager
def _write_path_explosive():
    """The router write path (the add_project rail / canonical add) and the
    #1509 consent builder must not be reached by a "yes" to the offer."""

    def _boom(*a, **k):
        raise AssertionError("write path reached from the offer's yes")

    with (
        patch.object(CanonicalHandlers, "_handle_add_project", _boom),
        patch.object(CanonicalHandlers, "_create_or_report_project", _boom),
        patch("services.intent_service.consent_gate.build_consent_check_offer", _boom),
    ):
        yield


def _peek(service, sid):
    return service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER)


# ---------------------------------------------------------------------------
# The three write offers, each with how to reach it through process_intent.
# ---------------------------------------------------------------------------


def _list_projects_rail(clf, db_projects=()):
    """IntentService._handle_projects_query (the served path)."""
    clf.next = _intent("list my projects", IntentCategory.QUERY, "list_projects")
    return "list my projects", EMPTY, "Would you like to add a project?"


def _manage_portfolio_list(clf, db_projects=()):
    """The manage_portfolio list branch (CanonicalHandlers.handle dispatch)."""
    clf.next = _intent("list my projects", IntentCategory.PORTFOLIO, "manage_portfolio")
    return "list my projects", EMPTY, "Would you like to add a project?"


@pytest.mark.asyncio
class TestEmptyProjectsOffer:
    @pytest.mark.parametrize("route", [_list_projects_rail, _manage_portfolio_list])
    async def test_offer_arms_846_and_yes_asks_the_name_with_no_consent_and_no_write(
        self, monkeypatch, svc, route
    ):
        clf = _Classify(monkeypatch, svc)
        db = _Db(monkeypatch, [])
        sid = str(uuid4())

        msg, expected, question = route(clf)
        first = await svc.process_intent(message=msg, session_id=sid, user_id=_USER)
        assert first.message == expected
        armed = _peek(svc, sid)
        assert armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW
        assert armed["question"] == question
        assert armed["pending_action"]["kind"] == ADD_PROJECT_OFFER_KIND
        assert armed["pending_action"]["user_id"] == _USER
        # Off the #852 rail: no contextual hint for "yes" to steer.
        assert get_or_create_context(sid, user_id=_USER).last_offer is None

        seen = len(clf.seen)
        with _write_path_explosive():
            yes = await svc.process_intent(message="yes", session_id=sid, user_id=_USER)
        assert yes.message == NAME_Q
        assert CONSENT not in yes.message
        assert len(clf.seen) == seen  # the classifier never saw the "yes"
        assert db.created == []
        name_q = _peek(svc, sid)
        assert name_q["workflow_type"] == "clarify_add_project_name"
        assert name_q["question"] == NAME_Q
        assert name_q["pending_action"]["kind"] == ADD_PROJECT_NAME_QUESTION_KIND

        # Only a name writes: the existing name rail and its existing create.
        named = await svc.process_intent(message="Klatch", session_id=sid, user_id=_USER)
        assert [c["name"] for c in db.created] == ["Klatch"]
        assert "Added Klatch to your portfolio" in named.message
        assert CONSENT not in named.message
        assert _peek(svc, sid) is None

    @pytest.mark.parametrize("decline", ["no", "not now", "later"])
    @pytest.mark.parametrize("route", [_list_projects_rail, _manage_portfolio_list])
    async def test_decline_gives_cxos_line_and_creates_nothing(
        self, monkeypatch, svc, route, decline
    ):
        clf = _Classify(monkeypatch, svc)
        db = _Db(monkeypatch, [])
        sid = str(uuid4())

        msg, expected, _q = route(clf)
        await svc.process_intent(message=msg, session_id=sid, user_id=_USER)
        seen = len(clf.seen)
        with _write_path_explosive():
            out = await svc.process_intent(message=decline, session_id=sid, user_id=_USER)
        assert out.message == DECLINE
        assert len(clf.seen) == seen
        assert db.created == []
        assert _peek(svc, sid) is None  # a statement: nothing armed
        assert get_or_create_context(sid, user_id=_USER).last_offer is None

    async def test_name_question_decline_is_the_existing_name_rail_line(self, monkeypatch, svc):
        # After "yes", the name question is the EXISTING #1886 rail: its own
        # decline copy, unchanged.
        clf = _Classify(monkeypatch, svc)
        db = _Db(monkeypatch, [])
        sid = str(uuid4())
        _list_projects_rail(clf)
        await svc.process_intent(message="list my projects", session_id=sid, user_id=_USER)
        await svc.process_intent(message="yes", session_id=sid, user_id=_USER)
        out = await svc.process_intent(message="no", session_id=sid, user_id=_USER)
        assert out.message == "Okay — I haven't added a project. Nothing was created."
        assert db.created == []


# ---------------------------------------------------------------------------
# 2370 / 2473 — the project-setup guidance offers, through both seams a
# canonical dict reaches (the read_canonical rail adapter and the canonical
# dispatch).
# ---------------------------------------------------------------------------


def _setup_patches(projects, label="warm"):
    ctx = MagicMock()
    ctx.projects = list(projects)
    return [
        patch(
            "services.intent_service.canonical_handlers.user_context_service.get_user_context",
            new_callable=AsyncMock,
            return_value=ctx,
        ),
        patch("services.personality.formality.formality_label", return_value=label),
    ]


@pytest.mark.asyncio
class TestSetupGuidanceOffers:
    @pytest.mark.parametrize(
        "projects,question",
        [
            ([], "Are you ready to set up your first project?"),
            (["Alpha", "Beta"], "Want to add another?"),
        ],
    )
    @pytest.mark.parametrize("action", ["get_contextual_guidance", "provide_guidance"])
    async def test_yes_asks_the_name_and_decline_gives_cxos_line(
        self, monkeypatch, svc, projects, question, action
    ):
        clf = _Classify(monkeypatch, svc)
        db = _Db(monkeypatch, [])
        msg = "help me set up my projects"

        with contextlib.ExitStack() as stack:
            for p in _setup_patches(projects):
                stack.enter_context(p)

            # yes -> the name question
            sid = str(uuid4())
            clf.next = _intent(msg, IntentCategory.GUIDANCE, action)
            first = await svc.process_intent(message=msg, session_id=sid, user_id=_USER)
            assert first.message.rstrip().endswith(question)
            armed = _peek(svc, sid)
            assert armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW
            assert armed["question"] == question
            assert armed["pending_action"]["user_id"] == _USER  # stamped at the seam
            assert get_or_create_context(sid, user_id=_USER).last_offer is None
            with _write_path_explosive():
                yes = await svc.process_intent(message="yes", session_id=sid, user_id=_USER)
            assert yes.message == NAME_Q
            assert CONSENT not in yes.message
            assert db.created == []

            # decline -> CXO's line, nothing armed
            sid2 = str(uuid4())
            clf.next = _intent(msg, IntentCategory.GUIDANCE, action)
            await svc.process_intent(message=msg, session_id=sid2, user_id=_USER)
            out = await svc.process_intent(message="not now", session_id=sid2, user_id=_USER)
            assert out.message == DECLINE
            assert _peek(svc, sid2) is None
            assert db.created == []

    async def test_integration_setup_offer_stays_contextual(self, monkeypatch, svc):
        # The READ offer is unchanged: #852 hint, nothing on the #846 store.
        from services.integrations.integration_status_service import (
            IntegrationStatusService,
        )

        clf = _Classify(monkeypatch, svc)
        monkeypatch.setattr(
            IntegrationStatusService, "get_all", AsyncMock(return_value={"github": {}})
        )
        sid = str(uuid4())
        msg = "help me set up integrations"
        clf.next = _intent(msg, IntentCategory.GUIDANCE, "get_contextual_guidance")
        out = await svc.process_intent(message=msg, session_id=sid, user_id=_USER)
        assert "Would you like guidance on setting up a specific integration?" in out.message
        assert _peek(svc, sid) is None
        offer = get_or_create_context(sid, user_id=_USER).last_offer
        assert offer is not None and offer.offer_type == "contextual"
        assert offer.continuation_hint == "provide guidance on setting up a specific integration"
        assert offer.offer_text == "Would you like guidance on setting up a specific integration?"


# ---------------------------------------------------------------------------
# The one-slot rule (#1770 first-arm-wins) and the seam handler's edges.
# ---------------------------------------------------------------------------


class TestOneSlot:
    def test_write_offer_never_replaces_a_same_turn_arm(self, svc):
        sid = str(uuid4())
        live = {"workflow_type": "clarify_add_project_name", "question": "Q?"}
        svc.workflow_offer_service.set_pending_offer(sid, live, user_id=_USER)
        svc._arm_write_offer(
            {"write_offer": build_add_project_offer("Want to add another?")}, sid, _USER
        )
        assert _peek(svc, sid)["workflow_type"] == "clarify_add_project_name"

    def test_write_offer_arms_a_free_slot_and_stamps_the_principal(self, svc):
        sid = str(uuid4())
        svc._arm_write_offer(
            {"write_offer": build_add_project_offer("Want to add another?")}, sid, _USER
        )
        armed = _peek(svc, sid)
        assert armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW
        assert armed["pending_action"]["user_id"] == _USER

    @pytest.mark.asyncio
    async def test_empty_projects_offer_never_replaces_a_same_turn_arm(self, monkeypatch, svc):
        _Db(monkeypatch, [])
        sid = str(uuid4())
        live = {"workflow_type": "clarify_add_project_name", "question": "Q?"}
        svc.workflow_offer_service.set_pending_offer(sid, live, user_id=_USER)
        out = await svc._handle_projects_query(
            _intent("list my projects", IntentCategory.QUERY, "list_projects"),
            "wf",
            session_id=sid,
            user_id=_USER,
        )
        assert out.message == EMPTY
        assert _peek(svc, sid)["workflow_type"] == "clarify_add_project_name"


@pytest.mark.asyncio
class TestOfferTurnHandler:
    async def test_principal_mismatch_holds_off(self):
        out = await handle_add_project_offer_turn(
            build_add_project_offer("Want to add another?", user_id=_USER),
            "yes",
            session_id="s",
            user_id="someone-else",
        )
        assert out["intent_data"]["principal_mismatch"] is True

    @pytest.mark.parametrize("reply", ["yes", "Klatch", "what projects do I have?", ""])
    async def test_non_declines_fall_through_to_the_generic_seam(self, reply):
        out = await handle_add_project_offer_turn(
            build_add_project_offer("Want to add another?", user_id=_USER),
            reply,
            session_id="s",
            user_id=_USER,
        )
        assert out is None

    async def test_accept_landing_fails_closed_with_cxos_line_when_the_store_is_down(self):
        """CXO's four-calls memo item 2 (2026-10-15): if the accept landing
        cannot arm the name question, the reply asks nothing (no question a
        store does not hold) and names the working phrase, verbatim."""
        from services.intent_service.add_project_clarify import run_offer_add_project_workflow

        exploding = SimpleNamespace(
            workflow_offer_service=SimpleNamespace(
                set_pending_offer=MagicMock(side_effect=RuntimeError("store down"))
            )
        )
        offer = build_add_project_offer("Want to add another?", user_id=_USER)
        out = await run_offer_add_project_workflow(
            "s-2035-armfail",
            user_id=_USER,
            context={"pending_action": offer["pending_action"], "intent_service": exploding},
        )
        assert out["message"] == (
            "I lost track of that. Say 'add project' and a name, like "
            "'add project Launch', and I'll add it."
        )
        assert "?" not in out["message"]
        assert out["intent_data"]["add_project_name_question_pending"] is False
