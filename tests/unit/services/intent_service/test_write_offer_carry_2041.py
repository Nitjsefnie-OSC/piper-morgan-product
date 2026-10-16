"""#2041: a composed (multi-intent) turn carries a sibling's #2035
``write_offer`` and arms it, the way #2030 carries ``offer_hint``.

Arch's ruling (on the issue, 2026-10-15; CXO concurs):

1. ``IntentExecutionResult`` carries ``write_offer``; the orchestrator does no
   store writes.
2. A write offer OUTRANKS a contextual hint. Within one kind, the first
   SUCCESSFUL sibling in plan order wins.
3. Every non-winner's question is stripped from its sibling's text by EXACT
   match (a write offer's question is the record's ``question``; a hint's is
   its ``offer_text``). A drifted question arms nothing and renders no
   question.
4. The winner's question goes LAST, as its own paragraph, once.
5. IntentService arms the winner through ``_arm_write_offer`` (or
   ``_track_offer_hint`` for a hint) BEFORE ``_apply_soft_offer``, so #1770
   first-arm-wins holds the slot.

Before the fix, ``_execute_single`` kept ``offer_hint`` but dropped
``write_offer``: "what time is it and list my projects" on a no-projects
account rendered "Would you like to add a project?" with nothing armed, and a
"yes" fell into the classifier. The source-level pin is check (d) of
``test_2035_write_offer_reach_tripwire`` in tests/test_architecture_enforcement.py.

Layer: the real ``IntentOrchestrator`` and ``IntentService.process_intent``
with the classifier's LLM explosive (any LLM call fails the test) and
``classify_multiple`` stubbed per turn. The headline pin runs the REAL
canonical handlers (time, and the manage_portfolio list branch with the DB
mocked to no projects); the precedence pins replace ``CanonicalHandlers.handle``
with per-category replies built from the real records.
"""

from __future__ import annotations

import contextlib
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from services.consciousness.files_consciousness import (
    empty_projects_message,
    empty_projects_offer,
)
from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.add_project_clarify import (
    ADD_PROJECT_NAME_QUESTION_KIND,
    OFFER_ADD_PROJECT_WORKFLOW,
)
from services.intent_service.canonical_handlers import CanonicalHandlers
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.intent_service.orchestrator import (
    IntentExecutionResult,
    IntentOrchestrator,
    OrchestratedResponse,
)
from services.intent_service.pre_classifier import MultiIntentResult
from services.shared_types import IntentCategory

MESSAGE = "what time is it and list my projects"
_USER = "3f7b8a52-2041-4b00-9e00-000000002041"
NAME_Q = "What would you like to call it?"
CONSENT = "Quick check before I act"

# The real empty-projects reply and its #846 record (one source).
EMPTY_MSG = empty_projects_message()
EMPTY_OFFER = empty_projects_offer(_USER)
EMPTY_Q = EMPTY_OFFER["question"]
assert EMPTY_Q == "Would you like to add a project?"

# The real setup-guidance reply and its #846 record (#2024 copy, #2035 record).
_SETUP = CanonicalHandlers()._format_project_setup_guidance()
SETUP_MSG = _SETUP["message"]
SETUP_OFFER = _SETUP["write_offer"]
SETUP_Q = SETUP_OFFER["question"]
assert SETUP_Q in SETUP_MSG

# A #852 contextual hint FIXTURE (the offer_hint contract shape) for the
# hint-vs-write precedence pins; its question renders verbatim in its reply.
HINT_Q = "Want me to walk you through connecting your calendar?"
HINT_MSG = f"Your calendar isn't connected yet. {HINT_Q}"
HINT = {"continuation_hint": "connect calendar", "offer_text": HINT_Q}


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


def _intent(category: IntentCategory, action: str, message: str = MESSAGE) -> Intent:
    return Intent(
        category=category,
        action=action,
        confidence=1.0,
        original_message=message,
        context={"original_message": message},
    )


TIME = _intent(IntentCategory.TEMPORAL, "get_current_time")
PORTFOLIO = _intent(IntentCategory.PORTFOLIO, "manage_portfolio")
GUIDANCE = _intent(IntentCategory.GUIDANCE, "provide_setup_guidance")


def _plan(*intents, message=MESSAGE):
    return MultiIntentResult(
        intents=list(intents), original_message=message, is_multi_intent=len(intents) > 1
    )


class _Classify:
    """Per-turn classify_multiple stub: records every message and returns the
    plan queued for it. A turn the #846 offer seam owns never gets here."""

    def __init__(self, monkeypatch, service):
        self.seen: list[str] = []
        self.next: MultiIntentResult | None = None
        monkeypatch.setattr(service.intent_classifier, "classify_multiple", self._classify)

    async def _classify(self, msg, context=None, user_id=None, session_id=None):
        self.seen.append(msg)
        assert self.next is not None, f"classifier reached for {msg!r}"
        plan, self.next = self.next, None
        return plan


@pytest.fixture(autouse=True)
def _router_consult_binds(monkeypatch):
    """The #1886(b) armed-turn router consult: "none" (BIND), no router call."""
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


class _FakeScope:
    async def __aenter__(self):
        return MagicMock()

    async def __aexit__(self, *exc):
        return False


@pytest.fixture
def no_projects(monkeypatch):
    """The portfolio list read returns no projects; every create is recorded."""
    from services.database.repositories import ProjectRepository
    from services.database.session_factory import AsyncSessionFactory
    from services.onboarding.portfolio_service import PortfolioService

    created: list[dict] = []

    async def _list_active(_self, user_id):
        return []

    async def _create(_self, **kwargs):
        created.append(kwargs)
        return MagicMock(id="proj-2041", name=kwargs.get("name"))

    monkeypatch.setattr(AsyncSessionFactory, "session_scope", staticmethod(lambda: _FakeScope()))
    monkeypatch.setattr(PortfolioService, "list_active_projects", _list_active)
    monkeypatch.setattr(ProjectRepository, "create", _create)
    return created


@contextlib.contextmanager
def _write_path_explosive():
    """A "yes" to the offer must never reach the add_project write or #1509."""

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


def _last_offer(sid):
    return get_or_create_context(sid, user_id=_USER).last_offer


def _reply(message, *, hint=None, write_offer=None):
    out = {"message": message, "intent": {"category": "c", "action": "x"}}
    if hint is not None:
        out["offer_hint"] = dict(hint)
    if write_offer is not None:
        out["write_offer"] = dict(write_offer)
    return out


def _stub_handle(service, monkeypatch, replies):
    """Replace CanonicalHandlers.handle (shared by the service and its
    orchestrator) with per-category replies; a callable value raises."""

    async def handle(intent, session_id, user_id=None):
        reply = replies[intent.category]
        if isinstance(reply, Exception):
            raise reply
        return reply

    monkeypatch.setattr(service.canonical_handlers, "handle", AsyncMock(side_effect=handle))


# ---------------------------------------------------------------------------
# The headline pin: real handlers, the composed turn, then "yes".
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
class TestComposedTurnArmsTheWriteOffer:
    async def test_time_and_list_projects_arms_and_yes_asks_the_name(
        self, monkeypatch, svc, no_projects
    ):
        clf = _Classify(monkeypatch, svc)
        assert svc._is_orchestratable_sibling(TIME)
        assert svc._is_orchestratable_sibling(PORTFOLIO)
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())

        with (
            patch.object(svc, "_arm_write_offer", wraps=svc._arm_write_offer) as arm,
            patch.object(svc, "_track_offer_hint", wraps=svc._track_offer_hint) as track,
        ):
            first = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        assert first.multi_intent_orchestrated
        # the write offer is armed on the #846 store with its own landing
        armed = _peek(svc, sid)
        assert armed is not None
        assert armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW
        assert armed["question"] == EMPTY_Q
        assert armed["pending_action"]["user_id"] == _USER
        # through the single path's own arming method, before the hint seam
        arm.assert_called_once()
        assert arm.call_args.args[0]["write_offer"]["question"] == EMPTY_Q
        track.assert_called_once_with({"offer_hint": None}, sid, _USER)
        assert _last_offer(sid) is None  # never the #852 hint
        # the question renders once, as its own last paragraph
        assert first.message.count(EMPTY_Q) == 1
        assert first.message.endswith(f"\n\n{EMPTY_Q}")
        assert "Regarding your portfolio, you don't have any active projects yet." in (
            first.message
        )

        seen = len(clf.seen)
        with _write_path_explosive():
            yes = await svc.process_intent(message="yes", session_id=sid, user_id=_USER)
        assert yes.message == NAME_Q
        assert CONSENT not in yes.message
        assert len(clf.seen) == seen  # the classifier never saw the "yes"
        assert no_projects == []
        name_q = _peek(svc, sid)
        assert name_q["question"] == NAME_Q
        assert name_q["pending_action"]["kind"] == ADD_PROJECT_NAME_QUESTION_KIND

    async def test_single_intent_list_projects_is_unchanged(self, monkeypatch, svc, no_projects):
        """The single path renders the handler's message as-is (no stripping,
        no reordering) and arms through _process_intent_internal."""
        clf = _Classify(monkeypatch, svc)
        clf.next = _plan(_intent(IntentCategory.PORTFOLIO, "manage_portfolio", "list my projects"))
        sid = str(uuid4())
        result = await svc.process_intent(message="list my projects", session_id=sid, user_id=_USER)
        assert result.message == EMPTY_MSG
        assert _peek(svc, sid)["question"] == EMPTY_Q


# ---------------------------------------------------------------------------
# Precedence: write offer over hint; first in plan order within a kind.
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
class TestPrecedence:
    @pytest.mark.parametrize("hint_first", [True, False])
    async def test_hint_and_write_offer_arms_the_write_offer_only(
        self, monkeypatch, svc, hint_first
    ):
        clf = _Classify(monkeypatch, svc)
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply(HINT_MSG, hint=HINT),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, write_offer=EMPTY_OFFER),
            },
        )
        clf.next = _plan(TIME, PORTFOLIO) if hint_first else _plan(PORTFOLIO, TIME)
        sid = str(uuid4())
        result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        assert _peek(svc, sid)["question"] == EMPTY_Q
        assert _last_offer(sid) is None  # the hint is not armed
        assert HINT_Q not in result.message  # its question is stripped
        assert "calendar isn't connected yet." in result.message
        assert result.message.count("?") == 1
        assert result.message.endswith(f"\n\n{EMPTY_Q}")

    async def test_two_write_offer_siblings_the_first_in_plan_order_wins(self, monkeypatch, svc):
        """The stub is keyed by category; GUIDANCE is not an orchestratable
        sibling (#1763), so the setup-guidance reply rides the TEMPORAL
        sibling (the #2030 pins' fixture shape)."""
        clf = _Classify(monkeypatch, svc)
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply(SETUP_MSG, write_offer=SETUP_OFFER),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, write_offer=EMPTY_OFFER),
            },
        )
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())
        result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        armed = _peek(svc, sid)
        assert armed["question"] == SETUP_Q
        assert armed["pending_action"]["user_id"] == _USER  # stamped at the seam
        assert EMPTY_Q not in result.message
        assert result.message.count(SETUP_Q) == 1
        assert result.message.endswith(f"\n\n{SETUP_Q}")
        assert result.message.count("?") == 1

    async def test_a_failed_write_offer_sibling_contributes_nothing(self, monkeypatch, svc):
        clf = _Classify(monkeypatch, svc)
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: RuntimeError("portfolio down"),
            },
        )
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())
        result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        assert _peek(svc, sid) is None
        assert _last_offer(sid) is None
        assert EMPTY_Q not in result.message
        assert "?" not in result.message

    async def test_drift_arms_nothing_and_asks_no_question(self, monkeypatch, svc):
        """The record's question is not verbatim in the rendered reply: the
        sibling arms nothing, nothing is appended, its text stays as rendered."""
        clf = _Classify(monkeypatch, svc)
        drifted = {**EMPTY_OFFER, "question": "Want to add one?"}
        rendered = "You don't have any active projects yet."
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(rendered, write_offer=drifted),
            },
        )
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())
        result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        assert _peek(svc, sid) is None
        assert _last_offer(sid) is None
        assert "?" not in result.message
        assert result.message == "It's 3:15 PM. Regarding your portfolio, " + (
            "you don't have any active projects yet."
        )

    async def test_drifted_write_offer_lets_the_hint_win(self, monkeypatch, svc):
        """A drifted write offer is not a winner, so the hint sibling arms."""
        clf = _Classify(monkeypatch, svc)
        drifted = {**EMPTY_OFFER, "question": "Want to add one?"}
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply(HINT_MSG, hint=HINT),
                IntentCategory.PORTFOLIO: _reply(
                    "You don't have any active projects yet.", write_offer=drifted
                ),
            },
        )
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())
        result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)

        assert _peek(svc, sid) is None
        assert _last_offer(sid).offer_text == HINT_Q
        assert result.message.count("?") == 1
        assert result.message.endswith(f"\n\n{HINT_Q}")

    async def test_write_offer_plus_soft_offer_candidate_asks_once(self, monkeypatch, svc):
        """#1770: the armed write offer is live before _apply_soft_offer, so a
        live soft candidate is skipped."""
        clf = _Classify(monkeypatch, svc)
        _stub_handle(
            svc,
            monkeypatch,
            {
                IntentCategory.TEMPORAL: _reply("It's 3:15 PM."),
                IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, write_offer=EMPTY_OFFER),
            },
        )
        offer = MagicMock(workflow_type="soft_wf", offer_message="SOFT ASK?", decline_message="ok")
        detection = MagicMock(has_offer=True, offer=offer)
        clf.next = _plan(TIME, PORTFOLIO)
        sid = str(uuid4())
        with (
            patch.object(svc.soft_invocation_detector, "detect", return_value=detection),
            patch.object(svc.workflow_offer_service, "should_offer", return_value=(True, "ok")),
            patch.object(
                svc.workflow_offer_service,
                "format_offer",
                side_effect=lambda o, m: f"{m}\n\n{o.offer_message}",
            ),
        ):
            result = await svc.process_intent(message=MESSAGE, session_id=sid, user_id=_USER)
        assert "SOFT ASK?" not in result.message
        assert result.message.count("?") == 1
        assert _peek(svc, sid)["question"] == EMPTY_Q


# ---------------------------------------------------------------------------
# The orchestrator alone: carry, pick, compose (no store writes).
# ---------------------------------------------------------------------------


class TestOrchestratorPick:
    def _orch(self):
        return IntentOrchestrator(canonical_handlers=MagicMock())

    def test_a_failed_write_offer_sibling_arms_nothing(self):
        orch = self._orch()
        failed = IntentExecutionResult(
            intent=PORTFOLIO, response=EMPTY_MSG, success=False, write_offer=dict(EMPTY_OFFER)
        )
        ok = IntentExecutionResult(intent=TIME, response="It's 3:15 PM.", success=True)
        response = OrchestratedResponse(results=[ok, failed], has_partial_failure=True)
        response.armed_write_offer = orch._pick_armed_write_offer(response.results)
        assert response.armed_write_offer is None
        assert "?" not in orch._aggregate_messages(response)

    def test_a_failed_first_write_offer_lets_the_first_successful_one_arm(self):
        orch = self._orch()
        failed = IntentExecutionResult(
            intent=GUIDANCE, response=SETUP_MSG, success=False, write_offer=dict(SETUP_OFFER)
        )
        ok = IntentExecutionResult(
            intent=PORTFOLIO, response=EMPTY_MSG, success=True, write_offer=dict(EMPTY_OFFER)
        )
        assert orch._pick_armed_write_offer([failed, ok]) == EMPTY_OFFER

    @pytest.mark.asyncio
    async def test_execute_plan_carries_and_the_write_offer_outranks_the_hint(self):
        handlers = CanonicalHandlers()
        replies = {
            IntentCategory.TEMPORAL: _reply(HINT_MSG, hint=HINT),
            IntentCategory.PORTFOLIO: _reply(EMPTY_MSG, write_offer=EMPTY_OFFER),
        }
        handlers.handle = AsyncMock(side_effect=lambda i, s, u=None: replies[i.category])
        orch = IntentOrchestrator(canonical_handlers=handlers)
        out = await orch.execute_plan(orch.create_plan(_plan(TIME, PORTFOLIO)), "s", None)

        assert out.results[0].offer_hint == HINT  # carried
        assert out.results[1].write_offer == EMPTY_OFFER  # carried
        assert out.armed_write_offer == EMPTY_OFFER
        assert out.armed_offer_hint is None
        assert out.aggregated_message == (
            "Your calendar isn't connected yet. Regarding your portfolio, "
            f"you don't have any active projects yet.\n\n{EMPTY_Q}"
        )
