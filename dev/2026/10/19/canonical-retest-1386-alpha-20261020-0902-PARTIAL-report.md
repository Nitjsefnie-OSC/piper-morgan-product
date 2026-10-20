# Canonical Query Retest Report — Post-M1 (v3)

**Date**: 2026-10-20 09:02
**Version**: v0.8.6 (post-M1, M1 closed Apr 11)
**User**: web-oauth-test (fresh account)
**Total Queries**: 9
**Methodology**: canonical-query-test-matrix-v3.md (dual scoring + LLM-as-judge)

---

## Routing Verdict (M0-comparable dimension)

| Metric | Count | Percentage |
|--------|-------|------------|
| Routing PASS | 9 | 100.0% |
| Routing FAIL | 0 | 0.0% |

**M0 baseline (Mar 12)**: 70.5% routing pass (43/61)
**M1 routing**: 100.0% (9/9)

---

## Quality Verdict (Colleague Test, new in v3)

| Verdict | Count | Percentage |
|---------|-------|------------|
| PASS (judge ≥7) | 5 | 55.6% |
| MARGINAL (judge 5-6) | 2 | 22.2% |
| FAIL (judge <5 or auto-fail) | 1 | 11.1% |
| Skipped (NOT_IMPL or ERROR) | 1 | 11.1% |

**Quality pass rate (judged queries)**: 5/8 (62.5%)

---

## Quality Pass Rate — Expected-Pass vs Known-Pathological (#994)

Per PPM 2026-04-16: aggregate quality conflates "things that should work" with
"things we know can't work yet." The split below makes the per-category thresholds
(≥80% conversational, ≥90% action handlers) meaningful — those targets apply to
the expected-pass set, not the full corpus.

| Bucket | Queries | Judged | PASS | Pass Rate |
|--------|---------|--------|------|-----------|
| **Expected-pass** | 9 | 8 | 5 | **62.5%** |
| Known-pathological | 0 | 0 | 0 | 0.0% |

*The expected-pass quality rate is the headline number for progress tracking.*
*Known-pathological pass rate over time tracks progress on the hard problems.*

---

## AAXT Failure-Mode Distribution (#993)

Six-mode diagnostic taxonomy aligned with Klatch's AAXT harness so
cross-project results are directly comparable. The R/C/T rubric tells
you PASS/FAIL; the failure mode tells you *why*.

| Mode | Count | % of Total |
|------|-------|------------|
| Correct | 5 | 55.6% |
| Reconstructed | 0 | 0.0% |
| Confabulated | 0 | 0.0% |
| Absent | 2 | 22.2% |
| Phantom | 1 | 11.1% |
| Subliminal | 0 | 0.0% |
| _(unset/error)_ | 1 | 11.1% |

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
| Identity | 5 | 0 | 5/5 | 2 | 1 | 1 |
| Temporal | 4 | 0 | 4/4 | 3 | 1 | 0 |

---

## Human Escalation Queue (5 items)

These results need human review. Triggers: low judge confidence, auto-fail (dimension=0), or judge error.

- **Q1** (Identity): `What's your name?` — low confidence (0.60)
  - Judge: R=3 C=1 T=2 = 6/MARGINAL (conf 0.60)
- **Q2** (Identity): `What can you help me with?` — judge error
- **Q4** (Identity): `How do I get help?` — low confidence (0.60)
  - Judge: R=1 C=1 T=2 = 4/FAIL (conf 0.60)
- **Q5** (Identity): `What makes you different?` — low confidence (0.60)
  - Judge: R=2 C=2 T=3 = 7/PASS (conf 0.60)
- **Q7** (Temporal): `What did we accomplish yesterday?` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)

---

## Errors (1 items)

- **Q2** (Identity): `What can you help me with?` —  | judge: judge JSON parse failed: Extra data: line 3 column 1 (char 493)

---

## Methodology Notes

- **Routing verdict**: Compares actual route taken (floor / canonical / action) to v3 expected route. M0 baseline used a different methodology (literal category matching) so this is a reframed but loosely comparable number.
- **Quality verdict**: LLM-as-judge using Colleague Test rubric. Judge model: claude-sonnet-5-5, default sampling, with calibration examples in system prompt.
- **Confidence threshold for human escalation**: < 0.7
- **Auto-fail rule**: any single dimension scoring 0 forces FAIL verdict regardless of total.
- **Known issues** are run anyway per PM guidance — honest reporting over hiding.

*Generated 2026-10-20 09:02 by canonical-retest-m1.py*