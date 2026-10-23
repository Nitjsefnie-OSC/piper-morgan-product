# Router ×6 control — main

Run 2026-10-23 01:39Z · 6 sample(s) per phrase · 60 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (60/60)

| phrase | routes (count) | confidence range |
|---|---|---|
| modify the status document | `update_document` ×6 | 0.72–0.85 |
| show priorities for this sprint | `get_top_priority` ×6 | 0.85–0.85 |
| what's the most critical thing | `attention_query` ×3, `get_top_priority` ×3 | 0.85–0.92 |
| any old prs lying around | `stale_prs` ×6 | 0.95–0.95 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.72–0.75 |
| what did we make earlier | `session_activity_query` ×6 | 0.85–0.85 |
| what meetings are coming up | `week_calendar` ×6 | 0.85–0.92 |
| show today's assignments | `NONE` ×5, `attention_query` ×1 | 0.72–0.85 |
| what are my active projects | `list_projects` ×5, `manage_portfolio` ×1 | 0.95–0.95 |
| Analyze this document | `CLARIFY` ×6 | 0.40–0.40 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| modify the status document | 1 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 2 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 3 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 4 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 5 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 6 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `get_top_priority` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 1 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 2 | `get_top_priority` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 3 | `get_top_priority` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 4 | `get_top_priority` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 5 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what's the most critical thing | 6 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 1 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 2 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 3 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 4 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 5 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 6 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 6 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 1 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 2 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 3 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 4 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 5 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 6 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 1 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 2 | `week_calendar` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 3 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 4 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 5 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 6 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 1 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 2 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 3 | `attention_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 4 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 5 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's assignments | 6 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 1 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 2 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 3 | `manage_portfolio` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 4 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 5 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what are my active projects | 6 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
