"""The quiet count (xian's ruling 2026-10-20; grant condition 3): name-free, rolling 30 minutes."""

from services.infrastructure.turn_activity import WINDOW_SECONDS, TurnActivity


def test_counts_distinct_accounts_and_turns_in_the_window():
    a = TurnActivity()
    a.record("user-a", now=1000.0)
    a.record("user-a", now=1100.0)
    a.record("user-b", now=1200.0)
    assert a.snapshot(now=1300.0) == {"accounts": 2, "turns": 3}


def test_turns_and_accounts_leave_the_window_after_30_minutes():
    a = TurnActivity()
    a.record("user-a", now=0.0)
    a.record("user-b", now=600.0)
    assert a.snapshot(now=WINDOW_SECONDS + 1.0) == {"accounts": 1, "turns": 1}
    assert a.snapshot(now=WINDOW_SECONDS + 601.0) == {"accounts": 0, "turns": 0}


def test_no_principal_is_a_turn_but_not_an_account():
    a = TurnActivity()
    a.record(None, now=10.0)
    assert a.snapshot(now=11.0) == {"accounts": 0, "turns": 1}


def test_no_raw_id_is_kept():
    a = TurnActivity()
    a.record("694d8f4e-0000-0000-0000-000000000042", now=5.0)
    keys = list(a._last_turn_by_account)
    assert keys and all("694d8f4e" not in k and len(k) == 16 for k in keys)


def test_window_is_thirty_minutes():
    assert WINDOW_SECONDS == 1800
