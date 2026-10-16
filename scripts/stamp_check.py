#!/usr/bin/env python3
"""stamp_check.py — catch a guessed clock time in a memo's `date:` or a session-log heading.

xian, 2026-10-16 (Ship #065 week review, via Exec): "Yes, date-check seems sound." 7 of 10 roles wrote
guessed times in the week of 10-09, and every one had to be corrected. Writing the rule down (duty-cycle-tick
v1.50) wasn't enough, so the tool checks instead. The clock is `America/Los_Angeles` now.

  stamp_check.py --mail PATH...    memos about to be sent (scripts/mail-send.sh calls this)
  stamp_check.py --log-staged      session-log headings in `git diff --cached` (check-branch.sh calls this)

Mail mode looks only at memos that are new: a file whose exact content is already on origin/main (a move
to read/, a triage of someone else's memo) is skipped. For each new memo's front-matter `date:`:
  BLOCK  a time more than 5 minutes ahead of now, or an `HH:Mx` form more than 10 minutes from now
  WARN   an `HH:Mx` or `~HH:MM` form near now (v1.50 bans both; write the minute), a time more than
         30 minutes behind now (drafted earlier? say so), or a date-only stamp that isn't today
`MAIL_STAMP_CHECK=warn` turns every BLOCK into a WARN, for a memo deliberately stamped another time.
Log mode only warns. It looks at added lines in staged `dev/YYYY/MM/DD/*-log.md` files that are `#`
headings carrying a time, and only for today's log: it flags an estimated form or a time ahead of now, not
one behind (a heading can fairly carry the time a wake began).
Exit 0 = nothing blocking; 1 = a BLOCK (mail mode only). Owner: CIO. Review: 2026-12-08.
"""

import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

PT = ZoneInfo("America/Los_Angeles")
AHEAD = timedelta(minutes=5)
BEHIND = timedelta(minutes=30)
MX = re.compile(r"\b(\d{1,2}):(\d)[xX]\b")
NEAR = timedelta(minutes=10)
CLOCK = re.compile(r"\b(\d{1,2}):(\d{2})\b")
DAY = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)


def judge(stamp: str, now: datetime, default_day: str):
    """Return (level, reason) for one stamp, or None if it's fine."""
    d = DAY.search(stamp)
    day = d.group(1) if d else default_day
    rest = stamp[d.end() :] if d else stamp
    m = MX.search(rest)
    if m:
        lo = datetime.strptime(
            f"{day} {int(m.group(1)):02d}:{m.group(2)}0", "%Y-%m-%d %H:%M"
        ).replace(tzinfo=PT)
        hi = lo + timedelta(minutes=9)
        if lo - NEAR <= now <= hi + NEAR:
            return (
                "WARN",
                f"'{stamp.strip()}' is an estimated form (duty-cycle-tick v1.50); write the minute from date",
            )
        return (
            "BLOCK",
            f"'{stamp.strip()}' is an estimated time more than 10 min from now ({now:%H:%M})",
        )
    estimated = "~" in rest
    c = CLOCK.search(rest)
    if not c:
        if d and day != now.strftime("%Y-%m-%d"):
            return "WARN", f"dated {day}, today is {now:%Y-%m-%d}"
        return None
    when = datetime.strptime(f"{day} {int(c.group(1)):02d}:{c.group(2)}", "%Y-%m-%d %H:%M").replace(
        tzinfo=PT
    )
    if when - now > AHEAD:
        return (
            "BLOCK",
            f"{when:%Y-%m-%d %H:%M} is {int((when - now).total_seconds() // 60)} min ahead of now ({now:%H:%M})",
        )
    if now - when > BEHIND:
        return (
            "WARN",
            f"{when:%Y-%m-%d %H:%M} is {int((now - when).total_seconds() // 60)} min behind now ({now:%H:%M})",
        )
    if estimated:
        return (
            "WARN",
            f"'{stamp.strip()}' is an estimated form (duty-cycle-tick v1.50); write the minute from date",
        )
    return None


def front_date(text: str):
    if not text.startswith("---"):
        return None
    fm = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    m = re.search(r"^date:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def mail(paths, now) -> int:
    on_main = set()
    r = git("ls-tree", "-r", "origin/main", "mailboxes/")
    for line in r.stdout.splitlines():
        on_main.add(line.split()[2])
    soft = os.environ.get("MAIL_STAMP_CHECK") == "warn"
    blocked = 0
    for p in paths:
        if not os.path.isfile(p):
            continue
        blob = git("hash-object", p).stdout.strip()
        if blob in on_main:
            continue
        stamp = front_date(open(p, encoding="utf-8", errors="replace").read())
        if not stamp:
            continue
        v = judge(stamp, now, now.strftime("%Y-%m-%d"))
        if not v:
            continue
        level, why = v
        if level == "BLOCK" and soft:
            level = "WARN"
        print(f"stamp-check {level}: {p}: date: {why}", file=sys.stderr)
        blocked += level == "BLOCK"
    return 1 if blocked else 0


def log_staged(now) -> int:
    today = now.strftime("%Y-%m-%d")
    files = git("diff", "--cached", "--name-only").stdout.split()
    for f in files:
        m = re.match(r"dev/\d{4}/\d{2}/\d{2}/(\d{4}-\d{2}-\d{2})-.*-log\.md$", f)
        if not m or m.group(1) != today:
            continue
        for line in git("diff", "--cached", "-U0", "--", f).stdout.splitlines():
            if not line.startswith("+#"):
                continue
            v = judge(line[1:], now, today)
            if v and "behind" not in v[1] and "dated" not in v[1]:
                print(f"stamp-check WARN: {f}: heading '{line[1:].strip()[:70]}': {v[1]}")
    return 0


def main(argv) -> int:
    now = datetime.now(PT).replace(second=0, microsecond=0)
    if argv[:1] == ["--mail"]:
        return mail(argv[1:], now)
    if argv == ["--log-staged"]:
        return log_staged(now)
    print(__doc__.split("\n\n")[2], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
