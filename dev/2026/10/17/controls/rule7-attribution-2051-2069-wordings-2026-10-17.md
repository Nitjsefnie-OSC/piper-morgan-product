# Rule 7 batch (#2051 alias + #2069 add_project description): ×6 attribution, three wordings — DROP

Run 2026-10-17 16:51–17:01Z (09:51–10:01 PT) · `scripts/inversion_router_control.py --provider anthropic --samples 6` · 25 phrases per tree · every run 150/150 served `anthropic:claude-haiku-4-5`, 0 ERROR · main = detached worktree of origin/main 7fe8bfc1ee; candidate = branch `claude/lead-rule7-catalog-batch-2051-2069` 8abd57b00c (+ the wording under test). Main was re-run in the same minute as each candidate wording.

## What reaches the router

Router prompt, main vs candidate (scratch dump of `_SYSTEM_PROMPT` + `build_routing_prompt`): **exactly one catalog line differs, `add_project`'s description.** The #2051 alias is not rendered in the catalog (`build_routing_prompt` prints canonical names only); it changes only `alias_to_canonical` (`list_assigned_issues → list_issues`). The alias half of the batch therefore has no router-facing text.

## Wordings screened (the `add_project` description's args sentence)

| # | args sentence | controls |
|---|---|---|
| 1 | "Put the parts in args: name = the project's name only; description = the description the user gave, if any; repo = an owner/repo the user named, if any" (as merged from #2069) | `rule7-baseline-main-x6.md` / `rule7-candidate-x6.md` |
| 2 | 1 with "the new project's name" and "repo = an owner/repo the user named for the new project" | `rule7-baseline-main-w2-minute-x6.md` / `rule7-candidate-w2-x6.md` |
| 3 | "Put the parts in args: name = the new project's name only; description = the description the user gave, if any" (repo arg dropped) | `rule7-baseline-main-w3-minute-x6.md` / `rule7-candidate-w3-x6.md` |

## Every row that moved (main same minute → candidate)

| phrase | corpus expected | W1 main → cand | W2 main → cand | W3 main → cand | reading |
|---|---|---|---|---|---|
| add octocat/hello-world to the project | action:link_repo | link_repo ×6 → **CLARIFY ×6 @0.40** | link_repo ×6 → **CLARIFY ×6 @0.40** | link_repo ×6 → **CLARIFY ×6 @0.40** | **candidate-attributed regression, all three wordings** (passes ×6 on main every minute, fails ×6 on every candidate). Same row #1976 wording 1 broke on 10-13. |
| list my projects | action:list_projects | manage_portfolio 4/ list_projects 2 → same 4/2 | manage_portfolio 5/1 → list_projects ×6 | list_projects 5/ manage_portfolio 1 → list_projects ×6 | main wobbles (4/2, 5/1, 1/5 across three minutes): perturbation-sensitive on main itself; candidate W2/W3 6/6 right. Noise, not attributed (an improvement on W2/W3, read→read). |

Unmoved on every wording (route identical at ×6, main and candidate): `what issues are assigned to me?` (NONE ×6 — the router does not pick `list_issues`; see below), both Baz rows and `add a project called Atlas` (add_project ×6), `I'd like to start a new project` (declarative, add_project ×6), `How do I setup my projects?` (get_contextual_guidance ×6), the five PM todo phrasings (create_todo ×6), `remind me to send the invoice on Friday` (create_reminder ×6), `delete a reminder` (CLARIFY ×6), `mark the first two complete` (complete_todo ×6), `what needs my attention?` (attention_query ×6), `show the team calendar` (NONE ×6), `create an issue about the login bug` (create_issue ×6), clear family ×3 (clear_todos ×6), `My default repo should be …` (declarative, set_default_repo ×6), `Can we just mark done here?` (question, CLARIFY ×6), **standing member `let's analyze the risk here` analyze_blockers ×6 @0.95 on all six runs.** Confidence-only shifts (0.95→0.99 on the Baz description row; 0.50–0.60 on delete a reminder) are not route moves.

## Is the description needed at all? (the #1976 question)

`scripts/inversion_phase1_shadow_score.py --provider anthropic --phrase "Add a project called Baz with description testing the description"` ×3 each:
- candidate W1 wording: action AND args right **3/3** (PORTFOLIO 1 asserted, 1 right, 0 ARGS_MISMATCH).
- **main's wording** (the description reverted in the working tree; prompt verified byte-identical to main's): action AND args right **3/3**. The served router already names `name = Baz`, `description = testing the description` without the args sentence.

## Outcome

**DROP the #2069 rail-description change** (three wordings, the cap; each puts `add octocat/hello-world to the project` link_repo → CLARIFY 6/6, attributed). No full corpus run spent: the full run is owed only by a candidate that lands.

What remains measured-safe: the #2069 handler (consumes router `name`/`description`/`repo` behind the honesty guard), the one resolver (Arch's consent-line condition), and the #2051 alias. With the description at main's text the router prompt is byte-identical to main's (verified), so that batch is not a catalog change; whether it still owes a full run is Lead's/Arch's call. The #2069 pin `test_rail_description_names_the_three_args` and the routing-stack #2069 paragraph would change with that drop.

`what issues are assigned to me?` → NONE ×6 on both trees: the alias serves the classifier path only. A router fix would be a `list_issues` description change (a new catalog candidate, not in this batch).
