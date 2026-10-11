#!/usr/bin/env python3
"""Per-row diff of two Phase-1 shadow-score reports (the rule-7 'diff vs the
last full run' step), from their own '## Row detail (asserted rows)' tables.
No LLM calls.

    venv/bin/python scripts/inversion_report_diff.py OLD.md NEW.md

Prints: shared-row totals, IMPROVED (MISMATCH→MATCH), WORSENED (MATCH→MISMATCH),
and ROUTE-CHANGED rows whose verdict did not change (same answer, different
op — the ones ×6 attribution usually has to look at), then rows only in one
report. Worsened rows are the candidates for a ×6 attribution control
(`scripts/inversion_router_control.py`) before anyone calls them regressions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_ROUTE_RE = re.compile(r"`([^`]*)`\s*@?([0-9.]*)")


def parse(path: Path) -> dict[str, dict]:
    lines = path.read_text().splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Row detail (asserted rows)")
    except StopIteration:
        raise SystemExit(f"{path}: no '## Row detail (asserted rows)' section")
    rows: dict[str, dict] = {}
    in_table = False
    for line in lines[start + 1 :]:
        s = line.strip()
        if s.startswith("| phrase |"):
            in_table = True
            continue
        if not in_table or s.startswith("|---"):
            continue
        if not s.startswith("|"):
            break
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 5:
            continue
        phrase, category, expected, route_cell, verdict = cols[:5]
        m = _ROUTE_RE.search(route_cell)
        route = m.group(1) if m else route_cell
        conf = m.group(2) if m and m.group(2) else ""
        rows[f"{category}::{phrase}"] = {
            "phrase": phrase,
            "category": category,
            "expected": expected,
            "route": route,
            "conf": conf,
            "verdict": verdict,
        }
    if not rows:
        raise SystemExit(f"{path}: parsed zero rows")
    return rows


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    old, new = parse(Path(argv[1])), parse(Path(argv[2]))
    shared = sorted(set(old) & set(new))
    improved, worsened, moved = [], [], []
    for k in shared:
        o, n = old[k], new[k]
        if o["verdict"] != n["verdict"]:
            (improved if n["verdict"] == "MATCH" else worsened).append((o, n))
        elif o["route"] != n["route"]:
            moved.append((o, n))
    om = sum(1 for k in shared if old[k]["verdict"] == "MATCH")
    nm = sum(1 for k in shared if new[k]["verdict"] == "MATCH")
    print(
        f"shared asserted rows: {len(shared)} · old MATCH {om} · new MATCH {nm} · net {nm - om:+d}"
    )
    print(f"only in old: {len(set(old) - set(new))} · only in new: {len(set(new) - set(old))}")

    def table(title: str, pairs: list) -> None:
        print(f"\n## {title} ({len(pairs)})")
        if not pairs:
            return
        print("| category | phrase | expected | old route | new route | old→new verdict |")
        print("|---|---|---|---|---|---|")
        for o, n in pairs:
            print(
                f"| {o['category']} | {o['phrase']} | {o['expected']} | `{o['route']}` @{o['conf']} | "
                f"`{n['route']}` @{n['conf']} | {o['verdict']}→{n['verdict']} |"
            )

    table("IMPROVED (→MATCH)", improved)
    table("WORSENED (MATCH→)", worsened)
    table("ROUTE CHANGED, verdict unchanged", moved)
    only_new = sorted(set(new) - set(old))
    if only_new:
        print(f"\n## only in new: {', '.join(only_new[:20])}{' …' if len(only_new) > 20 else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
