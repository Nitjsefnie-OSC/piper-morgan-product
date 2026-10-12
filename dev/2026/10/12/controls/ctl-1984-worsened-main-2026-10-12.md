# Router ×6 control — 1984-worsened-main

Run 2026-10-12 14:04Z · 6 sample(s) per phrase · 48 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (48/48)

| phrase | routes (count) | confidence range |
|---|---|---|
| let's analyze the risk here | `analyze_blockers` ×6 | 0.72–0.72 |
| show priorities for this sprint | `get_top_priority` ×3, `prioritize` ×3 | 0.85–0.85 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.75–0.85 |
| tasks I'm actively working on | `list_todos_query` ×5, `session_activity_query` ×1 | 0.72–0.85 |
| what projects am I working on | `list_projects` ×6 | 0.95–0.95 |
| what's the current status | `get_project_status` ×4, `CLARIFY` ×2 | 0.40–0.85 |
| I need to remember to submit my timesheet | `create_reminder` ×4, `create_todo` ×2 | 0.95–0.95 |
| when am i in a meeting | `CLARIFY` ×6 | 0.60–0.60 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| let's analyze the risk here | 1 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 6 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 1 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 2 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 3 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 4 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 5 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 6 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 1 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 2 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 3 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 4 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 5 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what projects am I working on | 6 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 1 | `get_project_status` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 3 | `get_project_status` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 4 | `get_project_status` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the current status | 6 | `get_project_status` | 0.85 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 1 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 2 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 3 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 4 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 5 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 6 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 2 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 3 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 4 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 5 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 6 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
