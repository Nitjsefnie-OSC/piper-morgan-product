"""#2135 (Arch and CXO, 2026-10-22): the trust ladder stays dormant through beta.

Nothing outside ``services/trust/`` records a trust interaction. The chain as built
(``outcome_classifier`` decides "successful" by regex; the success count moves the stage;
the stage widens proactivity) is code deciding meaning and writing a permission, which
ADR-080 forbids. Wiring it later takes an ADR-053 amendment conformant with ADR-080, not
a build. This is a ceiling-0 tripwire: a new caller fails here until that amendment lands.
"""

from __future__ import annotations

import ast
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GUARDED = {"record_interaction", "process_interaction"}
CEILING = 0


def _callers_outside_trust():
    out = []
    for root in ("services", "web"):
        for f in sorted((REPO / root).rglob("*.py")):
            rel = f.relative_to(REPO)
            if rel.parts[:2] == ("services", "trust"):
                continue
            tree = ast.parse(f.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    fn = node.func
                    name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
                    if name in GUARDED:
                        out.append(f"{rel}:{node.lineno} {name}")
    return out


def test_no_turn_path_records_trust_while_the_ladder_is_dormant():
    callers = _callers_outside_trust()
    assert len(callers) <= CEILING, (
        f"Trust recording called outside services/trust/ (#2135): {callers}. The ladder is "
        "dormant through beta by Arch's and CXO's ruling; wiring it needs an ADR-053 "
        "amendment conformant with ADR-080 first."
    )
