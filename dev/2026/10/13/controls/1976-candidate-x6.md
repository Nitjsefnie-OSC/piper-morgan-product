# Router ×6 control — candidate-1976

Run 2026-10-13 14:13Z · 6 sample(s) per phrase · 72 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (72/72)

| phrase | routes (count) | confidence range |
|---|---|---|
| add a todo to web test one | `create_todo` ×6 | 0.99–0.99 |
| add a todo to call the dentist | `create_todo` ×6 | 0.99–0.99 |
| add todo: buy milk | `create_todo` ×6 | 0.99–0.99 |
| create a new todo - water the plants | `create_todo` ×6 | 0.99–0.99 |
| add todo buy oat milk | `create_todo` ×6 | 0.99–0.99 |
| remind me to send the invoice on Friday | `create_reminder` ×6 | 0.95–0.95 |
| delete a reminder | `CLARIFY` ×6 | 0.60–0.60 |
| mark the first two complete | `complete_todo` ×6 | 0.95–0.95 |
| what needs my attention? | `attention_query` ×6 | 0.99–0.99 |
| show the team calendar | `NONE` ×6 | 0.95–0.95 |
| add a project called Atlas | `add_project` ×6 | 0.99–0.99 |
| create an issue about the login bug | `create_issue` ×6 | 0.85–0.85 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| add a todo to web test one | 1 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 2 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 3 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 4 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 5 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 6 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 1 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 2 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 3 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 4 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 5 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a todo to call the dentist | 6 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 1 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 2 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 3 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 4 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 5 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo: buy milk | 6 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 1 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 2 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 3 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 4 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 5 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create a new todo - water the plants | 6 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 1 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 2 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 3 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 4 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 5 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add todo buy oat milk | 6 | `create_todo` | 0.99 | anthropic:claude-haiku-4-5 |  |
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
| delete a reminder | 5 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
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
| show the team calendar | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| show the team calendar | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 1 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 2 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 3 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 4 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 5 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Atlas | 6 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 1 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 2 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 3 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 4 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 5 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
| create an issue about the login bug | 6 | `create_issue` | 0.85 | anthropic:claude-haiku-4-5 |  |
