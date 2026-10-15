#!/usr/bin/env python3
"""stuck-session-check.py: find a seat that has mail waiting and hasn't woken since it landed.

Why (Exec, 2026-10-15): Lead's session sat on a permission prompt from 12:43 to 15:30 with
xian's promotion approval unread. The mail wakes fired, but nothing checks whether a woken
session actually woke, and the freeze detector's window (hours) is too wide to see it.

The rule, for each role in dev/active/duty-cycle-registry.tsv (origin/main), inside its wake
window (wake_start..wake_end, Pacific):

  STUCK  when some mail addressed to it landed more than --minutes ago (default 30)
         AND the role shows no sign of life since that mail landed.

Mail is both systems: v3 files in mailboxes/<role>/inbox/ (landing = the commit that added the
file) and v4 messages addressed to the role and not acked (landing = sent_at). A sign of life is
the newest of: a heartbeat row in the store (~/.local/state/piper-heartbeats/<date>/<role>.tsv;
a fire, a wake or a post-commit hook), a commit on origin/main whose subject is the role's
(`<role>:`, `<role>(`, or `<type>(<role>)`), or a v4 ack by the role. A session blocked on a prompt
produces none of these. Heartbeats alone weren't enough: only some seats write one per commit, and
the first backtest flagged Web as stuck at 14:30 while it was building an account.

Read-only: no fetch, no write. It reads origin/main as the caller last fetched it, in this repo
and in the v4 clone (PIPER_MAIL4_REPO, default ~/Development/piper-morgan-mail).

Usage:
  scripts/stuck-session-check.py [--minutes N] [--at "YYYY-MM-DD HH:MM"]
  --at replays a past moment (Pacific), using the tree, acks and heartbeat rows as of then.
Exit 0 = none stuck; 1 = at least one STUCK; 2 = could not run.

Limits, stated: it can't tell a stuck session from one that's busy and hasn't committed or
heartbeated in N minutes. The wake window and the N-minute grace reduce that, but it alerts on
silence, not on a prompt it can see. A role with no registry row isn't checked (state the
denominator). v3 mail a role left unfiled for days doesn't flag once the role has heartbeated
after it.

Cost: a few git reads per role, about a second. Benefit: none yet: measuring (backtest on
2026-10-15 in the CIO log). Review: 2026-12-08. Owner: CIO (the rule); where it runs is Pard's.
Concept: docs/internal/operations/liveness-current-state.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

PT = ZoneInfo("America/Los_Angeles")
ROOT = Path(__file__).resolve().parent.parent
MAIL4 = Path(os.environ.get("PIPER_MAIL4_REPO", str(Path.home() / "Development/piper-morgan-mail")))
STORE = Path(os.environ.get("PIPER_HB_STORE", str(Path.home() / ".local/state/piper-heartbeats")))
SKIP = {"MANIFEST.md", ".gitkeep", "README.md"}


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def rev_at(repo: Path, at: int | None) -> str:
    if at is None:
        return git(repo, "rev-parse", "-q", "--verify", "origin/main").strip()
    return git(repo, "rev-list", "-1", f"--before={at}", "origin/main").strip()


def registry(rev: str) -> list[tuple[str, int, int, str]]:
    rows = []
    for line in git(ROOT, "show", f"{rev}:dev/active/duty-cycle-registry.tsv").splitlines():
        f = line.split("\t")
        if not f or f[0] in ("", "role") or f[0].startswith("#") or len(f) < 5:
            continue
        try:
            rows.append((f[0], int(f[3]), int(f[4]), f[7] if len(f) > 7 else ""))
        except ValueError:
            continue
    return rows


def v3_pending(rev: str, role: str) -> list[tuple[int, str]]:
    out = []
    prefix = f"mailboxes/{role}/inbox/"
    for p in git(ROOT, "ls-tree", "--name-only", rev, prefix).splitlines():
        if p.rsplit("/", 1)[-1] in SKIP:
            continue
        ct = git(ROOT, "log", "-1", "--diff-filter=A", "--format=%ct", rev, "--", p).strip()
        if ct:
            out.append((int(ct), f"v3 {p.rsplit('/', 1)[-1]}"))
    return out


_V4: list[tuple[str, list[str], int]] | None = None


def v4_messages() -> list[tuple[str, list[str], int]]:
    """Every v4 message as (id, recipients, sent epoch), read once per run in one cat-file call."""
    global _V4
    if _V4 is not None:
        return _V4
    import yaml

    _V4 = []
    tip = rev_at(MAIL4, None)
    if not tip:
        return _V4
    shas = [
        line.split()[2]
        for line in git(MAIL4, "ls-tree", "-r", tip, "messages").splitlines()
        if line.endswith(".md")
    ]
    r = subprocess.run(
        ["git", "-C", str(MAIL4), "cat-file", "--batch"],
        input="\n".join(shas) + "\n",
        capture_output=True,
        text=True,
    )
    out, i = r.stdout, 0
    while i < len(out):
        header_end = out.index("\n", i)
        size = int(out[i:header_end].split()[2])
        text = out[header_end + 1 : header_end + 1 + size]
        i = header_end + 1 + size + 1
        if not text.startswith("---\n"):
            continue
        meta = yaml.safe_load(text[4:].partition("\n---\n")[0]) or {}
        if meta.get("id") and meta.get("sent_at"):
            to = list(meta.get("to") or []) + list(meta.get("cc") or [])
            sent = int(dt.datetime.fromisoformat(str(meta["sent_at"])).timestamp())
            _V4.append((str(meta["id"]), to, sent))
    return _V4


def v4_pending(role: str, at: int) -> list[tuple[int, str]]:
    tip = rev_at(MAIL4, None)
    acked = {}
    for line in git(MAIL4, "show", f"{tip}:acks/{role}.log").splitlines() if tip else []:
        parts = line.split(" ", 3)
        if len(parts) >= 2:
            try:
                acked.setdefault(parts[0], int(dt.datetime.fromisoformat(parts[1]).timestamp()))
            except ValueError:
                continue
    out = []
    for mid, to, sent in v4_messages():
        if role not in to or sent > at:
            continue
        a = acked.get(mid)
        if a is not None and a <= at:
            continue
        out.append((sent, f"v4 {mid}"))
    return out


def last_heartbeat(role: str, at: int) -> int | None:
    best = None
    day = dt.datetime.fromtimestamp(at, PT).date()
    for d in (day, day - dt.timedelta(days=1)):
        f = STORE / d.isoformat() / f"{role}.tsv"
        if not f.is_file():
            continue
        for line in f.read_text().splitlines():
            try:
                e = int(line.rsplit("\t", 1)[-1])
            except ValueError:
                continue
            if e <= at and (best is None or e > best):
                best = e
    return best


def last_commit(rev: str, role: str, at: int) -> int | None:
    import re

    mine = re.compile(rf"^(?:{role}[:(]|\w+\({role}\))")
    log = git(ROOT, "log", rev, f"--since={at - 2 * 86400}", f"--until={at}", "--format=%ct %s")
    for line in log.splitlines():
        ct, _, subj = line.partition(" ")
        if mine.match(subj):
            return int(ct)
    return None


def last_ack(role: str, at: int) -> int | None:
    tip = rev_at(MAIL4, None)
    best = None
    for line in git(MAIL4, "show", f"{tip}:acks/{role}.log").splitlines() if tip else []:
        parts = line.split(" ", 2)
        try:
            e = int(dt.datetime.fromisoformat(parts[1]).timestamp())
        except (IndexError, ValueError):
            continue
        if e <= at and (best is None or e > best):
            best = e
    return best


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--minutes", type=int, default=30)
    ap.add_argument("--at", help='replay a past moment, Pacific: "YYYY-MM-DD HH:MM"')
    a = ap.parse_args()
    at = (
        int(dt.datetime.strptime(a.at, "%Y-%m-%d %H:%M").replace(tzinfo=PT).timestamp())
        if a.at
        else int(dt.datetime.now(PT).timestamp())
    )
    rev = rev_at(ROOT, at if a.at else None)
    if not rev:
        print("stuck-session-check: origin/main did not resolve", file=sys.stderr)
        return 2
    hour = dt.datetime.fromtimestamp(at, PT).hour
    stuck = checked = 0
    for role, ws, we, state in registry(rev):
        if "parked" in state.lower()[:20]:
            print(f"skip   {role:<6} parked")
            continue
        if not (ws <= hour < we):
            print(f"skip   {role:<6} outside wake window {ws:02d}-{we:02d}")
            continue
        checked += 1
        signs = [
            x
            for x in (last_heartbeat(role, at), last_commit(rev, role, at), last_ack(role, at))
            if x
        ]
        hb = max(signs) if signs else None
        mail = v3_pending(rev, role) + v4_pending(role, at)
        late = sorted(m for m in mail if m[0] <= at - a.minutes * 60 and (hb is None or m[0] > hb))
        hb_s = dt.datetime.fromtimestamp(hb, PT).strftime("%m-%d %H:%M") if hb else "none"
        if late:
            stuck += 1
            first = late[0]
            age = (at - first[0]) // 60
            print(
                f"STUCK  {role:<6} {len(late)} mail waiting, oldest {age} min ({first[1]}); "
                f"last sign of life {hb_s}"
            )
        else:
            print(
                f"ok     {role:<6} {len(mail)} pending, none unanswered past {a.minutes} min; last sign of life {hb_s}"
            )
    when = dt.datetime.fromtimestamp(at, PT).strftime("%Y-%m-%d %H:%M %Z")
    print(
        f"stuck-session-check: {when}: {checked} roles checked, {stuck} STUCK (grace {a.minutes} min)"
    )
    return 1 if stuck else 0


if __name__ == "__main__":
    sys.exit(main())
