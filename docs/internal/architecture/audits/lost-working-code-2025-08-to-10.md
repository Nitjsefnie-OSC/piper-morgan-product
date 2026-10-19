# What the 2025-10-01 "docs:" commit removed, and what else was lost the same way

Arch, 2026-10-19, at xian's request (relayed by Comms, `mailboxes/arch/read/handoff-comms-to-arch-…-aad66d9d1-2026-10-19.md`). Read-only git archaeology on `origin/main`. Every sha below was read this session. Method notes and denominators are in the last section.

## Bottom line

1. **The 10-01 commit was the third blow, not the first.** Chat summarization of an uploaded file was already broken when the "docs:" commit deleted `main.py`. It died in three steps, and the first was the one that mattered:
   - **2025-08-22, `2ad8d639dd`** ("feat: add comprehensive multi-agent system and morning standup MVP") replaced `services/orchestration/engine.py` (1,326 lines) with a different 345-line engine. The new engine had no handler for **eight** task types that `WorkflowFactory` still built, ANALYZE_FILE and SUMMARIZE among them. It also dropped `create_workflow_from_intent`, which `main.py` called on every workflow-bound chat turn. From that day, any chat request that needed a workflow failed. File summaries, GitHub issue creation from chat and listing projects all went down together.
   - **2025-09-17, `b5f861c645`** (#172) and **2025-09-23, `4ecdd5ef3d`** (#186): the browser stopped talking to `main.py` (port 8001). The page moved to relative URLs on the web app (8081), which proxied only `/api/v1/intent`. Then intent handling moved in-process into `web/app.py`, with ANALYSIS and EXECUTION intents answered by a placeholder: *"requires full orchestration workflow. This is being restored in Phase 3."* The upload route was never proxied, so uploads from the page went to a web app with no upload route. Workflow polling became a stub that always says "completed".
   - **2025-10-01, `effa5fe2a6`** (the copy on main; `aad66d9d1` is the same commit in a history not on `origin/main`) replaced `main.py` with a 109-line config-validator stub and parked the old file as `main.py.backup`. By then the UI no longer reached that code. The commit removed the last copy of the July chat path and stopped the 8001 backend. `main.py` started a server again by 2025-10-16 (`e986dc531b`), now running `web.app:app`.
2. **#172 misdiagnosed the 08-22 break.** Its "root cause" was a missing proxy. The 500 errors it describes match `main.py` calling an engine method that 08-22 had deleted. The proxy fix moved traffic away from the broken code instead of repairing it, so the loss stayed invisible.
3. **The cost was a year of decisions built on "it never worked".** #1158 (2026-06) ruled the summarize handler "effectively dead code" and routed summaries to the floor, with Arch's vocabulary ruling. #1187 built issue summaries on that floor. #1624 (2026-08, still open) and the 08-15 forensics doc say chat document summarization "never once worked", and both date the break to 10-01. Both are wrong on "never". The July 2025 path worked roughly (Comms' fact-check has the record), and the break came on 08-22.
4. **Other surprises of this shape:** a full-history sweep (36,177 commits) found **no other unexplained loss of live behaviour**. It found one follow-on: `a47eaf9ea8` (10-04, "docs(GREAT-3C)") deleted `main.py.backup`, the last tree copy of the old backend. Two 2026 log commits picked up staged disposals and were caught within minutes. One more "never" claim is false: `technical-spec.md:548` on the query layer. See §3.

## 1. What the commits removed

### 2025-08-22, `2ad8d639dd`: the engine swap (the real break)
- `engine.py` 1,326 → 345 lines. The new file is not an old snapshot. It is a different, smaller engine built around the commit's multi-agent work. Its own `engine.py.backup` (347 lines) is nearly identical to the new file, not to the engine it replaced. So the 1,326-line engine was kept nowhere in the tree.
- Task handlers in the old engine: ANALYZE_REQUEST, EXTRACT_REQUIREMENTS, IDENTIFY_DEPENDENCIES, CREATE_WORK_ITEM, UPDATE_WORK_ITEM, NOTIFY_STAKEHOLDERS, ANALYZE_GITHUB_ISSUE, ANALYZE_FILE, SUMMARIZE, EXTRACT_WORK_ITEM, GITHUB_CREATE_ISSUE, GENERATE_GITHUB_ISSUE_CONTENT, LIST_PROJECTS, GENERATE_DOCUMENT, CREATE_SUMMARY, PROCESS_USER_FEEDBACK, plus two placeholders (Jira, Slack).
- The new engine handles ANALYZE_REQUEST, EXTRACT_REQUIREMENTS, IDENTIFY_DEPENDENCIES, GENERATE_DOCUMENTATION and EXECUTE_GITHUB_ACTION. Anything else raises `ValueError("Unknown task type")`.
- `WorkflowFactory` (unchanged, read at `b5f861c645~1`) still built tasks of eight types the new engine could not run: ANALYZE_FILE, SUMMARIZE, ANALYZE_GITHUB_ISSUE, GENERATE_GITHUB_ISSUE_CONTENT, GITHUB_CREATE_ISSUE, CREATE_WORK_ITEM (×2), EXTRACT_WORK_ITEM, LIST_PROJECTS.
- `create_workflow_from_intent` was gone from 08-22 until `e9f1d62868` (#185, 09-23) re-added it. The eight handlers never returned: pickaxe on `TaskType.ANALYZE_FILE` and `_create_github_issue` in `engine.py` shows the 08-22 removal and no re-add. The engine was deleted entirely on 2026-05-15 (`9af4ef43ea`, #1094).
- A comment in `web/app.py` on 09-23 already says *"query actions that were broken in August 22 refactor"*, restoring only `show_standup`. So the break was seen, and only the standup was mended.
- **Why it happened: unverified.** The commit message lists only standup and multi-agent work. It is a plain commit, not a merge. Possible reasons include an agent rewriting the file from a smaller design, or committing from a working copy carrying a different engine. Nothing in the message or the tree says which.

### 2025-09-17 and 09-23: the UI moves off `main.py`
- Before `b5f861c645`, the page's `API_BASE_URL` was the backend (8001), so chat, upload and workflow polling all hit `main.py`.
- `b5f861c645` (#172, "Fixes #172"): relative URLs on 8081, with a proxy for `/api/v1/intent` only. `web/app.py` at that commit has no `/api/v1/files/upload` route. It still had none on 10-01, while the page still posted to it. The upload route came back as `web/api/routes/files.py` on 2025-11-01 (`3fb0660fa1`).
- `4ecdd5ef3d` (#186): the proxy is replaced by in-process classification. QUERY goes through QueryRouter, CONVERSATION through the handler, and everything else gets the placeholder above. `/api/v1/workflows/{id}` returns a fixed "completed".

### 2025-10-01, `effa5fe2a6` / `aad66d9d1`: `main.py` replaced
The old `main.py` had these routes and pieces, with where each stands today:

| Removed | Came back? |
|---|---|
| `POST /api/v1/intent` (chat, with the only live `IntentEnricher` file-reference call) | Chat moved to `web/app.py` → `IntentService` (09-23 onward). File enrichment never returned to chat. The 08-15 forensics measured zero non-test callers, and #1624's C+A (08-16) re-used `FileResolver` instead. |
| `GET /api/v1/workflows/{id}`, which rendered results including "Here's my summary of {filename}:" | No. Web's version was a stub. The summary template survives only as a vestige. |
| `POST /api/v1/files/upload`, `GET /api/v1/files/search` | Upload: yes, 2025-11-01 (`web/api/routes/files.py`). Search: no route today (`git grep files/search` in web and services: 0). |
| `POST /api/v1/clarification`, `handle_file_disambiguation` | No route today (0 hits). Clarification lives in the intent service's own turns now. |
| `GET /api/v1/products`, `GET /api/v1/workflows` | No (0 hits). |
| `/api/standup` | Already proxied by `web/app.py`; standup lives on. |
| Slack, staging-health, transparency and feedback routers; `/health` | Transparency and feedback routers are mounted under `web/app.py` today. Slack moved to the plugin system (GREAT-3, 2025-10). staging_health was deleted 2026-09-23 (#1499). `/health` is served by `web/api/routes/admin.py`. |
| Lifespan background execution (`safe_execute_workflow`) | No. The engine was deleted in 2026-05. |

## 2. What losing it cost

- **Fourteen months without chat file summaries**, from 2025-08-22, and still open as #1624. The July path worked roughly, and nothing replaced it.
- **The diagnosis went wrong twice.** #172 (09-17) called the 08-22 break a missing proxy. The 08-15 forensics doc dated the break to 10-01 and built "never worked … since the first commit" on a search that skipped June 23 to October 1, 2025. #1624's title carries that claim.
- **Decisions made on "dead" or "never":**
  - **#1158** (2026-06-09) called `_handle_summarize` effectively dead and routed summaries to the floor. Arch's verb-plus-source-slot vocabulary ruling was part of it. The handler was "dead" because the 2025 path behind it had been cut, not because the design had failed.
  - **#1187** (2026-06-12) built issue summaries on the floor, and that works. Its document branch was deferred and closed with no successor. #1624 exists because of that.
  - **#1624** (C+A, 2026-08-16) re-wired chat to the #290 REST handler. Comms' fact-check says it failed live on 08-18, and it is still open. It restored vocabulary #1158 had removed, so the same ground was crossed twice.
- **Other capabilities that went silently with 08-22:** chat GitHub issue creation and analysis, work-item creation and extraction, and list projects through workflows. Most came back later on the action rail under other issues. When each returned is not traced here.
- **Work redone:** the upload route (2025-11), the summarize handler (#290, 2025-11), file resolution (#1624, 2026-08), and the vocabulary twice (#1158 removed it, #1624 restored it).

## 3. Other surprises of this shape

An Opus subagent swept every non-merge commit on `origin/main` (36,177, from 2025-06-01 to 2026-10-19 at `e20ad0d57d`) for commits whose subject implies no behaviour change but that deleted source. It counted .py, .js, .ts, .html, .css, .yml, .toml, .sh and the Dockerfile, and excluded md, dev/, docs/, mailboxes/ and archive/. 158 commits deleted ≥150 source lines. 59 of those carry no deletion word in the subject. A Python AST pass on 143 commits listed definitions and routes that vanished from the whole tree. It ranked `effa5fe2a6` (the sanity check) and **`2ad8d639dd` as the only two with lost live behaviour.** Arch re-checked the starred items.

| sha | date | label | what happened | class |
|---|---|---|---|---|
| `2ad8d639dd` | 2025-08-22 | feat (standup / multi-agent) | §1. 26 handler definitions gone tree-wide. ★ The new dispatcher also branches on `TaskType.GENERATE_DOCUMENTATION` and `EXECUTE_GITHUB_ACTION`, which do not exist in `shared_types.py` at that sha (0 hits; only engine.py and its backup name them). The #1092 issue audit (2026-05-15, `dev/2026/05/15/1020-issue-audit.md`) reportedly saw the handler gap and called it "latent", without tracing it to this commit (the subagent's reading; not re-checked). | **Lost live behaviour, unexplained** |
| `a47eaf9ea8` | 2025-10-04 | docs(GREAT-3C) | ★ Deleted `main.py.backup`, the parked July `main.py`, three days after 10-01. It also removed 28 root ad-hoc scripts, which were not live. The old backend now survives only in history. | Mislabelled, finishes the 10-01 loss |
| `541dbb9561` | 2026-09-23 | docs(lead): … log | The #1499 Class-2 disposal (Arch GO) was swept into a log commit by the shared index. It left `admin.py` importing a deleted module for about 9 minutes. Fixed and recorded in `73a2cd1260`. | Mislabelled, documented, fixed |
| `e05a994aa5` | 2026-08-31 | docs(lead): probe report | The #1613 disposal was swept into a log commit the same way. It left dangling imports for about 9 minutes, fixed and recorded in `7e4d78e4df`. | Mislabelled, documented, fixed |
| `0f33b442ed`, `e1b1e76f80` | 2025-07-10, 07-13 | "formatting", "docs:" | The reverse case: real feature code arrived under a no-change label (JSON summary parsing, workflow-result rendering, the "Here's my summary" template). Nothing was lost. | Mislabelled, additive |
| `a510c572d3` | 2025-08-26 | Cleanup | `document_memory.py` deleted. Only a test imported it. | Mislabelled, nothing live lost |
| `c2727e8b08` | 2026-01-11 | chore: sync | Real code changes. No Python definitions lost. Template and JS behaviour not checked. | Unclear |

Five style and format commits were checked by AST: identical structure apart from import order. Root scratch scripts moved or deleted in several commits were not live.

**The shape behind it.** Every real loss, here and in §1, came from **a commit that did two things under one label**. A feature commit swapped a core module (08-22). A docs commit replaced an entry point (10-01). Log commits picked up a staged disposal from the shared index (2026-08-31, 2026-09-23). The two 2026 cases were caught within minutes, because the disposals had issues and the ratchet and test suite were watching. The 2025 cases went unseen because nothing tested the paths they cut.

**"Never" claims resting on a bounded search** (66 regex hits in `docs/internal`; code-relevant ones listed, only the starred one verified):
- ★ `architecture/current/technical-spec.md:548`: "the CQRS-lite query layer was never wired to any entrypoint". **Contradicted:** the 2025 `main.py` constructed `QueryRouter(` at two sites (`aad66d9d1~1:main.py:531,575`), and `web/app.py` used it from 09-23 (#186). It became unwired, which is not the same as never wired.
- `operations/summarize-intent-forensics-2026-08-15.md:65,104`: corrected by this audit.
- Snapshot or date-unstated "never wired / never existed / never fired" claims, unverified: `reviews/2026-08-architectural-review/findings/leg-b-live-state-census.md:33,36,102`; `patterns/pattern-052-personality-bridge.md:13,388`; `pattern-053-warmth-calibration.md:13,450`; `current/grammar-compliance-audit.md:777`; `current/feature-object-model-map.md:922`; `methodology-core/methodology-09-MCP-SPATIAL.md:12`; `design-records/design-record-grammar-conscious-family-2026-09-23.md:28`; `current/data-model.md:405,832`; `adrs/adr-007-staging-environment-architecture.md:18`; `operations/dashboard-welfare-criteria-v0.3.md:151`; `migration-checklist.md:81`. Each should say what it searched and when. Where it can't, "not found in <range>" is the honest form.

## 4. Corrections owed
- **`docs/internal/operations/summarize-intent-forensics-2026-08-15.md`:** add a correction note at the top. The break began 2025-08-22 (`2ad8d639dd`), not 10-01. Cite the on-main sha `effa5fe2a6` for 10-01. "Never worked" is wrong for July 2025. The OrchestrationEngine was the live chat path until 08-22. Owner: Lead (it's Lead's dispatched doc). This file is the source to cite.
- **#1624's title** says "has NEVER worked in chat". Edit to "has not worked in chat since 2025-08-22". Owner: Lead.
- **`docs/internal/architecture/current/technical-spec.md:548`:** "never wired to any entrypoint" should read "unwired by 2026-08 (wired in `main.py` 2025-07 to 10-01 and in `web/app.py` from 09-23)". Owner: Arch. Done in this same commit.
- **Comms' fact-check** (`docs/internal/planning/comms/fact-check-the-feature-that-was-never-real-2026-10-19.md`) names `aad66d9d1` and 10-01 as the loss. Both should move to `2ad8d639dd` / 08-22. Owner: Comms.

## Method and denominators
- Read on `origin/main` at 2026-10-19 ~10:00 PT: `git show` of `effa5fe2a6`, `aad66d9d1` (and its `merge-base --is-ancestor` check: not on main), `2ad8d639dd`, `b5f861c645`, `4ecdd5ef3d`, `e9f1d62868`. File reads at `2ad8d639dd~1`, `2ad8d639dd`, `b5f861c645~1`, `b5f861c645`, `4ecdd5ef3d` and `aad66d9d1~1` for `engine.py`, `workflow_factory.py`, `main.py` and `web/app.py`. Pickaxe (`git log -S`) for `def create_workflow_from_intent`, `TaskType.ANALYZE_FILE`, `_create_github_issue`, `web_proxy_url`, the "Replaces proxy" docstring and "summary of". `git grep` of today's tree for each removed route.
- Issues read: #172, #1158, #1187, #1624 (titles and states for #290 and #1659).
- **Static reading only.** No 2025 build was run. "Failed from 08-22" is what the code says: a missing method, then unhandled task types. It was not observed on a running server. How long the July path worked before 08-22 (between about 07-13 and 08-22) is unverified.
