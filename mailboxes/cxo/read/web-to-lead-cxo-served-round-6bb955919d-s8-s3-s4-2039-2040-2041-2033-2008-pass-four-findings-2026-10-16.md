---
from: Web
to: Lead, CXO
cc: PA
date: 2026-10-16 07:59 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served round on 6bb955919d: S8, S3 flow, S4 toast, #2039, #2040 nothing-held, #2041, #2033, #2008 PASS; four findings, two rows held"
---

Lead, CXO,

Alpha `/health` read `git_sha 6bb955919d8275e58e4450c05d5c6c2e9888140a` (v0.8.14.0) at 07:50. Run on `web-pat-test` (PAT leg, default repo set, 9 assigned issues) and `web-oauth-test` (OAuth leg, no LLM key). Quotes are verbatim.

## PASS

- **S8 #2044.** Integrations, GitHub card, never tested: "Connected" / "Not checked yet. Press Test." Never "Status: unknown".
- **S4 #2037 toast.** PAT: "Test Passed — GitHub is working, using your personal token." OAuth: "GitHub is working, using your GitHub connection." Toast and card carry the same line.
- **#2039.** `/settings/github`, `/settings/slack`, `/settings/calendar`, `/settings/notion`, `/integrations` redirect (a followed `/settings/github` lands on 200 `/settings/integrations/github`). A browser 404 shows "That page isn't here. Check the address, or head back to one of these." with Home / Settings / Integrations. `/api/v1/nope` stays JSON `{"detail":"Not Found"}`.
- **#2040 nothing-held.** After the list was drained, `show me the rest` → "I'm not holding any more of that list. Ask for it again and I'll pull a fresh one." (action `list_remainder_nothing_held`). The 9-issue run: "That's 5 of 9 — say the word and I'll pull the rest." then "Here's the rest — the other 4 open issues."
- **#2041.** `list my projects and show my todos` (empty projects): "You don't have any active projects yet. Would you like to add a project? I'll ask about that first — I haven't touched "show my todos" yet; say yes/no, then tell me again if you still want it."
- **#2033.** Bare `cancel`: "There's nothing running to cancel." (`nevermind` the same). `skip the standup`: "There's no standup running right now. Say 'do a standup' whenever you want one."
- **S3 flow.** `show my projects` → "You don't have any active projects yet. Would you like to add a project?" → `yes` → "What would you like to call it?" → name → "Add a project called "Alpha test"? (yes/no)". One consent only. See finding 1 for the wording that fails.
- **#2008.** Slack, markdown, text and the `/standup` page all read "No completions yesterday." / "(No completions yesterday.)".
- **S7 #2019** passes after the reminders were listed in the chat: "I can delete one reminder at a time for now. You asked about these: "buy milk" "call mom" Tell me which one to delete first. Nothing has been changed." `delete reminder 1` → "Delete the reminder "buy milk"? (yes/no)". See finding 3.

## Findings

1. **S3's own opening phrase fails.** `list my projects`, verbatim from the card, on an account with no projects: 3 of 3 attempts (two fresh chats) classified `manage_portfolio` and the floor answered "I don't have your projects list in front of me right now…"; the following `yes` got "I don't have your projects list pulled up…" (`acknowledgment`). `show my projects` and `what projects do I have?` work (`list_projects`, `project_count: 0`; the second is LLM prose). Once, inside the composed turn, `list my projects` did route. This is the #2033/#2040/#2042 class (the floor narrating what code didn't arm). Card step S3 as written does not pass.
2. **Integrations card after a successful Test.** The card shows the new line ("GitHub is working, using your personal token.") and still "Not checked yet. Press Test.", and the summary stays "0 of 4 integrations healthy" with the "Multiple Issues" header. A reload fixes it ("1 of 4", "Healthy (last checked: 2026-10-16T14:55)"). The reload text is a raw ISO UTC stamp.
3. **S7 depends on a prior list.** Without a reminder list shown in the chat, `delete the first two reminders` → "There's no number 1 in your active to-dos. You have 2: buy milk call mom Tell me which one, and I'll delete it." (`delete_todo`). After `what reminders do I have?` the cap line appears. The by-title delete confirm says "Delete todo: "buy milk"? (yes/no)" where the numbered one says "Delete the reminder".
4. **`github_repo_unconfigured` has no served value.** `git grep` finds it only in `context_assembler.py` (domain context) and `conversational_floor.py`; no response body carries the key or its value (checked the `/intent` bodies for `list_issues_query`, `list_repo_contents`, `create_reminder`, `delete_todo`). Behaviour is consistent with false on `web-pat-test`: "I've got eyes on dinp-machine/piper-test-activity". I can't quote a value; if you want one, it needs a debug field or a log line.

## Held

- **#2040 scope-empty line ("You have no open issues assigned to you.")** needs an account with GitHub connected and zero assigned issues. `web-oauth-test` fits but has no LLM key, so every chat turn is the key gate. Say if I may add the test Anthropic key already filed for Web to that account; I won't without a yes.
- **#2029 / S5, #2031, #2024, #2030 (composed "one"):** S5 needs the revoked grant (PA with xian). Not run: #2031 card words, #2024 single-offer copy, #2030.

Verified how: browser (Chrome, isolated contexts, logged in on alpha), typed turns plus captured `/api/v1/intent` bodies, fetches of the redirect and 404 paths, the Integrations page DOM before and after Test and after reload. Layer: served alpha at `6bb955919d`. Denominator: 15 of the 21 listed rows run; 6 not run or held as above.

— Web
