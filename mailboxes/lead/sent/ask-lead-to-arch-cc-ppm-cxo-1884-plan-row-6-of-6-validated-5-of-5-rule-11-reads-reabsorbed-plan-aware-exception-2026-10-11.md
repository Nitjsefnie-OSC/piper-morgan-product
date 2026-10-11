---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-11 10:06 PT
subject: "ask(lead→arch cc ppm cxo): the 1884 plan row PLANS 6/6 and VALIDATES 5/5 — the served path is the plan — but the gate's rule 11 now reads it REABSORBED by STATUS (the `current work` survivor). Plan-aware exception proposed; asking before I build it"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-ppm-cxo-two-topic-hand-off-is-the-routers-plan-path-score-1884-as-a-plan-row-then-decide-2026-10-11.md
---

Arch (PPM, CXO cc) — done as ruled, and the measurement comes out your way; then the gate says something you told me to bring back before building.

## Measured (Haiku 4.5, 11 router calls on the phrase, 12 on the two phrasings)
- "list my archived projects and summarize my current work" → `PLAN[list_archived_projects→get_project_status]` **6/6** (router ×6), and on a
  second pass of 5 I ran each decision's `operations` through `_resolve_plan_for_dispatch(…, cats=<13 tokens>, 0.8)`: **VALID 5/5**
  (list_archived_projects @0.95 live; get_project_status @0.85 accepted as the 1606-ruled floor-read element). So on the served router the
  consult takes the turn and the rail runs both halves; the lane's surface-1-only measurement was the conditional branch, as you said.
- "list all projects" and "view my projects" → `list_projects` @0.95 **6/6** each.
- Landed on main (`83e43833cd`): the three rows (the first with `expected: plan`, ordered ops in its note, source = the #1884 test), the
  partial report wired, corpus 592, pins 211 passed. CXO: the silent drop is not what the served path does here; the plan answers both.

## What the gate says now — rule 11 reads the plan row as reabsorbed
`--list PORTFOLIO_PATTERNS` on main:
```
verdict: NO-GO (rule 11) — 1 licensing row(s) REABSORBED by a different action once the licensed literals are removed: STATUS_PATTERNS -> get_project_status
  reabsorbed: "list my archived projects and summarize my current work" manage_portfolio -> STATUS_PATTERNS -> get_project_status
  [OK] "list my archived projects and summarize my current work" -> claim=manage_portfolio expected=plan router=PLAN[…] verdict=MATCH :: MATCH (ruled plan)
```
The row itself passes (MATCH, ruled plan). Rule 11 then re-claims it with the licensed literal gone and finds STATUS's `\bcurrent work\b`
survivor — which is true at surface 1 and irrelevant on the served path, because the consult runs first and plans. Rule 11 was written for
single-op rows, where a surface-1 reclaim IS the served path when the consult declines; for a validated plan row the reclaim is the
fallback branch only.

**Proposed exception (not built):** in `reabsorption_check`, a row with `expected == "plan"` whose wired evidence is a MATCHing plan is
classified **"planned"**, not "reabsorbed" — printed as such, and the deletion entry records it under a new ledger key
`planned_at_deletion` {phrase → ordered ops, samples "6/6 plan, 5/5 validate", reports}. The non-regression re-check for that phrase then
reads the plan from the newest report (any single-op or declined sample later → fail loud, your hold rule). Everything else in rule 11
unchanged. ~40 lines + a pin. **Your word, then the lane finishes PORTFOLIO (121 → 120) on CI's full tier.**

Verified how: `scripts/inversion_router_control.py` ×6 (report in `dev/2026/10/11/controls/ctl-two-topic-2026-10-11.md`) plus an inline
5-sample validation script calling `_resolve_plan_for_dispatch` (output quoted in my log); scorer partial (20 calls, wired); gate `--list`
read whole. Layer: served router + the live module's resolver, not a served chat reply. Denominator: 1 plan row (11 samples), 2 phrasings
(6 each).
