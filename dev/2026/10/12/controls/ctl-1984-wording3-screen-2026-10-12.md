# Router ×6 control — 1984-wording3-screen

Run 2026-10-12 14:08Z · 6 sample(s) per phrase · 66 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (66/66)

| phrase | routes (count) | confidence range |
|---|---|---|
| let's analyze the risk here | `analyze_blockers` ×4, `CLARIFY` ×2 | 0.40–0.72 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.75–0.75 |
| tasks I'm actively working on | `session_activity_query` ×3, `attention_query` ×3 | 0.70–0.72 |
| what projects am I working on | `list_projects` ×6 | 0.95–0.95 |
| show priorities for this sprint | `prioritize` ×6 | 0.85–0.85 |
| summarize my current work | `get_project_status` ×6 | 0.92–0.92 |
| summarize my current work and I need the archived list too | `PLAN[get_project_status→list_archived_projects]` ×6 | - |
| what am I working on? | `session_activity_query` ×6 | 0.70–0.70 |
| tell me what I'm working on | `get_project_status` ×6 | 0.95–0.95 |
| what did we create this session | `session_activity_query` ×6 | 0.95–0.95 |
| summarize the document I uploaded | `summarize_document` ×6 | 0.99–0.99 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| let's analyze the risk here | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 6 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 1 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 2 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 3 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 4 | `attention_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 5 | `attention_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 6 | `attention_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 1 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 2 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 3 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 4 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 5 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 6 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 1 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 2 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 3 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 4 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 5 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 6 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 1 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 2 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 3 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 4 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 5 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 6 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 1 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 2 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 3 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 4 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 5 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 6 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 1 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 2 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 3 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 4 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 5 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| tell me what I'm working on | 6 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 1 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 2 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 3 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 4 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 5 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 6 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 1 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 2 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 3 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 4 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 5 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
| summarize the document I uploaded | 6 | `summarize_document` | 0.99 | anthropic:claude-haiku-4-5 |  |
