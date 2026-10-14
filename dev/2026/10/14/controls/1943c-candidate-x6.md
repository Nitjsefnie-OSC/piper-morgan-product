# Router ×6 control — 1943c-candidate

Run 2026-10-14 19:07Z · 6 sample(s) per phrase · 66 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (66/66)

| phrase | routes (count) | confidence range |
|---|---|---|
| clear my reminders | `clear_todos` ×6 | 0.95–0.95 |
| handle these | `CLARIFY` ×6 | 0.20–0.20 |
| reset my todos | `clear_todos` ×6 | 0.95–0.95 |
| clear all my todos except the first one | `clear_todos` ×6 | 0.99–0.99 |
| take care of my reminders | `clear_todos` ×6 | 0.92–0.92 |
| clear my calendar for tomorrow | `NONE` ×6 | 0.95–0.95 |
| mark the first two complete | `complete_todo` ×6 | 0.95–0.95 |
| delete the first two reminders | `delete_todo` ×6 | 0.95–0.95 |
| let's analyze the risk here | `CLARIFY` ×5, `analyze_blockers` ×1 | 0.40–0.72 |
| when am i in a meeting | `meeting_time` ×6 | 0.95–0.95 |
| show today's tasks | `attention_query` ×6 | 0.85–0.85 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| clear my reminders | 1 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 2 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 3 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 4 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 5 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my reminders | 6 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| handle these | 1 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| handle these | 2 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| handle these | 3 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| handle these | 4 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| handle these | 5 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| handle these | 6 | `CLARIFY` | 0.2 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 1 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 2 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 3 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 4 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 5 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| reset my todos | 6 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 1 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 2 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 3 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 4 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 5 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| clear all my todos except the first one | 6 | `clear_todos` | 0.99 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 1 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 2 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 3 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 4 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 5 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of my reminders | 6 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear my calendar for tomorrow | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 1 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 2 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 3 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 4 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 5 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 6 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 1 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 2 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 3 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 4 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 5 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 6 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `analyze_blockers` | 0.72 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
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
