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
  literals (#1935). Re-measured **Sun 10-11: 127 / 97** with the sizing table (memo 3e71c8297: ~35 served calls buy the rule-10 bucket; the router bucket costs a full run per candidate; nothing else moves on spend). Mon 10-12: confirm main unchanged, else re-measure. PORTFOLIO partial (2) HELD 10-11: `update … project` is a ruled survivor (#1933 option a); the show/list/view literal needs
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
  (3) `\bstatus report\b` re-delete waits on (1). (4) DONE 10-10 19:1x: PPM recounted 127 (d29bfef2ce). (5) DONE 10-11: `--all` table vs `--list` disagreement (partial GO / rule 10 / rule 11 missing from the table) fixed + pinned. (6) #1951 residue — **Filed**: 2026-10-11 · two PPM verdicts asked (link-my-repository, key-tasks-for-this-sprint); close #1951 when they land. (7) Proposal to Arch: `_PLEASANTRY_FILLER_PATTERNS` NOT_ROUTING by name (tail 97 → 87).

- **Description-change candidate: "show today's tasks" → list_todos_query** (Arch: worth doing for its own sake, its own rule-7 run, my timing) —
  **Filed**: 2026-10-10 · narrowed 10-11: of the three named, "show priorities for this sprint" (get_top_priority @0.85, MATCH) and "pull up my
  schedule" (week_calendar @0.85, MATCH) are already right on the 10-10 full run. The remaining row reads attention_query @0.85; the 10-10 lane
  found every list_todos_query wording regressed, and 10-11's inverse (attention_query excluding a plain list of today's tasks) screened
  clean then failed the full run (5 ×6-attributed regressions incl. a WRITE landing; held report
  `inversion-attention-query-description-CANDIDATE-HELD-full-score-2026-10-11-anthropic.md`). **No fourth wording.** Asked PPM/CXO for a
  re-judge: (a) attention_query, (b) REVIEW (Lead leans b), (c) keep as a known miss. Blocked on that ruling.
- **#1970 framing to the router** (Production, Arch's design on the issue, comment 6090297342) — **Filed**: 2026-10-09 · after the MVP
  gate work. Order: (1) plumbing behind the flag (`framing` in the router's top-level output → `context["inversion_framing"]`;
  `evaluate_consent(framing_hint=)`, where PRIVATE WRITE uses the hint, OUTWARD WRITE takes the stricter of hint and regex, DESTRUCTIVE is unchanged); (2) the prompt line
  + corpus WRITE rows get an expected framing → full run on the served model (rule 7); (3) a `MAX_EXECUTE_ALTERNATIVES` ratchet, retiring PRIVATE verbs
  only on a served framing MATCH.
- **Post-promotion served checks on alpha** (+ #1960: "my default repo should be test-piper-morgan" → quote the consent line) — **Filed**: 2026-10-08 · **Web runs these (xian 10-10, list sent 13:1x)**; quoted replies come to Lead + Exec. Quote each served
  answer (rule 8): "delete the first two reminders"; #1958 "remind me to X on Friday" → "(scheduled for Friday)" (needs the NEXT promotion); #1959 close of a nonexistent issue (honest reply, no confirm); #1889/#1963/#1964
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
