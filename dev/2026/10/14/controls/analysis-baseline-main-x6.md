# Router ×6 control — analysis-baseline-main

Run 2026-10-14 19:26Z · 6 sample(s) per phrase · 66 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (66/66)

| phrase | routes (count) | confidence range |
|---|---|---|
| let's analyze the risk here | `analyze_blockers` ×3, `CLARIFY` ×3 | 0.40–0.72 |
| analyze the file I uploaded | `analyze_document` ×6 | 0.95–0.95 |
| what's the main obstacle here | `CLARIFY` ×6 | 0.40–0.40 |
| what is blocking this release | `analyze_blockers` ×6 | 0.92–0.92 |
| I'd like a risk assessment for this project | `analyze_blockers` ×6 | 0.72–0.72 |
| what's in the way of finishing this | `CLARIFY` ×6 | 0.40–0.40 |
| when am i in a meeting | `meeting_time` ×6 | 0.95–0.95 |
| show today's tasks | `attention_query` ×6 | 0.85–0.85 |
| clear my reminders | `clear_todos` ×6 | 0.92–0.92 |
| what am I working on? | `session_activity_query` ×6 | 0.70–0.70 |
| analyze the impact of this change | `CLARIFY` ×6 | 0.40–0.40 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| let's analyze the risk here | 1 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 1 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 2 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 3 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 4 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 5 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 6 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's the main obstacle here | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 1 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 2 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 3 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 4 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 5 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what is blocking this release | 6 | `analyze_blockers` | 0.92 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 1 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 2 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 3 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 4 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 5 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| I'd like a risk assessment for this project | 6 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| what's in the way of finishing this | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 1 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 2 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 3 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 4 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 5 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| when am i in a meeting | 6 | `meeting_time` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 1 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 2 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 3 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 4 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 5 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 6 | `attention_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 1 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 2 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 3 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 4 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 5 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 6 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 1 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 2 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 3 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 4 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 5 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 6 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| analyze the impact of this change | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
