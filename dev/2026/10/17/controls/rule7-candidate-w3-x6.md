# Router ×6 control — candidate-w3

Run 2026-10-17 17:00Z · 6 sample(s) per phrase · 150 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (150/150)

| phrase | routes (count) | confidence range |
|---|---|---|
| what issues are assigned to me? | `NONE` ×6 | 0.95–0.95 |
| Add a project called Baz with description testing the description | `add_project` ×6 | 0.99–0.99 |
| add a project called Baz | `add_project` ×6 | 0.99–0.99 |
| list my projects | `list_projects` ×6 | 0.95–0.95 |
| add octocat/hello-world to the project | `CLARIFY` ×6 | 0.40–0.40 |
| I'd like to start a new project | `add_project` ×6 | 0.95–0.95 |
| How do I setup my projects? | `get_contextual_guidance` ×6 | 0.95–0.95 |
| add a todo to web test one | `create_todo` ×6 | 0.95–0.95 |
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
| clear the first two reminders | `clear_todos` ×6 | 0.95–0.95 |
| take care of the last reminder | `clear_todos` ×6 | 0.92–0.95 |
| clear all my reminders except the first one | `clear_todos` ×6 | 0.95–0.95 |
| My default repo should be mediajunkie/piper-morgan-product. | `set_default_repo` ×6 | 0.99–0.99 |
| Can we just mark done here? | `CLARIFY` ×6 | 0.40–0.40 |
| let's analyze the risk here | `analyze_blockers` ×6 | 0.95–0.95 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| what issues are assigned to me? | 1 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what issues are assigned to me? | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what issues are assigned to me? | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what issues are assigned to me? | 4 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what issues are assigned to me? | 5 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| what issues are assigned to me? | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 1 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 2 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 3 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 4 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 5 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Add a project called Baz with description testing the description | 6 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 1 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 2 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 3 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 4 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 5 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| add a project called Baz | 6 | `add_project` | 0.99 | anthropic:claude-haiku-4-5 |  |
| list my projects | 1 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list my projects | 2 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list my projects | 3 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list my projects | 4 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list my projects | 5 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| list my projects | 6 | `list_projects` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| add octocat/hello-world to the project | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 1 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 2 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 3 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 4 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 5 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| I'd like to start a new project | 6 | `add_project` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 1 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 2 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 3 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 4 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 5 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| How do I setup my projects? | 6 | `get_contextual_guidance` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 1 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 2 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 3 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 4 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 5 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
| add a todo to web test one | 6 | `create_todo` | 0.95 | anthropic:claude-haiku-4-5 |  |
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
| clear the first two reminders | 1 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear the first two reminders | 2 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear the first two reminders | 3 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear the first two reminders | 4 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear the first two reminders | 5 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear the first two reminders | 6 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 1 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 2 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 3 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 4 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 5 | `clear_todos` | 0.92 | anthropic:claude-haiku-4-5 |  |
| take care of the last reminder | 6 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 1 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 2 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 3 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 4 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 5 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| clear all my reminders except the first one | 6 | `clear_todos` | 0.95 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 1 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 2 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 3 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 4 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 5 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| My default repo should be mediajunkie/piper-morgan-product. | 6 | `set_default_repo` | 0.99 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Can we just mark done here? | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 1 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 2 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 3 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 4 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 5 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
| let's analyze the risk here | 6 | `analyze_blockers` | 0.95 | anthropic:claude-haiku-4-5 |  |
