"""#1984 — the plan-reply joiner never prints an action id (Arch's placement, 2026-10-11).

CXO's served sample: "Regarding list archived projects, you don't have any archived
projects." — ``_intent_topic_label``'s fallback humanized the action id. The plan
path (#1595 unit 4) can emit ANY catalog operation, so one label row fixes one
symptom; this test pins the class: for every operation the router grammar can
emit, the rendered transition and the failure note contain neither the id nor
its humanized form, with or without a label row.
"""

from __future__ import annotations

import pytest

from services.domain.models import Intent
from services.intent_service.inversion_router import derive_routing_grammar
from services.intent_service.orchestrator import (
    TOPIC_FREE_TRANSITION,
    UNLABELED_FAILURE_TOPIC,
    IntentExecutionResult,
    IntentOrchestrator,
    OrchestratedResponse,
    _intent_topic_label,
)
from services.shared_types import IntentCategory


def _intent(action: str) -> Intent:
    return Intent(
        category=IntentCategory.QUERY,
        action=action,
        original_message="probe",
        confidence=1.0,
        context={"original_message": "probe"},
    )


def _ok(action: str, text: str) -> IntentExecutionResult:
    return IntentExecutionResult(intent=_intent(action), response=text, success=True)


def _failed(action: str) -> IntentExecutionResult:
    return IntentExecutionResult(intent=_intent(action), success=False, error="boom")


def _catalog_ops() -> list[str]:
    grammar = derive_routing_grammar()
    ops = sorted(set(grammar.names()) | set(grammar.alias_to_canonical))
    assert len(ops) >= 40, f"vacuity guard: the grammar lists only {len(ops)} ops"
    return ops


@pytest.fixture(scope="module")
def ops() -> list[str]:
    return _catalog_ops()


def _render(results: list[IntentExecutionResult]) -> str:
    orch = IntentOrchestrator.__new__(IntentOrchestrator)
    return orch._aggregate_messages(OrchestratedResponse(results=results))


def _forbidden(op: str) -> list[str]:
    return [op, op.replace("_", " ")]


class TestNoActionIdInProse:
    def test_every_catalog_op_as_a_second_reply(self, ops):
        offenders = {}
        for op in ops:
            text = _render([_ok("meeting_time", "Nothing on your calendar."), _ok(op, "Done.")])
            hit = [f for f in _forbidden(op) if f in text]
            if hit:
                offenders[op] = text
        assert not offenders, offenders

    def test_every_catalog_op_as_the_failed_half(self, ops):
        offenders = {}
        for op in ops:
            text = _render([_ok("meeting_time", "Nothing on your calendar."), _failed(op)])
            hit = [f for f in _forbidden(op) if f in text]
            if hit:
                offenders[op] = text
        assert not offenders, offenders

    def test_unlabeled_op_takes_the_topic_free_join(self):
        text = _render(
            [_ok("meeting_time", "Nothing on your calendar."), _ok("custom_op_x", "All good.")]
        )
        assert f"{TOPIC_FREE_TRANSITION}, all good." in text
        assert "custom op x" not in text and "custom_op_x" not in text

    def test_unlabeled_failures_collapse_to_one_mention(self):
        text = _render(
            [_ok("meeting_time", "Nothing."), _failed("custom_op_x"), _failed("custom_op_y")]
        )
        assert text.count(UNLABELED_FAILURE_TOPIC) == 1
        assert "custom" not in text

    def test_labeled_op_keeps_its_words(self):
        text = _render(
            [
                _ok("meeting_time", "Nothing on your calendar."),
                _ok("list_archived_projects", "You have none."),
            ]
        )
        assert "your archived projects" in text
        assert "list archived projects" not in text

    def test_label_or_none_for_every_op(self, ops):
        for op in ops:
            label = _intent_topic_label(_intent(op))
            assert label is None or (op not in label and op.replace("_", " ") != label), (op, label)
