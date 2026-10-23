# Router ×6 control — main

Run 2026-10-23 16:12Z · 6 sample(s) per phrase · 96 router calls · 0 ERROR · served: anthropic:claude-haiku-4-5 (96/96)

| phrase | routes (count) | confidence range |
|---|---|---|
| Compare these two documents | `CLARIFY` ×6 | 0.40–0.40 |
| Compare the two files I uploaded | `CLARIFY` ×6 | 0.40–0.40 |
| Compare launch-notes-2131.txt with roadmap.md | `NONE` ×6 | 0.85–0.95 |
| Analyze this document | `analyze_document` ×6 | 0.85–0.85 |
| What does this document say? | `CLARIFY` ×6 | 0.40–0.40 |
| Analyze the document called PRD Writing Guidelines | `analyze_document` ×6 | 0.95–0.95 |
| analyze the file I uploaded | `analyze_document` ×6 | 0.95–0.95 |
| Analyze launch-notes-2131.txt | `analyze_document` ×6 | 0.95–0.95 |
| Analyze our repo activity this week | `analyze_commits` ×6 | 0.85–0.85 |
| modify the status document | `update_document` ×6 | 0.72–0.85 |
| show priorities for this sprint | `prioritize` ×6 | 0.85–0.85 |
| any old prs lying around | `stale_prs` ×6 | 0.95–0.95 |
| are we behind upstream at all | `local_git_status_query` ×6 | 0.72–0.85 |
| what did we make earlier | `session_activity_query` ×6 | 0.85–0.85 |
| what meetings are coming up | `week_calendar` ×6 | 0.85–0.85 |
| show all events | `CLARIFY` ×6 | 0.60–0.60 |

## Samples

| phrase | # | route | conf | served | error |
|---|---|---|---|---|---|
| Compare these two documents | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare these two documents | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare these two documents | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare these two documents | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare these two documents | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare these two documents | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare the two files I uploaded | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 1 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 2 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 3 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 4 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 5 | `NONE` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Compare launch-notes-2131.txt with roadmap.md | 6 | `NONE` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 1 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 2 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 3 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 4 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 5 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze this document | 6 | `analyze_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 1 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 2 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 3 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 4 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 5 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| What does this document say? | 6 | `CLARIFY` | 0.4 | anthropic:claude-haiku-4-5 |  |
| Analyze the document called PRD Writing Guidelines | 1 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
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
| Analyze launch-notes-2131.txt | 1 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 2 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 3 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 4 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 5 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze launch-notes-2131.txt | 6 | `analyze_document` | 0.95 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 1 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 2 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 3 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 4 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 5 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| Analyze our repo activity this week | 6 | `analyze_commits` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 1 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 2 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 3 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 4 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 5 | `update_document` | 0.85 | anthropic:claude-haiku-4-5 |  |
| modify the status document | 6 | `update_document` | 0.72 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 1 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 2 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 3 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 4 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 5 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| show priorities for this sprint | 6 | `prioritize` | 0.85 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 1 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 2 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 3 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 4 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 5 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| any old prs lying around | 6 | `stale_prs` | 0.95 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 1 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 2 | `local_git_status_query` | 0.75 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 3 | `local_git_status_query` | 0.72 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 4 | `local_git_status_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
| are we behind upstream at all | 5 | `local_git_status_query` | 0.85 | anthropic:claude-haiku-4-5 |  |
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
| show all events | 1 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| show all events | 2 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| show all events | 3 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| show all events | 4 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| show all events | 5 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
| show all events | 6 | `CLARIFY` | 0.6 | anthropic:claude-haiku-4-5 |  |
