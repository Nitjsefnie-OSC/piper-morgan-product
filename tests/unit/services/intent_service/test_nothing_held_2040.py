"""#2040 part 2 — "show me the rest" with NOTHING held answers from code.

Web's served run on 6f2916d10f: after "You don't have any open issues right
now." (no list, nothing capped), ``could you show me the rest?`` drew an
LLM-composed "here are the two I didn't show yet: #2, #1", contradicting the
previous reply. The remainder seam (#1762, ``_check_pending_list_remainder``)
returns None when nothing is held, so the turn classified and the floor
narrated data code never returned (ADR-080; the class Arch named on #2033).

CXO's ruling: with nothing held, "There's nothing more to show; that was the
full list." Arch's condition (code may claim only what it holds): that line
fires only when the PREVIOUS turn rendered a list whole, a one-turn
``ListComplete`` fact recorded at render; otherwise the hold-only line, which
claims nothing about the previous turn. The ask is read with the remainder seam's OWN vocabulary
(``LIST_REMAINDER_TAUGHT_ACCEPTS`` full-message, plus the #1783 request-question
shape) via ``acceptance.names_offered_remainder``; the shared accept vocabulary
("yes", "sure") is not read, since with nothing armed it answers nothing.

Layer: the REAL ``process_intent`` with an LLM double that fails if touched;
the process registry is inert. Not a served run.
"""

from __future__ import annotations

import inspect
from datetime import datetime, timedelta
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentProcessingResult, IntentService
from services.intent_service import conversational_floor as cf
from services.intent_service.acceptance import names_offered_remainder
from services.intent_service.classifier import IntentClassifier
from services.intent_service.conversation_context import get_or_create_context
from services.intent_service.list_remainder import (
    HOLD_ONLY_REPLY,
    LIST_REMAINDER_TAUGHT_ACCEPTS,
    NOTHING_HELD_REPLY,
    REMAINDER_MAX_AGE_MINUTES,
    ListRemainder,
    compose_capped_list,
)
from services.intent_service.pre_classifier import MultiIntentResult
from services.intent_service.workflow_entries import register_default_workflows
from services.mcp.consumer.github_adapter import GitHubIssuesResult
from services.shared_types import IntentCategory

_USER = "7c4e3f50-2040-4b00-9e00-000000002041"
_REPO = "dinp-machine/piper-test-activity"
_FALLTHROUGH = "(fall-through answer)"

CXO_NOTHING_HELD = "There's nothing more to show; that was the full list."
# Arch's line, verbatim from his ruling (CXO owns the words).
ARCH_HOLD_ONLY = (
    "I don't have more of that list held right now. Ask for the list again and I'll pull it fresh."
)

CASH_PHRASES = [
    "show me the rest",
    "Show me the rest.",
    "the rest",
    "show them all",
    "let me see the rest",
    "could you show me the rest?",  # Web's served phrasing
    "can I see the rest?",
    "what are the others?",
]


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name}); this turn is deterministic")


@pytest.fixture
def live_service():
    register_default_workflows()
    return IntentService(intent_classifier=IntentClassifier(llm_service=_ExplosiveLLM()))


@pytest.fixture
def floor_calls(monkeypatch):
    calls = []

    async def fake_respond(self, ctx):
        calls.append(ctx)
        return cf.FloorResponse(message="(stubbed floor answer)")

    monkeypatch.setattr(cf.ConversationalFloor, "respond", fake_respond)
    return calls


def _inert_registry():
    registry = MagicMock()
    registry.check_suspended_processes = AsyncMock(return_value=None)
    registry.check_active_processes = AsyncMock(
        return_value=SimpleNamespace(
            handled=False, escaped=False, response_message=None, process_type=None
        )
    )
    return patch("services.intent.intent_service.get_process_registry", return_value=registry)


def _fallthrough(service, message):
    """For turns this step must NOT claim: classification is stubbed (no LLM)
    and both answer doors return a marker, so the test reads 'not claimed'."""
    intent = Intent(
        category=IntentCategory.UNKNOWN,
        action="unknown",
        confidence=0.2,
        original_message=message,
        context={"original_message": message},
    )
    answer = IntentProcessingResult(success=True, message=_FALLTHROUGH, intent_data={})
    return (
        patch.object(
            service.intent_classifier,
            "classify_multiple",
            new=AsyncMock(
                return_value=MultiIntentResult(intents=[intent], original_message=message)
            ),
        ),
        patch.object(service, "_handle_unknown_intent", new=AsyncMock(return_value=answer)),
        patch.object(service, "_handle_floor_with_context", new=AsyncMock(return_value=answer)),
    )


def _fresh(sid):
    ctx = get_or_create_context(sid, user_id=_USER)
    ctx.pending_list_remainder = None
    ctx.last_offer = None
    return ctx


def _arm(sid, *, held=12):
    lines = [f"\n- **#{100 + i}**: Issue number {100 + i}" for i in range(held)]
    rendered = compose_capped_list(lines=lines, cap=5, kind="open issues", source_total=held)
    _fresh(sid).pending_list_remainder = rendered.remainder
    return rendered


async def _turn(service, sid, message):
    with _inert_registry():
        return await service.process_intent(message=message, session_id=sid, user_id=_USER)


class TestRuledString:
    def test_the_constants_are_the_ruled_lines(self):
        assert NOTHING_HELD_REPLY == CXO_NOTHING_HELD
        assert HOLD_ONLY_REPLY == ARCH_HOLD_ONLY

    def test_statements_not_asks(self):
        assert "?" not in NOTHING_HELD_REPLY
        assert "?" not in HOLD_ONLY_REPLY


class TestTheReader:
    """``names_offered_remainder`` is the remainder seam's own two arms, with
    no shared accept vocabulary and no new phrase."""

    @pytest.mark.parametrize("text", CASH_PHRASES + list(LIST_REMAINDER_TAUGHT_ACCEPTS))
    def test_reads_the_taught_and_request_question_shapes(self, text):
        assert names_offered_remainder(text, taught_accepts=LIST_REMAINDER_TAUGHT_ACCEPTS)

    @pytest.mark.parametrize(
        "text",
        [
            "yes",
            "sure",
            "go ahead",
            "show me the rest?",  # a state question, not a request-question
            "the rest of my day looks busy",
            "can you delete the rest?",  # not a viewing verb (#1783)
            "what open issues do I have?",
            "",
        ],
    )
    def test_does_not_read_anything_else(self, text):
        assert not names_offered_remainder(text, taught_accepts=LIST_REMAINDER_TAUGHT_ACCEPTS)


def _issues_intent(message="what open issues do I have?"):
    return Intent(
        category=IntentCategory.QUERY,
        action="list_issues_query",
        confidence=0.95,
        original_message=message,
        context={"original_message": message, "user_id": _USER},
    )


async def _list_issues(service, sid, *, assigned, repo_total=0):
    """The real issues handler with the adapter stubbed: the render (and the
    arm or the whole-list fact) happen exactly as in production."""

    async def read(_self, user_id, *, limit=50, repository=None):
        if repository is None:
            page = [{"number": n, "title": f"t{n}", "labels": []} for n in range(assigned, 0, -1)]
            return GitHubIssuesResult(issues=page, total=assigned)
        return GitHubIssuesResult(issues=[], total=repo_total)

    with (
        patch(
            "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter.list_open_issues",
            new=read,
        ),
        patch(
            "services.integrations.github.repo_resolver.get_user_default_repo",
            new=AsyncMock(return_value=_REPO),
        ),
    ):
        return await service._handle_list_issues_query(_issues_intent(), "wf", sid)


class TestNothingHeldThroughProcessIntent:
    """Arch's four pins, through the real ``process_intent``."""

    pytestmark = pytest.mark.asyncio

    @pytest.mark.parametrize("text", CASH_PHRASES)
    async def test_full_render_then_the_rest_gets_the_complete_list_line(
        self, live_service, floor_calls, text
    ):
        sid = f"2040-full-{abs(hash(text))}"
        _fresh(sid)
        first = await _list_issues(live_service, sid, assigned=7)
        assert first.message.count("\n- **#") == 7  # rendered whole, nothing armed
        assert get_or_create_context(sid, user_id=_USER).pending_list_remainder is None
        assert get_or_create_context(sid, user_id=_USER).last_list_complete is not None
        result = await _turn(live_service, sid, text)
        assert result.message == CXO_NOTHING_HELD  # byte-for-byte, nothing appended
        assert result.intent_data["action"] == "list_remainder_nothing_held"
        assert result.intent_data["context"]["last_list_complete"] is True
        assert result.intent_data["context"]["refetched"] is False
        assert floor_calls == []
        # One turn: the fact is spent.
        assert get_or_create_context(sid, user_id=_USER).last_list_complete is None

    @pytest.mark.parametrize("text", CASH_PHRASES)
    async def test_nothing_at_all_then_the_rest_gets_the_hold_only_line(
        self, live_service, floor_calls, text
    ):
        sid = f"2040-nothing-{abs(hash(text))}"
        _fresh(sid)
        result = await _turn(live_service, sid, text)
        assert result.message == ARCH_HOLD_ONLY
        assert result.intent_data["context"]["last_list_complete"] is False
        assert floor_calls == []

    async def test_a_floor_prose_turn_then_the_rest_never_says_full_list(
        self, live_service, floor_calls
    ):
        """A list rendered whole, THEN a prose turn: "that" would now mean the
        prose, so the whole-list fact is void and only the hold-only line may
        answer."""
        sid = "2040-prose-between"
        _fresh(sid)
        await _list_issues(live_service, sid, assigned=3)
        aside = "tell me something about vector databases"
        p1, p2, p3 = _fallthrough(live_service, aside)
        with p1, p2, p3:
            prose = await _turn(live_service, sid, aside)
        assert prose.message == _FALLTHROUGH
        result = await _turn(live_service, sid, "show me the rest")
        assert result.message == ARCH_HOLD_ONLY
        assert "full list" not in result.message

    async def test_a_floor_prose_turn_alone_then_the_rest_never_says_full_list(
        self, live_service, floor_calls
    ):
        sid = "2040-prose-only"
        _fresh(sid)
        aside = "summarize what I've been working on"
        p1, p2, p3 = _fallthrough(live_service, aside)
        with p1, p2, p3:
            await _turn(live_service, sid, aside)
        result = await _turn(live_service, sid, "show me the rest")
        assert result.message == ARCH_HOLD_ONLY

    async def test_web_served_sequence_empty_scope_then_the_rest(self, live_service, floor_calls):
        """The served pair: the empty assigned read (no list rendered, nothing
        armed, no whole-list fact), then Web's follow-up. The follow-up claims
        nothing about the previous turn and touches no GitHub surface."""
        sid = "2040-served-sequence"
        _fresh(sid)
        first = await _list_issues(live_service, sid, assigned=0, repo_total=7)
        assert first.message.startswith("You have no open issues assigned to you.")
        ctx = get_or_create_context(sid, user_id=_USER)
        assert ctx.pending_list_remainder is None and ctx.last_list_complete is None

        refetch = AsyncMock(side_effect=AssertionError("the nothing-held turn fetched"))
        with patch(
            "services.mcp.consumer.github_adapter.GitHubMCPSpatialAdapter.list_open_issues",
            new=refetch,
        ):
            result = await _turn(live_service, sid, "could you show me the rest?")
        assert result.message == ARCH_HOLD_ONLY
        assert "#" not in result.message
        assert floor_calls == []

    async def test_a_stale_whole_list_fact_is_not_vouched_for(self, live_service, floor_calls):
        sid = "2040-stale-fact"
        _fresh(sid)
        await _list_issues(live_service, sid, assigned=4)
        get_or_create_context(sid, user_id=_USER).last_list_complete.recorded_at = (
            datetime.now() - timedelta(minutes=REMAINDER_MAX_AGE_MINUTES + 1)
        )
        result = await _turn(live_service, sid, "show me the rest")
        assert result.message == ARCH_HOLD_ONLY


class TestTheWholeListFact:
    """``compose_capped_list`` records ``complete`` only when every item the
    source has is on screen; it is never an armed remainder."""

    def test_a_whole_render_records_the_fact(self):
        r = compose_capped_list(
            lines=[f"\n- i{k}" for k in range(8)], cap=5, kind="open issues", source_total=8
        )
        assert r.remainder is None
        assert r.complete is not None and r.complete.shown == 8
        assert r.complete.kind == "open issues"

    def test_an_offered_remainder_records_no_fact(self):
        r = compose_capped_list(
            lines=[f"\n- i{k}" for k in range(9)], cap=5, kind="open issues", source_total=9
        )
        assert r.remainder is not None and r.complete is None

    def test_a_partial_hold_records_no_fact(self):
        r = compose_capped_list(
            lines=[f"\n- i{k}" for k in range(4)], cap=5, kind="open issues", source_total=179
        )
        assert r.remainder is None and r.complete is None

    def test_an_inexact_source_count_records_no_fact(self):
        r = compose_capped_list(
            lines=[f"\n- i{k}" for k in range(8)],
            cap=5,
            kind="open issues",
            source_total=8,
            source_total_display="8+",
        )
        assert r.complete is None

    def test_an_empty_list_records_no_fact(self):
        r = compose_capped_list(lines=[], cap=5, kind="open issues", source_total=0)
        assert r.complete is None

    def test_the_fact_is_not_an_armed_remainder(self):
        """A separate record: no lines, no offer text, nothing to bind a yes."""
        from services.intent_service.list_remainder import ListComplete

        r = compose_capped_list(lines=["\n- a", "\n- b"], cap=5, kind="labels", source_total=2)
        assert isinstance(r.complete, ListComplete)
        assert not isinstance(r.complete, ListRemainder)
        assert not hasattr(r.complete, "lines") and not hasattr(r.complete, "offer_text")

    @pytest.mark.asyncio
    async def test_a_bare_yes_after_a_whole_render_binds_nothing(self, live_service):
        sid = "2040-fact-no-yes"
        _fresh(sid)
        await _list_issues(live_service, sid, assigned=3)
        p1, p2, p3 = _fallthrough(live_service, "yes")
        with p1, p2, p3:
            result = await _turn(live_service, sid, "yes")
        assert result.message == _FALLTHROUGH


class TestHeldRemainderUnchanged:
    pytestmark = pytest.mark.asyncio

    async def test_a_held_remainder_still_cashes(self, live_service, floor_calls):
        sid = "2040-held-cashes"
        _arm(sid)
        result = await _turn(live_service, sid, "show me the rest")
        assert result.intent_data["action"] == "list_remainder_cash"
        assert result.message.startswith("Here's the rest — the other 7 open issues.")
        assert "**#105**" in result.message

    async def test_web_phrasing_with_a_held_remainder_cashes(self, live_service, floor_calls):
        sid = "2040-held-cashes-request-question"
        _arm(sid)
        result = await _turn(live_service, sid, "could you show me the rest?")
        assert result.intent_data["action"] == "list_remainder_cash"

    async def test_a_stale_remainder_still_says_moved(self, live_service, floor_calls):
        sid = "2040-held-stale"
        _arm(sid)
        get_or_create_context(sid, user_id=_USER).pending_list_remainder.armed_at = (
            datetime.now() - timedelta(minutes=REMAINDER_MAX_AGE_MINUTES + 1)
        )
        result = await _turn(live_service, sid, "show me the rest")
        assert result.intent_data["action"] == "list_remainder_moved"

    async def test_a_held_remainder_the_seam_lets_pass_is_never_called_nothing_held(
        self, live_service
    ):
        """A remainder that did not opt in to request-questions reads "could you
        show me the rest?" as a STATE_QUESTION and lets it pass (the arm
        persists). Something IS held, so the nothing-held line would be false:
        the step stands down and normal processing answers."""
        sid = "2040-held-not-opted-in"
        _fresh(sid).pending_list_remainder = ListRemainder(
            kind="open issues",
            shown=5,
            held_total=12,
            source_total_display="12",
            lines=tuple(f"\n- **#{n}**: x" for n in range(7)),
            offer_text="That's 5 of 12 — say the word and I'll pull the rest.",
        )
        text = "could you show me the rest?"
        p1, p2, p3 = _fallthrough(live_service, text)
        with p1, p2, p3:
            result = await _turn(live_service, sid, text)
        assert result.message == _FALLTHROUGH
        assert get_or_create_context(sid, user_id=_USER).pending_list_remainder is not None


class TestUnrelatedPhrasingsUnchanged:
    pytestmark = pytest.mark.asyncio

    @pytest.mark.parametrize("text", ["yes", "the rest of my day looks busy", "what's next?"])
    async def test_not_claimed(self, live_service, text):
        sid = f"2040-unrelated-{abs(hash(text))}"
        _fresh(sid)
        p1, p2, p3 = _fallthrough(live_service, text)
        with p1, p2, p3:
            result = await _turn(live_service, sid, text)
        assert result.message != CXO_NOTHING_HELD
        assert result.intent_data.get("action") != "list_remainder_nothing_held"


class TestSeamUnit:
    def test_an_armed_offer_rail_stands_down(self, live_service):
        sid = "2040-armed-rail"
        _fresh(sid)
        with patch.object(IntentService, "_armed_offer_signal", return_value="workflow_offer"):
            out = live_service._nothing_held_reply(
                "show me the rest", session_id=sid, user_id=_USER
            )
        assert out is None

    def test_a_failed_lookup_stands_down(self, live_service):
        with patch(
            "services.intent_service.conversation_context.get_or_create_context",
            side_effect=RuntimeError("boom"),
        ):
            out = live_service._nothing_held_reply(
                "show me the rest", session_id="2040-lookup-fails", user_id=_USER
            )
        assert out is None

    def test_no_session_stands_down(self, live_service):
        assert live_service._nothing_held_reply("the rest", session_id=None, user_id=_USER) is None

    def test_runs_after_the_remainder_check_and_before_classification(self):
        import services.intent.intent_service as mod

        src = inspect.getsource(mod.IntentService._process_intent_internal)
        step = src.index("self._nothing_held_reply(")
        assert src.index("self._check_pending_list_remainder(") < step
        assert step < src.index("await self._nothing_running_reply(")
        assert step < src.index("await self.intent_classifier.classify_multiple(")
