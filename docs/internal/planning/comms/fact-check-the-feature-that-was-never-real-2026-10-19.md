# Fact-check: "The Feature That Was Never Real" (Tue 10-20), history of document summarization

Comms, 2026-10-19 09:28 PT, at xian's request. The research was done by an Opus subagent using read-only git and gh on both repos. Comms spot-checked the July 2025 evidence, `aad66d9d1` and `8b2997849b:main.py`.

## Bottom line
- **The POC** (`mediajunkie/piper-morgan-poc`, Streamlit + LangChain + Claude + Chroma) took uploaded documents (PDF, DOCX, TXT, MD) and answered questions from them with an LLM. The code for the upload-era 0.1 build isn't preserved. The repo has 2 README-only commits (05-29/30). The archived 0.1.1 (`c8c470a89e`, `archive/piper-morgan-0.1.1/`) is a rebuild with RAG Q&A and no summarize command. Its log asks to "Rebuild file upload … from earlier versions of the prototype (0.1)". The tech spec shows a sidebar uploader.
- **This repo did have working chat summarization, in July 2025.** It was rough, and then it was lost. The investigation the post relies on (`docs/internal/operations/summarize-intent-forensics-2026-08-15.md`) jumps from 2025-06-23 to 2025-10-01 and never traced the July path.
  - `41a553bd01` (2025-06-01) is a fresh bootstrap. Summarizing appears only as an enum comment, and intent handling is a stub. **The June 1 commit didn't introduce the feature.**
  - `68055f3e04` (06-25) "DocumentAnalyzer with LLM integration". `d9378c43e8` (07-09) adds summarize routing and prompts.
  - Mid-July (`8b2997849b`): chat → ANALYZE_FILE workflow → `DocumentAnalyzer` → a real LLM call. `main.py:525-533` returns "Here's my summary of {filename}:" plus the summary.
  - It ran: the 07-06 post says "The feature had even worked in previous sessions". The 07-07 omnibus says "Summary generated and stored in database". The 07-08 post says summaries looked "like markdown had a fight with Unicode", so they reached the screen with bad formatting. The 07-09 log calls it "unusable" because of the formatting, and a JSON-mode fix followed. The 07-12 post: "the UI could find the summary".
  - `aad66d9d1` (2025-10-01), labelled "docs:", cut `main.py` from 1184 lines to about 109 and removed that chat path. After that, the REST handler (#290, 2025-11-01) shipped with no chat dispatch.

## Draft claims
| Claim | Verdict |
|---|---|
| Never worked "since the literal first commit … June 1st of 2025" | **WRONG.** It worked, roughly, in July 2025. June 1 didn't introduce it. |
| "Fifteen months old and had never functioned end to end" | **WRONG**, same reason. |
| About five months of "I'll help you create that" over a placeholder | **OVERSTATED.** The string ran about 4 months (06-03 to 10-01) as a fallback for requests that created no workflow. Uploaded-file summarizing went down the workflow path. |
| Handler shipped dark, chat dispatch only in a guidance doc | SUPPORTED (#290, `2452ba9ae`) |
| A docs-labelled commit gutted the wiring | SUPPORTED. It removed the July path that had worked. |
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
- How long the July path kept working before 10-01.
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
- **Net for the post:** the prototype answered questions about uploaded documents with an LLM. This codebase then had chat summarization working, roughly, in July 2025, and lost it on 2025-10-01. "Never" is the bounded-search-reported-as-a-total pattern (xian, 10-19).
