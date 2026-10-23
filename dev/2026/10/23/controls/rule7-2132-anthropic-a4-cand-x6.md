# Router ×6 control — candidate

Run 2026-10-23 15:21Z · 6 sample(s) per phrase · 102 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (102/102)

| phrase | routes (count) | confidence range |
|---|---|---|
| Create issues from this meeting's action items | `decline_batch_issues_from_meeting` ×6 | 0.95–0.95 |
| Create issues for all the action items from today's meeting | `decline_batch_issues_from_meeting` ×6 | 0.95–0.95 |
| Turn the meeting notes into GitHub issues | `CLARIFY` ×6 | 0.40–0.45 |
| Make tickets for each action item from the standup | `CLARIFY` ×6 | 0.40–0.45 |
| Create an issue about the login bug | `create_issue` ×6 | 0.95–0.95 |
| Analyze this document | `CLARIFY` ×6 | 0.40–0.40 |
| What does this document say? | `CLARIFY` ×6 | 0.40–0.60 |
| Analyze the document called PRD Writing Guidelines | `analyze_document` ×6 | 0.92–0.95 |
| analyze the file I uploaded | `analyze_document` ×6 | 0.95–0.95 |
| Analyze launch-notes-2131.txt | `analyze_document` ×6 | 0.92–0.92 |
| Analyze our repo activity this week | `analyze_commits` ×6 | 0.85–0.85 |
| modify the status document | `CLARIFY` ×4, `update_document` ×2 | 0.40–0.85 |
| show priorities for this sprint | `prioritize` ×6 | 0.85–0.85 |
| any old prs lying around | `list_prs` ×6 | 0.92–0.92 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.72–0.72 |
| what did we make earlier | `session_activity_query` ×6 | 0.85–0.85 |
| what meetings are coming up | `week_calendar` ×6 | 0.85–0.85 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| Create issues from this meeting's action items | 1 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues from this meeting's action items | 2 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues from this meeting's action items | 3 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues from this meeting's action items | 4 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues from this meeting's action items | 5 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues from this meeting's action items | 6 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 1 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 2 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 3 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 4 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 5 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create issues for all the action items from today's meeting | 6 | `decline_batch_issues_from_meeting` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 1 | `CLARIFY` | 0.45 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 2 | `CLARIFY` | 0.45 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 4 | `CLARIFY` | 0.45 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Turn the meeting notes into GitHub issues | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Make tickets for each action item from the standup | 6 | `CLARIFY` | 0.45 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 1 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 2 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 3 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 4 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 5 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Create an issue about the login bug | 6 | `create_issue` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 6 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 1 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 2 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 3 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 4 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 5 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 6 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 1 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 2 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 3 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 4 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 5 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| analyze the file I uploaded | 6 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 1 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 2 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 3 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 4 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 5 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 6 | `analyze_document` | 0.92 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 1 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 2 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 3 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 4 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 5 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 6 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 3 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 4 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 1 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 2 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 3 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 4 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 5 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 6 | `list_prs` | 0.92 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 6 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 1 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 2 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 3 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 4 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 5 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what did we make earlier | 6 | `session_activity_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 1 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 2 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 3 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 4 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 5 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
| what meetings are coming up | 6 | `week_calendar` | 0.85 | anthropic:claude-haiku-4-5 |  |
