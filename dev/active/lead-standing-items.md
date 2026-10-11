# Lead standing items — FULL REWRITE 2026-08-31 ~15:5x PT
(Prior version was 53 days stale — CIO's cohort audit caught it, 10 of its 14 cited issues already
closed. Same failure shape as the 8/29 carry-forward staleness; same fix: this file now gets the
freshness pass at START/STOP alongside the carry-forward, and cites NO issue states — issue state
lives in GitHub, this file holds only durable owed/queued items.)

## Durable owed
<!-- 2026-10-08 Lead: struck the cli/commands/issues.py 1613-residue row — done 10-05 in `2d0e7502b0`.
     2026-10-05 Lead: struck two rows found already on main during a drain check — the gotchas-doc
     lines (github-and-tooling-gotchas.md §"Four instrument-integrity gotchas", landed 08-31) and the
     _extract_completion_text ratchet gap (frozen in TestExtractionPatternRatchet 2026-09-01). -->
- Pre-claim shadow probe — **Filed**: 2026-08-29 · the INSTRUMENT is built (09-02: `preclaim_shadow.py` + `scripts/preclaim_shadow_report.py`,
  default OFF). What remains is the MEASUREMENT: enable `PIPER_PRECLAIM_SHADOW=1` where real claimed turns happen (alpha — PM's hand,
  a flag change to a deployed env) or run a local traffic pass, then read the report per pattern list against the 1.0 bar. Not a build item
  any more (corrected 2026-10-06 — the row said "build item" for five weeks after the build landed).
- #1522 false-trails audit — **Filed**: 2026-08-08 · scan DONE 2026-10-05 (table on the issue) · inert-deletion lane (C6, C8/C9, I3) DONE
  `b3f684822f` · dual-write/`get_github_repository` DONE 10-06 (`e394c6e084`). Places removed 10-06 (`d06e81186b`). `services/persistence/`
  deleted 10-07 (prod row count 0; migration `p1522drop`). Still open: Documents HELD on #1270, Pard/PM on pytest.ini ignore + the Next.js scaffold, I2 error pages (product call).
- Beta-conditions audit at the final gate (mine + subagent cross-check; PM ruling 8/15).
- **Epic 0 Phase 3 tail — re-plan trip-wire Wed 10-14** (PPM ruled 10-10 05:3x; the earlier "Tue" was a label error) — **Filed**: 2026-10-09 · end of 10-10: ceiling **127** (121 + 6 restores), routing tail re-measure Mon; 10-09 was 121/91 (measured 17:5x PDT: `pattern_literal_counts` TOTAL 121, `routing_tail` 91; reported to PPM). Batch 26 + chunk 8 (5) + GUIDANCE (3).
  121 is still just above PPM's 110–120 band. The gate (rules 10/11 + the #1973 threshold in every arm) reads no list GO. What's left needs
  router/catalog work or new rows: COMPLETION_HISTORY (#1117 row @0.72; 4 rule-10 holds), the greeting/thanks/farewell family (rule-10 holds;
  pleasantry is NOT ROUTING), STAKEHOLDER (#1256, blocked on DOCUMENT_QUERY's loose "update … with", rule 11), and the 3 delete-family
  literals (#1935). Re-measured **Sun 10-11: 127 / 97** with the sizing table (memo 3e71c8297: ~35 served calls buy the rule-10 bucket; the router bucket costs a full run per candidate; nothing else moves on spend). Mon 10-12: confirm main unchanged, else re-measure. **COMPLETION_HISTORY partial LANDED 10-11 (9cb5e45c1e): ceiling 124, tail 94.** Gate commit 4037c9a267 (ruled survivors, 1974 HELD, restore pin, ledger-key hint). **STATUS 2 + PRIORITY 1 LANDED 10-11 (6bb22031a6): ceiling 121.** PORTFOLIO show/list/view: Arch ruled 10-11 the plan path runs first; the #1884 phrase is now a `plan` row — PLAN 6/6, validated 5/5 — and the 2 pin phrasings have rows (list_projects 6/6). Plan-aware rule 11 BUILT 10-11 (Arch's ruling, with the fallback condition): the row reads "planned, fallback partial (STATUS_PATTERNS)" → **PORTFOLIO holds at 121 on #1977**; the prepared deletion stays on `claude/lead-spp-portfolio-wip` (2831d622c2). **Wed reads 121**, reason: the last PORTFOLIO literal holds on #1977 (the served path plans it; the fallback would drop half the turn).
- **#1977 design pass (mine; Arch filed 10-11)** — **Filed**: 2026-10-11 · generalize #1416's residue rule: a single surface-1 claim with a substantive second clause outside its span declines, or the reply acknowledges the unanswered half (CXO's option 1; CXO offers the copy). Routing change → rule 7 full run before landing. Design POSTED 10-11 10:2x (issue comment): step 1 = span-based residue decline at the detect_multiple_intents tail + single-entry parity; step 2 = CXO's acknowledgement copy (on the issue) for the armed branch. Arch NODDED 10-11 10:4x (no comma marker; WRITE pin) + corrected: unclaimed fallback = "planned, fallback unacknowledged" NO-GO until step 2 (gate 3492fc8a55). **Step 1 LANDED 10-11 11:2x (0ba7b951e5)** with two review changes (leading clause counts; unclaimed clause must be ask-shaped — PM's #1856 correction stays with its handler; trade: a declarative second ask stays with the first claim). Measurement: census diff 2 of 592 rows (both two-topic, router evidence on file); router ×6 on newly-declined phrasings; no full run spent (router unchanged) — offered to Arch. **Step 2 code LANDED 10-11 (7a9d2fb6ab + review) and SERVED on a local server** (armed branch: `I haven't done "summarize my current work" yet. Want me to?`; the "yes" binds; negative case no line; quotes in `dev/2026/10/11/controls/served-1977-step2-2026-10-11.md`). CXO's final copy (no "I did" half) applied. **Flip landed (6127d246df) then WITHDRAWN 12:3x (Arch + CXO: the 12:0x quote named the other half by luck; the shape the flag licenses — served intent covers the claimed half, the line names the leftover — had no quote).** Flag False on main again. **RULED 12:5x–13:1x (CXO + Arch): covered branch only** (both withdrew 'name both'); **the licence = a preregistered measurement**: 20 armed-branch declines, ≥3 phrasings, 0 silent partials and ≤2 neither. **Measured 12:4x: 0 silent partials, 6 neither (all 'summarize my current work …' → summarize_document) → HOLD. PORTFOLIO's literal stays; main reads 121.** Covered-only step 2 lands with the flag False (unit tier running). The lane's prepared deletion is held on origin `claude/lead-portfolio-last-literal` (5cda6c2c1e; 3 unit failures unconverted; not for merge). **Arch 13:0x: HOLD accepted, no re-cut; TRIGGER = #1979** ("summarize my current work" → upload prompt, esp. after an offer; CXO filed): when its fix lands on main, re-run the SAME 20 (same 4 phrasings, armed branch, 0 silent partials and ≤2 neither) — that decides the literal. The 28-probe counts are on the #1884 corpus row's note. **#1979 design (where the misroute is fixed: classifier prompt / catalog) — Filed**: 2026-10-11 · mine with Arch; trigger: a fresh context (this session is long) — not today's drain. **#1978** found + fixed + closed. **CXO owes** the served-reply check on the #1884 example after an offer, once deployed to alpha. **Ask-cue widening** (request-statements) measured clean on Arch's sentinels; landing on the unit tier; trade row deposited (593). **120 needs both steps; Wed reads 121** unless PM admits both via Exec. Pleasantry family (GREETING 8 / FAREWELL 4 / THANKS 4 + filler 10): **RULED KEEP 10-11 (CXO, #1974 comment 6110663876)** — named permanent floor; HELD_FOR_CAUSE reads "ruled keep, permanent floor (#1974)" in the gate commit; close #1974 there. Tail stays 97; the cheap path ends at 121–122, outside the band (CXO accepts knowingly). PORTFOLIO partial (2) HELD 10-11: `update … project` is a ruled survivor (#1933 option a); the show/list/view literal needs
  corpus rows for 5 pin phrasings ("show my archived projects", "show archived projects", "view my archived projects", "show my projects",
  "list my archived projects (show all names)") plus a look at the #1738 single-intent guard before any pin converts. Arch asked for a
  per-literal ruled-survivor mark in the gate so the census stops licensing it.
- **#1970 — router framing DEFERRED (Arch option c, 10-10)** — **Filed**: 2026-10-10 · landed: step-1 plumbing (flag off), the inert
  scorer framing column + mapping, and the `_EXECUTE_RE` ratchet (MAX_EXECUTE_ALTERNATIVES 39, justified-bump rule). The prompt stays on
  `claude/lead-1970-framing-prompt-held` (not merged). **Retry trigger**: every `framing: declarative|question` row reads ambiguous at N=5
  on the served model, AND the full-run operation diff shows no ×6-attributed regression. Compose corpus rows: 0 exist (needed for any retry).
- **Rule 7 as refined by Arch (10-10)**: the full ~577-call run is owed only by the candidate that LANDS. Exploration screens on the moved rows
  plus a fixed sentinel set (PM's phrasings, the clear family, the declarative and question rows). Apply this to the held catalog batch and any #1970 retry.
- **Key move on Fri 10-16 (Themis 10-10; xian's call)** — **Filed**: 2026-10-10 · keep the current key through 10-15 (it spends Krink's credit,
  which expires 10-15). On 10-16 xian stores `lead-scoring` (Amber keychain, my 13:4x command). **Have ready by 10-16, if asked:** the steps
  to move prod alpha's server key to the pipermorgan.ai org. That's PM's hand: `fly secrets set -a piper-morgan ANTHROPIC_API_KEY=…` via a
  hidden prompt, never pasted into the repo or mail. Fly restarts the app. Then PASS: alpha /health is up, and one chat turn by a user
  WITHOUT a stored key is served (fly logs show no limit error). Also decide: a separate workspace for prod (not lead-scoring's $50, so dev
  scoring can't starve users). Testers on their own stored keys are unaffected.
- **API restored 16:33 10-10** (xian raised workspace + org limits to $250). lead-scoring key ($50, pipermorgan.ai org) STORED 17:2x and served
  17:41 (one confirm call); workspace attribution is xian's console check. The catalog batch is RESOLVED 10-10 19:1x: week_calendar clause landed
  (1110c6a03a), the todo-query description edit dropped (regressed in every wording); held branches superseded (remote delete permission-denied, don't retry).
- **Post-landing follow-ups (10-10 evening)** — **Filed**: 2026-10-10 · (1) **Gate evaluator disagreement** (lane's finding): `--list` census
  credits restored STATUS/PRIORITY literals as deletable (GO) while `check_deleted_entry_non_regression` refuses them; they differ on liveness
  for FLOOR actions (get_project_status, get_top_priority). Report to Arch; one liveness source for both. Until fixed, the census GO on those
  lists is NOT a licence. (2) CLOSED 10-10 19:3x: CXO withdrew the progress-report re-point; the row stays generate_report, no literal bought.
  (3) `\bstatus report\b`: SURVIVOR (10-11 surface-2 N=5 → SYNTHESIS/generate_status_report 5/5, rule 3 fails); Arch's 10-11 ruling: the evaluator split was the mis-serve proof, not liveness — CLOSED as a disagreement. (4) DONE 10-10 19:1x: PPM recounted 127 (d29bfef2ce). (5) DONE 10-11: `--all` table vs `--list` disagreement (partial GO / rule 10 / rule 11 missing from the table) fixed + pinned. (6) DONE 10-11 08:2x: #1951 CLOSED (PPM's two verdicts + CXO's REVIEW landed). (7) RULED 10-11 (Arch): filler stays in the tail; **tail is 97**, "87" only as a labelled sub-number. (8) DONE 10-11 (4037c9a267) gate commit: `ruled_survivors` (#1933 pair) + restore pin (literal claims the ruled op or known-miss note) + HELD_FOR_CAUSE GREETING/FAREWELL/THANKS on #1974 + `--list` ledger-key hint; then a lane: STATUS 2 (`project landscape`, `upcoming milestones?`) + PRIORITY 1 (`where.*focus`, CXO withdrew the survivor 10-11) under misserved_at_deletion, + PORTFOLIO show/list/view 1 (5 rows deposited 10-11). 127 → 124 → 121 → 120.

- **Description-change candidate: "show today's tasks" → list_todos_query** (Arch: worth doing for its own sake, its own rule-7 run, my timing) —
  **Filed**: 2026-10-10 · narrowed 10-11: of the three named, "show priorities for this sprint" (get_top_priority @0.85, MATCH) and "pull up my
  schedule" (week_calendar @0.85, MATCH) are already right on the 10-10 full run. The remaining row reads attention_query @0.85; the 10-10 lane
  found every list_todos_query wording regressed, and 10-11's inverse (attention_query excluding a plain list of today's tasks) screened
  clean then failed the full run (5 ×6-attributed regressions incl. a WRITE landing; held report
  `inversion-attention-query-description-CANDIDATE-HELD-full-score-2026-10-11-anthropic.md`). **No fourth wording.** CXO ruled 10-11: (b) REVIEW — landed (builder + fixture + ledger rejudged). CLOSED; the served check rides the post-promotion row.
- **#1970 framing to the router** (Production, Arch's design on the issue, comment 6090297342) — **Filed**: 2026-10-09 · after the MVP
  gate work. Order: (1) plumbing behind the flag (`framing` in the router's top-level output → `context["inversion_framing"]`;
  `evaluate_consent(framing_hint=)`, where PRIVATE WRITE uses the hint, OUTWARD WRITE takes the stricter of hint and regex, DESTRUCTIVE is unchanged); (2) the prompt line
  + corpus WRITE rows get an expected framing → full run on the served model (rule 7); (3) a `MAX_EXECUTE_ALTERNATIVES` ratchet, retiring PRIVATE verbs
  only on a served framing MATCH.
- **Post-promotion served checks on alpha** — **Filed**: 2026-10-08 · **DONE 10-11 on 4bd1a236e9 (Web):** #1959 + #1960 CLOSED; delete-first-two + mark-first-two → #1943; identity + guidance PASS (IDENTITY/GUIDANCE deletions served-verified); #1975 + the "to web test one" title issue filed. **Remaining for the NEXT promotion:** Quote each served
  answer (rule 8): a pure "hello" and "thank you!" (CXO 10-11, #1974: canned copy must be Piper's voice, short and warm, no "How can I assist you today?" boilerplate; #1416 residue rule unchanged); "show today's tasks" (CXO 10-11: today's tasks first or clearly marked, else CXO rules on the reply shape); #1958 "remind me to X on Friday" → "(scheduled for Friday)" (needs the NEXT promotion); #1959 close of a nonexistent issue (honest reply, no confirm); #1889/#1963/#1964
  (#1965 a+b landed 10-08: quote the served standup + Radar for an OAuth-only account AND a PAT-only account, the latter on its
  owner's own PAT that PM provisions, never a Piper-held one; CXO closes #1889/#1963 on the quoted output); if PM turns on the `clear_todos` token, PM's 08-15 sentence first.

- **Next catalog change's full run — named rows** (Arch 2026-10-08) — **Filed**: 2026-10-08. Batch into the NEXT rule-7 run, never a
  dedicated one: `week_calendar` description clause "the user's own calendar only; never a team's, a shared or another person's
  calendar" ADDED to CXO's 10-06 clause (not replacing it); checklist rows: "show the team calendar" (expected floor, known live miss
  in the TEMPORAL ledger), then CXO's served floor probe (pass = says it can only see the user's own calendar; never invents a team's).
  Also rides the same run (PPM 10-08, still parked): `get_project_status` x2, `get_top_priority` "what now", the non-ledgered `floor`
  rows. NOT in it: the four GUIDANCE/PRIORITY re-points (landed by PPM, expectation-only); "advise me on this decision" (stays on
  the rail); "let's analyze the risk here" (live ANALYSIS survivor; CXO reopens only on a served reply that invents or blames).

## Sequenced from Arch's aging-items route (2026-08-31)
- #973 MEM-CACHE-AUDIT Phase 1 (96d): queue position — after the corpus tag-pass lands and PM's
  next test round clears; the June blockers Arch cites are confirmed cleared.
- #1459: next after #973 (Arch's route memo in read/ has the detail; sequencing mine, action later).

## Standing disciplines (the ones this file exists to survive compaction)
- One lane at a time in this worktree — NO commits of any kind while a lane is active (hardened
  8/31 after the docs-commit sweep).
- Pinned-ruff (0.6.9) format+check before code-bearing pushes; belt green is per-push discipline.
- Deploys only on PM's explicit word; flag changes to deployed env count.
- Verify awaited items against the ISSUE, not local files; merge origin/main BEFORE inbox listing.
