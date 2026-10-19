"""Pins scripts/draft_births.py (10-19 mini retro: a 06:45 draft sent unread at 11:19)."""

import importlib.util
from datetime import datetime
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "draft_births", Path(__file__).resolve().parents[3] / "scripts" / "draft_births.py"
)
db = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(db)


def at(hhmm: str) -> int:
    return int(
        datetime.strptime(f"2026-10-19 {hhmm}", "%Y-%m-%d %H:%M").replace(tzinfo=db.PT).timestamp()
    )


MEMO = "mailboxes/lead/sent/notice-lead-to-exec-board-line-2026-10-19.md"
LOG = (
    "2026-10-19 09:28 PT (arch) — #2083 RULED\n"
    "2026-10-19 10:01 PT (xian, in conversation with Lead) — ADMIN ACCOUNT: mvp-tester gets is_admin now\n"
    "continuation line without a stamp\n"
    "2026-10-19 12:28 PT (arch) — after the send\n"
)


def test_replays_the_1019_memo():
    rows = db.read_ledger(f"{MEMO}\t{at('06:45')}\n")
    msgs = db.warnings([MEMO], rows, LOG, at("11:19"))
    assert "first written 06:45, sending 11:19 (4h34m)" in msgs[0]
    assert msgs[1] == "  decisions.log since the draft (2):"
    assert "09:28" in msgs[2] and "ADMIN ACCOUNT" in msgs[3]
    assert not any("12:28" in m for m in msgs)


def test_fresh_draft_and_unknown_path_are_quiet():
    rows = db.read_ledger(f"{MEMO}\t{at('11:00')}\n")
    assert db.warnings([MEMO], rows, LOG, at("11:19")) == []
    assert db.warnings(["mailboxes/x/sent/other.md"], rows, LOG, at("23:00")) == []


def test_first_sighting_wins():
    rows = db.read_ledger(f"{MEMO}\t{at('06:45')}\n{MEMO}\t{at('11:00')}\nbad line\n")
    assert rows == {MEMO: at("06:45")}
