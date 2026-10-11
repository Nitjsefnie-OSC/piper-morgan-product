# Inversion Phase-1 shadow score — CONSTRAINED ROUTER vs Phase-0 baseline
Run: 2026-10-11 15:24Z · corpus: inversion_corpus_phase0.yaml (17 rows) · scripts/inversion_phase1_shadow_score.py
Served (#1620 — resolved, post-fallback, per row): anthropic:claude-haiku-4-5 (17/17)

LAYER (m-43): **router only, context-free** — one constrained Haiku-class call per row (17 LLM calls incl. repair retries; 0 ERROR, 0 REFUSED), grammar derived from the live registry at run time (72 canonical operations, 86 input-side aliases collapsed, + NONE/CLARIFY). The production chain was NOT executed in this run; the baseline column is Phase-0's FULL-CHAIN production decision (inversion-phase0-baseline-full-2026-08-12.md). Context-dependent rows (the 1529 offer/flow family) ran WITHOUT session state — their answers are informational for Phase 2, not its measured shape.

## Per-category vs baseline (denominators stated — m-44)

| category | rows | asserted | router match | baseline match | Δ | REVIEW | gate |
|---|---|---|---|---|---|---|---|
| PORTFOLIO | 17 | 14 | 12 | 6/7 | +6 | 3 | no regression |
| **TOTAL** | 17 | 14 | 12 | 36/39 | -24 | 3 | (aggregate is NOT the gate) |

Gate reading (Arch condition 1 as amended 08-09 08:3x, PPM): **no category may regress; the aggregate is never the gate** (the M2 precedent: 72.1% aggregate passed while a category was broken). CONVERSATION / DISCOVERY / PROVENANCE / TRUST / ANALYSIS have REVIEW-only denominators in Phase 0 and remain **ungateable** here — same as Phase 0 stated; growing asserted expectations there is outstanding Phase-0 work, not a Phase-1 scoring artifact.

⚠️ **m-44: the table above compares two different denominators** (this run's 116-row corpus vs the baseline's 93-row corpus) — its `Δ`/`gate` cells are INFORMATIONAL ONLY from this run forward. The shared-subset table below, scored on rows asserted in BOTH corpora, is the actual gate.

## Shared-subset score vs 2026-08-12 baseline (m-44 fix — THIS is the gate)

Matching rule: phrase normalized (strip + collapse whitespace + casefold), exact match required; on a miss, fall back to an unambiguous ≥20-char prefix match in either direction (markdown row-detail tables truncate long phrases with no ellipsis, at different fixed lengths in different docs). Only rows asserted (non-REVIEW) on BOTH sides are scored here; the per-category table above compares two different denominators and is informational only from this point forward.

| category | shared asserted | router match | baseline match | gate |
|---|---|---|---|---|
| PORTFOLIO | 1 | 1/1 | 1/1 | no regression |

**Denominator deltas (m-44)** — rows in the 08-12 baseline no longer asserted in the current corpus (dropped), and rows asserted now that the baseline never saw (added). Neither is scored above; both are why the totals table's Δ column is informational, not the gate.

Dropped (baseline-asserted, not in current corpus):
- [EXECUTION] create a ticket for the login bug
- [EXECUTION] close issue 42
- [EXECUTION] comment on issue 42: looks good
- [EXECUTION] set my default repo to acme/widgets
- [EXECUTION] update the project plan doc with the new dates
- [EXECUTION] give me a project status report
- [GUIDANCE] how do I create a ticket?
- [IDENTITY] who am I?
- [IDENTITY] what's my role?
- [MEMORY] what have you learned about my workstyle?
- [PORTFOLIO] list my projects
- [PORTFOLIO] what projects have I archived?
- [PORTFOLIO] what projects do I have?
- [PORTFOLIO] Archive my project Test.
- [PORTFOLIO] Archive my project "Test"
- [PORTFOLIO] Archive the project called Test
- [PRIORITY] what should I focus on today?
- [PRIORITY] what are my top priorities?
- [QUERY] analyze the file I uploaded
- [QUERY] show my open issues
- [QUERY] show my open pull requests
- [QUERY] any stale PRs?
- [QUERY] what needs my attention?
- [QUERY] what changed since yesterday?
- [QUERY] how productive was I this week?
- [QUERY] what is my default repo?
- [QUERY] can we connect my github?
- [QUERY] connect my slack
- [QUERY] link mediajunkie/test-piper-morgan to the project
- [QUERY] help me set up github
- [STATUS] give me my standup
- [STATUS] what am I working on?
- [SYNTHESIS] summarize the document
- [SYNTHESIS] write a short update for the CEO on where we are
- [TEMPORAL] what's on my calendar today?
- [TEMPORAL] when is my next meeting?
- [TEMPORAL] what time is it?
- [TEMPORAL] remind me at 9:41 today to check in with the lead developer

Added (current-asserted, not in the 08-12 baseline):
- [PORTFOLIO] show my archived projects
- [PORTFOLIO] show archived projects
- [PORTFOLIO] view my archived projects
- [PORTFOLIO] show my projects
- [PORTFOLIO] hide the project Beta
- [PORTFOLIO] put the old project away
- [PORTFOLIO] restore project Epsilon
- [PORTFOLIO] unarchive the old project
- [PORTFOLIO] bring back my archived project
- [PORTFOLIO] search projects for budget
- [PORTFOLIO] find project deadline
- [PORTFOLIO] add a new project
- [PORTFOLIO] I'd like to start a new project

## Exhibit A (PM 2026-08-08 live transcript) + Arch's demanded row

Selection rule: corpus `source` containing one of ('exhibit-a', 'issue-1559', 'issue-1492') → 0 rows (the 8 Exhibit-A failures), plus the demanded row `"what reminders do I have?"` (probe-row-11, REVIEW — the sharpest test of the thesis: the LLM classifier misrouted it until the pre-classifier claimed it).

| phrase | expected | router route @conf | verdict | source |
|---|---|---|---|---|

## REVIEW rows — the router's answers as data (informational, unscored)

These 54 rows are the Inversion's question book (36 probe-DISAGREEs by construction + PM's live failures). Nothing here is scored; the router's answer is recorded so the questions accumulate evidence.

| phrase | category | router route @conf | rationale | source |
|---|---|---|---|---|
| delete my project Gamma | PORTFOLIO | `archive_project` @0.85 | User asks to delete project Gamma; archive_project is the re | phase3-rule10/PORTFOLIO_PATTERNS tests/u |
| remove the project Delta | PORTFOLIO | `archive_project` @0.85 | User asks to remove project; archive is the reversible remov | phase3-rule10/PORTFOLIO_PATTERNS tests/u |
| get rid of my test project | PORTFOLIO | `archive_project` @0.85 | User wants to remove a project; archive is the reversible op | phase3-rule10/PORTFOLIO_PATTERNS tests/u |

## Row detail (asserted rows)

| phrase | category | expected | router route @conf | verdict | note | framing |
|---|---|---|---|---|---|---|
| show my archived projects | PORTFOLIO | action:list_archived_projects | `list_archived_projects` @0.99 | MATCH |  | - |
| show archived projects | PORTFOLIO | action:list_archived_projects | `list_archived_projects` @0.95 | MATCH |  | - |
| view my archived projects | PORTFOLIO | action:list_archived_projects | `list_archived_projects` @0.99 | MATCH |  | - |
| show my projects | PORTFOLIO | action:list_projects | `list_projects` @0.95 | MATCH |  | - |
| list my archived projects (show all names) | PORTFOLIO | action:list_archived_projects | `list_archived_projects` @0.95 | MATCH |  | - |
| hide the project Beta | PORTFOLIO | action:archive_project | `archive_project` @0.95 | MATCH |  | execute:MISMATCH(none) |
| put the old project away | PORTFOLIO | action:archive_project | `archive_project` @0.75 | MATCH |  | execute:MISMATCH(none) |
| restore project Epsilon | PORTFOLIO | action:restore_project | `restore_project` @0.99 | MATCH |  | execute:MISMATCH(none) |
| unarchive the old project | PORTFOLIO | action:restore_project | `restore_project` @0.95 | MATCH |  | execute:MISMATCH(none) |
| bring back my archived project | PORTFOLIO | action:restore_project | `CLARIFY` @0.6 | MISMATCH | CLARIFY | execute:MISMATCH(none) |
| search projects for budget | PORTFOLIO | action:search_projects | `search_projects` @0.99 | MATCH |  | - |
| find project deadline | PORTFOLIO | action:search_projects | `CLARIFY` @0.4 | MISMATCH | CLARIFY | - |
| add a new project | PORTFOLIO | action:add_project | `add_project` @0.95 | MATCH |  | execute:MISMATCH(none) |
| I'd like to start a new project | PORTFOLIO | action:add_project | `add_project` @0.95 | MATCH |  | ambiguous:MISMATCH(none) |

## Framing score (#1970 step (1)/(6))

Per-value denominators (m-44) — rows with NO framing expectation (most of the corpus: READ actions, DESTRUCTIVE actions, REVIEW rows, anything the expected-framing mapping doesn't cover) are counted separately below, never folded into either side of the table.

| expected framing | matched | expected | rate |
|---|---|---|---|
| execute | 0 | 6 | 0% |
| ambiguous | 0 | 1 | 0% |
| compose | 0 | 0 | — |
| (no expectation) | — | 10 | — |
