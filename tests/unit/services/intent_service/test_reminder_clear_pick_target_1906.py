"""#1906 — the pick-target BINDER (``reminder_clear._resolve_pick_target``).

#1906 armed the reminder-clear "which one do you mean?" clarify with a
carrier whose answer bound by ordinal / name / an unambiguous status word.
That CARRIER (its offer, answer turn, registry entry and re-entry into the
old three-variant flow) retired on 2026-10-14 with the regex seam that armed
it (detect_clear_family_ask / maybe_handle_clear_family — Arch's clear_todos
ruling, point 1; see reminder_clear.py's module docstring). Its end-to-end
classes went with it. The BINDER survives: #1987's delete_todo pick
(delete_todo_pick.py) and todo_handlers share it, so its pure-function pins
stay here unchanged.
"""

from datetime import datetime, timedelta, timezone

import pytest

from services.intent_service import reminder_clear as rc

_NOW = datetime.now(timezone.utc)
_PAST = _NOW - timedelta(days=1)
_SOON = _NOW + timedelta(days=1)
_LATER = _NOW + timedelta(days=2)


# ---------------------------------------------------------------------------
# Unit — the binding predicate itself (no service, no DB, pure function)
# ---------------------------------------------------------------------------


class TestResolvePickTargetOrdinal:
    _TEXTS = ["check the test card", "review the pr"]

    @pytest.mark.parametrize(
        "text,expected_index",
        [
            ("Clear the first one.", 0),
            ("the first one", 0),
            ("first", 0),
            ("second", 1),
            ("#2", 1),
            ("2", 1),
            ("last", 1),
        ],
    )
    def test_ordinal_forms_bind(self, text, expected_index):
        assert rc._resolve_pick_target(text, self._TEXTS, [None, None]) == (
            "bound",
            expected_index,
        )

    def test_out_of_range_ordinal_does_not_bind(self):
        """'#108' (an unrelated command's issue number) must never be read
        as a position reference into a 2-item list — it falls through to
        the other binding forms (and here, to 'none')."""
        status, idx = rc._resolve_pick_target("close issue #108", self._TEXTS, [None, None])
        assert status == "none"
        assert idx is None


class TestResolvePickTargetName:
    _TEXTS = ["check the test card", "review the pr"]

    def test_literal_substring_match_binds(self):
        assert rc._resolve_pick_target("review the pr", self._TEXTS, [None, None]) == (
            "bound",
            1,
        )

    def test_partial_significant_word_overlap_binds(self):
        """'the test card one' names no ordinal and isn't a literal
        substring of either candidate, but shares 'test'/'card' with only
        one of the two."""
        assert rc._resolve_pick_target("the test card one", self._TEXTS, [None, None]) == (
            "bound",
            0,
        )

    def test_tied_overlap_is_ambiguous(self):
        texts = ["check the test card", "check the test card again"]
        status, idx = rc._resolve_pick_target("the test card one", texts, [None, None])
        assert status == "ambiguous"
        assert idx is None

    def test_no_overlap_is_none(self):
        status, idx = rc._resolve_pick_target("maybe later", self._TEXTS, [None, None])
        assert status == "none"
        assert idx is None


class TestResolvePickTargetStatus:
    _TEXTS = ["check the test card", "review the pr"]

    def test_unambiguous_overdue_binds(self):
        due = [_PAST.isoformat(), _SOON.isoformat()]
        assert rc._resolve_pick_target("the overdue one", self._TEXTS, due) == (
            "bound",
            0,
        )

    def test_multiple_overdue_is_ambiguous(self):
        due = [_PAST.isoformat(), _PAST.isoformat()]
        status, idx = rc._resolve_pick_target("the overdue one", self._TEXTS, due)
        assert status == "ambiguous"
        assert idx is None

    def test_no_due_data_skips_the_form_honestly(self):
        """No candidate carries a timestamp — 'overdue' resolves to 'none'
        (never guessed), per the task's own instruction to skip the form
        when status isn't available."""
        status, idx = rc._resolve_pick_target("the overdue one", self._TEXTS, [None, None])
        assert status == "none"
        assert idx is None
