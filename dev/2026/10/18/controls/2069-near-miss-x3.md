# Router ×3 control — 2069-near-miss

Run 2026-10-18 14:25Z · 3 sample(s) per phrase · 9 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (9/9)

| phrase | routes (count) | confidence range |
|---|---|---|
| create a project plan for the launch | `get_contextual_guidance` ×3 | 0.72–0.75 |
| add a task to the Piper Morgan project | `CLARIFY` ×2, `create_todo` ×1 | 0.40–0.85 |
| what would it take to start a new project? | `get_contextual_guidance` ×3 | 0.95–0.95 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| create a project plan for the launch | 1 | `get_contextual_guidance` | 0.75 | anthropic:claude-haiku-4-5 |  |
| create a project plan for the launch | 2 | `get_contextual_guidance` | 0.75 | anthropic:claude-haiku-4-5 |  |
| create a project plan for the launch | 3 | `get_contextual_guidance` | 0.72 | anthropic:claude-haiku-4-5 |  |
| add a task to the Piper Morgan project | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add a task to the Piper Morgan project | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add a task to the Piper Morgan project | 3 | `create_todo` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what would it take to start a new project? | 1 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what would it take to start a new project? | 2 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what would it take to start a new project? | 3 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
