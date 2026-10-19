#!/usr/bin/env python3
"""draft_births.py — warn at send when a memo was drafted hours earlier, and show what was decided since.

10-19 (Exec's mini-retro ask, xian: "worth a mini retro"): Lead's 11:19 board memo was a 06:45 draft. The sha was
filled in, `date:` re-stamped and the body sent unread. It still said `dinp`, five hours after xian's 10:01
mvp-tester ruling. Nothing already in place could see it: stamp_check read a fresh `date:`; a file's birth time
resets on every Edit or `sed -i` (both write a new inode, measured 10-19); the sha was the one fact refreshed; and
the superseding decisions.log line cites #1599, not the memo's #2081. What the drafter can't fake is when the
file first appeared, so a hook records that.

  draft_births.py record          .claude/hooks/draft-birth-record.sh (PostToolUse) calls this: every untracked
                                  file under mailboxes/ not yet in the ledger gets the current time
  draft_births.py check PATH...   scripts/mail-send.sh calls this: for a path first seen more than 60 min ago,
                                  WARN with its age and today's decisions.log lines stamped after it; then drop
                                  those rows. Never blocks: exit 0 always.

Ledger: dev/state/draft-births.tsv (gitignored, per worktree; drafting and sending happen in the same one).
Cost:    one `git ls-files --others` per tool call (~20 ms), one read at send
Benefit: none yet: measuring (the 10-19 memo is the motivating miss, replayed in the tests)
Review:  2026-12-14
Owner:   CIO
Concept: docs/internal/operations/hooks-registry.md
"""

import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

PT = ZoneInfo("America/Los_Angeles")
LEDGER = Path("dev/state/draft-births.tsv")
DECISIONS = Path("docs/internal/architecture/decisions/decisions.log")
OLD = 60 * 60
LINE = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d{1,2}):(\d{2})")


def read_ledger(text: str) -> dict:
    rows = {}
    for line in text.splitlines():
        path, _, when = line.partition("\t")
        if when.strip().isdigit():
            rows.setdefault(path, int(when))
    return rows


def decided_since(log_text: str, born: int, now: int):
    """decisions.log lines whose leading stamp falls after `born` and not after `now`."""
    out = []
    for line in log_text.splitlines():
        m = LINE.match(line)
        if not m:
            continue
        t = datetime.strptime(f"{m.group(1)} {int(m.group(2)):02d}:{m.group(3)}", "%Y-%m-%d %H:%M")
        stamp = int(t.replace(tzinfo=PT).timestamp())
        if born < stamp <= now:
            out.append(line)
    return out


def warnings(paths, rows: dict, log_text: str, now: int):
    msgs = []
    for p in paths:
        born = rows.get(p)
        if born is None or now - born <= OLD:
            continue
        age = (now - born) // 60
        b = datetime.fromtimestamp(born, PT)
        n = datetime.fromtimestamp(now, PT)
        msgs.append(
            f"draft-age WARN: {p} was first written {b:%H:%M}, sending {n:%H:%M} ({age // 60}h{age % 60:02d}m). "
            "Re-read the body: facts may have moved."
        )
        since = decided_since(log_text, born, now)
        if since:
            msgs.append(f"  decisions.log since the draft ({len(since)}):")
            msgs += [f"    {s[:150]}" for s in since[:10]]
            if len(since) > 10:
                msgs.append(
                    f"    (+{len(since) - 10} more; the earliest come first, nearest the draft)"
                )
    return msgs


def record():
    r = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "mailboxes"],
        capture_output=True,
        text=True,
    )
    if r.returncode:
        return
    unsent = [p for p in r.stdout.splitlines() if p]
    old = read_ledger(LEDGER.read_text() if LEDGER.exists() else "")
    now = int(time.time())
    rows = {p: old.get(p, now) for p in unsent}  # keep first sightings; drop files no longer unsent
    if rows != old:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text("".join(f"{p}\t{w}\n" for p, w in rows.items()))


def check(paths):
    if not LEDGER.exists():
        return
    root = Path.cwd()
    paths = [
        str(Path(p).resolve().relative_to(root)) if Path(p).is_absolute() else p for p in paths
    ]
    rows = read_ledger(LEDGER.read_text())
    log_text = DECISIONS.read_text(errors="replace") if DECISIONS.exists() else ""
    for m in warnings(paths, rows, log_text, int(time.time())):
        print(m, file=sys.stderr)
    keep = {p: w for p, w in rows.items() if p not in set(paths)}
    LEDGER.write_text("".join(f"{p}\t{w}\n" for p, w in keep.items()))


def main(argv) -> int:
    try:
        if argv[:1] == ["record"]:
            record()
        elif argv[:1] == ["check"]:
            check(argv[1:])
        else:
            print(__doc__.split("\n\n")[2], file=sys.stderr)
    except Exception as e:  # advisory: never break a tool call or a send
        print(f"draft_births: skipped ({type(e).__name__})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
