# Classifier ×6 — lead-2132b

Run 2026-10-23 19:10Z · provider forced: openai · † = not a rail key

| phrase | expected | actions |
|---|---|---|
| give me my standup | action:show_standup | `show_standup` ×6 |
| what's on my calendar today? | action:meeting_time | `meeting_time` ×6 |
| when is my next meeting? | action:meeting_time | `meeting_time` ×6 |
| what am I working on? | category:STATUS | `get_project_status†` ×6 |
| what should I focus on today? | category:PRIORITY | `prioritize` ×6 |
| what are my top priorities? | category:PRIORITY | `get_top_priority†` ×4, `prioritize` ×2 |
| who am I? | action:get_identity | `get_identity` ×6 |
| what's my role? | category:IDENTITY | `get_role†` ×6 |
| how do I create a ticket? | category:GUIDANCE | `provide_guidance†` ×6 |
| create a ticket for the login bug | action:create_issue | `create_ticket` ×6 |
| analyze the file I uploaded | action:analyze_document | `analyze_document` ×6 |
| summarize the document | action:summarize_document | `summarize_document` ×6 |
| what time is it? | category:TEMPORAL | `get_time_info†` ×6 |
| show my open issues | action:list_issues_query | `list_issues` ×6 |
| show my open pull requests | action:list_prs_query | `list_pull_requests` ×6 |
| any stale PRs? | action:stale_prs_query | `stale_prs_query` ×6 |
| what needs my attention? | action:attention_query | `attention_query` ×6 |
| what changed since yesterday? | action:changes_query | `get_project_status†` ×6 |
| how productive was I this week? | action:productivity_query | `analyze_productivity` ×6 |
| list my projects | action:manage_portfolio | `manage_portfolio†` ×6 |
| close issue 42 | action:close_issue_query | `close_issue_query` ×6 |
| comment on issue 42: looks good | action:comment_issue_query | `comment_issue_query` ×6 |
| what have you learned about my workstyle? | action:pull_insights | `get_learned_patterns†` ×3, `get_learned_preferences†` ×3 |
| set my default repo to acme/widgets | action:set_default_repo | `set_default_repo` ×6 |
| what is my default repo? | action:get_default_repo | `get_identity` ×6 |
| write a short update for the CEO on where we are | action:write_stakeholder_update | `write_stakeholder_update` ×6 |
| update the project plan doc with the new dates | action:update_document_query | `update_document_query` ×6 |
| can you clarify what you meant? | REVIEW | `clarification_needed†` ×6 |
| give me a project status report | REVIEW | `get_project_status†` ×6 |
| change the title of issue owner/repo#107 to 'Foo' | action:update_issue | `update_issue` ×6 |
| add label bug to issue owner/repo#107 | action:update_issue | `add_label†` ×6 |
| can we connect my github? | action:get_contextual_guidance | `get_contextual_guidance` ×6 |
| connect my slack | action:get_contextual_guidance | `get_contextual_guidance` ×6 |
| link mediajunkie/test-piper-morgan to the project | action:manage_repos | `link_repository_to_project†` ×6 |
| help me set up github | action:get_contextual_guidance | `get_contextual_guidance` ×6 |
| show me my archived projects | REVIEW | `manage_portfolio†` ×6 |
| list my archived projects | action:manage_portfolio | `manage_portfolio†` ×6 |
| what projects have I archived? | action:list_archived_projects | `manage_portfolio†` ×6 |
| Compare these two documents | extra | `compare_documents` ×6 |
| Compare the two files I uploaded | extra | `compare_documents` ×6 |
| Compare launch-notes-2131.txt with roadmap.md | extra | `compare_documents` ×6 |
| Analyze this document | extra | `analyze_document` ×6 |
| What does this document say? | extra | `analyze_document` ×6 |
| Summarize this file | extra | `summarize_document` ×6 |
