"""#2003 — with the numbered delete pick armed, a typed name that matches no
candidate must NOT be matched to a different reminder. Found by CXO on
Web's served run of alpha b713b91cb5 (2026-10-13): 'delete the reminder
"web check alpha one"' (already deleted) → 'Delete the reminder "web check
alpha two"? (yes/no)'.

Bar (CXO): a plain no-match line ('I don't see a reminder called "…".')
followed by the same numbered list, slot still armed, no guess; number and
exact title still bind as before.

Layer (m-43): the shared #1906 binder (`reminder_clear._resolve_pick_target`)
on strings, and `handle_delete_todo_pick_turn` with todo_service, the
one-slot offer store and the router oracle stubbed. No LLM, no DB, no
served turn — the served check is owed on the card after the next
promotion.
"""

import datetime as _dt
from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import UUID, uuid4

import pytest

from services.domain.models import Todo
from services.intent_service import reminder_clear as rc
from services.intent_service.delete_todo_pick import (
    DELETE_PICK_KIND,
    PICK_PENDING_FLAG,
    arm_delete_pick,
    handle_delete_todo_pick_turn,
)
from services.intent_service.todo_handlers import TodoIntentHandlers

_USER = "3f7b8a52-2003-4b00-9e00-000000002003"
_SESSION = "sess-2003-pick"
_T0 = _dt.datetime(2026, 10, 14, 16, 0, tzinfo=_dt.timezone.utc)

# ---------------------------------------------------------------------------
# 1. The binder — strings only
# ---------------------------------------------------------------------------

_SERVED = [
    "web check alpha two",
    "send the budget review to finance",
    "water the plants",
    "check the test card",
    "review the pr",
]
_NONE = [None] * len(_SERVED)


class TestQuotedName:
    def test_the_served_miss_is_none_not_the_sibling(self):
        """The #2003 turn verbatim: the quoted title no longer exists; the
        old word-overlap rule bound it to '…alpha two'."""
        assert rc._resolve_pick_target(
            'delete the reminder "web check alpha one"', _SERVED, _NONE
        ) == ("none", None)

    @pytest.mark.parametrize(
        "text",
        [
            '"web check alpha two"',
            'delete the reminder "web check alpha two"',
            "remove 'web check alpha two' please",
            "delete “web check alpha two”",
        ],
    )
    def test_a_quoted_existing_title_binds_by_containment(self, text):
        assert rc._resolve_pick_target(text, _SERVED, _NONE) == ("bound", 0)

    def test_a_quoted_fragment_contained_in_one_title_binds(self):
        assert rc._resolve_pick_target('"budget review"', _SERVED, _NONE) == ("bound", 1)

    def test_a_quoted_fragment_in_two_titles_is_ambiguous(self):
        texts = ["check the test card", "check the test card again"]
        assert rc._resolve_pick_target('"test card"', texts, [None, None]) == ("ambiguous", None)

    def test_a_quoted_name_is_never_fuzzy_matched(self):
        """Three of four words overlap one candidate — under the old rule a
        unique best score; quoted, it must stay unmatched."""
        assert rc._resolve_pick_target('"budget review for finance"', _SERVED, _NONE) == (
            "none",
            None,
        )
        assert rc._resolve_pick_target('"send the budget review"', _SERVED, _NONE) == (
            "bound",
            1,
        )  # contained


class TestUnquotedCoverage:
    def test_the_served_miss_unquoted_is_none_sibling_guard(self):
        assert rc._resolve_pick_target(
            "delete the reminder web check alpha one", _SERVED, _NONE
        ) == ("none", None)

    @pytest.mark.parametrize(
        "text,idx",
        [
            ("the budget one", 1),
            ("the plants reminder", 2),
            ("delete the plants one", 2),
            ("the test card one", 3),
            ("review the pr", 4),
            ("web check alpha two", 0),
            ("the alpha two", 0),
            ("2", 1),
            ("second", 1),
        ],
    )
    def test_partial_and_exact_references_still_bind(self, text, idx):
        assert rc._resolve_pick_target(text, _SERVED, _NONE) == ("bound", idx)

    def test_a_word_the_candidate_lacks_blocks_the_bind(self):
        """'the budget board one' — 'board' is in no candidate: the old rule
        scored 'budget' and bound; coverage says none."""
        assert rc._resolve_pick_target("the budget board one", _SERVED, _NONE) == ("none", None)

    def test_tie_is_ambiguous(self):
        texts = ["check the test card", "check the test card again"]
        assert rc._resolve_pick_target("the test card one", texts, [None, None]) == (
            "ambiguous",
            None,
        )

    def test_no_overlap_is_none(self):
        assert rc._resolve_pick_target("maybe later", _SERVED, _NONE) == ("none", None)

    def test_sibling_guard_lets_a_shared_number_word_through(self):
        texts = ["web check alpha one", "web check alpha two"]
        assert rc._resolve_pick_target("the alpha one", texts, [None, None]) == ("ambiguous", None)
        assert rc._resolve_pick_target(
            "alpha one", ["web check alpha one", "water the plants"], [None, None]
        ) == ("bound", 0)
        assert rc._resolve_pick_target("alpha three", texts, [None, None]) == ("none", None)


# ---------------------------------------------------------------------------
# 2. The carrier — a quoted miss answers, re-arms, deletes nothing
# ---------------------------------------------------------------------------


def _todo(text, reminder_hours):
    return Todo(
        id=str(uuid4()),
        text=text,
        priority="medium",
        status="pending",
        completed=False,
        reminder_date=_T0 + _dt.timedelta(hours=reminder_hours),
    )


class _Store:
    def __init__(self):
        self.slot = None

    def set_pending_offer(self, session_id, offer, user_id=None):
        self.slot = offer

    def peek_pending_offer(self, session_id):
        return self.slot

    def get_and_clear_pending_offer(self, session_id, user_id=None):
        offer, self.slot = self.slot, None
        return offer


@pytest.fixture
def rows():
    return [_todo("web check alpha two", 1), _todo("send the budget review to finance", 2)]


@pytest.fixture
def todo_service(rows):
    svc = AsyncMock()
    svc.list_todos = AsyncMock(return_value=rows)
    svc.delete_todo = AsyncMock(return_value=True)
    return svc


@pytest.fixture
def store():
    return _Store()


@pytest.fixture
def intent_service(todo_service, store):
    handlers = TodoIntentHandlers()
    handlers.todo_service = todo_service
    return SimpleNamespace(todo_handlers=handlers, workflow_offer_service=store)


@pytest.fixture(autouse=True)
def _router_must_not_be_touched(monkeypatch):
    """A named miss is answered BEFORE the release discriminator's router
    read — the oracle must not be consulted at all."""
    from services.intent_service import inversion_live

    async def _boom(*a, **k):  # pragma: no cover - the assertion is that it never runs
        raise AssertionError("read_op_claims_turn consulted on a quoted named miss")

    monkeypatch.setattr(inversion_live, "read_op_claims_turn", _boom)


async def _arm(todo_service, store):
    q = await arm_delete_pick(
        "delete a reminder", _SESSION, _USER, UUID(_USER), todo_service, store
    )
    assert q is not None and store.slot is not None
    return q


async def _answer(text, intent_service, store):
    return await handle_delete_todo_pick_turn(
        store.get_and_clear_pending_offer(_SESSION), text, _SESSION, _USER, intent_service
    )


@pytest.mark.asyncio
class TestNamedMiss:
    async def test_quoted_miss_says_so_reshows_the_list_and_stays_armed(
        self, intent_service, todo_service, store
    ):
        question = await _arm(todo_service, store)
        ids_before = list(store.slot["pending_action"]["pick_ids"])
        out = await _answer('delete the reminder "web check alpha one"', intent_service, store)
        assert out is not None
        lines = out["message"].splitlines()
        assert lines[0] == 'I don\'t see a reminder called "web check alpha one".'
        assert lines[1] == ""
        assert "\n".join(lines[2:]) == question  # the SAME numbered list
        assert out["intent_data"][PICK_PENDING_FLAG] is True
        assert out["intent_data"]["pick_named_miss"] is True
        assert out["requires_clarification"] is True
        # re-armed with the record unchanged
        pa = store.slot["pending_action"]
        assert pa["kind"] == DELETE_PICK_KIND
        assert pa["pick_ids"] == ids_before
        assert pa["pick_reasked"] is False
        todo_service.delete_todo.assert_not_awaited()

    async def test_quoted_miss_preserves_a_prior_reask(self, intent_service, todo_service, store):
        await _arm(todo_service, store)
        store.slot["pending_action"]["pick_reasked"] = True
        out = await _answer('"nothing like this"', intent_service, store)
        assert out["intent_data"]["pick_named_miss"] is True
        assert store.slot["pending_action"]["pick_reasked"] is True

    async def test_a_quoted_hit_still_arms_the_confirm(self, intent_service, todo_service, store):
        """Control: the bound path is untouched — the quoted EXISTING title
        goes to the #1666 title-bound confirm."""
        await _arm(todo_service, store)
        out = await _answer('delete the reminder "web check alpha two"', intent_service, store)
        assert out["message"].startswith("Delete the reminder")
        assert "web check alpha two" in out["message"]
        assert store.slot["pending_action"]["kind"] != DELETE_PICK_KIND

    async def test_the_number_still_binds(self, intent_service, todo_service, store):
        await _arm(todo_service, store)
        out = await _answer("2", intent_service, store)
        assert "send the budget review to finance" in out["message"]
        assert out["message"].startswith("Delete the reminder")
