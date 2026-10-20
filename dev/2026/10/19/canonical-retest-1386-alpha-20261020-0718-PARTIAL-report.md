# Canonical Query Retest Report — Post-M1 (v3)

**Date**: 2026-10-20 07:18
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
| PASS (judge ≥7) | 0 | 0.0% |
| MARGINAL (judge 5-6) | 0 | 0.0% |
| FAIL (judge <5 or auto-fail) | 0 | 0.0% |
| Skipped (NOT_IMPL or ERROR) | 9 | 100.0% |

**Quality pass rate (judged queries)**: 0/0 (0.0%)

---

## Quality Pass Rate — Expected-Pass vs Known-Pathological (#994)

Per PPM 2026-04-16: aggregate quality conflates "things that should work" with
"things we know can't work yet." The split below makes the per-category thresholds
(≥80% conversational, ≥90% action handlers) meaningful — those targets apply to
the expected-pass set, not the full corpus.

| Bucket | Queries | Judged | PASS | Pass Rate |
|--------|---------|--------|------|-----------|
| **Expected-pass** | 9 | 0 | 0 | **0.0%** |
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
| Correct | 0 | 0.0% |
| Reconstructed | 0 | 0.0% |
| Confabulated | 0 | 0.0% |
| Absent | 0 | 0.0% |
| Phantom | 0 | 0.0% |
| Subliminal | 0 | 0.0% |
| _(unset/error)_ | 9 | 100.0% |

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
| Identity | 5 | 0 | 5/5 | 0 | 0 | 0 |
| Temporal | 4 | 0 | 4/4 | 0 | 0 | 0 |

---

## Human Escalation Queue (9 items)

These results need human review. Triggers: low judge confidence, auto-fail (dimension=0), or judge error.

- **Q1** (Identity): `What's your name?` — judge error
- **Q2** (Identity): `What can you help me with?` — judge error
- **Q3** (Identity): `Are you working properly?` — judge error
- **Q4** (Identity): `How do I get help?` — judge error
- **Q5** (Identity): `What makes you different?` — judge error
- **Q6** (Temporal): `What day is it?` — judge error
- **Q7** (Temporal): `What did we accomplish yesterday?` — judge error
- **Q8** (Temporal): `What's on the agenda for today?` — judge error
- **Q9** (Temporal): `When was the last time we worked on this?` — judge error

---

## Errors (9 items)

- **Q1** (Identity): `What's your name?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdXaP6taUNp3znq5pRi'}
- **Q2** (Identity): `What can you help me with?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdYd86GyyrdH4RMWh3f'}
- **Q3** (Identity): `Are you working properly?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdZaA2ET9cwnsGuMbaC'}
- **Q4** (Identity): `How do I get help?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdakTv65KsqzXA4vzd3'}
- **Q5** (Identity): `What makes you different?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdcBAEx7oPPB2sHMj8P'}
- **Q6** (Temporal): `What day is it?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdd2vfffrGBfW44fQ61'}
- **Q7** (Temporal): `What did we accomplish yesterday?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDddxr8nZezEPHcuLCUz'}
- **Q8** (Temporal): `What's on the agenda for today?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdejs4Bon453C6xhxEV'}
- **Q9** (Temporal): `When was the last time we worked on this?` —  | judge: judge call failed: BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` is deprecated for this model.'}, 'request_id': 'req_011CgDdgHrBu86njBXk4XCv5'}

---

## Methodology Notes

- **Routing verdict**: Compares actual route taken (floor / canonical / action) to v3 expected route. M0 baseline used a different methodology (literal category matching) so this is a reframed but loosely comparable number.
- **Quality verdict**: LLM-as-judge using Colleague Test rubric. Judge model: claude-sonnet-5-5, temperature 0.2, with calibration examples in system prompt.
- **Confidence threshold for human escalation**: < 0.7
- **Auto-fail rule**: any single dimension scoring 0 forces FAIL verdict regardless of total.
- **Known issues** are run anyway per PM guidance — honest reporting over hiding.

*Generated 2026-10-20 07:18 by canonical-retest-m1.py*