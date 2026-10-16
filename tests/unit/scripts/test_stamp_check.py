"""Pins scripts/stamp_check.py's rules (xian 2026-10-16 via Exec: a date check in mail-send and the log)."""

import importlib.util
from datetime import datetime
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "stamp_check", Path(__file__).resolve().parents[3] / "scripts" / "stamp_check.py"
)
sc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sc)

NOW = datetime(2026, 10, 16, 16, 20, tzinfo=sc.PT)
DAY = "2026-10-16"


@pytest.mark.parametrize(
    "stamp, level",
    [
        ("2026-10-16 16:20 PT", None),
        ("2026-10-16 16:24 PT", None),
        ("2026-10-16", None),
        ("2026-10-16 16:26 PT", "BLOCK"),
        ("2026-10-16 17:40 PT", "BLOCK"),
        ("2026-10-16 16:2x PT", "WARN"),
        ("2026-10-16 16:1x PT", "WARN"),
        ("2026-10-16 14:2x PT", "BLOCK"),
        ("2026-10-16 16:5x PT", "BLOCK"),
        ("~16:20", "WARN"),
        ("2026-10-16 15:40 PT", "WARN"),
        ("2026-10-14", "WARN"),
        ("2026-10-17 09:00 PT", "BLOCK"),
    ],
)
def test_judge(stamp, level):
    v = sc.judge(stamp, NOW, DAY)
    assert (v[0] if v else None) == level, v


def test_front_date_reads_only_front_matter():
    assert (
        sc.front_date("---\nfrom: cio\ndate: 2026-10-16 16:20 PT\n---\ndate: nope\n")
        == "2026-10-16 16:20 PT"
    )
    assert sc.front_date("no front matter\ndate: 2026-10-16\n") is None
