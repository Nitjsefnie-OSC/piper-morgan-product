# Router ×3 control — list-phrasings

Run 2026-10-14 17:45Z · 3 sample(s) per phrase · 12 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (12/12)

| phrase | routes (count) | confidence range |
|---|---|---|
| what reminders do I have? | `list_reminders_query` ×3 | 0.99–0.99 |
| show my todos | `list_todos_query` ×3 | 0.99–0.99 |
| delete the first two reminders | `delete_todo` ×3 | 0.95–0.95 |
| mark the first two complete | `complete_todo` ×3 | 0.95–0.95 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| what reminders do I have? | 1 | `list_reminders_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what reminders do I have? | 2 | `list_reminders_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| what reminders do I have? | 3 | `list_reminders_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| show my todos | 1 | `list_todos_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| show my todos | 2 | `list_todos_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| show my todos | 3 | `list_todos_query` | 0.99 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 1 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 2 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| delete the first two reminders | 3 | `delete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 1 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 2 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| mark the first two complete | 3 | `complete_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
