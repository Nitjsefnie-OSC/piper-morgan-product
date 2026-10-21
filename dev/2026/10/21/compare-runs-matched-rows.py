#!/usr/bin/env python3
"""Compare two canonical-run CSVs on matched rows (PPM's OpenAI pass bar, 10-20 18:21).

Reads two results CSVs written by dev/2026/10/19/canonical-retest-1386-alpha.py and reports,
on the rows both runs count:
  - routing, effect reading (the harness's routing_pass column)
  - routing, category reading (expected_routing against actual_routing_category)
  - expected-pass quality (judge PASS / judged, known_pathological rows left out)

Rows whose answer depends on the #1386 seed are excluded from both sides, so an unseeded
OpenAI account is compared fairly against the seeded Anthropic run. The seed rows come from
dev/2026/10/20/1386-seeded-account-spec-2026-10-20.md, sections 2-4.

This is analysis only. It does not touch the frozen harness (f7ae6f66a4).

Usage:
    python3 compare-runs-matched-rows.py BASELINE.csv CANDIDATE.csv [--keep-seeded]
"""

import argparse
import csv
import sys

# Seed-dependent rows, by spec section. Q53 and Q51 are fed by two sections.
SEED_GITHUB = {19, 25, 41, 42, 43, 45, 51, 52, 53}
SEED_CALENDAR = {8, 33, 34, 35, 61, 62}
SEED_PIPER = {10, 11, 12, 13, 14, 18, 21, 30, 51, 53, 55, 56}
SEEDED = SEED_GITHUB | SEED_CALENDAR | SEED_PIPER

JUDGED = ("PASS", "MARGINAL", "FAIL")
BAR_POINTS = 5.0


def routing_match(expected: str, actual: str) -> bool:
    # Same rule as the harness's routing_match (preclass reads as canonical or floor).
    return expected == actual or (expected == "preclass" and actual in ("canonical", "floor"))


def load(path: str) -> dict:
    with open(path, newline="") as f:
        return {int(r["query_num"]): r for r in csv.DictReader(f)}


def score(rows: list) -> dict:
    n = len(rows)
    effect = sum(1 for r in rows if r.get("routing_pass") == "True")
    has_cat = all("actual_routing_category" in r for r in rows)
    category = (
        sum(
            1
            for r in rows
            if routing_match(r["expected_routing"], r.get("actual_routing_category") or "")
        )
        if has_cat
        else None
    )
    ep = [r for r in rows if r.get("known_pathological") != "True"]
    judged = [r for r in ep if r.get("judge_verdict") in JUDGED]
    passes = sum(1 for r in judged if r["judge_verdict"] == "PASS")
    return {
        "n": n,
        "effect": effect,
        "category": category,
        "ep_pass": passes,
        "ep_judged": len(judged),
    }


def pct(a, b):
    return (100.0 * a / b) if b else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline")
    ap.add_argument("candidate")
    ap.add_argument("--keep-seeded", action="store_true", help="do not exclude seed rows")
    a = ap.parse_args()

    base, cand = load(a.baseline), load(a.candidate)
    common = sorted(set(base) & set(cand))
    excluded = set() if a.keep_seeded else SEEDED
    matched = [q for q in common if q not in excluded]

    sb = score([base[q] for q in matched])
    sc = score([cand[q] for q in matched])

    print(
        f"Matched rows: {len(matched)} of {len(common)} common "
        f"(excluded seed rows: {len(set(common) & excluded)})"
    )
    print(f"Excluded: {sorted(set(common) & excluded)}")
    print()
    print(
        f"{'measure':<28}{'baseline':>14}{'candidate':>14}{'delta pts':>11}  within {BAR_POINTS:g}?"
    )
    ok = True
    lines = [
        ("routing (effect)", "effect", "n"),
        ("routing (category)", "category", "n"),
        ("expected-pass quality", "ep_pass", "ep_judged"),
    ]
    for label, num, den in lines:
        if sb[num] is None or sc[num] is None:
            print(f"{label:<28}{'n/a':>14}{'n/a':>14}")
            continue
        pb, pc = pct(sb[num], sb[den]), pct(sc[num], sc[den])
        d = pc - pb
        within = d >= -BAR_POINTS
        # The bar compares effect routing and quality; category is reported, not barred.
        if num != "category":
            ok = ok and within
        print(
            f"{label:<28}{f'{sb[num]}/{sb[den]} {pb:.1f}%':>14}{f'{sc[num]}/{sc[den]} {pc:.1f}%':>14}"
            f"{d:>+11.1f}  {'yes' if within else 'NO'}{'' if num != 'category' else ' (reported only)'}"
        )
    print()
    diffs = [
        q
        for q in matched
        if base[q].get("routing_pass") != cand[q].get("routing_pass")
        or base[q].get("judge_verdict") != cand[q].get("judge_verdict")
    ]
    print(f"Rows that differ ({len(diffs)}):")
    for q in diffs:
        b, c = base[q], cand[q]
        print(
            f"  Q{q:<3} routing {b.get('routing_pass')}->{c.get('routing_pass')}  "
            f"judge {b.get('judge_verdict') or '-'}->{c.get('judge_verdict') or '-'}  | {c['query'][:50]}"
        )
    print()
    print(
        "COMPARATIVE BAR:",
        "PASS" if ok else "FAIL",
        "(a candidate higher than baseline passes; only a drop of more than 5 points fails)",
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
