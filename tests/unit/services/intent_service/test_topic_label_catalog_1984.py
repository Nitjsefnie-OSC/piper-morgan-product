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

    def test_unlabeled_failure_reads_do_part_of_that(self):
        """CXO's copy (2026-10-11): an unlabeled part is something Piper could
        not "do" (a plan can include writes), never "checked on"."""
        text = _render([_ok("meeting_time", "Nothing."), _failed("custom_op_x")])
        assert f"I wasn't able to do {UNLABELED_FAILURE_TOPIC} right now" in text
        assert "custom" not in text

    def test_mixed_failures_list_labels_then_part_of_that(self):
        text = _render(
            [_ok("list_todos_query", "Nothing."), _failed("meeting_time"), _failed("custom_op_x")]
        )
        assert "check on your calendar and part of that right now" in text
        assert "custom" not in text

    def test_third_result_never_reads_on_the_your_front(self):
        """CXO's second defect (2026-10-11): "On the {topic} front" at index 2
        produced "On the your calendar front" for every "your …" label."""
        text = _render(
            [
                _ok("list_todos_query", "Two todos."),
                _ok("list_archived_projects", "None archived."),
                _ok("meeting_time", "Nothing on your calendar."),
            ]
        )
        assert "On the your" not in text and " front," not in text
        assert "As for your calendar" in text or "Regarding your calendar" in text

    def test_cxo_labels_present(self):
        assert _intent_topic_label(_intent("list_milestones")) == "your milestones"
        assert _intent_topic_label(_intent("session_activity_query")) == "this session"

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
