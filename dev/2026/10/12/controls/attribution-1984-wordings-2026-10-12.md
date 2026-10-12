# #1984 half (2) — three wordings of the `get_project_status` description, screened ×6 — 2026-10-12 07:0x–07:1x PT

main's text: "Answer project status questions (how a project is going, status reports)".
W1 (40b3c95b33, full run + ×6, `attribution-1984-wording1-2026-10-12.md`): "Answer questions about the user's own current work and
project status: how a project is going, what they are working on, a summary of their current work, status reports. Not session
activity (what was created this session) and not an uploaded document."
W2 (screen only, `ctl-1984-wording2-screen-2026-10-12.md`): "Answer questions about the user's own project status and current work:
how a project is going, a summary of their current work, status reports. Not session activity (what was created this session)."
W3 (screen only, `ctl-1984-wording3-screen-2026-10-12.md`): W2 without the "Not session activity" sentence.

×6 on the candidate tree per wording; main ×6 from `ctl-1984-worsened-main-2026-10-12.md` (same minute as W1's).

| row | expected | main ×6 | W1 ×6 | W2 ×6 | W3 ×6 |
|---|---|---|---|---|---|
| summarize my current work and I need the archived list too (#1984 row) | PLAN[get_project_status→list_archived_projects] | session_activity_query→list_archived_projects (10-11, 5/5) | ruled plan ×6 | ruled plan ×6 | ruled plan ×6 |
| summarize my current work | get_project_status | get_project_status | ×6 | ×6 | ×6 |
| what am I working on? | floor (get_project_status) | session_activity_query (10-10 report) | get_project_status ×6 | get_project_status ×6 | **session_activity_query ×6** |
| tell me what I'm working on | floor | session_activity_query (10-10) | get_project_status ×6 | ×6 | ×6 |
| what projects am I working on | list_projects | list_projects ×6 | **get_project_status ×6** | list_projects ×6 | list_projects ×6 |
| tasks I'm actively working on | list_todos_query | list_todos_query ×5, session_activity ×1 | **session_activity_query ×6** | **session_activity_query ×6** | **session_activity ×3, attention_query ×3** |
| let's analyze the risk here | analyze_blockers | analyze_blockers ×6 | **CLARIFY ×6** | **CLARIFY ×6** | analyze_blockers ×4, CLARIFY ×2 |
| are we behind upstream at all | local_git_status_query | local_git_status_query ×6 | **analyze_commits ×5, CLARIFY ×1** | **analyze_commits ×6** | local_git_status_query ×6 |
| show priorities for this sprint | floor (get_top_priority) | get_top_priority ×3, prioritize ×3 | prioritize ×6 | get_top_priority ×4, prioritize ×2 | prioritize ×6 |
| what did we create this session | session_activity_query | ×6 | ×6 | ×6 | ×6 |
| summarize the document I uploaded | summarize_document | ×6 @0.99 | ×6 | ×6 | ×6 |

Read: every wording moves the #1984 row to the ruled plan and keeps the two sentinels; none is clean on the neighbours. The
"what they are working on" clause (W1 only) pulls the two list rows into status. The "Not session activity" sentence (W1, W2) is what
buys "what am I working on?" and is also what moves "tasks I'm actively working on" to session_activity_query and, less explicably,
"let's analyze the risk here" to CLARIFY and "are we behind upstream at all" to analyze_commits (both 6/6 on W1 and W2, back on W3).
Three wordings, no fourth (the 10-11 attention/todo finding: this neighbourhood moves under any edit on either side; screens are not
the measurement). Spend: 593 + 48 + 48 + 12 + 20 + 66 + 66 = 853 Haiku router calls today, plus 6 chat turns on the local server.
