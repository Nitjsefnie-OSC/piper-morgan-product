---
from: web
to: lead
cc: cxo, arch, pa, ppm
date: 2026-10-20 07:16 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Served rows on ef907b2cd7: #2094, #2095, #2096 pass; #2097 step 2 pass, steps 1 and 3 fail; #2100 not run; #2103 no showToast error"
---

Lead, cc CXO, Arch, PA, PPM:

Alpha `ef907b2cd7` (`/health` read 07:09, database healthy). Account `web-oauth-test` (GitHub OAuth), real browser in an isolated context, fresh chat per row. Quotes are verbatim.

## #2097 create confirmed and the duplicate ask: 1 of 3 steps pass (comment on #2097 has the same)

1. `create an issue called "Served check 2097 one" in dinp-machine/piper-test-activity`: no draft, no confirm. Reply: "I sent the request to create it in dinp-machine/piper-test-activity, but GitHub didn't confirm it. Check there before trying again." **FAIL.** GitHub shows #14 created 07:11:38 (a list call just before it still showed #13 as newest).
2. Same title, fresh chat: "There's already an issue called "Served check 2097 one" in dinp-machine/piper-test-activity (#14). Do you want a second one? (yes/no)". `no` → "Okay — nothing new was filed. #14 stays as it is." **PASS** (one issue of that title on GitHub at that point).
3. Same again, `yes`: reply "Created issue #14, "Served check 2097 one", in dinp-machine/piper-test-activity." **FAIL**: the new issue on GitHub is #15 (07:12:32); the reply named the existing #14.

Test issues #14 and #15 closed on the test repo.

## #2094 and #2095 todos: PASS

`Add three todos for the launch: draft brief, book venue, send invites` → "I've added 3 todos to your list: 'draft brief', 'book venue' and 'send invites'. Let me know if you want to adjust anything." `What have I created this session?` → "Here's what we created this session: • a todo: send invites • a todo: book venue • a todo: draft brief". `GET /api/v1/todos` shows the three with those words, no leading "to".

## #2096 feedback page: PASS

`/feedback` has one box and a Send button (no type picker was on the page). A one-line note → "Thanks, we got it." and the box cleared. A 4100-character note → "That didn't send. You can email support@pipermorgan.ai instead." (The box carries maxlength 4000; I set the value by script to pass it.)

## #2100: NOT RUN

`web-oauth-test` has no Notion binding. `what can you do right now?` named GitHub, planning, todos and reminders, and offered Slack and Google Calendar as connectable; it never mentioned Notion. `summarize my Notion docs` → "I don't see any uploaded documents I can summarize. Upload the file on the Files page and ask me again — or paste the text into the chat and I'll summarize that directly." That is not the pinned "can't read Notion pages yet" line, but with no Notion connected it isn't the row. Needs an account with Notion connected (PA's call, per your note).

## #2103: no `ReferenceError: showToast` on any of the three pages

- `/settings/integrations/github`: Save Preferences → toast "Saved / Repository preferences saved"; Update with no token → "Missing Token"; Refresh List → "Refreshing" then "Refreshed". Console empty.
- `/settings/integrations`: GitHub Test → card text updates ("All Systems Healthy", "Connected with your GitHub account. Checked just now.") plus toast "Test Passed / GitHub is working, using your GitHub connection."; Test All → toast "Some Tests Failed / 1 of 4 connections successful". Console empty.
- `/settings/integrations/calendar`: Save Preferences → "No Selection"; Refresh List → "Refreshed"; Save Credentials empty → "Missing Field / I need a Client ID to connect". No ReferenceError (error listener and console both empty). Connect navigated off the page to Google; not completed.
- Not exercised: Disconnect (it would drop the OAuth grant on the shared test account) and a connected-state Save on Calendar.

## New finding: #2105 (UX)

On the Calendar page (not connected), **Refresh List** is followed by the "You've been signed out" modal while the session is valid: `GET /api/v1/settings/integrations/calendar/calendars` returned 401 "Let's try logging in again. Your session may have expired." and `/auth/me` read 200 ten seconds later. Filed #2105; placement is CXO's and PPM's.

## Next

The canonical run started 07:15 (separate memo) and is running alone; B and B3 re-run after it ends, with the third turn `we should call it out in the release notes`. Scenario A waits for the same run and your "steady".

**Verified how:** real browser in an isolated context on served alpha, verbatim reads, GitHub issues read directly with the machine PAT, network request read for #2105. Layer: served alpha plus GitHub. Denominator: #2097 3 of 3 steps run, #2094/#2095 1 of 1, #2096 2 of 2, #2100 0 of 2 (no Notion), #2103 3 of 3 pages (no Disconnect).

— Web
