# Session log: prog-code (Coding Agent), 2026-10-17 09:45 PT

- Model: Opus (claude-opus-5-5)
- Role: Coding Agent (prog-code), briefed by Lead (rule-7 batch lane)
- Worktree: /Users/xian/Development/piper-morgan-worktrees/lead-rule7
- Branch: claude/lead-rule7-catalog-batch-2051-2069 (origin/main + held #2069 branch merged at 7dfb6739e7; merged origin/main eb7af9554d at 09:45, docs-only)
- Issues: #2051 (list_assigned_issues alias), #2069 (add_project router args; Arch's consent-line condition)

## 09:45 Start
- Read CLAUDE.md, routing-stack rule-7 record (#1976, #2069, meeting_time paragraphs, week_calendar full-run section), standing items "Rule 7 as refined by Arch", 10-13 controls.
- Same-minute main at start: eb7af9554d (origin/main, 09:45 PT).

## 09:46-09:50 Build (commit e087bcbaaa)
- #2051: `list_assigned_issues` added to `_READ_QUERY_COHORT["_handle_list_issues_query"]`. **Finding: aliases are not rendered in the router catalog** (`build_routing_prompt` prints the canonical name only). Measured: router prompt byte-identical before/after the alias (scratch dump diff; only the alias map gains `list_assigned_issues → list_issues`). `wired_chat_actions()` names entries by canonical key, so the floor manifest is unchanged too.
- #2069 condition: `portfolio_service.resolve_add_project_slots(message, router_args)` (router name first via `router_add_project_args`, the moved #1976 honesty guard; #1856 extractor fallback; description only from the router). Callers: `_handle_add_project`, `display_name_for(…, router_args)` → `consent_gate._summary_for` (reads `intent.context["inversion_args"]`), `question_how_to(…, router_args)` (rail seam passes inversion_args), adopted-category confirm. `CanonicalHandlers._router_add_project_args` kept as a delegate.
- Pins: `test_add_project_consent_name_2069.py` (13), `test_list_assigned_issues_alias_2051.py` (6, through `dispatch_workflow` with action `list_assigned_issues`: 0 assigned → #2040 line; 9 assigned → "That's 5 of 9"). Corpus row `what issues are assigned to me?` → `action:list_issues_query` inserted by hand in YAML and builder; census pin 597 → 598. Scorer `--dry-run` OK (598 rows).

## 09:50 Rule 7: same-minute main and the prompt diff
- origin/main 7fe8bfc1ee (docs/mail only since eb7af9554d); merged into the branch → candidate 8abd57b00c. Detached main worktree `/private/tmp/claude-501/rule7-main` at 7fe8bfc1ee (venv symlinked).
- Router prompt main vs candidate: exactly ONE catalog line differs, the `add_project` description (the #2069 "Put the parts in args…" sentence). The alias contributes nothing to the prompt.

## 09:51-09:53 ×6 screen, wording 1 (the #2069 description as merged)
- `scripts/inversion_router_control.py --provider anthropic --samples 6`, 25 phrases (4 moved/target rows, 3 PORTFOLIO neighbours incl. the declarative add, the 10-13 sentinel 12, clear family 3, declarative + question rows, standing member), both trees in the same minute. 150 calls each, 0 errors, served claude-haiku-4-5 150/150.
- Controls: `dev/2026/10/17/controls/rule7-baseline-main-x6.md`, `rule7-candidate-x6.md`.
- 24/25 identical. **Moved: `add octocat/hello-world to the project` link_repo ×6 (main) → CLARIFY ×6 @0.40 (candidate): candidate-attributed** (the same row wording 1 of #1976 broke on 10-13). Standing member analyze_blockers ×6 @0.95 on both.
- `what issues are assigned to me?` → NONE ×6 on BOTH trees: the router does not choose list_issues for it; the alias serves only the classifier path. Not attributable (identical), the row will read as a router miss.
- Next: wording 2 (scope the repo arg to the NEW project), re-screen.

## 09:55-09:57 ×6 screen, wording 2 ("the new project's name"; "repo = an owner/repo the user named for the new project")
- Both trees re-run in the same minute (16:57Z), 150 calls each, 0 errors, served haiku 150/150. Controls `rule7-baseline-main-w2-minute-x6.md`, `rule7-candidate-w2-x6.md`.
- `add octocat/hello-world to the project`: main link_repo ×6, candidate **CLARIFY ×6 @0.40 — still candidate-attributed.** `list my projects` main manage_portfolio 5/1 → candidate list_projects ×6 (improvement). Everything else identical in route; standing member ×6 both.
- Next: wording 3 (last allowed): drop the `repo` arg from the sentence (the handler still links an utterance repo clause through the resolver's extractor half).

## 09:58-10:00 ×6 screen, wording 3 (repo arg dropped from the sentence)
- Same-minute pair at 17:00Z, 150 calls each, 0 errors, haiku 150/150. Controls `rule7-baseline-main-w3-minute-x6.md`, `rule7-candidate-w3-x6.md`.
- `add octocat/hello-world to the project`: main link_repo ×6, candidate **CLARIFY ×6 @0.40 — attributed again.** Three wordings, the cap: **DROP the #2069 description change.** No full run (owed only by a landing candidate).

## 10:00-10:01 Is the sentence needed? (scorer --phrase, args row)
- `inversion_phase1_shadow_score.py --provider anthropic --phrase "Add a project called Baz with description testing the description"` ×3 on wording 1: action AND args right 3/3.
- Same ×3 with the description reverted to main's text in the working tree (prompt verified byte-identical to main's): **action AND args right 3/3.** The served router already names name/description under main's wording (the #1976 outcome again). Working tree restored to the branch's wording 1 afterwards (nothing committed from W2/W3/main-wording).
- Main tree scorer runs on this row returned 0 rows (the row is not in main's corpus; it came with the #2069 branch) — not a measurement, noted.
- Attribution table: `dev/2026/10/17/controls/rule7-attribution-2051-2069-wordings-2026-10-17.md`. Routing-stack paragraph added after the #2069 paragraph.
- LLM calls: screens 6 × 150 = 900 (control script) + scorer 9 = 909 Haiku calls, ~3.3k prompt tokens each (no spend line printed by the scripts; rough estimate ≈ $3 at Haiku 4.5 list price, unverified).
- Disclosure: the ×6 screens ran through `scripts/inversion_router_control.py` (the kept rule-7 ×N screen tool; same router + grammar as the scorer, its docstring names it as the refined-rule-7 screen and the 10-13 controls were made with it); the brief named only the scorer. The scorer has no repeat flag.

## 10:02-10:08 Tiers (branch state = wording 1 + alias + resolver, 8abd57b00c + docs)
- pytest (`-m "not llm"`, importlib): intent_service 6560 passed (3 deselected); intent 64; llm 126; consciousness 66; enforcement 137 (+1 skipped); web 1093; phase3 deletion 76; integrations 460 (+3 skipped); database 168; corpus pin `test_create_todo_router_text_1976.py` 20. 0 failures.
- mypy gate: total=1096, all 24 codes at ceiling. ruff 0.6.9 check + format: clean on all touched .py.
- Detached main worktree `/private/tmp/claude-501/rule7-main` removed at wrap.

## Outcome: DROP the #2069 description (screen), stop and report to Lead. Nothing pushed, no mail.

## 10:11 Lead's decision: land with main's add_project description (commit a4d429e246, merge of origin/main 50c6fd8475 docs/mail only)
- Reverted the add_project description to main's text byte for byte (and its #2069 comment). `git diff origin/main -- services/intent_service/workflow_entries.py`: the `list_assigned_issues` alias (+ comment) and the #2069 handler threading in `run_add_project_workflow` (`router_args = …inversion_args` + `router_args=` kwarg + comment). The description lines no longer differ. The threading is the #2069 handler that lands, so it stays.
- Prompt identity: scratch `dump_prompt.py` (`_SYSTEM_PROMPT` + `build_routing_prompt("X", derive_routing_grammar())`) on a detached worktree of origin/main 0b52b1b873 vs this branch; `diff <(grep -v '^ALIASES' main) <(grep -v '^ALIASES' cand)` → **PROMPT_IDENTICAL** (91 lines each); alias map diff: `+ ('list_assigned_issues', 'list_issues')` only. Worktree removed. No LLM calls.
- Pin flipped: `test_rail_description_is_unchanged_from_main` (quotes main's text, no "args") + `test_handler_consumes_router_args_without_the_description_sentence`; honesty-guard and resolver pins unchanged.
- Routing-stack #2069 paragraph rewritten to the #1976 shape (description UNCHANGED, three wordings DROPPED, attributed row, controls/attribution paths, Baz 3/3 under main's wording) + #2051 alias note; my earlier batch paragraph folded into it.
- Tiers: intent_service 6561; intent 64; llm 126; enforcement 137 (+1 skipped); phase3 deletion 76; web 1093; integrations 460 (+3 skipped); database 168; consciousness 66; 1976 corpus pin 20. 0 failures. mypy gate 1096. ruff check + format clean.
- Not done (out of scope, listed): the Baz corpus row's notes (YAML + builder) still say "UNMEASURED at deposit: the rail-description change … owes rule 7's served run" — now stale.
