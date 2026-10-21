#!/usr/bin/env python3
"""Rescore the 10-20 12:27 canonical run with the frozen harness's readings (f7ae6f66a4).

The 12:27 CSV predates the effect reading and the ten Lead-signed relabels, so its
routing_pass column is the old category reading against the old labels. PPM's OpenAI bar
(10-20 18:21) may use 12:27 as the baseline, which needs it on the same footing as a new run.

This writes a copy with:
  - expected_routing from the harness's CANONICAL_QUERIES (parsed from source, not imported,
    so the harness's .env/keychain bootstrap does not run)
  - actual_routing_category = the old reading (the CSV's actual_routing)
  - actual_routing / routing_pass = the effect reading, same rule as determine_actual_routing
    with UNWIRED_EXECUTION_READS_ACTION on

Run from the repo root:
    python3 dev/2026/10/21/rescore-1227-effect-reading.py IN.csv OUT.csv
"""

import ast
import csv
import sys
from pathlib import Path

sys.path.insert(0, ".")

HARNESS = Path("dev/2026/10/19/canonical-retest-1386-alpha.py")


def expected_labels() -> dict:
    tree = ast.parse(HARNESS.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            getattr(t, "id", "") == "CANONICAL_QUERIES" for t in node.targets
        ):
            rows = ast.literal_eval(node.value)
            return {r[0]: r[3] for r in rows}
    raise SystemExit("CANONICAL_QUERIES not found in harness")


def effects() -> dict:
    from services.intent_service.workflow_dispatcher import get_action_workflows
    from services.intent_service.workflow_entries import register_default_workflows

    register_default_workflows()
    return {k: v.effect for k, v in get_action_workflows().items()}


def routing_match(expected: str, actual: str) -> bool:
    return expected == actual or (expected == "preclass" and actual in ("canonical", "floor"))


def main() -> int:
    src, dst = sys.argv[1], sys.argv[2]
    from services.shared_types import EffectClass

    labels, eff = expected_labels(), effects()
    with open(src, newline="") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    if "actual_routing_category" not in fields:
        fields.insert(fields.index("actual_routing") + 1, "actual_routing_category")

    relabelled = 0
    for r in rows:
        q = int(r["query_num"])
        old_actual = r["actual_routing"]
        if labels[q] != r["expected_routing"]:
            relabelled += 1
        r["expected_routing"] = labels[q]
        r["actual_routing_category"] = old_actual
        if old_actual == "floor":
            actual = "floor"
        else:
            e = eff.get(r.get("actual_intent_action") or "")
            cat = (r.get("actual_intent_category") or "").lower()
            if e is not None and e >= EffectClass.WRITE:
                actual = "action"
            elif e is None and cat == "execution":
                actual = "action"
            else:
                actual = "canonical"
        r["actual_routing"] = actual
        r["routing_pass"] = str(routing_match(labels[q], actual))

    with open(dst, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    eff_n = sum(1 for r in rows if r["routing_pass"] == "True")
    cat_n = sum(
        1 for r in rows if routing_match(r["expected_routing"], r["actual_routing_category"])
    )
    print(f"relabelled {relabelled}; effect {eff_n}/{len(rows)}; category {cat_n}/{len(rows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
