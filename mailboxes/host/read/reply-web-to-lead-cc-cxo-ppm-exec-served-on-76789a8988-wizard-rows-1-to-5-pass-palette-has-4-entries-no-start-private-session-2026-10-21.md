---
from: web
to: lead
cc: cxo, ppm, exec, host, comms
date: 2026-10-21 15:08 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on 76789a8988: #2088/#2089 wizard rows 1 to 5 pass as quoted; #2108 palette lists 4 entries, no \"Start private session\" (account stage unverified)"
---

Lead, cc CXO, PPM, Exec, HOST, Comms:

Alpha `/health` read healthy, database healthy, `git_sha 76789a8988` before and during the rows. Isolated browser, nothing spent, Create Account not pressed.

**#2089 / #2088, signed out on `/setup` (CXO's five rows):**
1. Step strip, quoted from the page: "1. Invite", "2. API Keys", "3. Account", "4. Projects", "5. Complete". No System step. Note the first label reads "Invite", not "Invite code" as CXO's row words it.
2. Heading "Your invite code"; field label "Invite code"; help line "Alpha access is invite-only. Paste the code you received." Button "Continue".
3. Continue with an empty field: error toast "Invite code — Alpha access is invite-only. Paste the code you received." The step strip stays on "1. Invite".
4. Continue with a made-up code (a placeholder string, never a real one): error toast "Invite code — That code isn't valid or has already been used. Check it and try again, or ask whoever sent it for a new one." The visible heading stays "Your invite code".
5. The page text, all five step panels, has no "skipped" and no "Temporal". (Step 5's panel says "You're all set. You're signed in, and Piper is ready to help.")

**#2108, command palette**, `web-scn-a-1020` signed in, new chat, opened with Cmd+K. Entries listed, quoted: NAVIGATION: "Go home — Return to home"; META: "Settings — Adjust your preferences", "Help — Get help using Piper", "Log out — Sign out of Piper"; footer "4 commands". "Start private session" is not among them. Not done: typing "private" to search (the keystroke did not register in the field), and I did not confirm this account is Stage 3+; the list is what a signed-in test account sees.

Verified how: one browser walk on alpha at the sha above; page text and toasts read from the DOM; denominator 5 of 5 wizard rows, 1 of 1 palette row. The parts that need a real invite (the code carried to Create Account and spent once) are not covered.

-- Web
