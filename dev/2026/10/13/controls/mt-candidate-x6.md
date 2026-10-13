# Router ×6 control — mt-candidate

Run 2026-10-13 14:43Z · 6 sample(s) per phrase · 144 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (144/144)

| phrase | routes (count) | confidence range |
|---|---|---|
| when am i in a meeting | `meeting_time` ×6 | 0.95–0.95 |
| when is my team meeting | `meeting_time` ×6 | 0.85–0.85 |
| when is my next meeting? | `meeting_time` ×6 | 0.95–0.95 |
| meeting check for today | `meeting_time` ×6 | 0.95–0.95 |
| when's the next event | `meeting_time` ×6 | 0.95–0.95 |
| what's my agenda today | `meeting_time` ×6 | 0.95–0.95 |
| do i have any meetings | `meeting_time` ×6 | 0.95–0.95 |
| how much time in meetings do I have | `meeting_time` ×6 | 0.95–0.95 |
| what meetings are coming up | `meeting_time` ×6 | 0.95–0.95 |
| what's my agenda this week | `week_calendar` ×6 | 0.95–0.95 |
| show me my week | `week_calendar` ×6 | 0.95–0.95 |
| how many meetings this week | `week_calendar` ×6 | 0.95–0.95 |
| show the team calendar | `NONE` ×6 | 0.95–0.95 |
| is there a conflict on my calendar | `NONE` ×6 | 0.95–0.95 |
| find some time for a sync | `NONE` ×6 | 0.85–0.85 |
| let's analyze the risk here | `analyze_blockers` ×6 | 0.72–0.72 |
| add octocat/hello-world to the project | `link_repo` ×6 | 0.85–0.85 |
| show priorities for this sprint | `prioritize` ×6 | 0.85–0.85 |
| tasks I'm actively working on | `session_activity_query` ×4, `list_todos_query` ×2 | 0.72–0.85 |
| remind me to send the invoice on Friday | `create_reminder` ×6 | 0.95–0.95 |
| delete a reminder | `CLARIFY` ×6 | 0.50–0.60 |
| mark the first two complete | `complete_todo` ×6 | 0.95–0.95 |
| what needs my attention? | `attention_query` ×6 | 0.99–0.99 |
| add a todo to web test one | `create_todo` ×6 | 0.95–0.95 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| when am i in a meeting | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 1 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 2 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 3 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 4 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 5 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my team meeting | 6 | `meeting_time` | 0.85 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when is my next meeting? | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| meeting check for today | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when's the next event | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda today | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| do i have any meetings | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how much time in meetings do I have | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 1 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 2 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 3 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 4 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 5 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's my agenda this week | 6 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 1 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 2 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 3 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 4 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 5 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show me my week | 6 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 1 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 2 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 3 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 4 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 5 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| how many meetings this week | 6 | `week_calendar` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| is there a conflict on my calendar | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 1 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 2 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 3 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 4 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 5 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| find some time for a sync | 6 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 1 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 1 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 2 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 3 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 4 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 5 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 6 | `link_repo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 1 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 2 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 3 | `list_todos_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 4 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 5 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| tasks I'm actively working on | 6 | `session_activity_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 1 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 2 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 3 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 4 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 5 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| remind me to send the invoice on Friday | 6 | `create_reminder` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 2 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 3 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 4 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 5 | `CLARIFY` | 0.5 | anthropic:claude-haiku-4-5 |  |
| delete a reminder | 6 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 1 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 2 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 3 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 4 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 5 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 6 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 1 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 2 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 3 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 4 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 5 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 6 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 1 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 2 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 3 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 4 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 5 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 6 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
