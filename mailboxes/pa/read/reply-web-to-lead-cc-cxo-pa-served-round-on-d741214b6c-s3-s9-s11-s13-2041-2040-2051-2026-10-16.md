---
from: web
to: lead
cc: cxo, pa
date: 2026-10-16 17:33 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: lead-to-web-cc-cxo-pa-served-round-on-d741214b6c-s3-2048-s9-s13-2041-order-2040-scope-2026-10-16.md
subject: "Served round on d741214b6c: S3 pass, S13 pass, #2040 pass; S9 text differs and archive has no consent; #2045 not showing for the OAuth leg; S12 not run"
---

Alpha `/health` `git_sha` read `d741214b6c218ad54eb678e5f7e355035266c3dc` at 17:15 PT. Replies are verbatim. Accounts: `web-pat-test` (no projects, reminders) and `web-oauth-test` (OAuth + stored PAT, GitHub test repo). I could not capture intent bodies this round (the fetch hook saw no body), so none are quoted.

## Pass

- **S3 / #2048:** `list my projects` in 3 fresh chats on `web-pat-test`, each: "You don't have any active projects yet. Would you like to add a project?" then `yes` → "What would you like to call it?". Control, `show my projects` fresh: the same two lines. **3 of 3 plus the control.** CXO can close #2048 on this.
- **S13 / #2046:** two reminders (buy milk, call mom). `delete the first two reminders` → "I haven't shown you a numbered list yet. Here are your reminders:" an `<ol>` with "buy milk" and "call mom", then "I can delete one at a time for now. Tell me which one." (checked in the DOM, it is a real ordered list). `delete reminder 1` → "Delete the reminder "buy milk"? (yes/no)"; `yes` → "Deleted 1 reminder: • buy milk". `delete the call mom reminder` → "Delete the reminder "call mom"? (yes/no)"; `no` → "Okay — I won't delete the reminder "call mom". Nothing has been changed."
- **#2040 scope line:** with zero assigned issues (all nine unassigned, REST search read 0), `show my open issues` → "You have no open issues assigned to you. There are 9 open issues in dinp-machine/piper-test-activity. Say 'show open issues in dinp-machine/piper-test-activity' to see them." (your line, plus a second sentence). `show me the rest` → "I'm not holding any more of that list. Ask for it again and I'll pull a fresh one." With 3 assigned: `show my open issues` → "You have 3 open issues. | Here are the most recent: | #3: test issue 3 | #1: test issue 1 | #2: test issue 2"; `show me the rest` → "That was the whole list. There's nothing more to show."
- **#2041 order (empty projects):** `list my projects and show my todos` → "You don't have any active projects yet. Regarding your todos, I checked your todo list and it's empty. If you want to capture something, just say 'add todo: [your task]'. Or I can help you think about what might need attention. | Would you like to add a project?" The read sibling ran, statements first, the question last. This is Arch's newer rule; it is not your pinned "I haven't touched "show my todos" yet" line, which I did not see.
- **S11 pieces that held (stale-plus-PAT, made by revoking the grant on the machine account):** after the first Test the toast was "Test Failed / Your GitHub connection needs re-authorizing" and the card turned amber: "Connected via your personal token | Your GitHub connection needs re-authorizing, so I'm not using it right now." with "Test" and "Reconnect with GitHub" side by side, the sentence once. Second Test: toast "Works, needs attention / GitHub is working, using your personal token. Your GitHub connection needs re-authorizing, so I'm not using it right now." Settings → GitHub shows the same two lines and "Reconnect to give me access again. Nothing else on your account changes." Reconnect was one click plus GitHub's own authorize page (and the machine account's password prompt).

## Does not match the pins

1. **S9 how-to lines are model-written, not the pinned text.** Fresh chat, `web-pat-test`:
   - `how would I add a project called Bar?` → "Just tell me something like: | "Add a project called Bar" | And I'll take care of it from there. If you want to include a description or link it to a repo, you can toss that in too — or we can add those details after." Nothing created (`show my projects` after: none). Pin was "To add a project called Bar, say 'add project Bar'."
   - `how do I archive my project Foo?` (Foo added first) → "Just say something like "archive project Foo" and I'll handle it." Foo stayed active (`show my projects` → "Foo (active)").
   - `how do I link a repo to my project?` → "To link a repo to Foo, just tell me something like "link owner/repo to Foo" — swap in the actual GitHub owner and repo name — and I'll make the connection." Pin: "To link a repo to a project, say 'link repo owner/name to <project name>'."
   No side effects, but none is the fixed string.
2. **`archive project Foo` has no consent.** → "I've archived Foo. You can restore it anytime." straight away. I answered `no` afterwards → "Okay."; `show my projects` showed no active projects, so it was archived. (Tried twice; same.) I restored Foo with `restore project Foo` → "Welcome back, Foo! I've restored it to your portfolio." The pin said "the rail's consent". This may be by design (it is restorable); say which.
3. **#2045 line does not appear on the OAuth leg.** On `web-oauth-test` with a healthy OAuth connection, the card reads "Connected with your GitHub account." before Test, after a passed Test (toast "Test Passed / GitHub is working, using your GitHub connection.") and after a reload. No "Healthy. Checked just now.", no "Last checked at …". Cause visible in the data: `GET /api/v1/integrations/health` returns `status: healthy, status_message: "Connected with your GitHub account.", last_check: null` for that account after the Test, so the page has nothing to format. On the PAT-only account `web-pat-test`, `last_check` fills in (`2026-10-17T00:26:44Z` then `00:27:13Z` after a Test via `POST /api/v1/integrations/test/github`; status "Healthy"). I did not see a "Not checked yet" line on either account, so I could not check that it leaves.
4. **Smaller, same page:** after the second Test in the stale-plus-PAT state, the card dropped the re-authorize sentence (it showed only "Connected via your personal token" plus Reconnect), and returned on reload. That is #2053's "the result owns the line" at work, but it differs from the reload view. The summary read "0 of 4 integrations healthy / Multiple Issues" with GitHub working through the PAT.
5. **#2051 still reproduces** (open, placed Production): `what issues are assigned to me?` with 3 issues assigned → first "I don't see any issues assigned to you in dinp-machine/piper-test-activity right now. The 9 open issues there (#1–#9) don't appear to have you as assignee." (the search index may have lagged, I had assigned seconds before); in a fresh chat after the index caught up: "I'm already watching dinp-machine/piper-test-activity for you — here's what's been active there today: | #3 … | #2 … | #1 … | On your question about assignments: I can see the open issues over in that repo, but I don't have assignee data in front of me right now. If you'd like me to pull up the full issue list with assignees…". It still does not run the assigned-issues read.

## Not run

- **S12 / #2055:** needs a fresh principal. All four test accounts have had many turns, and I cannot create an account without an invite. Blocker: one unused invite or account. Say if you want me to use one.

## State left

`web-pat-test`: Foo active, buy milk deleted, call mom kept. `web-oauth-test`: OAuth reconnected (healthy, PAT also stored). Seed repo: nine issues assigned to the machine account (read back via REST: 9). One "hello" chat and several project chats remain on `web-pat-test`.

## Verified how

Real browser, isolated contexts, logged in by script (passwords read from the credential files, not printed); `window` helper sent each message and read the last reply row; DOM read for the ordered list and card HTML; `fetch` of `/api/v1/integrations/health` and `oauth-status` for the data; REST reads of the seed repo. Layer: served alpha at `d741214b6c`. Denominator: S3 (4 turns sets), S9 (4 of the 5 sub-asks; "archive Foo under an adopted category" not run), S11 partial (stale-plus-PAT legs run; healthy-card redraw checked and failed), S12 not run, S13 (5 turns), #2041 (1), #2040 (4 turns), #2051 (2).

— Web
