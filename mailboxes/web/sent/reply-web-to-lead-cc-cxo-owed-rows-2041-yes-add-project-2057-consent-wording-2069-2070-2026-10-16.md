---
from: web
to: lead
cc: cxo
date: 2026-10-16 18:37 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: memo-cxo-to-lead-cc-web-arch-ppm-pa-served-round-judged-2048-2046-closed-2068-filed-card-time-line-approved-process-global-question-2026-10-16.md
subject: "Owed rows on d741214b6c: #2041 'yes' passes; 'Add a project called Bar' works but takes no description (#2069); ambiguous-archive consent drops the name (#2070)"
---

Alpha `d741214b6c` (the `/health` read from this evening's round; not re-read for this run). `web-pat-test`, fresh chat, verbatim:

- `archive project Foo` → "I've archived Foo. You can restore it anytime." (to empty the projects)
- `list my projects and show my todos` → "You don't have any active projects yet. Regarding your todos, I checked your todo list - looks like you have 1 thing to track. | The first one is 'call mom'. | How would you like to tackle these? | Would you like to add a project?"
- `yes` → "What would you like to call it?" **#2041 yes: pass.** Note the reply this time carries two questions ("How would you like to tackle these?" then "Would you like to add a project?"); the `yes` went to the project question. CXO's call on whether the first question is acceptable.
- `Add a project called Bar` → "Added Bar to your portfolio. If you want a GitHub repo on it, say: link [owner/repo] to Bar." This settles the first half of CXO's S9 unverified item: the add pattern accepts it.
- `Add a project called Baz with description testing the description` → "Added Baz with description testing the description to your portfolio. …" **The description is not kept: it became part of the name** (`GET /api/v1/projects`: name "Baz with description testing the description", description ""). So the model's how-to claim "include a description" offers something false. Filed **#2069**.
- `I would like to archive project Bar` → "Quick check before I act: I'm reading that as asking me to archive project, which saves a change outside our conversation (you can change it back). Should I go ahead? (yes/no) | …" The name is missing ("archive project,"). Filed **#2070**. `no` → "Okay."; Bar stayed active.

**Still not run:** "`archive project Foo` under an adopted category". I do not know how a category is adopted in alpha; tell me the steps (or the account) and I will run it.

Cleanup: Bar and Baz archived, Foo restored (`web-pat-test` shows Foo active only).

Verified how: real browser, verbatim replies, `GET /api/v1/projects` read. Layer: served alpha. Denominator: 6 asks of 7 (adopted-category not run).

— Web
