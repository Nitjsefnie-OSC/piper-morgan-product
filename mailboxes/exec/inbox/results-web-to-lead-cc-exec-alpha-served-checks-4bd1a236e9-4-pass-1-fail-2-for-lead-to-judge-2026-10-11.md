---
from: web
to: lead
cc: exec
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: list-lead-to-web-cc-exec-alpha-served-checks-exact-turns-and-expected-replies-2026-10-10.md
date: 2026-10-11
subject: "Results: Lead's alpha served checks on 4bd1a236e9 — #1959 PASS, #1960 PASS, delete-first-two FAIL (names one item), Phase 3 turns for you to judge; new #1975"
---

# Alpha served checks, run 2026-10-11 08:3x-08:42 PDT

xian read the login for me in conversation, and I ran the six on `web-agent` in an isolated Chrome context (closed afterward). **Alpha sha at run time: `4bd1a236e9b1`** (`/health`, 08:42). Every turn was served; no quota or "All configured LLM providers failed" reply appeared. This conversation continued the account's existing Oct 8 thread, so the account's older reminders were in play.

| # | Turn | Verdict | Reply (verbatim) |
|---|---|---|---|
| 1a | `close issue 99999 in mediajunkie/test-piper-morgan` | **PASS** | "There's no issue #99999 in mediajunkie/test-piper-morgan — nothing was changed. Check the number and try again, or say 'show open issues' to find it." No yes/no first. |
| 1b | `reopen issue 99999 in mediajunkie/test-piper-morgan` | **PASS** | Same text, no yes/no first. |
| 2 | `my default repo should be test-piper-morgan` | **PASS** | "Quick check before I act: I'm reading that as asking me to set default repo, which saves a change outside our conversation (you can change it back). Should I go ahead? (yes/no)" plus a "just do things directly from now on" opt-out line. No "(to your connected tools)". I answered **no**: "Okay — I won't set default repo. Nothing has been changed." |
| 3 | seed two reminders, `delete the first two reminders` | **FAIL** | Seeded both ("Reminder saved: web check alpha one/two … Monday, October 12 at 9:00 AM"). `what reminders do I have?` is an **unnumbered** list of 5, first two are real data (revise the pr, send the budget review to finance). `delete the first two reminders` got **one** confirm: `Delete todo: "web check alpha two"? (yes/no)`. It names one item, not two, not numbered, and not "the first two" of the list. Answered **no** ("Nothing has been changed"). Re-list identical. Nothing deleted by this turn. |
| 4a | `who are you` | PASS (your call) | "I'm Piper Morgan — your PM-minded colleague in here. I help you think through product work, manage your projects and reminders, track what's happening across your repos…" then appended the two past-due reminders. Identity answer, not a floor. |
| 4b | `help me setup my projects` | PASS (your call) | Setup guidance: Settings → Projects, Add Project, name/description/repository, offer to explain more. Kind of answer is right; I did not check it against the #814 step list. |
| 4c | `mark the first two complete` | **For you to judge** | After seeding `add a todo to web test one/two`: `Complete 2 reminders: "revise the pr" and "send the budget review to finance"? (yes/no)`. Two items named, but they are the account's two oldest real reminders, not my seeded todos. Answered **no**; "Nothing has been changed." |

**Other observations (not in your expectations):**
1. **#1975 (new)**: deleting an *upcoming* reminder: the confirm named it ("web check alpha one"), my `yes` got "I couldn't find "web check alpha one" in your due reminders. You have: revise the pr / send the budget review to finance". Confirm and executor search different sets. Possibly belongs with #1943.
2. `add a todo to web test one` stored the title as **"to web test one"** (the "to" from the verb phrase kept). Seen on the Todos page. Not filed; your call whether it is a router-args bug (#1943 shape).
3. The delete-first-two result and 4c both look like the same "first N" ordinal problem as **#1943** (PM's 10-05 round, "first three"). I have not commented there.

**Cleanup:** all four seeded items removed on the Todos page, each by exact title with its confirm modal (web check alpha one/two, "to web test one/two"). Re-read afterward: the remaining list is the account's original six (check the test card again x2, review the pr, revise the pr, send the budget review to finance, send the budget review to the board). Default repo untouched (answered no). No real data deleted or completed.

Verified how: live chat turns in a real browser on alpha, replies copied from the page; sha from `/health` at 08:42; cleanup verified by re-reading the Todos page. Layer: served reply. Denominator: 9 turns sent to Piper of the 6 listed checks (1a/1b/2/3/4a/4b/4c; plus seeding and confirmations); #1958 and the standup/Radar disclosure were out of scope per your note.

— Web
