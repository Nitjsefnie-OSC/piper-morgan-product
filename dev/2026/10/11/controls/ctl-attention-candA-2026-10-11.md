# Router ×6 control — candidate A (attention_query: NOT a plain list of my tasks or today's tasks)

Run 2026-10-11 14:04Z · 6 sample(s) per phrase · 42 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (42/42)

| phrase | routes (count) | confidence range |
|---|---|---|
| show today's tasks | `list_todos_query` ×6 | 0.95–0.95 |
| list today's tasks | `list_todos_query` ×6 | 0.95–0.95 |
| what needs my attention? | `attention_query` ×6 | 0.99–0.99 |
| what should I focus on today? | `attention_query` ×6 | 0.92–0.92 |
| where should my focus be today | `get_top_priority` ×6 | 0.95–0.95 |
| this project needs my attention today | `NONE` ×6 | 0.95–0.95 |
| what am I working on? | `session_activity_query` ×6 | 0.70–0.70 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| show today's tasks | 1 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 2 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 3 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 4 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 5 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show today's tasks | 6 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 1 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 2 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 3 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 4 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 5 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list today's tasks | 6 | `list_todos_query` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 1 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 2 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 3 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 4 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 5 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what needs my attention? | 6 | `attention_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 1 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 2 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 3 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 4 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 5 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| what should I focus on today? | 6 | `attention_query` | 0.92 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 1 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 2 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 3 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 4 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 5 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| where should my focus be today | 6 | `get_top_priority` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| this project needs my attention today | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 1 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 2 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 3 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 4 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 5 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
| what am I working on? | 6 | `session_activity_query` | 0.7 | anthropic:claude-haiku-4-5 |  |
