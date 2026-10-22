---
from: pa
to: lead, ppm
cc: web, exec, cxo
date: 2026-10-22 10:12 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#1386 runs done on 76789a8988: the seeded run misses both bars (routing 86.9%, expected-pass 57.1%); the OpenAI run fails PPM's bar (a missing-key refusal at Q21, filed #2127, and expected-pass -42.9 points on matched rows), so the invitation names Anthropic only; promotions are free; Web may go"
---

Lead, PPM, cc Web, Exec, CXO:

**End mail.** Both runs finished on `76789a8988`; `/health` read the same build after Run 2.
- **Lead:** promotions are free.
- **Web:** your #2112, #2091 and #2092 rows on `web-seed-1386` can go.

## Run 1: #1386 criterion 2, `web-seed-1386` (Anthropic), 09:51–10:04

| | Result | Bar |
|---|---|---|
| Routing, effect reading | **53/61, 86.9%** | ≥ 90%: **miss** |
| Routing, category reading | 52/61, 85.2% | (reported) |
| Expected-pass, judged PASS | **24/42, 57.1%** | ≥ 75%: **miss** |
| Seeded rows (25) | routing 20/25; expected-pass 10/21 | |
| Unseeded rows (36) | routing 33/36 (91.7%); expected-pass 14/21 (66.7%) | |

By seed section:
- **GitHub (9 rows):** routing 6/9, expected-pass 4/6.
- **Calendar (6 rows):** routing 4/6, expected-pass 1/5.
- **Piper-side (12 rows):** routing 12/12, expected-pass 6/12.

There were no HTTP errors and no stop. AAXT modes: Correct 31, Absent 24, Reconstructed 4, Phantom 2 (Q17 and Q37, both document asks).

**The 8 routing misses:**
- Q19 and Q25 expect floor, read canonical.
- Q31, Q33 and Q62 expect canonical, read floor.
- Q37 expects floor, reads canonical.
- Q44 and Q45 expect floor, read action.

**What the seed showed:**
- **The calendar reads work.** Q8, Q34 and Q61 list Team sync, the 1:1 with Sam and Planning review. Q35 finds the weekly recurring meeting. Q21 and Q30 show them as upcoming. That's the first served proof since xian enabled the API, and it bears on #2092: a real read, not "no events".
- **Q62 "Check my calendar for conflicts":** the reply says conflict-checking "isn't something I can do yet". But Q61's own list shows the 1:1 at 11:00 (30 min) overlapping Planning review at 11:15. The judge gave PASS; CXO, this one is yours to read with #2112.
- **Q25 "What's the next milestone?":** "You don't have any open milestones right now." The repo has "Beta launch", due 10-29. From source, the milestone handler calls the GitHub router with no user context, and an unresolved repo returns `[]`, which renders as "none". The served instance is on #1524 (comment 6346681788).
- **Q41 "What did we ship this week?"** found no closed issues or PRs, and **Q51** counts "Issues/PRs Closed: 0". This week PR #27 merged and #8 and #9 closed. The connection itself works: Q19 read 5 commits, and Q42 read "2 open, none stale", which is the honest answer the spec predicted.
- **Q53** calls "Team sync" a GitHub issue. It's a calendar event. That's a mild conflation; it's in the CSV for the judge's read.

## Run 2: the OpenAI run, `web-openai-run`, 10:05–10:1x, same build

**Hard conditions (PPM 10-20 18:21):**
- 0 provider failures: **failed** (Q21, below).
- 0 5xx, and 0 `event_loop_blocked` in alpha's log across both runs: met.
- **No missing-key refusal: failed.** Q21 "What should I focus on today?" got "That needs an LLM key of your own … Add an OpenAI or Anthropic key". Alpha's log for that turn: `task_type: intent_classification … No LLM key configured for provider 'anthropic' on this call` (#1815/#1819 refusing to spend across providers, correctly). The multi-intent classifier chose Anthropic for an OpenAI-only account. **Filed #2127** (Lead's lane).
- No reply names the wrong provider or model: none found. The only provider names are in Q21's refusal ("an OpenAI or Anthropic key"). CXO judges.

**Comparative, on matched rows** (36 left after the 25 seed rows; baseline is Run 1 on the same build; `dev/2026/10/21/compare-runs-matched-rows.py`):

| | Run 1 | Run 2 | Δ | within 5 |
|---|---|---|---|---|
| Routing (effect) | 33/36, 91.7% | 33/36, 91.7% | +0.0 | yes |
| Expected-pass | 14/21, 66.7% | 5/21, 23.8% | **−42.9** | **no** |

Of the 18 rows that differ, 16 drop in judged quality with no routing change (Q1, Q3–Q5, Q23, Q24, Q26–Q28, Q38, …). Q37 rises.

**The verdict under the 10-20 discipline:** one run, with a rerun only for an infrastructure failure. Q21 is a product defect, not quota or infrastructure (the log names the provider choice). So **no rerun, and the invitation names Anthropic only.** Exec, that's the line for xian's 10-23 read.

**Related signal for #2127:** `Default provider openai not available, using anthropic` was logged 220 times during Run 1's 61 turns and fewer times during Run 2. Some calls appear to resolve their provider without the acting user. Which calls is unverified.

## One harness change, transport only (`700309c395`)

Run 1's first start sent Q1 with the fixed session id `canonical-retest-m1-q1`, which `web-oauth-test` created on 10-20. Alpha correctly refused it: 404 "Conversation not found for this account", logged as `conversation_session_owner_mismatch`. Nothing reached the account. The harness now uses a per-run id prefix (`canonical-1386-<user>-<stamp>`), so each query opens a fresh conversation on the measured account. The 61 queries, the routing rules and the judge are unchanged from `f7ae6f66a4`. The first attempt also exited before login on the credential file's `key: value` format; the files were passed through a converted stream, never written or printed.

**Files:**
- `dev/2026/10/19/canonical-retest-1386-alpha-20261022-1004-{results.csv,report.md}` (Run 1)
- `dev/2026/10/19/canonical-retest-1386-alpha-20261022-1010-{results.csv,report.md}` (Run 2)

Verified how:
- The harness reports and CSVs.
- The matched-row script run on both CSVs.
- A seed-section split of Run 1 by the spec's row sets.
- Alpha's app and DB `fly logs` streams (session scratch only; reduced lines quoted here).
- `/health` before and after.
- Source read of the milestone handler and router.
- Layer: served replies through `/api/v1/intent` on alpha, judged by `claude-sonnet-5-5`.
- Denominator: 61 of 61 queries in each run.

-- PA
