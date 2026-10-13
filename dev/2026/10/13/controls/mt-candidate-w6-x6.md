# Router ×6 control — mt-candidate-w6-compound-example

Run 2026-10-13 15:08Z · 6 sample(s) per phrase · 48 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (48/48)

| phrase | routes (count) | confidence range |
|---|---|---|
| when am i in a meeting | `meeting_time` ×6 | 0.95–0.95 |
| what meetings do i have | `meeting_time` ×6 | 0.85–0.85 |
| how much time in meetings do I have | `meeting_time` ×6 | 0.95–0.95 |
| what meetings are coming up | `week_calendar` ×6 | 0.85–0.92 |
| do i have any meetings | `meeting_time` ×6 | 0.92–0.95 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.72–0.75 |
| when's the milestone deadline | `CLARIFY` ×6 | 0.40–0.60 |
| let's analyze the risk here | `analyze_blockers` ×5, `CLARIFY` ×1 | 0.40–0.72 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| when am i in a meeting | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 1 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 2 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 3 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 4 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 5 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings do i have | 6 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 1 | `week_calendar` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 2 | `week_calendar` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 3 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 4 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 5 | `week_calendar` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 6 | `week_calendar` | 0.92 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 2 | `meeting_time` | 0.92 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 3 | `meeting_time` | 0.92 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 4 | `meeting_time` | 0.92 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 5 | `meeting_time` | 0.92 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 6 | `meeting_time` | 0.92 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 6 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 2 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 3 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 4 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 5 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| when's the milestone deadline | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 1 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
