"""The ANALYSIS margin fix (Lead 2026-10-14; Arch's standing-member rule,
decisions.log 10-13 d13dafd172 and 10-14): the corpus row "let's analyze the
risk here" (expects analyze_blockers) read CLARIFY 5/6 on main in the
2026-10-14 baseline block, tripping the watch. The fix is the least-perturbing
lever: an ADDITIVE ACTION_EXAMPLES phrase, description unchanged. Rule 7 was
paid (x6 vs same-minute main; full corpus run) before landing; controls in
dev/2026/10/14/controls/analysis-*. No LLM, no DB.
"""

from __future__ import annotations

from services.intent_service.action_registry import ACTION_DESCRIPTIONS, ACTION_EXAMPLES


def test_example_carries_the_member_phrasing_additively():
    ex = ACTION_EXAMPLES[("ANALYSIS", "analyze_blockers")]
    assert ex.startswith("What's blocking the milestone?"), ex  # the original example kept
    assert "Let's analyze the risk here" in ex, ex


def test_description_unchanged_by_the_margin_fix():
    desc = ACTION_DESCRIPTIONS[("ANALYSIS", "analyze_blockers")]
    # the description already says "putting at risk"; what must NOT appear is the
    # member phrasing itself — the fix is an example, never a description sentence
    assert "analyze the risk" not in desc.lower(), desc
