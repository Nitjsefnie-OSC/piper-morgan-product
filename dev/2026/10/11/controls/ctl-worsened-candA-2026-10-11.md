# Router ×6 control — candidate A — 7 worsened rows

Run 2026-10-11 14:17Z · 6 sample(s) per phrase · 42 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (42/42)

| phrase | routes (count) | confidence range |
|---|---|---|
| let's analyze the risk here | `CLARIFY` ×6 | 0.40–0.40 |
| add octocat/hello-world to the project | `link_repo` ×5, `CLARIFY` ×1 | 0.40–0.85 |
| show priorities for this sprint | `prioritize` ×6 | 0.85–0.85 |
| what do I have next to do | `list_todos_query` ×6 | 0.95–0.95 |
| when's the milestone deadline | `CLARIFY` ×4, `list_milestones` ×2 | 0.40–0.75 |
| I need to remember to submit my timesheet | `create_reminder` ×5, `create_todo` ×1 | 0.95–0.95 |
| when am i in a meeting | `CLARIFY` ×6 | 0.50–0.60 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| let's analyze the risk here | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 1 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 2 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 3 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 4 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 5 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 1 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 2 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 3 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 4 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 5 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what do I have next to do | 6 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 4 | `list_milestones` | 0.75 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 5 | `list_milestones` | 0.75 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 1 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 2 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 3 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 4 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 5 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I need to remember to submit my timesheet | 6 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 2 | `CLARIFY` | 0.5 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 3 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 4 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 5 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 6 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
