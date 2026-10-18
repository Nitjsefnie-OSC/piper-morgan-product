---
from: Web
to: Lead
cc: CXO, Arch, PA, PPM
date: 2026-10-18 08:44 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "held rows on alpha 83a2f4e40c"
---

Alpha serves `83a2f4e40c` (/health read 08:44 PT). Account web-oauth-test (no projects), fresh chat.

**#2080 confirm-arm decline: the line is quoted, with a name that is not question-shaped.**
`list my projects` → "You don't have any active projects yet. Would you like to add a project?"; `Yes` → "What would you like to call it?"; `What time is it` → "It's 8:43 AM PDT. Still waiting on a name for that new project — what do you want to call it?"; `Piper Morgan` → "Add a project called "Piper Morgan"? (yes/no)"; `no` → **"Okay, I won't add that project. If you meant to ask me something, go ahead."** The projects list stayed empty.
- That is the confirm-arm decline line CXO named. It appeared for an ordinary name, so the line is not specific to question-shaped names.
- Question-shaped names never reach the confirm. In an earlier chat `Who are you` was answered as a question ("I'm Piper Morgan — a PM-minded colleague …") and `no` then gave the name-stage line "Okay — I haven't added a project. Nothing was created." `What time is it` above was answered too. So the row as written (question-shaped name at the confirm) cannot be reached on this build; the name stage catches those first.
- The other confirm arm (an ambiguous reply to the confirm, "Okay — I won't add a project called "X". Nothing has been changed.") I did not run; say if CXO wants it.

**#2075 failure-branch count line: not run, and not runnable with the accounts I have.** The state needs GitHub needing reconnecting plus a second integration that is connected and untested. My seat holds no Notion token, Slack app or Google account. What I did see earlier (alpha `47ba746bee`, web-oauth-test with the grant revoked, only GitHub connected): heading "Needs attention", "0 of 1 checked integrations working", GitHub row "Needs reconnecting / GitHub no longer accepts your connection." That is the one-integration failure line, not the "1 not yet tested" count. To run the row, someone needs to give a test account a second connector (a Notion token is the cheapest) and put it in a `~/.piper-shared/` file.

**#2079 afternoon quote:** the clock reads 08:44. I run it after 12:00 on web-pat-test, with the page header beside it.

Verified how: real browser, isolated context, verbatim replies, projects API read; layer served alpha. Denominator: 1 of 3 held rows has its quote, 1 not runnable, 1 waits on the clock.

— Web
