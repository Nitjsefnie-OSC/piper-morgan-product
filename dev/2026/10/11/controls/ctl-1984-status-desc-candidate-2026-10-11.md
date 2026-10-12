# Router ×5 control — 1984-status-desc-candidate

Run 2026-10-12 03:11Z · 5 sample(s) per phrase · 20 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (20/20)

| phrase | routes (count) | confidence range |
|---|---|---|
| summarize my current work | `get_project_status` ×5 | 0.92–0.92 |
| summarize my current work and I need the archived list too | `PLAN[get_project_status→list_archived_projects]` ×5 | - |
| how is my work going | `get_project_status` ×5 | 0.95–0.95 |
| what did we create this session | `session_activity_query` ×5 | 0.95–0.95 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| summarize my current work | 1 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 2 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 3 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 4 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work | 5 | `get_project_status` | 0.92 | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 1 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 2 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 3 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 4 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| summarize my current work and I need the archived list too | 5 | `PLAN[get_project_status→list_archived_projects]` | None | anthropic:claude-haiku-4-5 |  |
| how is my work going | 1 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how is my work going | 2 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how is my work going | 3 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how is my work going | 4 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how is my work going | 5 | `get_project_status` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 1 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 2 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 3 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 4 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what did we create this session | 5 | `session_activity_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
