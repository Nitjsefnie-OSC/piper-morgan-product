"""1942 — every Intent hands handlers the user's message in BOTH places.

The message lives in ``Intent.original_message`` AND
``Intent.context["original_message"]`` (Issue #744's duality). The routing
surfaces filled them unevenly — the pre-classifier set context only, the
Inversion router set the top-level field only — and handlers read one or the
other, so a router-served "get issue 101" reached a context-only reader as
an empty string (PM live, alpha v169, 2026-10-05). The model now mirrors
whichever side is present, so no constructor can produce a one-sided Intent.

Layer: the dataclass alone — these are model tests, not routing tests. The
router-side pin is test_inversion_intent_shape_1942.py.
"""

from unittest.mock import patch

from services.domain import models
from services.domain.models import Intent
from services.shared_types import IntentCategory


def test_top_level_only_is_mirrored_into_context():
    i = Intent(
        category=IntentCategory.QUERY, action="review_issue_query", original_message="get issue 101"
    )
    assert i.context["original_message"] == "get issue 101"
    assert i.original_message == "get issue 101"


def test_context_only_is_mirrored_to_top_level():
    i = Intent(
        category=IntentCategory.QUERY,
        action="review_issue_query",
        context={"original_message": "get issue #101"},
    )
    assert i.original_message == "get issue #101"
    assert i.context["original_message"] == "get issue #101"


def test_both_set_and_equal_are_left_alone():
    i = Intent(
        category=IntentCategory.QUERY,
        action="x",
        original_message="same turn",
        context={"original_message": "same turn"},
    )
    assert i.original_message == "same turn"
    assert i.context["original_message"] == "same turn"


def test_both_set_and_different_normalizes_to_attribute_and_warns():
    """#1459 (Arch, 2026-10-12): divergence is repaired, not pinned. The typed
    top-level field wins, the dict follows, and the repair is logged — never
    raised. No writer on main produces this shape; the model makes it
    impossible to keep rather than relying on that."""
    with patch.object(models, "logger") as log:
        i = Intent(
            category=IntentCategory.QUERY,
            action="x",
            original_message="whole turn",
            context={"original_message": "the segment"},
        )
    assert i.original_message == "whole turn"
    assert i.context["original_message"] == "whole turn"
    log.warning.assert_called_once()
    assert log.warning.call_args.args[0] == "intent_original_message_diverged"
    assert log.warning.call_args.kwargs["repair"] == "normalized_to_attribute"


def test_bind_original_message_sets_both_surfaces():
    """The one setter (#1459): a fill after construction lands on both sides."""
    i = Intent(category=IntentCategory.QUERY, action="x")
    i.bind_original_message("filled later")
    assert i.original_message == "filled later"
    assert i.context["original_message"] == "filled later"


def test_bind_original_message_tolerates_a_none_context():
    i = Intent(category=IntentCategory.QUERY, action="x")
    i.context = None  # type: ignore[assignment]  # a legacy caller's shape
    i.bind_original_message("still both")
    assert i.original_message == "still both"
    assert i.context == {"original_message": "still both"}


def test_neither_set_stays_empty_and_context_is_a_dict():
    i = Intent(category=IntentCategory.QUERY, action="x")
    assert i.original_message == ""
    assert "original_message" not in i.context
    assert isinstance(i.context, dict)


def test_other_context_keys_survive_the_mirror():
    i = Intent(
        category=IntentCategory.QUERY,
        action="x",
        original_message="hello",
        context={"inversion_live": True, "inversion_args": {"n": 1}},
    )
    assert i.context == {
        "inversion_live": True,
        "inversion_args": {"n": 1},
        "original_message": "hello",
    }


def test_the_failing_handler_shape_now_sees_the_number():
    """The exact read _handle_review_issue_query does, against the exact
    shape the router used to produce."""
    import re

    i = Intent(
        category=IntentCategory.QUERY, action="review_issue_query", original_message="get issue 101"
    )
    m = re.search(r"#?(\d+)", i.context.get("original_message", ""))
    assert m and m.group(1) == "101"
