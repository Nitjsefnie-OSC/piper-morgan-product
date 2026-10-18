"""#2079: the standup's greeting follows the user's clock, not the server's.

Served 2026-10-17 16:29 PT (xian, alpha 118241587e): "give me a standup" opened
"**Good morning!**" under a page header reading "Good afternoon". CXO (18:48):
the greeting follows the user's local time; when the zone is unknown, a
neutral "Hi". Pins: the helper under a patched clock at 09:00 / 16:00 / 21:00
Pacific, the neutral line for no zone and for a bogus zone, and the per-user
wrapper resolving the zone and degrading on a resolver failure.

Layer: unit; the clock and the zone resolver are patched.
"""

from __future__ import annotations

from datetime import datetime

import pytest

from services.consciousness import conversation_consciousness as cc
from services.standup import greeting as g

LA = "America/Los_Angeles"


def _freeze(monkeypatch, hour: int) -> None:
    """Pin ``datetime.now(tz)`` inside the day-part helper to ``hour`` in ``tz``."""

    class _Frozen(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[override]
            return datetime(2026, 10, 17, hour, 0, tzinfo=tz)

    monkeypatch.setattr(cc, "datetime", _Frozen)


class TestGreetingFollowsTheUsersClock:
    @pytest.mark.parametrize(
        "hour, expected",
        [
            (7, "Good morning!"),
            (9, "Good morning!"),
            (16, "Good afternoon!"),
            (21, "Good evening!"),
        ],
    )
    def test_day_part_in_the_users_zone(self, monkeypatch, hour, expected):
        _freeze(monkeypatch, hour)
        assert g.standup_greeting(LA) == expected

    def test_unknown_zone_is_neutral(self, monkeypatch):
        _freeze(monkeypatch, 9)
        assert g.standup_greeting(None) == "Hi!"

    def test_bogus_zone_is_neutral(self, monkeypatch):
        _freeze(monkeypatch, 9)
        assert g.standup_greeting("Mars/Olympus_Mons") == "Hi!"


class TestPerUserWrapper:
    async def test_resolves_the_users_zone(self, monkeypatch):
        _freeze(monkeypatch, 16)
        seen = {}

        async def _tz(user_id):
            seen["user_id"] = user_id
            return LA

        monkeypatch.setattr(g, "get_user_timezone", _tz)
        assert await g.standup_greeting_for("u-2079") == "Good afternoon!"
        assert seen["user_id"] == "u-2079"

    async def test_resolver_failure_degrades_to_neutral(self, monkeypatch):
        _freeze(monkeypatch, 16)

        async def _boom(user_id):
            raise RuntimeError("store down")

        monkeypatch.setattr(g, "get_user_timezone", _boom)
        assert await g.standup_greeting_for("u-2079") == "Hi!"

    async def test_no_zone_on_record_is_neutral(self, monkeypatch):
        _freeze(monkeypatch, 16)

        async def _none(user_id):
            return None

        monkeypatch.setattr(g, "get_user_timezone", _none)
        assert await g.standup_greeting_for("u-2079") == "Hi!"
