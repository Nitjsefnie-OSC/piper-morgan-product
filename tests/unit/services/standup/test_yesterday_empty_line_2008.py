"""#2008 (CXO's ruling 2026-10-14): the Yesterday empty line states the fact and
guesses nothing. Served on alpha de7d0c1c57 the old line said "looks like you
were in planning mode" over an account with 25 stale open items and nothing
planned; Piper has no signal for what the person was doing. Ruled copy:
``No completions yesterday.`` Nothing added. No LLM, no DB.
"""

from __future__ import annotations

from services.domain.models import StandupItem, StandupSummary

RULED = "No completions yesterday."


def _summary_with_only_a_watch_item() -> StandupSummary:
    # One Watch item so the section renderer runs (an all-empty summary takes
    # the "Nothing to show yet" early return, which is a different face).
    return StandupSummary(watch=[StandupItem(display="issue body test", source="work")])


def test_yesterday_empty_line_is_the_ruled_copy():
    prose = _summary_with_only_a_watch_item().to_prose()
    assert RULED in prose, prose


def test_yesterday_empty_line_guesses_nothing():
    prose = _summary_with_only_a_watch_item().to_prose()
    assert "planning mode" not in prose, prose
    assert "looks like" not in prose, prose


def test_source_carries_no_planning_mode_guess_anywhere():
    import inspect

    import services.domain.models as m

    assert "planning mode" not in inspect.getsource(m)
