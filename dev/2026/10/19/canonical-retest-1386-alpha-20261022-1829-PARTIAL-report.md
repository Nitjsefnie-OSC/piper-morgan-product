# Canonical Query Retest Report — Post-M1 (v3)

**Date**: 2026-10-22 18:29
**Version**: v0.8.6 (post-M1, M1 closed Apr 11)
**User**: web-seed-1386 (fresh account)
**Total Queries**: 43
**Transport**: one fresh UUID session per query (request context built, as in a browser chat; PA 10-22, PPM yes 12:50). Runs before this change had no context.
**Methodology**: canonical-query-test-matrix-v3.md (dual scoring + LLM-as-judge)

---

## Routing Verdict (M0-comparable dimension)

| Metric | Count | Percentage |
|--------|-------|------------|
| Routing PASS | 37 | 86.0% |
| Routing FAIL | 6 | 14.0% |

**M0 baseline (Mar 12)**: 70.5% routing pass (43/61)
**M1 routing**: 86.0% (37/43)
**Routing by the rail entry's effect** (PPM 10-20, the headline): 37/43. **By the classifier's category** (the pre-10-20 reading, for comparison): 36/43 (83.7%).

---

## Quality Verdict (Colleague Test, new in v3)

| Verdict | Count | Percentage |
|---------|-------|------------|
| PASS (judge ≥7) | 25 | 58.1% |
| MARGINAL (judge 5-6) | 15 | 34.9% |
| FAIL (judge <5 or auto-fail) | 2 | 4.7% |
| Skipped (NOT_IMPL or ERROR) | 1 | 2.3% |

**Quality pass rate (judged queries)**: 25/42 (59.5%)

---

## Quality Pass Rate — Expected-Pass vs Known-Pathological (#994)

Per PPM 2026-04-16: aggregate quality conflates "things that should work" with
"things we know can't work yet." The split below makes the per-category thresholds
(≥80% conversational, ≥90% action handlers) meaningful — those targets apply to
the expected-pass set, not the full corpus.

| Bucket | Queries | Judged | PASS | Pass Rate |
|--------|---------|--------|------|-----------|
| **Expected-pass** | 30 | 29 | 16 | **55.2%** |
| Known-pathological | 13 | 13 | 9 | 69.2% |

*The expected-pass quality rate is the headline number for progress tracking.*
*Known-pathological pass rate over time tracks progress on the hard problems.*

---

## AAXT Failure-Mode Distribution (#993)

Six-mode diagnostic taxonomy aligned with Klatch's AAXT harness so
cross-project results are directly comparable. The R/C/T rubric tells
you PASS/FAIL; the failure mode tells you *why*.

| Mode | Count | % of Total |
|------|-------|------------|
| Correct | 24 | 55.8% |
| Reconstructed | 4 | 9.3% |
| Confabulated | 0 | 0.0% |
| Absent | 12 | 27.9% |
| Phantom | 2 | 4.7% |
| Subliminal | 0 | 0.0% |
| _(unset/error)_ | 1 | 2.3% |

- **Correct** = accurate and well-formed
- **Reconstructed** = accurate but inferred rather than directly known
- **Confabulated** = hedged invention with uncertainty markers
- **Absent** = honest absence acknowledgement (PASS-shaped on missing data)
- **Phantom** = confident invention (Pattern-045 fail case)
- **Subliminal** = uses knowledge it can't attribute

Phantom counts > 0 should trigger fabrication-probe (#995) re-run.

---

## Results by Category

| Category | Total | Pathological | Routing PASS | Quality PASS | MARGINAL | FAIL |
|----------|-------|--------------|-------------|--------------|----------|------|
| Identity | 5 | 0 | 5/5 | 5 | 0 | 0 |
| Temporal | 5 | 0 | 5/5 | 3 | 2 | 0 |
| Spatial | 4 | 0 | 4/4 | 2 | 2 | 0 |
| Capability | 5 | 0 | 4/5 | 2 | 2 | 1 |
| Predictive | 5 | 4 | 4/5 | 4 | 1 | 0 |
| Conversational | 5 | 0 | 5/5 | 2 | 2 | 0 |
| Scheduling | 5 | 3 | 4/5 | 3 | 2 | 0 |
| Documents | 4 | 4 | 3/4 | 2 | 1 | 1 |
| GitHub Ops | 5 | 2 | 3/5 | 2 | 3 | 0 |

---

## Human Escalation Queue (10 items)

These results need human review. Triggers: low judge confidence, auto-fail (dimension=0), or judge error.

- **Q8** (Temporal): `What's on the agenda for today?` — low confidence (0.65)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.65)
- **Q11** (Spatial): `What projects are we working on?` — low confidence (0.60)
  - Judge: R=3 C=2 T=1 = 6/MARGINAL (conf 0.60)
- **Q18** (Capability): `List all my projects` — low confidence (0.60)
  - Judge: R=3 C=2 T=2 = 7/PASS (conf 0.60)
- **Q19** (Capability): `Generate a status report` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)
- **Q27** (Conversational): `Tell me more about the GitHub integration` — judge error
- **Q28** (Conversational): `How do I use the calendar feature?` — low confidence (0.60)
  - Judge: R=3 C=2 T=2 = 7/PASS (conf 0.60)
- **Q30** (Conversational): `What needs my attention?` — low confidence (0.60)
  - Judge: R=3 C=2 T=1 = 6/MARGINAL (conf 0.60)
- **Q31** (Scheduling): `Schedule a meeting about the roadmap` — low confidence (0.60)
  - Judge: R=3 C=2 T=2 = 7/PASS (conf 0.60)
- **Q34** (Scheduling): `How much time am I spending in meetings?` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)
- **Q37** (Documents): `Compare these two documents` — auto-fail (dimension scored 0)
  - Judge: R=0 C=1 T=0 = 1/FAIL (conf 0.80)

---

## Errors (1 items)

- **Q27** (Conversational): `Tell me more about the GitHub integration` —  | judge: judge JSON parse failed: Unterminated string starting at: line 1 column 620 (char 619)

---

## Known Issues Run Anyway (11 items)

Per PM guidance: known failures are still run honestly. Tag indicates tracking.

- **Q22** (Predictive, M2 Beta): `What patterns do you see?` — PASS
- **Q23** (Predictive, M2 Beta): `What risks should I be aware of?` — PASS
- **Q24** (Predictive, M2 Beta): `What opportunities should I pursue?` — PASS
- **Q25** (Predictive, M2 Beta): `What's the next milestone?` — PASS
- **Q31** (Scheduling, M2): `Schedule a meeting about the roadmap` — PASS
- **Q32** (Scheduling, M2): `Remind me to review PRs tomorrow` — PASS
- **Q33** (Scheduling, M2): `Find time for a 1:1 with the team lead` — PASS
- **Q36** (Documents, M2): `Create a doc from this conversation` — PASS
- **Q37** (Documents, M2): `Compare these two documents` — FAIL
- **Q38** (Documents, M2): `Synthesize these sources into a summary` — PASS
- **Q40** (Documents, M2): `Update the project roadmap document` — MARGINAL

---

## Known-Pathological Queries (13 items, #994)

These queries are tagged as known-pathological — we expect them to fail
under current conditions (M2 features not shipped, fresh-account lacks real data,
etc.). They run anyway for tracking progress on the hard problems over time.

- **Q22** (Predictive, _M2-beta-pending_): `What patterns do you see?` — PASS
- **Q23** (Predictive, _M2-beta-pending_): `What risks should I be aware of?` — PASS
- **Q24** (Predictive, _M2-beta-pending_): `What opportunities should I pursue?` — PASS
- **Q25** (Predictive, _M2-beta-pending_): `What's the next milestone?` — PASS
- **Q31** (Scheduling, _fresh-account-no-data_): `Schedule a meeting about the roadmap` — PASS
- **Q32** (Scheduling, _M2-feature-pending_): `Remind me to review PRs tomorrow` — PASS
- **Q33** (Scheduling, _fresh-account-no-data_): `Find time for a 1:1 with the team lead` — PASS
- **Q36** (Documents, _M2-feature-pending_): `Create a doc from this conversation` — PASS
- **Q37** (Documents, _M2-feature-pending_): `Compare these two documents` — FAIL
- **Q38** (Documents, _M2-feature-pending_): `Synthesize these sources into a summary` — PASS
- **Q40** (Documents, _M2-feature-pending_): `Update the project roadmap document` — MARGINAL
- **Q41** (GitHub Ops, _fresh-account-no-data_): `What did we ship this week?` — MARGINAL
- **Q42** (GitHub Ops, _fresh-account-no-data_): `Show me stale PRs` — MARGINAL

---

## Methodology Notes

- **Routing verdict**: Compares actual route taken (floor / canonical / action) to v3 expected route. M0 baseline used a different methodology (literal category matching) so this is a reframed but loosely comparable number.
- **Quality verdict**: LLM-as-judge using Colleague Test rubric. Judge model: claude-sonnet-5-5, default sampling, with calibration examples in system prompt.
- **Confidence threshold for human escalation**: < 0.7
- **Auto-fail rule**: any single dimension scoring 0 forces FAIL verdict regardless of total.
- **Known issues** are run anyway per PM guidance — honest reporting over hiding.

*Generated 2026-10-22 18:29 by canonical-retest-m1.py*