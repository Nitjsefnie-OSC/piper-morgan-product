# Fact-check: "The Feature That Was Never Real" (Tue 10-20), history of document summarization

Comms, 2026-10-19 09:28 PT, at xian's request. The research was done by an Opus subagent using read-only git and gh on both repos. Comms spot-checked the July 2025 evidence, `aad66d9d1` and `8b2997849b:main.py`.

## Bottom line
- **The POC** (`mediajunkie/piper-morgan-poc`, Streamlit + LangChain + Claude + Chroma) took uploaded documents (PDF, DOCX, TXT, MD) and answered questions from them with an LLM. The code for the upload-era 0.1 build isn't preserved. The repo has 2 README-only commits (05-29/30). The archived 0.1.1 (`c8c470a89e`, `archive/piper-morgan-0.1.1/`) is a rebuild with RAG Q&A and no summarize command. Its log asks to "Rebuild file upload … from earlier versions of the prototype (0.1)". The tech spec shows a sidebar uploader.
- **This repo did have working chat summarization, in July 2025.** It was rough, and then it was lost. The investigation the post relies on (`docs/internal/operations/summarize-intent-forensics-2026-08-15.md`) jumps from 2025-06-23 to 2025-10-01 and never traced the July path.
  - `41a553bd01` (2025-06-01) is a fresh bootstrap. Summarizing appears only as an enum comment, and intent handling is a stub. **The June 1 commit didn't introduce the feature.**
  - `68055f3e04` (06-25) "DocumentAnalyzer with LLM integration". `d9378c43e8` (07-09) adds summarize routing and prompts.
  - Mid-July (`8b2997849b`): chat → ANALYZE_FILE workflow → `DocumentAnalyzer` → a real LLM call. `main.py:525-533` returns "Here's my summary of {filename}:" plus the summary.
  - It ran: the 07-06 post says "The feature had even worked in previous sessions". The 07-07 omnibus says "Summary generated and stored in database". The 07-08 post says summaries looked "like markdown had a fight with Unicode", so they reached the screen with bad formatting. The 07-09 log calls it "unusable" because of the formatting, and a JSON-mode fix followed. The 07-12 post: "the UI could find the summary".
  - **Corrected per Arch 10-19:** the chat path broke on **2025-08-22**. `2ad8d639dd` ("feat: add comprehensive multi-agent system and morning standup MVP") replaced `engine.py` (1,326 lines) with a 345-line engine that had no handler for file analysis, summarize and six other task types, and dropped `create_workflow_from_intent`. On 09-17 and 09-23 (#172, #186) the browser stopped talking to `main.py`. **`effa5fe2a6`** (2025-10-01, "docs:", the on-main sha; `aad66d9d1` is the same commit off main) then cut `main.py` from 1184 lines to about 109. Three days later `a47eaf9ea8` ("docs:") deleted `main.py.backup`. The REST handler (#290, 2025-11-01) shipped with no chat dispatch.

## Draft claims
| Claim | Verdict |
|---|---|
| Never worked "since the literal first commit … June 1st of 2025" | **WRONG.** It worked, roughly, in July 2025. June 1 didn't introduce it. |
| "Fifteen months old and had never functioned end to end" | **WRONG**, same reason. |
| About five months of "I'll help you create that" over a placeholder | **OVERSTATED.** The string ran about 4 months (06-03 to 10-01) as a fallback for requests that created no workflow. Uploaded-file summarizing went down the workflow path. |
| Handler shipped dark, chat dispatch only in a guidance doc | SUPPORTED (#290, `2452ba9ae`) |
| A docs-labelled commit gutted the wiring | **PARTLY (Arch 10-19).** The 10-01 docs commit removed the old chat wiring, but that path had already been broken since 2025-08-22, by an engine swap inside a feat commit. |
| Working REST endpoint "the whole time" | **OVERSTATED.** It has existed since 2025-11-01. Non-PDF uploads also failed (#1659). |
| Two decisions chose the floor, the branch was deferred, the issue closed with no successor | SUPPORTED (#1158, #1187) |
| A cleanup a couple of weeks earlier dropped "document" | SUPPORTED (08-02), but it re-landed a prompt and deleted an orphaned file, not records |
| The Inversion surfaced it | SUPPORTED |
| "Lead's investigation called it acknowledgment theater" | **MISATTRIBUTED.** The Coding Agent wrote the report, Lead dispatched it and quoted the phrase. |
| Approved "deleting the dead vocabulary" and wiring chat to REST | **WRONG on the vocabulary.** What was built *restored* it (decisions.log:1697). |
| A fourth, larger option deferred | PARTLY. Deferred to Production, but estimated at about a day more than C, so not larger. |
| "The repair itself took an evening" | **OVERSTATED.** Merged the next morning, failed live 08-18. #1624 is still OPEN. |
| Saturday fresh-deploy test, flagged as a regression | Mostly supported (08-15 was a Saturday, baseline tested on v52) |

## Not verified
- What the 0.1 POC did with an upload: its code isn't preserved in either repo.
- Whether any July 2025 summary displayed cleanly after the JSON fix.
- ~~How long the July path kept working~~: until 2025-08-22 (Arch's static reading, no 2025 build run).
- Whether chat summarization works today: #1624 is open, though #1729 (closed 09-08) shows summaries rendering.

## Also wrong in the 08-15 forensics doc (internal record)
- It says the OrchestrationEngine was "never the live chat path", but in mid-2025 `main.py` ran `engine.execute_workflow` for every chat workflow.
- It says the "Here's my summary of {filename}:" template "never fired", but the 2025-07-13 omnibus shows it firing.

## Addendum 09:50: the POC code IS kept (xian was right), in this repo's history
- `c8c470a89e` (2025-06-09, "archiving poc and prototype") added `archive/piper-morgan-0.1.1/` (Streamlit app: `chat_interface.py`, `claude_client.py`, `knowledge_base.py`, `llm_adapter.py`, github agent/reviewer, Chroma stores, the 05-30/31 Claude and Gemini docs) and `archive/piper-morgan-1.0/piper-morgan-b0rked/` (a second copy), plus `archive/app_with_clarifying.py` and `app_with_feedback.py`.
- More POC commits followed in this repo: `946a0657c8` (06-14) "Restore file upload functionality with context assignment … Document processing now works with metadata", `dd2c8fbf0e` (06-14), `5d366cc781` (06-15) "demo safe version of the prototype", `b1843e5ae7` (07-02) "cleaned up prototype demo".
- `492c357aaa` (2026-01-22) removed `archive/` from tracking "for lighter clones". It's still fully in history (read it at `88ce2f7bc6`). Nothing is on Amber's disk (find, depth 6). PM's Mac wasn't checked.
- **What the archived POC does with a document:** `chat_interface.py` (at 88ce2f7bc6) has a sidebar `st.file_uploader("Upload Document", type=pdf/docx/txt/md)` → "Add to Knowledge Base" with a context level → Chroma. Chat ("How can I help you with a GitHub issue?") draws on that knowledge base through RAG. There's no dedicated summarize command (grep "summar" = 0 across all archived .py). In the archived 0.1.1, only .txt/.md content is stored, and PDF/DOCX store just "Document: {name}".
- **Your own account at the time:** `superseded/pre-convention-2025/working-prototype.md:57`: "I asked the system a question about an uploaded doc and, it did OK." `rag-revelation.md:81`: "PMs could upload their actual documents".
- **Still not found:** the POC's own pre-05-29 commit history (the GitHub poc repo has only 2 README commits). The 0.1.1 log asks to "rebuild file upload … from earlier versions (0.1)", so 0.1's own repo may be on xian's Mac.
- **Net for the post:** the prototype answered questions about uploaded documents with an LLM. This codebase then had chat summarization working, roughly, in July 2025. It broke on 2025-08-22 in a commit about something else, and the evidence was deleted under "docs" labels on 10-01 and 10-04 (Arch). "Never" is the bounded-search-reported-as-a-total pattern (xian, 10-19).

## Correction 10:13 (Arch's audit, `docs/internal/architecture/audits/lost-working-code-2025-08-to-10.md`)
The loss date was 2025-08-22 (`2ad8d639dd`), not the 10-01 docs commit. The 10-01 commit (`effa5fe2a6` on main) removed a `main.py` the UI no longer reached. Arch's sweep of 36,177 commits found no other unexplained loss of live behaviour. In every real loss, one commit did two things under one label.

## Full-draft ledger, 2026-10-20 (every claim in the 10-20 rewrite, checked against primary sources)

xian, 10-20: "please use that same rigor with the draft. read it through for sense." The 10-20 draft is a rewrite whose backbone is the record, not the 08-15 investigation. Each claim, with its source:

| Claim in the draft | Source read 10-20 | Verdict |
|---|---|---|
| Saturday fresh-deploy test, Piper said it couldn't, flagged as regression | 2026-08-15 is a Saturday (`date`); Lead 08-15 log "PM's baseline round… summarize regression"; forensics layer 6 (floor answers with no source content) | Holds. The exact reply is xian's account, no transcript found |
| Lead dispatched an investigating agent | Lead 08-15 log 12:2x | Holds |
| Report within the hour, "no regression" | dispatched ~12:2x, delivered ~13:0x, heading "not a regression" (Lead 08-15) | Holds |
| It said never worked since the June 2025 first commit | forensics §1; #1624 body | Holds as what it said |
| Every commit cited was real, Lead checked two claims | forensics footer; Lead 08-15 log line 80 | Holds |
| Summarizer built late 2025, API only, chat dispatch only in a guidance doc | forensics row 2025-11-01 (`2452ba9ae`, #290) | Holds |
| Two June 2026 decisions, floor route, document deferred, issue closed with no successor | forensics rows 06-08/09 (#1158) and 06-10/11 (#1187, closed 06-12) | Holds |
| Cleanup two weeks earlier dropped "document" from the classifier's vocabulary | forensics row 2026-08-02 (#1432) | Holds |
| The Inversion had no entry for summarizing a document | forensics row 08-14 (62 ops, zero "summar") | Holds. It didn't surface the failure (xian's test did), so the old "what finally surfaced it" line was cut |
| Approved that evening: wire chat to the API's summarizer and fix the vocabulary; the build put "document" back | decisions.log 08-15 22:2x (C+A, "delete the dead vocabulary"); Lead 08-16 log "vocab restored not invented" | Holds |
| A fourth option, about a day more, to a later milestone | decisions.log 08-15 (D deferred to Production) and the fact-check's estimate | Holds |
| Merged next morning | decisions.log 08-16 10:06 | Holds |
| Upload page failed on every attempt two days later | Lead 08-18 log; #1656 title | Holds |
| Early September: accurate summary in chat, bullets mashed into one line; fixed later in the month | #1729 body (PM live 09-08 ~05:14, "The summarization itself worked"); #1729 closed 09-23 with the cause | Holds. **The old "still isn't fixed" was false.** #1624 is open, but as a tracker |
| July 2025: Piper summarized uploaded files in chat | `8b2997849b:main.py` (ANALYZE_FILE result → "Here's my summary of…"); `workflow_factory.py` analyze_file mapping; omnibus 07-07, 07-12, 07-13 | Holds |
| One path said "couldn't generate a summary" when it had made one | omnibus 07-07 line 14, 07-12 ("misleading") | Holds |
| "like markdown had a fight with Unicode and everybody lost", in a post about that week | "Two-Fisted Coding", work 07-08, published 2025-08-01 (calendar) | Holds |
| Within days both were fixed: structured output, the app builds the formatting, the false failure gone | omnibus 07-09 (JSON mode, `DocumentSummary.to_markdown()`, 19 tests), 07-12 (SUMMARIZE result contract fixed); the Two-Fisted post (about 07-08) still says "remains unsolved" | Holds (revised 10-20 on xian's question). No July screenshot of a clean summary was found. Aside: the 09-2026 run-on bullets (#1729) came from code re-bulleting that same `to_markdown()` output |
| Broke 2025-08-22 in a commit about multi-agent and standup; smaller engine; no handler for file analyze/summarize or six others incl. GitHub issue creation | Arch audit §1; `2ad8d639dd` message | Holds |
| September bug diagnosed as a missing connection, fixed by routing around | #172 (closed 09-18), Arch audit §2 | Holds |
| Comment "broken in August 22 refactor", only the standup restored | `4ecdd5ef3d:web/app.py:715` | Holds |
| Placeholder "being restored in Phase 3", and it wasn't | `4ecdd5ef3d:web/app.py:821`; Arch audit (the eight handlers never returned) | Holds |
| Oct 1 "documentation" commit deleted code nothing reached | `effa5fe2a6`; Arch audit | Holds |
| Fall 2025 chat summarize: GitHub issues, commits, pasted text, not documents | `8a3a74ff2d:services/intent/intent_service.py` `_handle_summarize` (valid_sources) | Holds |
| The investigation's timeline jumped from late June to October 2025 | forensics table (06-23 → 10-01) | Holds |
| Arch's full sweep found no other loss like it | Arch audit §4 (36,177 commits) | Holds |

**Cut from the old draft because false:** "I'll help you create that" as what kept it invisible (in July 2025 a summarize request always started a workflow, so that string never answered it: `8b2997849b` `main.py` 333-360 and `workflow_factory.py` SYNTHESIS → GENERATE_REPORT); "acknowledgment theater"; "the Inversion surfaced it"; "still isn't fixed".
