# Canonical Query Retest Report — Post-M1 (v3)

**Date**: 2026-10-20 11:09
**Version**: v0.8.6 (post-M1, M1 closed Apr 11)
**User**: web-oauth-test (fresh account)
**Total Queries**: 61
**Methodology**: canonical-query-test-matrix-v3.md (dual scoring + LLM-as-judge)

---

## Routing Verdict (M0-comparable dimension)

| Metric | Count | Percentage |
|--------|-------|------------|
| Routing PASS | 32 | 52.5% |
| Routing FAIL | 29 | 47.5% |

**M0 baseline (Mar 12)**: 70.5% routing pass (43/61)
**M1 routing**: 52.5% (32/61)

---

## Quality Verdict (Colleague Test, new in v3)

| Verdict | Count | Percentage |
|---------|-------|------------|
| PASS (judge ≥7) | 10 | 16.4% |
| MARGINAL (judge 5-6) | 9 | 14.8% |
| FAIL (judge <5 or auto-fail) | 5 | 8.2% |
| Skipped (NOT_IMPL or ERROR) | 37 | 60.7% |

**Quality pass rate (judged queries)**: 10/24 (41.7%)

---

## Quality Pass Rate — Expected-Pass vs Known-Pathological (#994)

Per PPM 2026-04-16: aggregate quality conflates "things that should work" with
"things we know can't work yet." The split below makes the per-category thresholds
(≥80% conversational, ≥90% action handlers) meaningful — those targets apply to
the expected-pass set, not the full corpus.

| Bucket | Queries | Judged | PASS | Pass Rate |
|--------|---------|--------|------|-----------|
| **Expected-pass** | 42 | 20 | 9 | **45.0%** |
| Known-pathological | 19 | 4 | 1 | 25.0% |

*The expected-pass quality rate is the headline number for progress tracking.*
*Known-pathological pass rate over time tracks progress on the hard problems.*

---

## AAXT Failure-Mode Distribution (#993)

Six-mode diagnostic taxonomy aligned with Klatch's AAXT harness so
cross-project results are directly comparable. The R/C/T rubric tells
you PASS/FAIL; the failure mode tells you *why*.

| Mode | Count | % of Total |
|------|-------|------------|
| Correct | 6 | 9.8% |
| Reconstructed | 2 | 3.3% |
| Confabulated | 1 | 1.6% |
| Absent | 14 | 23.0% |
| Phantom | 1 | 1.6% |
| Subliminal | 0 | 0.0% |
| _(unset/error)_ | 37 | 60.7% |

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
| Identity | 5 | 0 | 5/5 | 2 | 1 | 0 |
| Temporal | 5 | 0 | 5/5 | 4 | 1 | 0 |
| Spatial | 4 | 0 | 3/4 | 2 | 2 | 0 |
| Capability | 5 | 0 | 1/5 | 1 | 2 | 2 |
| Predictive | 5 | 4 | 3/5 | 1 | 1 | 2 |
| Conversational | 5 | 0 | 2/5 | 0 | 1 | 0 |
| Scheduling | 5 | 3 | 4/5 | 0 | 0 | 0 |
| Documents | 4 | 4 | 0/4 | 0 | 1 | 0 |
| GitHub Ops | 8 | 4 | 4/8 | 0 | 0 | 0 |
| Slack | 5 | 3 | 1/5 | 0 | 0 | 1 |
| Productivity | 3 | 0 | 0/3 | 0 | 0 | 0 |
| Todos | 4 | 0 | 2/4 | 0 | 0 | 0 |
| Calendar Ext | 2 | 0 | 2/2 | 0 | 0 | 0 |
| Knowledge | 1 | 1 | 0/1 | 0 | 0 | 0 |

---

## Human Escalation Queue (11 items)

These results need human review. Triggers: low judge confidence, auto-fail (dimension=0), or judge error.

- **Q1** (Identity): `What's your name?` — low confidence (0.60)
  - Judge: R=3 C=2 T=2 = 7/PASS (conf 0.60)
- **Q2** (Identity): `What can you help me with?` — judge error
- **Q4** (Identity): `How do I get help?` — low confidence (0.55)
  - Judge: R=2 C=1 T=2 = 5/MARGINAL (conf 0.55)
- **Q5** (Identity): `What makes you different?` — judge error
- **Q7** (Temporal): `What did we accomplish yesterday?` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)
- **Q16** (Capability): `Create a GitHub issue about testing` — low confidence (0.60)
  - Judge: R=3 C=2 T=1 = 6/MARGINAL (conf 0.60)
- **Q17** (Capability): `Analyze this document` — auto-fail (dimension scored 0)
  - Judge: R=0 C=1 T=1 = 2/FAIL (conf 0.80)
- **Q19** (Capability): `Generate a status report` — auto-fail (dimension scored 0)
  - Judge: R=2 C=2 T=0 = 4/FAIL (conf 0.70)
- **Q21** (Predictive): `What should I focus on today?` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)
- **Q23** (Predictive): `What risks should I be aware of?` — auto-fail (dimension scored 0)
  - Judge: R=0 C=1 T=1 = 2/FAIL (conf 0.80)
- **Q30** (Conversational): `What needs my attention?` — low confidence (0.60)
  - Judge: R=2 C=2 T=1 = 5/MARGINAL (conf 0.60)

---

## Errors (37 items)

- **Q2** (Identity): `What can you help me with?` —  | judge: judge JSON parse failed: Extra data: line 3 column 1 (char 554)
- **Q5** (Identity): `What makes you different?` —  | judge: judge call failed: AttributeError: 'ThinkingBlock' object has no attribute 'text'
- **Q24** (Predictive): `What opportunities should I pursue?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q26** (Conversational): `What else can you help with?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q27** (Conversational): `Tell me more about the GitHub integration` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q28** (Conversational): `How do I use the calendar feature?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q29** (Conversational): `What changed since yesterday?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q31** (Scheduling): `Schedule a meeting about the roadmap` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q32** (Scheduling): `Remind me to review PRs tomorrow` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q33** (Scheduling): `Find time for a 1:1 with the team lead` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q34** (Scheduling): `How much time am I spending in meetings?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q35** (Scheduling): `Review my recurring meetings` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q36** (Documents): `Create a doc from this conversation` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q37** (Documents): `Compare these two documents` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q38** (Documents): `Synthesize these sources into a summary` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q41** (GitHub Ops): `What did we ship this week?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q42** (GitHub Ops): `Show me stale PRs` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q43** (GitHub Ops): `What's blocking the milestone?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q44** (GitHub Ops): `Create issues from this meeting's action items` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q45** (GitHub Ops): `Close completed issues` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q58** (GitHub Ops): `Update issue #123` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q59** (GitHub Ops): `Comment on issue #456` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q60** (GitHub Ops): `Review issue #789` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q46** (Slack): `Any mentions I missed?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q47** (Slack): `Summarize #general from yesterday` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q48** (Slack): `Post this update to the team channel` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q50** (Slack): `/piper help` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q51** (Productivity): `What's my productivity this week?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q52** (Productivity): `Are we on track for the milestone?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q53** (Productivity): `What did the team accomplish this sprint?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q54** (Todos): `Add a todo: review the deployment plan` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q55** (Todos): `Complete the PR review todo` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q56** (Todos): `Show my todos` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q57** (Todos): `What's my next todo?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q61** (Calendar Ext): `What's my week look like?` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q62** (Calendar Ext): `Check my calendar for conflicts` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.
- **Q63** (Knowledge): `Upload a file to the knowledge base` — service: I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment.

---

## Known Issues Run Anyway (15 items)

Per PM guidance: known failures are still run honestly. Tag indicates tracking.

- **Q22** (Predictive, M2 Beta): `What patterns do you see?` — PASS
- **Q23** (Predictive, M2 Beta): `What risks should I be aware of?` — FAIL
- **Q24** (Predictive, M2 Beta): `What opportunities should I pursue?` — ERROR
- **Q25** (Predictive, M2 Beta): `What's the next milestone?` — FAIL
- **Q31** (Scheduling, M2): `Schedule a meeting about the roadmap` — ERROR
- **Q32** (Scheduling, M2): `Remind me to review PRs tomorrow` — ERROR
- **Q33** (Scheduling, M2): `Find time for a 1:1 with the team lead` — ERROR
- **Q36** (Documents, M2): `Create a doc from this conversation` — ERROR
- **Q37** (Documents, M2): `Compare these two documents` — ERROR
- **Q38** (Documents, M2): `Synthesize these sources into a summary` — ERROR
- **Q40** (Documents, M2): `Update the project roadmap document` — MARGINAL
- **Q46** (Slack, M2): `Any mentions I missed?` — ERROR
- **Q47** (Slack, M2): `Summarize #general from yesterday` — ERROR
- **Q48** (Slack, M2): `Post this update to the team channel` — ERROR
- **Q63** (Knowledge, M2): `Upload a file to the knowledge base` — ERROR

---

## Known-Pathological Queries (19 items, #994)

These queries are tagged as known-pathological — we expect them to fail
under current conditions (M2 features not shipped, fresh-account lacks real data,
etc.). They run anyway for tracking progress on the hard problems over time.

- **Q22** (Predictive, _M2-beta-pending_): `What patterns do you see?` — PASS
- **Q23** (Predictive, _M2-beta-pending_): `What risks should I be aware of?` — FAIL
- **Q24** (Predictive, _M2-beta-pending_): `What opportunities should I pursue?` — ERROR
- **Q25** (Predictive, _M2-beta-pending_): `What's the next milestone?` — FAIL
- **Q31** (Scheduling, _fresh-account-no-data_): `Schedule a meeting about the roadmap` — ERROR
- **Q32** (Scheduling, _M2-feature-pending_): `Remind me to review PRs tomorrow` — ERROR
- **Q33** (Scheduling, _fresh-account-no-data_): `Find time for a 1:1 with the team lead` — ERROR
- **Q36** (Documents, _M2-feature-pending_): `Create a doc from this conversation` — ERROR
- **Q37** (Documents, _M2-feature-pending_): `Compare these two documents` — ERROR
- **Q38** (Documents, _M2-feature-pending_): `Synthesize these sources into a summary` — ERROR
- **Q40** (Documents, _M2-feature-pending_): `Update the project roadmap document` — MARGINAL
- **Q41** (GitHub Ops, _fresh-account-no-data_): `What did we ship this week?` — ERROR
- **Q42** (GitHub Ops, _fresh-account-no-data_): `Show me stale PRs` — ERROR
- **Q58** (GitHub Ops, _fresh-account-no-data_): `Update issue #123` — ERROR
- **Q60** (GitHub Ops, _fresh-account-no-data_): `Review issue #789` — ERROR
- **Q46** (Slack, _M2-feature-pending_): `Any mentions I missed?` — ERROR
- **Q47** (Slack, _M2-feature-pending_): `Summarize #general from yesterday` — ERROR
- **Q48** (Slack, _M2-feature-pending_): `Post this update to the team channel` — ERROR
- **Q63** (Knowledge, _M2-feature-pending_): `Upload a file to the knowledge base` — ERROR

---

## Methodology Notes

- **Routing verdict**: Compares actual route taken (floor / canonical / action) to v3 expected route. M0 baseline used a different methodology (literal category matching) so this is a reframed but loosely comparable number.
- **Quality verdict**: LLM-as-judge using Colleague Test rubric. Judge model: claude-sonnet-5-5, default sampling, with calibration examples in system prompt.
- **Confidence threshold for human escalation**: < 0.7
- **Auto-fail rule**: any single dimension scoring 0 forces FAIL verdict regardless of total.
- **Known issues** are run anyway per PM guidance — honest reporting over hiding.

*Generated 2026-10-20 11:09 by canonical-retest-m1.py*