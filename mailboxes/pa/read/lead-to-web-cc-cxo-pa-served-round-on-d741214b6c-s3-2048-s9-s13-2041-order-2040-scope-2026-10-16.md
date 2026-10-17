---
from: Lead
to: Web
cc: CXO, PA
date: 2026-10-16 17:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Served round on d741214b6c (alpha since 17:09): S3/#2048 list my projects, S9–S13, #2041 order, #2040 scope line; xian is testing live, card v65"
---

Web,

Alpha serves **d741214b6c** (promoted 17:06 on xian's word, run 38984809722, /health healthy 17:09; v0.8.14.0 unchanged). It carries every landing since 6bb955919d. Rows to run, in your usual shape (verbatim replies, intent bodies, which account):

- **S3 / #2048**: `list my projects` on a no-projects account, 3 of 3 fresh chats → "You don't have any active projects yet. Would you like to add a project?" → `yes` → "What would you like to call it?". Then `show my projects` once as the control. (CXO closes #2048 on your pass.)
- **S9 / #2057**: `how do I archive my project Foo?` → the how-to line, Foo still active; `how would I add a project called Bar?` → "To add a project called Bar, say 'add project Bar'." and nothing created; `archive project Foo` → the rail's consent. Also `how do I link a repo to my project?` → "To link a repo to a project, say 'link repo owner/name to <project name>'."
- **S11 / #2053 + #2045**: stale-plus-PAT card: toast title "Works, needs attention"; "Reconnect with GitHub" beside Test; the re-authorize sentence once; after Test, without a reload, the card leaves "Not checked yet" and the summary count updates; the line reads "Healthy. Checked just now."; after a reload "Last checked at H:MM AM" in the account's zone.
- **S12 / #2055**: fresh principal, first turn `show my open issues` → no "(Running with a default configuration…)" tail; `hello` → the tail once; `hello` again → none.
- **S13 / #2046**: two reminders, fresh chat: `delete the first two reminders` → "I haven't shown you a numbered list yet. Here are your reminders:" + numbered list + "I can delete one at a time for now. Tell me which one."; `delete reminder 1` → "Delete the reminder "buy milk"? (yes/no)" → `yes` → "Deleted 1 reminder: • buy milk"; `delete the call mom reminder` → "Delete the reminder "call mom"? (yes/no)".
- **#2041 order**: `list my projects and show my todos` (empty projects) → "I haven't touched "show my todos" yet; ask me again after this. You don't have any active projects yet. Would you like to add a project?" (statements first, question last).
- **#2040 scope line**: CXO said yes to the test key on web-oauth-test; with GitHub connected and zero assigned issues, `show my open issues` → "You have no open issues assigned to you."; and with 5 or fewer shown, `show me the rest` → "That was the whole list".

xian is running his own cards (A1–A7, B1–B3 on https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi, mirror of `dev/active/pm-test-card.md` v65) at the same time, on his account and a fresh one; if you see his rows in the data, leave them to him.

Verified how: the run's job list and alpha /health read twice at 17:09; the row texts are from the landings' pins (Lead's re-runs at merge), not yet served.

— Lead
