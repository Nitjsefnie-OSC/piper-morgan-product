"""#2048 — "list my projects" must answer from code, never from the floor.

Served on alpha ``6bb955919d`` (Web, no-projects account, 3 of 3 across two
fresh chats): the reply was the floor's "I don't have your projects list in
front of me right now…", with ``manage_portfolio`` in the reply's intent body.

The path, reproduced here without an LLM:

1. Surface 1 no longer claims the phrase (the ``PORTFOLIO_LIST_PATTERN``
   literal was deleted 2026-10-11, #1595 Phase 3), so with the inversion flag
   empty — or with the router naming ``manage_portfolio``, which has no rail
   entry and so declines (``not_live_*`` / ``not_rail_dispatchable``) — the
   LLM classifier decides the turn.
2. The classifier emits category and action independently. Its own prompt
   teaches ``"list all projects" → {"category": "query", "action":
   "manage_portfolio"}`` (``prompts.py``, since 2026-07-09), so a
   ``(QUERY, manage_portfolio)`` pair is an expected draw.
3. ``QUERY`` is not a canonical category: ``can_handle`` declines, the rail
   has no ``manage_portfolio`` key, and ``_handle_query_intent`` →
   ``_handle_generic_query`` → ``_handle_unknown_intent`` (the floor), whose
   reply repeats the classifier's action — which is why the served body said
   ``manage_portfolio``. Every other non-PORTFOLIO category reaches the floor
   or a non-portfolio handler the same way (measured before the fix: 19 of
   the 19 non-PORTFOLIO categories missed the empty-state line; with the fix's
   call disabled, 22 of this file's pins fail).
4. ``IntentCache`` keys the classification by message text for an hour, so
   one bad draw serves every repeat ("3 of 3 across two fresh chats").

Not a code regression: the same dispatch, run against ``6f2916d10f``, sends
``(QUERY, manage_portfolio)`` to the floor too; the 10-15 build served the
code line because its draw (or its cached draw) was PORTFOLIO or
``list_projects``.

The fix (dispatch layer, no pattern, no catalog change):
``IntentService._adopt_canonical_portfolio_category`` — an action registered
in ``ACTION_REGISTRY`` only as a PORTFOLIO CANONICAL key takes the PORTFOLIO
category before the Action Gate, so ``_handle_portfolio_query``'s own
operation sniff answers it (list → the empty-state line, armed).

⚠️ LAYER HONESTY: the classifier and router are deterministic stubs. These
pins prove the DISPATCH for each classification the LLM can emit; they do not
prove which classification alpha's model draws. The served acceptance (3 of 3,
then ``yes`` → "What would you like to call it?") is CXO's, on a build.
"""

import contextlib

import pytest
import pytest_asyncio

aiosqlite = pytest.importorskip("aiosqlite")

from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from services.database.models import SessionActivityDB  # noqa: E402
from services.domain.models import Intent  # noqa: E402
from services.intent.intent_service import (  # noqa: E402
    IntentProcessingResult,
    IntentService,
)
from services.intent_service.add_project_clarify import (  # noqa: E402
    ADD_PROJECT_ACCEPT_NAME_QUESTION,
    OFFER_ADD_PROJECT_WORKFLOW,
)
from services.intent_service.classifier import IntentClassifier  # noqa: E402
from services.intent_service.inversion_router import RoutingDecision  # noqa: E402
from services.intent_service.pre_classifier import PreClassifier  # noqa: E402
from services.intent_service.workflow_dispatcher import get_action_workflows  # noqa: E402
from services.intent_service.workflow_entries import (  # noqa: E402
    register_default_workflows,
)
from services.shared_types import IntentCategory  # noqa: E402

_USER = "3f7b8a52-2048-4b00-9e00-000000002048"  # valid UUID: survives principal parsing
MSG = "list my projects"
EMPTY_LINE = "You don't have any active projects yet. Would you like to add a project?"
FLOOR = "FLOOR-SENTINEL (_handle_floor_with_context)"
UNKNOWN = "FLOOR-SENTINEL (_handle_unknown_intent)"

NON_PORTFOLIO = [c for c in IntentCategory if c is not IntentCategory.PORTFOLIO]


# ---------------------------------------------------------------------------
# Fixtures (the #1595 unit-4 harness shapes)
# ---------------------------------------------------------------------------


@pytest_asyncio.fixture
async def sm(monkeypatch):
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(lambda c: SessionActivityDB.__table__.create(c, checkfirst=True))
    maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    @contextlib.asynccontextmanager
    async def _scope():
        async with maker() as s:
            yield s

    import services.database.session_factory as sf

    monkeypatch.setattr(sf.AsyncSessionFactory, "session_scope", staticmethod(_scope))
    yield maker
    await engine.dispose()


@pytest.fixture
def mem_prefs(monkeypatch):
    store: dict = {_USER: {}}

    async def _load(user_id):
        return dict(store.get(str(user_id), {}))

    from services.intent_service import collaboration_gate

    monkeypatch.setattr(collaboration_gate, "_load_preferences", _load)
    return store


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    monkeypatch.delenv("PIPER_INVERSION_LIVE_CATEGORIES", raising=False)
    monkeypatch.delenv("PIPER_INVERSION_LIVE_MIN_CONFIDENCE", raising=False)
    monkeypatch.delenv("PIPER_INVERSION_SHADOW", raising=False)


@pytest.fixture(autouse=True)
def _rail_registered():
    register_default_workflows()


@pytest.fixture
def no_projects(monkeypatch):
    """The account has no projects (the served account's state)."""
    from services.onboarding.portfolio_service import PortfolioService

    async def _list(self, user_id=None, **kwargs):
        return []

    monkeypatch.setattr(PortfolioService, "list_active_projects", _list)


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


def _service(monkeypatch, *, category, action="manage_portfolio"):
    """IntentService whose LLM classifier draws ``(category, action)`` and
    whose two floor doors return sentinels (so a floor answer is visible and
    spends nothing)."""
    service = IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))
    calls = []

    async def _classify(message, *a, **k):
        calls.append(message)
        return Intent(
            category=category,
            action=action,
            confidence=0.9,
            original_message=message,
            context={"original_message": message},
        )

    monkeypatch.setattr(service.intent_classifier, "classify", _classify)

    async def _floor(self_, intent, *a, **k):
        return IntentProcessingResult(
            success=True, message=FLOOR, intent_data={"action": intent.action}
        )

    async def _unknown(self_, intent, *a, **k):
        return IntentProcessingResult(
            success=True, message=UNKNOWN, intent_data={"action": intent.action}
        )

    monkeypatch.setattr(IntentService, "_handle_floor_with_context", _floor)
    monkeypatch.setattr(IntentService, "_handle_unknown_intent", _unknown)
    service._classify_calls = calls  # type: ignore[attr-defined]
    return service


def _route_to(monkeypatch, op, confidence=0.95):
    from services.intent_service import inversion_router as ir

    async def _route(utterance, session_state=None, **kwargs):
        return RoutingDecision(outcome="operation", operation=op, confidence=confidence)

    monkeypatch.setattr(ir, "route", _route)


def _assert_empty_state_from_code(service, result, sid):
    assert result.message == EMPTY_LINE, result.message
    assert result.intent_data["category"] == IntentCategory.PORTFOLIO.value
    assert result.intent_data["action"] == "list_projects"
    assert result.intent_data["context"] == {"project_count": 0}
    armed = service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER)
    assert armed is not None, "the empty state's question was not armed"
    assert armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW
    assert armed["question"] == "Would you like to add a project?"


# ---------------------------------------------------------------------------
# 0. Why the LLM decides this phrase at all
# ---------------------------------------------------------------------------


class TestThePhraseReachesTheClassifier:
    def test_surface_one_does_not_claim_it(self):
        assert PreClassifier.pre_classify(MSG) is None
        assert PreClassifier.detect_multiple_intents(MSG).intents == []

    def test_manage_portfolio_has_no_rail_entry(self):
        """So a router decision naming it cannot dispatch live; the legacy
        chain (the classifier) answers the turn."""
        assert "manage_portfolio" not in get_action_workflows()

    def test_the_classifier_prompt_teaches_query_manage_portfolio(self):
        """The draw that reaches the floor is one the classifier's own prompt
        teaches. Recorded for Arch (catalog/prompt owner); not changed here."""
        from services.intent_service import prompts

        assert (
            '"list all projects" → {{"category": "query", "action": "manage_portfolio"'
            in prompts.INTENT_CLASSIFICATION_PROMPT
        )


# ---------------------------------------------------------------------------
# 1. The fix: every category the classifier can pair with manage_portfolio
# ---------------------------------------------------------------------------


class TestListMyProjectsAnswersFromCode:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("category", list(IntentCategory), ids=lambda c: c.value)
    async def test_empty_state_line_armed_whatever_the_category(
        self, monkeypatch, sm, mem_prefs, no_projects, category
    ):
        service = _service(monkeypatch, category=category)
        sid = f"sess-2048-{category.value}"
        result = await service.process_intent(MSG, session_id=sid, user_id=_USER)
        assert service._classify_calls == [MSG]
        _assert_empty_state_from_code(service, result, sid)

    @pytest.mark.asyncio
    async def test_yes_after_the_empty_state_asks_the_name(
        self, monkeypatch, sm, mem_prefs, no_projects
    ):
        """CXO's acceptance second half: the follow-up ``yes`` lands on the
        armed add-project offer, not the floor ("…pulled up…")."""
        service = _service(monkeypatch, category=IntentCategory.QUERY)
        sid = "sess-2048-yes"
        first = await service.process_intent(MSG, session_id=sid, user_id=_USER)
        _assert_empty_state_from_code(service, first, sid)
        second = await service.process_intent("yes", session_id=sid, user_id=_USER)
        assert second.message == ADD_PROJECT_ACCEPT_NAME_QUESTION, second.message
        assert service._classify_calls == [MSG], "the 'yes' reached the classifier"


# ---------------------------------------------------------------------------
# 2. The inversion flag set: the router's pick does not change the outcome
# ---------------------------------------------------------------------------


class TestWithTheInversionLive:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "live", ["PORTFOLIO", "read_status,read_portfolio,read_canonical,PORTFOLIO,QUERY"]
    )
    async def test_router_names_manage_portfolio_then_classifier_draws_query(
        self, monkeypatch, sm, mem_prefs, no_projects, live
    ):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", live)
        _route_to(monkeypatch, "manage_portfolio")
        service = _service(monkeypatch, category=IntentCategory.QUERY)
        sid = f"sess-2048-live-{len(live)}"
        result = await service.process_intent(MSG, session_id=sid, user_id=_USER)
        assert service._classify_calls == [MSG], "the consult should have declined"
        _assert_empty_state_from_code(service, result, sid)

    @pytest.mark.asyncio
    async def test_router_names_list_projects_control(
        self, monkeypatch, sm, mem_prefs, no_projects
    ):
        """Control: the router's other legitimate pick (``list_projects``,
        read_status) dispatches live and never asks the classifier."""
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_status")
        _route_to(monkeypatch, "list_projects")
        service = _service(monkeypatch, category=IntentCategory.QUERY)
        sid = "sess-2048-live-control"
        result = await service.process_intent(MSG, session_id=sid, user_id=_USER)
        assert service._classify_calls == []
        assert result.message == EMPTY_LINE, result.message
        armed = service.workflow_offer_service.peek_pending_offer(sid, user_id=_USER)
        assert armed is not None and armed["workflow_type"] == OFFER_ADD_PROJECT_WORKFLOW


# ---------------------------------------------------------------------------
# 3. The helper's scope
# ---------------------------------------------------------------------------


def _intent(category, action):
    return Intent(
        category=category,
        action=action,
        confidence=0.9,
        original_message=MSG,
        context={"original_message": MSG},
    )


class TestAdoptionScope:
    @pytest.mark.parametrize("action", ["manage_portfolio", "manage_repos"])
    @pytest.mark.parametrize("category", NON_PORTFOLIO, ids=lambda c: c.value)
    def test_portfolio_canonical_keys_adopt_portfolio(self, action, category):
        service = IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))
        intent = _intent(category, action)
        service._adopt_canonical_portfolio_category(intent)
        assert intent.category is IntentCategory.PORTFOLIO
        assert intent.action == action

    @pytest.mark.parametrize(
        "category,action",
        [
            # The other CANONICAL keys keep their own (message-level) gate.
            (IntentCategory.QUERY, "greeting"),
            (IntentCategory.IDENTITY, "thanks"),
            (IntentCategory.STATUS, "farewell"),
            # A real rail key is not a CANONICAL registry row.
            (IntentCategory.QUERY, "list_projects"),
            (IntentCategory.STATUS, "get_project_status"),
            # Unknown to the registry.
            (IntentCategory.QUERY, "get_information"),
        ],
    )
    def test_everything_else_is_untouched(self, category, action):
        service = IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))
        intent = _intent(category, action)
        service._adopt_canonical_portfolio_category(intent)
        assert intent.category is category
        assert intent.action == action
