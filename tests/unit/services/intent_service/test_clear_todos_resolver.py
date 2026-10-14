"""Clear-family build plan piece 2 (2026-10-07) — ``clear_todos``, the
RESOLVER rail entry (Arch's ruling 2026-10-06; CXO's strings, same date).

``clear_todos`` mutates nothing: it resolves the ambiguous "clear/handle/
take care of/reset" verb (the #1605 three-variant question, or the user's
stored default) against the router's ``inversion_args``, then re-enters the
action-dispatch rail as a concrete ``complete_todo`` or ``delete_todo``
Intent carrying the SAME args, via ``workflow_dispatcher.dispatch_workflow``
— never calling ``todo_handlers`` directly, so the concrete op's own gates
(consent, the #1190 enumerating confirm) run unchanged.

Layer (m-43): handler/dispatcher-level tests. ``dispatch_workflow`` and the
rail registry are REAL (registered via ``register_default_workflows``) so
the re-entry is genuinely exercised end to end through
``run_complete_todo_workflow`` / ``run_delete_todo_workflow`` and
``todo_handlers.handle_complete_todo_targets`` / ``handle_delete_todo_
targets``; only ``todo_service`` (DB), the offer store, the session
context, and the verified-inference store are mocked. No LLM, no DB.
"""

from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest

from services.domain.models import Intent, IntentCategory, Todo
from services.intent_service import clear_todos as ct
from services.intent_service import reminder_clear as rc
from services.intent_service import todo_handlers as th
from services.intent_service import workflow_entries as we
from services.intent_service.conversation_context import NumberedList
from services.intent_service.destructive_confirm import CONFIRMED_CONTEXT_KEY
from services.intent_service.todo_handlers import (
    BATCH_COMPLETE_IDS_KEY,
    BATCH_COMPLETE_LEFT_KEY,
    BATCH_COMPLETE_TEXTS_KEY,
    TodoIntentHandlers,
)
from services.shared_types import EffectClass

we.register_default_workflows()  # idempotent — the rail must be populated

_NOW = datetime.now(timezone.utc)
_USER_ID = str(uuid4())


def _due(text: str, minutes_ago: int) -> Todo:
    t = Todo(text=text, priority="medium")
    t.id = str(uuid4())
    t.reminder_date = _NOW - timedelta(minutes=minutes_ago)
    t.completed = False
    return t


@pytest.fixture
def four():
    return [
        _due("check the test card again", 400),
        _due("check the test card again", 300),
        _due("review the pr", 200),
        _due("revise the pr", 100),
    ]


@pytest.fixture
def intent_service(four, monkeypatch):
    svc = MagicMock()
    th_instance = TodoIntentHandlers()
    th_instance.todo_service = AsyncMock()
    th_instance.todo_service.list_todos = AsyncMock(return_value=four)
    th_instance.todo_service.complete_todo = AsyncMock(return_value=MagicMock())
    th_instance.todo_service.delete_todo = AsyncMock(return_value=True)
    svc.todo_handlers = th_instance

    # A REAL in-memory offer store (not a dumb MagicMock): the stored-delete
    # branch PEEKS what it just armed in order to overwrite its question —
    # a mock with a fixed return value wouldn't reflect that write. Spied
    # (side_effect=) so call-count/call_args assertions still work.
    from services.intent_service.soft_invocation import WorkflowOfferService

    real_offers = WorkflowOfferService()
    offers = MagicMock(wraps=real_offers)
    offers.set_pending_offer = MagicMock(side_effect=real_offers.set_pending_offer)
    offers.peek_pending_offer = MagicMock(side_effect=real_offers.peek_pending_offer)
    offers.get_and_clear_pending_offer = MagicMock(
        side_effect=real_offers.get_and_clear_pending_offer
    )
    svc.workflow_offer_service = offers

    ctx = MagicMock()
    ctx.last_numbered_list = None
    monkeypatch.setattr(
        "services.intent_service.conversation_context.get_or_create_context",
        lambda session_id, user_id=None: ctx,
    )
    svc._session_ctx = ctx
    return svc


def _clear_intent(targets, exclude=None, message="clear my reminders"):
    args = {"targets": targets}
    if exclude is not None:
        args["exclude"] = exclude
    ctx = {"original_message": message, "inversion_args": args}
    return Intent(
        category=IntentCategory.EXECUTION,
        action="clear_todos",
        original_message=message,
        confidence=0.9,
        context=ctx,
    )


def _stub_router(monkeypatch, *, outcome="operation", operation=None, confidence=None, args=None):
    """Stubs the SAME ``inversion_router.route`` the generalized #1886(b)
    armed-turn consult (``armed_turn_consult.classify_armed_reply``) calls
    — mirrors ``test_armed_turn_consult_1886.py``'s own ``_stub_route``
    helper. Deterministic, no LLM, no network."""
    from services.intent_service import inversion_router as ir
    from services.intent_service.inversion_router import RoutingDecision

    async def _route(message, session_state=None, **kwargs):
        return RoutingDecision(
            outcome=outcome,
            operation=operation if outcome == "operation" else None,
            confidence=confidence,
            args=dict(args or {}),
        )

    monkeypatch.setattr(ir, "route", _route)


def _always_live(op: str) -> bool:
    return True


@pytest.fixture(autouse=True)
def _live_by_default(monkeypatch):
    monkeypatch.setattr(ct, "_op_is_live_eligible", _always_live)


@pytest.fixture
def no_stored(monkeypatch):
    monkeypatch.setattr(
        "services.intent_service.verified_inference.get_verified_inference",
        AsyncMock(return_value=None),
    )


def _stored(monkeypatch, value):
    monkeypatch.setattr(
        "services.intent_service.verified_inference.get_verified_inference",
        AsyncMock(return_value={"value": value}),
    )


class TestUnresolved:
    @pytest.mark.asyncio
    async def test_unresolved_strikes_the_verb_clause(self, intent_service, no_stored):
        intent = _clear_intent(["name:nonexistent reminder"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.requires_clarification is False
        assert "Tell me which one." in result.message
        # the verb-neutral tail only — never "mark it done" / "delete it" /
        # "clear it"
        for word in ("mark", "delete", "clear it"):
            assert word not in result.message
        intent_service.workflow_offer_service.set_pending_offer.assert_not_called()

    @pytest.mark.asyncio
    async def test_unresolved_with_some_picked_promises_only_what_state_holds(
        self, intent_service, no_stored, four
    ):
        intent = _clear_intent(["name:review the pr", "name:nonexistent"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert "Nothing has been changed. Say it again with the right name or number." in (
            result.message
        )


class TestUnresolvedListingStatesItsElision:
    """#1762's defect class (a silent cap under a definite "you have:")
    must not return with the retired #1605 clarify's successor: past ten,
    the resolver's unresolved reply SAYS how many it left out."""

    @pytest.mark.asyncio
    async def test_twelve_candidates_list_ten_and_count_the_rest(self, intent_service, no_stored):
        many = [_due(f"reminder {i}", 500 - i) for i in range(12)]
        intent_service.todo_handlers.todo_service.list_todos = AsyncMock(return_value=many)
        result = await ct.run_clear_todos(
            _clear_intent(["name:nothing like this"]), "s1", _USER_ID, intent_service
        )
        lines = result.message.splitlines()
        assert sum(1 for ln in lines if ln[:1].isdigit()) == 10
        assert "…and 2 more." in lines


class TestNoStoredDefault:
    @pytest.mark.asyncio
    async def test_variant_one_with_set_and_carve_out(self, intent_service, no_stored, four):
        """RECORDED: no-stored, 3 items, with a carve-out."""
        intent = _clear_intent(["1-3"], exclude=["3"])
        intent_service._session_ctx.last_numbered_list = NumberedList(
            kind="reminders", ids=[t.id for t in four], texts=[t.text for t in four]
        )
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.requires_clarification is True
        assert result.message == (
            'You want to clear 2 reminders: "check the test card again" (2 items). '
            'Leaving "review the pr" and "revise the pr" as is. '
            "Before I touch these — when you say 'clear' on a reminder, do you want "
            "me to mark it done, or delete it? I'll remember for next time."
        )
        intent_service.workflow_offer_service.set_pending_offer.assert_called_once()
        _sid, offer = intent_service.workflow_offer_service.set_pending_offer.call_args.args[:2]
        assert offer["question"] == result.message
        pa = offer["pending_action"]
        assert pa["kind"] == rc.CLEAR_VERB_QUESTION_KIND
        # 2026-10-14: the interim delegation marker retired with the
        # off-rail answer path — the kind alone routes the answer here.
        assert "clear_todos_resolver" not in pa
        assert len(pa["clear_target_ids"]) == 2

    @pytest.mark.asyncio
    async def test_variant_one_one_item_no_carve_out_no_leaving_line(
        self, intent_service, no_stored
    ):
        only = [_due("review the pr", 100)]
        intent_service.todo_handlers.todo_service.list_todos = AsyncMock(return_value=only)
        intent = _clear_intent(["name:review the pr"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.message == (
            'You want to clear the reminder "review the pr". '
            "Before I touch these — when you say 'clear' on a reminder, do you want "
            "me to mark it done, or delete it? I'll remember for next time."
        )
        assert "Leaving" not in result.message

    @pytest.mark.asyncio
    async def test_guard_declines_honestly_when_either_op_not_live(
        self, intent_service, no_stored, monkeypatch
    ):
        """A resolver is never a back door (Arch). Until 2026-10-14 this
        returned None for the legacy #1605 regex seam to take the turn;
        that seam is retired, so the guard answers honestly instead —
        nothing armed, nothing changed."""
        monkeypatch.setattr(ct, "_op_is_live_eligible", lambda op: op == "complete_todo")
        intent = _clear_intent(["name:review the pr"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.message == (
            "I can't do that yet — that capability isn't live right now. Nothing has been changed."
        )
        assert result.requires_clarification is False
        assert result.intent_data["op_not_live"] is True
        intent_service.workflow_offer_service.set_pending_offer.assert_not_called()
        intent_service.todo_handlers.todo_service.complete_todo.assert_not_awaited()
        intent_service.todo_handlers.todo_service.delete_todo.assert_not_awaited()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("stored", [rc.VALUE_COMPLETE, rc.VALUE_DELETE])
    async def test_stored_branch_declines_honestly_when_its_op_not_live(
        self, intent_service, monkeypatch, stored
    ):
        monkeypatch.setattr(ct, "_op_is_live_eligible", lambda op: False)
        _stored(monkeypatch, stored)
        intent = _clear_intent(["name:review the pr"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.intent_data["op_not_live"] is True
        intent_service.workflow_offer_service.set_pending_offer.assert_not_called()
        intent_service.todo_handlers.todo_service.complete_todo.assert_not_awaited()
        intent_service.todo_handlers.todo_service.delete_todo.assert_not_awaited()


class TestStoredDone:
    @pytest.mark.asyncio
    async def test_one_item_completes_with_disclosure(self, intent_service, monkeypatch, four):
        """RECORDED: stored = done, 1 item."""
        _stored(monkeypatch, rc.VALUE_COMPLETE)
        intent = _clear_intent(["name:review the pr"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.requires_clarification is False
        intent_service.todo_handlers.todo_service.complete_todo.assert_awaited_once()
        assert result.message.endswith(
            "That's what 'clear' has meant for you. " "Say so if you meant delete this time."
        )

    @pytest.mark.asyncio
    async def test_multi_item_confirm_is_complete_todos_own_unchanged(
        self, intent_service, monkeypatch, four
    ):
        """CXO ruling 2: 2+ or a carve-out arms complete_todo's OWN
        enumerating confirm with NO extra clause."""
        _stored(monkeypatch, rc.VALUE_COMPLETE)
        intent = _clear_intent(["1-3"])
        intent_service._session_ctx.last_numbered_list = NumberedList(
            kind="reminders", ids=[t.id for t in four], texts=[t.text for t in four]
        )
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.requires_clarification is True
        assert result.message == (
            'Complete 3 reminders: "check the test card again" (2 items) and '
            '"review the pr"? Leaving "revise the pr" as is. (yes/no)'
        )
        assert "clear" not in result.message.lower()
        intent_service.todo_handlers.todo_service.complete_todo.assert_not_awaited()
        _sid, offer = intent_service.workflow_offer_service.set_pending_offer.call_args.args[:2]
        bound = offer["pending_action"]["intent"]
        assert bound.context.get(ct.VIA_CLEAR_VERB_CONTEXT_KEY) == "clear"

    @pytest.mark.asyncio
    async def test_confirmed_reentry_appends_disclosure_to_the_summary(self, intent_service, four):
        """The "yes" turn to the confirm above re-enters
        handle_complete_todo_targets directly (as run_confirm_pending_
        action_workflow would), with via_clear_verb carried on the bound
        Intent's context — the summary gets the disclosure appended."""
        picked = four[:3]
        ctx = {
            "inversion_args": {"targets": []},
            CONFIRMED_CONTEXT_KEY: True,
            BATCH_COMPLETE_IDS_KEY: [t.id for t in picked],
            BATCH_COMPLETE_TEXTS_KEY: [t.text for t in picked],
            BATCH_COMPLETE_LEFT_KEY: [four[3].text],
            ct.VIA_CLEAR_VERB_CONTEXT_KEY: "clear",
        }
        intent = Intent(
            category=IntentCategory.EXECUTION,
            action="complete_todo",
            original_message="",
            confidence=1.0,
            context=ctx,
        )
        msg, armed = await intent_service.todo_handlers.handle_complete_todo_targets(
            intent, "s1", _USER_ID, intent_service.workflow_offer_service, _USER_ID
        )
        assert armed is False
        assert msg.endswith(
            "That's what 'clear' has meant for you. Say so if you meant delete this time."
        )
        assert msg.startswith("Marked 3 reminders done:")


class TestStoredDelete:
    @pytest.mark.asyncio
    async def test_one_item_confirm_is_variant_three(self, intent_service, monkeypatch):
        """RECORDED: stored = delete, 1 item (a pool of exactly one — no
        Leaving line, CXO's D1 shape mirrored)."""
        only = [_due("review the pr", 100)]
        intent_service.todo_handlers.todo_service.list_todos = AsyncMock(return_value=only)
        _stored(monkeypatch, rc.VALUE_DELETE)
        intent = _clear_intent(["name:review the pr"])
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.requires_clarification is True
        assert result.message == (
            "You've set 'clear' to mean delete — " 'delete the reminder "review the pr"? (yes/no)'
        )
        intent_service.todo_handlers.todo_service.delete_todo.assert_not_awaited()
        _sid, offer = intent_service.workflow_offer_service.set_pending_offer.call_args.args[:2]
        assert offer["question"] == result.message

    @pytest.mark.asyncio
    async def test_multi_item_confirm_is_variant_three_with_leaving(
        self, intent_service, monkeypatch, four
    ):
        _stored(monkeypatch, rc.VALUE_DELETE)
        intent = _clear_intent(["1-3"], exclude=["3"])
        intent_service._session_ctx.last_numbered_list = NumberedList(
            kind="reminders", ids=[t.id for t in four], texts=[t.text for t in four]
        )
        result = await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert result.message == (
            "You've set 'clear' to mean delete — "
            'delete 2 reminders: "check the test card again" (2 items)? '
            'Leaving "review the pr" and "revise the pr" as is. (yes/no)'
        )


class TestReentryUsesDispatchWorkflowWithSameArgs:
    @pytest.mark.asyncio
    async def test_complete_reentry_carries_the_same_args(self, intent_service, monkeypatch):
        captured = {}

        async def spy(workflow_type, session_id, user_id=None, context=None, resume=False):
            captured["workflow_type"] = workflow_type
            captured["args"] = context["intent"].context.get("inversion_args")
            captured["original_message"] = context["intent"].original_message
            captured["context_keys"] = set(context["intent"].context)
            from services.intent.intent_service import IntentProcessingResult

            return IntentProcessingResult(
                success=True, message="stub", intent_data={}, requires_clarification=False
            )

        monkeypatch.setattr("services.intent_service.workflow_dispatcher.dispatch_workflow", spy)
        _stored(monkeypatch, rc.VALUE_COMPLETE)
        intent = _clear_intent(["name:review the pr"], exclude=["name:revise the pr"])
        await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert captured["workflow_type"] == "complete_todo"
        assert captured["args"] == {
            "targets": ["name:review the pr"],
            "exclude": ["name:revise the pr"],
        }
        # Arch's 2026-10-07 ruling, point 2: the message is NOT blanked. The
        # interim stand-down marker retired 2026-10-14 with its only reader.
        assert captured["original_message"] == "clear my reminders"
        assert "clear_family_resolved" not in captured["context_keys"]

    @pytest.mark.asyncio
    async def test_delete_reentry_carries_the_same_args(self, intent_service, monkeypatch):
        captured = {}

        async def spy(workflow_type, session_id, user_id=None, context=None, resume=False):
            captured["workflow_type"] = workflow_type
            captured["args"] = context["intent"].context.get("inversion_args")
            captured["original_message"] = context["intent"].original_message
            captured["context_keys"] = set(context["intent"].context)
            from services.intent.intent_service import IntentProcessingResult

            return IntentProcessingResult(
                success=True, message="stub", intent_data={}, requires_clarification=True
            )

        monkeypatch.setattr("services.intent_service.workflow_dispatcher.dispatch_workflow", spy)
        _stored(monkeypatch, rc.VALUE_DELETE)
        intent = _clear_intent(["name:review the pr"])
        await ct.run_clear_todos(intent, "s1", _USER_ID, intent_service)
        assert captured["workflow_type"] == "delete_todo"
        assert captured["args"] == {"targets": ["name:review the pr"]}
        assert captured["original_message"] == "clear my reminders"
        assert "clear_family_resolved" not in captured["context_keys"]


def _bound_payload(ids, texts, message="clear my reminders"):
    return {
        "kind": rc.CLEAR_VERB_QUESTION_KIND,
        "clear_target_ids": list(ids),
        "clear_target_texts": list(texts),
        "original_message": message,
    }


class TestAnswerTurnReentry:
    @pytest.mark.asyncio
    async def test_answer_turn_reenters_with_the_bound_ids(self, intent_service, monkeypatch):
        """The router names the answering operation (complete_todo) at/above
        threshold — Arch's generalized armed-turn consult BINDS it as the
        answer (point 3), with no refinement (no targets/exclude on this
        turn's args), so the full bound set carries through unchanged."""
        captured = {}

        async def spy(workflow_type, session_id, user_id=None, context=None, resume=False):
            captured["workflow_type"] = workflow_type
            captured["targets"] = context["intent"].context["inversion_args"]["targets"]
            captured["original_message"] = context["intent"].original_message
            captured["context_keys"] = set(context["intent"].context)
            from services.intent.intent_service import IntentProcessingResult

            return IntentProcessingResult(
                success=True, message="Marked done.", intent_data={}, requires_clarification=False
            )

        monkeypatch.setattr("services.intent_service.workflow_dispatcher.dispatch_workflow", spy)
        monkeypatch.setattr(
            "services.intent_service.verified_inference.store_verified_inference",
            AsyncMock(return_value=True),
        )
        _stub_router(monkeypatch, outcome="operation", operation="complete_todo", confidence=0.95)
        payload = _bound_payload(["id-1", "id-2"], ["review the pr", "revise the pr"])
        result = await ct.handle_clear_todos_verb_answer(
            payload, "mark them done", "s1", _USER_ID, intent_service
        )
        assert captured["workflow_type"] == "complete_todo"
        assert captured["targets"] == ["name:review the pr", "name:revise the pr"]
        assert result["message"] == "Marked done."
        assert result["intent_data"]["verb_default_stored"] == rc.VALUE_COMPLETE
        # Arch's 2026-10-07 ruling, point 2: message intact (no marker since
        # the 2026-10-14 retirement).
        assert captured["original_message"] == "clear my reminders"
        assert "clear_family_resolved" not in captured["context_keys"]

    @pytest.mark.asyncio
    async def test_answer_turn_refines_the_set_from_the_routers_own_args(
        self, intent_service, monkeypatch
    ):
        """ "delete them, but not the PR one" — the router names delete_todo
        (the answering operation) with its OWN ``exclude`` arg; the carrier
        refines the BOUND set by code (D2) and re-enters delete_todo with
        the narrowed set. The dispatched op's own confirm renders it."""
        captured = {}

        async def spy(workflow_type, session_id, user_id=None, context=None, resume=False):
            captured["workflow_type"] = workflow_type
            captured["targets"] = context["intent"].context["inversion_args"]["targets"]
            from services.intent.intent_service import IntentProcessingResult

            return IntentProcessingResult(
                success=True,
                message=(
                    'Delete 2 reminders: "check the test card again" and '
                    '"revise the pr"? (yes/no)'
                ),
                intent_data={},
                requires_clarification=True,
            )

        monkeypatch.setattr("services.intent_service.workflow_dispatcher.dispatch_workflow", spy)
        monkeypatch.setattr(
            "services.intent_service.verified_inference.store_verified_inference",
            AsyncMock(return_value=True),
        )
        _stub_router(
            monkeypatch,
            outcome="operation",
            operation="delete_todo",
            confidence=0.95,
            args={"exclude": ["name:review the pr"]},
        )
        payload = _bound_payload(
            ["id-1", "id-2", "id-3"],
            ["review the pr", "check the test card again", "revise the pr"],
        )
        result = await ct.handle_clear_todos_verb_answer(
            payload, "delete them, but not the PR one", "s1", _USER_ID, intent_service
        )
        assert captured["workflow_type"] == "delete_todo"
        assert captured["targets"] == [
            "name:check the test card again",
            "name:revise the pr",
        ]
        assert result["requires_clarification"] is True
        assert result["message"] == (
            'Delete 2 reminders: "check the test card again" and "revise the pr"? (yes/no)'
        )
        assert result["intent_data"]["verb_default_stored"] == rc.VALUE_DELETE

    @pytest.mark.asyncio
    async def test_clarify_on_the_verb_turn_falls_back_to_the_1605_parse_unrefined(
        self, intent_service, monkeypatch
    ):
        """The router answering CLARIFY is not informative for a yes/no verb
        question (Arch's shared-fallback rule) — the carrier falls back to
        the ORIGINAL #1605 crisp-claim regex parse, acting on the UNREFINED
        bound set (the full three items, not narrowed by anything)."""
        captured = {}

        async def spy(workflow_type, session_id, user_id=None, context=None, resume=False):
            captured["workflow_type"] = workflow_type
            captured["targets"] = context["intent"].context["inversion_args"]["targets"]
            from services.intent.intent_service import IntentProcessingResult

            return IntentProcessingResult(
                success=True, message="stub", intent_data={}, requires_clarification=False
            )

        monkeypatch.setattr("services.intent_service.workflow_dispatcher.dispatch_workflow", spy)
        monkeypatch.setattr(
            "services.intent_service.verified_inference.store_verified_inference",
            AsyncMock(return_value=True),
        )
        _stub_router(monkeypatch, outcome="clarify")
        payload = _bound_payload(
            ["id-1", "id-2", "id-3"],
            ["review the pr", "check the test card again", "revise the pr"],
        )
        result = await ct.handle_clear_todos_verb_answer(
            payload, "mark them done", "s1", _USER_ID, intent_service
        )
        assert captured["workflow_type"] == "complete_todo"
        assert captured["targets"] == [
            "name:review the pr",
            "name:check the test card again",
            "name:revise the pr",
        ]
        assert result["intent_data"]["verb_default_stored"] == rc.VALUE_COMPLETE

    @pytest.mark.asyncio
    async def test_unrelated_operation_above_threshold_releases(self, intent_service, monkeypatch):
        """An operation that is NOT in the verb carrier's answering set
        (complete_todo/delete_todo), named at/above threshold, means the
        user moved on to a brand-new ask — release, never bind or refine."""
        dispatch_spy = AsyncMock()
        monkeypatch.setattr(
            "services.intent_service.workflow_dispatcher.dispatch_workflow", dispatch_spy
        )
        _stub_router(monkeypatch, outcome="operation", operation="create_todo", confidence=0.9)
        payload = _bound_payload(["id-1", "id-2"], ["review the pr", "revise the pr"])
        result = await ct.handle_clear_todos_verb_answer(
            payload, "remind me to call mom at 5", "s1", _USER_ID, intent_service
        )
        assert result is None
        dispatch_spy.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_offer_seam_hands_every_verb_answer_to_the_resolver(
        self, intent_service, monkeypatch
    ):
        """2026-10-14 (Arch's point 1, the named retirement): the offer
        seam's reminder-clear entry, ``handle_reminder_clear_turn``, hands a
        verb-question answer STRAIGHT to the resolver's handler — no marker
        check, no off-rail path left to fall into — threading the armed
        question through."""
        called = {}

        async def fake_handler(
            payload, message, session_id, user_id, intent_service, armed_question=None
        ):
            called["payload"] = payload
            called["armed_question"] = armed_question
            return {"message": "delegated", "intent_data": {}}

        monkeypatch.setattr(ct, "handle_clear_todos_verb_answer", fake_handler)
        payload = {"kind": rc.CLEAR_VERB_QUESTION_KIND}
        out = await rc.handle_reminder_clear_turn(
            {"pending_action": payload, "question": "Q?"},
            "anything",
            "s1",
            _USER_ID,
            intent_service,
        )
        assert out == {"message": "delegated", "intent_data": {}}
        assert called["payload"] is payload
        assert called["armed_question"] == "Q?"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "kind", ["reminder_clear_correction", "reminder_clear_pick_target_question", None]
    )
    async def test_offer_seam_claims_no_retired_kind(self, intent_service, monkeypatch, kind):
        """The retired carriers' kinds (and a kindless payload) are never
        claimed — they fall through to the generic seam."""
        monkeypatch.setattr(
            ct, "handle_clear_todos_verb_answer", AsyncMock(side_effect=AssertionError("claimed"))
        )
        out = await rc.handle_reminder_clear_turn(
            {"pending_action": {"kind": kind}}, "anything", "s1", _USER_ID, intent_service
        )
        assert out is None


class TestOneQuestionPerClearTurn:
    """The #1605 three variants, through the RESOLVER and the REAL rail
    (``workflow_entries.run_clear_todos_workflow`` -> ``run_clear_todos`` ->
    ``dispatch_workflow`` -> the concrete op), each turn asking exactly ONE
    question: one offer armed, and the reply IS the armed question (#1665).
    With ``detect_clear_family_ask`` gone nothing else can arm a second ask
    (the old consent passthrough existed only to prevent that)."""

    async def _run(self, intent_service, four, targets, exclude=None):
        intent_service._session_ctx.last_numbered_list = NumberedList(
            kind="reminders", ids=[t.id for t in four], texts=[t.text for t in four]
        )
        return await we.run_clear_todos_workflow(
            session_id="s1",
            user_id=_USER_ID,
            context={
                "intent": _clear_intent(targets, exclude=exclude),
                "intent_service": intent_service,
            },
        )

    def _one_armed_question(self, intent_service, result):
        offers = intent_service.workflow_offer_service
        # The stored-delete branch re-stores the SAME offer with CXO's
        # variant-3 text, so count distinct live records, not writes.
        armed = offers.peek_pending_offer("s1", user_id=_USER_ID)
        assert armed is not None
        assert result.requires_clarification is True
        assert armed["question"] == result.message
        assert result.message.count("?") == 1, result.message
        intent_service.todo_handlers.todo_service.complete_todo.assert_not_awaited()
        intent_service.todo_handlers.todo_service.delete_todo.assert_not_awaited()
        return armed

    @pytest.mark.asyncio
    async def test_variant_one_no_stored_default(self, intent_service, no_stored, four):
        result = await self._run(intent_service, four, ["1-3"])
        armed = self._one_armed_question(intent_service, result)
        assert armed["pending_action"]["kind"] == rc.CLEAR_VERB_QUESTION_KIND
        assert result.message.endswith(rc.variant_one_question())
        intent_service.workflow_offer_service.set_pending_offer.assert_called_once()

    @pytest.mark.asyncio
    async def test_variant_two_stored_done(self, intent_service, monkeypatch, four):
        _stored(monkeypatch, rc.VALUE_COMPLETE)
        result = await self._run(intent_service, four, ["1-3"])
        self._one_armed_question(intent_service, result)
        assert result.message.startswith("Complete 3 reminders: ")
        intent_service.workflow_offer_service.set_pending_offer.assert_called_once()

    @pytest.mark.asyncio
    async def test_variant_three_stored_delete(self, intent_service, monkeypatch, four):
        _stored(monkeypatch, rc.VALUE_DELETE)
        result = await self._run(intent_service, four, ["1-3"])
        self._one_armed_question(intent_service, result)
        assert result.message.startswith("You've set 'clear' to mean delete — delete 3 reminders")


class TestRetiredOffRailPathIsGone:
    """Source pins for Arch's rework point 1 (2026-10-07; restated
    2026-10-14 point 5): the regex ask-detector, its seam, the consent
    passthrough it fed, the off-rail verb-answer path and both interim
    markers are DELETED — not commented out, not unreachable-but-present."""

    @pytest.mark.parametrize(
        "name",
        [
            "detect_clear_family_ask",
            "maybe_handle_clear_family",
            "is_clear_family_passthrough",
            "_handle_verb_answer_turn",
            "_act_on_resolved_targets",
            "_handle_correction_turn",
            "_handle_pick_target_turn",
            "CLEAR_FAMILY_RESOLVED_KEY",
            "_EXPLICIT_VERB_RE",
        ],
    )
    def test_reminder_clear_no_longer_defines(self, name):
        assert not hasattr(rc, name), f"reminder_clear.{name} must stay deleted"

    def test_resolver_marker_is_gone(self):
        assert not hasattr(ct, "CLEAR_TODOS_RESOLVER_MARKER")

    @pytest.mark.parametrize(
        "path",
        [
            "services/intent/intent_service.py",
            "services/intent_service/workflow_entries.py",
            "services/intent_service/destructive_confirm.py",
            "services/intent_service/reminder_clear.py",
            "services/intent_service/clear_todos.py",
        ],
    )
    def test_no_caller_or_definition_left_in_source(self, path):
        import ast
        import pathlib

        root = pathlib.Path(__file__).resolve().parents[4]
        tree = ast.parse((root / path).read_text())
        retired = {
            "detect_clear_family_ask",
            "maybe_handle_clear_family",
            "is_clear_family_passthrough",
            "_handle_verb_answer_turn",
        }
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                assert node.name not in retired, f"{path} defines {node.name}"
            if isinstance(node, ast.Attribute):
                assert node.attr not in retired, f"{path} calls .{node.attr}"
            if isinstance(node, ast.Name):
                assert node.id not in retired, f"{path} references {node.id}"
            if isinstance(node, ast.alias):
                assert node.name not in retired, f"{path} imports {node.name}"
