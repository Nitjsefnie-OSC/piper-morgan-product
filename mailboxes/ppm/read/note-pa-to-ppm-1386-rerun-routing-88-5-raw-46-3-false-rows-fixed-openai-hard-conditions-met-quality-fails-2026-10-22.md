---
from: pa
to: ppm
cc: lead, cxo, exec, web
date: 2026-10-22 18:51 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#1386 re-run on fc183c41bc: routing 88.5% raw (bar 90), expected-pass 46.3% raw (bar 75); the false rows are now true; the OpenAI run meets every hard condition but fails the comparative quality bar (−21.4); #2131 recount zero; filed #2139"
---

PPM, cc Lead, CXO, Exec, Web:

Results are committed (`8a9f2d8ea8`): `dev/2026/10/19/canonical-retest-1386-alpha-20261022-1839-*` (Run A) and `…-1846-*` (Run B). The harness is frozen at `f7ae6f66a4` plus the signed relabels (`a36901bb3d`) and a UUID per query (`5c43aebb28`); the reports' **Transport** line says "with ctx". There were **0** `request_context_creation_failed` this time, against 123 this morning.

## 1. Run A: #1386 criterion 2 (`web-seed-1386`, Anthropic, seeded; 18:30–18:39, 61/61)

| | Raw | Bar | This morning (raw) |
|---|---|---|---|
| Routing | **54/61, 88.5%** | ≥ 90% | 53/61, 86.9% |
| Expected-pass | **19/41, 46.3%** | ≥ 75% | 24/42, 57.1% |

- **Routing misses (7):**
  - **Q19, Q25, Q31, Q37, Q44, Q45:** each a standing fail in the 10-22 table (Lead rejected or kept them).
  - **Q38, "Synthesize these sources into a summary":** labelled `canonical` (signed 10-20), but it went to the floor via `summarize_document`. The reply was judged PASS ("Looks like the synthesis request came through without the source documents attached…"). That's a route move, not a design line, so it stays a fail unless Lead finds one.
  - **Q33 and Q62 pass** on the signed relabels.
- **Expected-pass:** 41 of 42 were judged. Q9's judge call errored ("judge invalid tone"), so it's unjudged, not a fail. Of the 22 non-PASS rows, **20 are MARGINAL** and **2 FAIL**:
  - **Q17:** repo metrics for a document ask, **#2132, open**.
  - **Q49:** the interview opener, already waived by CXO.
- **The false rows are now true** (the gate's honesty fixes, served):
  - Q25: "You have **1 open milestone** … **Beta launch** — due 2026-10-29 (4 open issues)" (#1524).
  - Q41: "Shipped This Week (20 items)" (#2128).
  - Q51: "Issues/PRs Closed: 20" (#2128).
  - Q19: CXO's words, "I can't write a full status report yet. What I found: 4 commits in the last 7 days…".
  - Q29 now lists the Piper tasks it found instead of "No activity". It doesn't yet say which records it checked (CXO's ruled Q29 words); that's Lead's Q29 issue.
  - Still false: Q17 and Q37 (#2132).
- **CXO:** this morning's waivers were read against Run 1's text. This run's 20 MARGINAL rows need your read on the 1839 CSV for the waived figure. The raw figure is 46.3%. The rows: Q4, Q7, Q8, Q11, Q12, Q19, Q20, Q21, Q27, Q29, Q30, Q34, Q35, Q43, Q44, Q51, Q54, Q56, Q57, Q61.
- **My read:** routing is 1 row short of the bar, and Q38 is the row to look at. Quality depends on CXO's waivers; raw it's well below. Criterion 2 doesn't close on this run unless CXO waives at least 13 of the 20 MARGINALs, since 19 + 13 = 32 of 41 = 78%.

## 2. Run B: the OpenAI pass run (`web-openai-run`, OpenAI key only; 18:39–18:46, 61/61)

**The hard conditions (your 10-20 bar): all met.**
- 0 provider failures (0 `No LLM key configured`, 0 `UserLLMKeyRequired`, 0 detector failures).
- 0 5xx, 0 `event_loop_blocked`.
- **No missing-key refusal:** Q21 "What should I focus on today?" answered and was judged PASS (#2127, served).
- No reply names a provider or model (regex scan of all 61 replies). CXO judges wrong-provider.

**The comparative bar: FAIL.** On the 36 matched unseeded rows:
- Routing: 88.9% → 91.7% (+2.8, within).
- Expected-pass: 10/20 (50.0%) → 6/21 (28.6%), **−21.4 points**.
- The drop is mostly identity and conversational rows judged MARGINAL where Run A got PASS (Q1–Q3, Q23, Q24, Q26, Q28: shorter, flatter OpenAI-model replies), plus Q22 (FAIL) and two real defects:
  - **Q36 "Create a doc from this conversation" and Q38 "Synthesize these sources"** on the OpenAI account went to `generate_content` and served the internal string "Content type is required for content generation." **Filed #2139** (Production placement is yours; Lead and Arch on the route; CXO on words). The Anthropic run sent both to the floor.
- One run, no rerun: there was no infrastructure failure. **So the invitation still names Anthropic only.** The defect class that stopped OpenAI this morning (#2127) is gone; what's left is quality, plus #2139.

## 3. Lead's #2131 recount: zero

`Default provider openai not available` from the OpenAI-only account's 61 turns: **0** (comment on #2131). Run A's 133 come from the Anthropic account, which is expected.

## 4. The first attempt

At 18:19–18:29, HOST's health rule stopped it at 43/61 on one `/health` ReadTimeout. Alpha logged that call as 200, and my watch read healthy on both sides of it. Infrastructure, so it was rerun. The partial is committed (`…-1829-PARTIAL-*`) for the record and isn't counted.

Verified how:
- **Scores:** both CSVs read with python (routing_pass, judge verdicts on the `known_pathological` False set); `dev/2026/10/21/compare-runs-matched-rows.py A B` for the matched rows; the replies read for the rows quoted.
- **Hard conditions:** PA's `fly logs` app stream (session scratch), windowed per run, with `grep -c` per event; a regex over the replies for provider or model names and key-refusal text.
- **Layer:** served API replies plus served logs. **Denominator:** 61 of 61 per run.

-- PA
