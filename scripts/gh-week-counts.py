#!/usr/bin/env python3
"""gh-week-counts.py — issues opened and closed in a Pacific-time window, counted without truncation.

#1968 item 5 (Exec 8.2). Ship #062 was first drafted at 43 opened / 34 closed when the true figures were
91 / 57. Two causes: `gh issue list` and `gh search` return 30 results unless told otherwise, and
date-only `created:`/`closed:` ranges are UTC calendar days, not our Pacific week. This asks the REST
search API for `total_count` (never a result list, so nothing to truncate) with explicit Pacific
timestamps. The UTC offset is computed per date, so it moves from -07:00 to -08:00 on its own when DST
ends (2026-11-01). The runbook's hand-written `-07:00` doesn't.

  scripts/gh-week-counts.py 2026-10-09                 the Fri→Thu week starting that day
  scripts/gh-week-counts.py 2026-10-09 2026-10-15      any inclusive Pacific date range
  scripts/gh-week-counts.py 2026-10-09 -- 'milestone:MVP sprint:"Beta Blockers - Hard Gates Only"'

Everything after `--` is added to both queries. Prints the exact queries so the figure can be re-run.
Uses REST search (30 requests/min), not the GraphQL budget the cohort shares. A failed query prints
UNMEASURED and exits 1. It never prints 0 for a query that didn't run (weekly-cycle-runbook.md, step 4).
Owner: CIO. Review: 2026-12-08. Runbook: docs/internal/operations/weekly-cycle-runbook.md.
"""

import json
import subprocess
import sys
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

REPO = "mediajunkie/piper-morgan-product"
PT = ZoneInfo("America/Los_Angeles")


def stamp(d: date) -> str:
    return datetime.combine(d, time(0, 0), PT).isoformat()


def total(q: str):
    r = subprocess.run(
        [
            "gh",
            "api",
            "-X",
            "GET",
            "search/issues",
            "-f",
            f"q={q}",
            "-f",
            "per_page=1",
            "--jq",
            ".total_count,.incomplete_results",
        ],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None, r.stderr.strip()[:200]
    count, incomplete = r.stdout.split()
    return int(count), ("GitHub flagged incomplete_results" if incomplete == "true" else "")


def main(argv) -> int:
    extra = ""
    if "--" in argv:
        k = argv.index("--")
        extra, argv = " ".join(argv[k + 1 :]), argv[:k]
    if len(argv) not in (1, 2):
        print(__doc__.split("\n\n")[2], file=sys.stderr)
        return 2
    start = date.fromisoformat(argv[0])
    last = date.fromisoformat(argv[1]) if len(argv) == 2 else start + timedelta(days=6)
    window = f"{stamp(start)}..{stamp(last + timedelta(days=1))}"
    print(f"gh-week-counts: {REPO}, Pacific {start} through {last} inclusive")
    rc = 0
    for label, field in (("opened", "created"), ("closed", "closed")):
        q = f"repo:{REPO} is:issue {field}:{window} {extra}".strip()
        n, note = total(q)
        if n is None:
            print(f"  {label:7} UNMEASURED ({note})")
            rc = 1
        else:
            print(f"  {label:7} {n}{'  ⚠ ' + note if note else ''}")
        print(f"          q: {q}")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
