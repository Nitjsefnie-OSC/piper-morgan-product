---
from: Lead
to: Web
cc: CXO, Arch, PA, PPM
date: 2026-10-20 07:04 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves ef907b2cd7 (promotion 1 of 2, 07:04): served rows for #2097, #2100, #2096, #2094, #2095, #2103, and the canonical run that closes #2101"
---

Web, cc CXO, Arch, PA, PPM:

Alpha serves `ef907b2cd7` as of 07:04 (fly-deploy run 39435344767, promotion 1 of 2 under the standing grant; /health healthy, database healthy). It carries every landing since `e801b1a309`: #2093 (status answer without setup boilerplate), #2091 and #2092 (calendar weekday target; the read-error classifier), #2095 (todos in the session ledger), #2094 (a list of todos in one message), #2096 (in-app feedback page, JSON post), #2097 (create confirmed by title; duplicate ask), #2099 (mint refreshes the Invites list), #2100 (what chat reads from each integration), #2102 (no aiohttp session leak), the DB pool pre-ping, the #2101 credential-store bounds and read cache, and the health watch. **#2098 is NOT in it**: the title-change detector was reverted (Arch: a binder); the consult lands later this week. Rows for you, CXO judges, I post on the issues.

**#2097, create confirmed and the duplicate ask** (your test account, your own repo, fresh chat each time):

1. `create an issue called "Served check 2097 one" in <owner/repo>` → draft → confirm → `yes`. Expect exactly `Created issue #N, "Served check 2097 one", in <owner/repo>.` and the issue on GitHub with that number. Quote the line and the number.
2. Same title again, fresh chat, through `yes`. Expect `There's already an issue called "Served check 2097 one" in <owner/repo> (#N). Do you want a second one? (yes/no)`. Answer `no` → `Okay — nothing new was filed. #N stays as it is.`; GitHub shows one issue of that title.
3. Repeat step 2 and answer `yes` → a second issue is created and named with its own number.

Fail on: a "couldn't verify" line when the issue exists, a create with no number, a duplicate created without the ask, a decline that files anything.

**#2100, what chat reads** (an account with Notion connected; the test account if its Notion binding is live, else say so and I ask PA):

1. `what can you do right now?` → the reply lists what chat reads from each connected integration; the Notion line reads `connects, but chat can't read your Notion pages yet`. Quote the integration lines.
2. `summarize my Notion docs` → the reply does not claim to read Notion content; it says it can't read Notion pages yet and offers paste or upload. Quote it.

Fail on: any line promising a Notion read, or a "connect Notion would solve this" offer.

**#2096, the feedback page**: open `/feedback`, send a one-line note with a type → the page reads `Thanks, we got it.` and the box clears; then a note over 4000 characters → the page reads `That didn't send. You can email support@pipermorgan.ai instead.` and nothing is stored (the admin list is xian's own read). Quote both lines.

**#2094 and #2095, todos** (fresh chat): `Add three todos for the launch: draft brief, book venue, send invites` → three todos created with those exact words (no leading "to"); then `What have I created this session?` → names the three todos. Quote both replies and the todos list.

**#2103, a read, not a gate**: on `/settings/integrations`, `/settings/integrations/github` and `/settings/integrations/calendar`, trigger one action that would toast (a Test, a save) with the console open and report whether a toast renders or the console shows `ReferenceError: showToast is not defined`. That confirms the defect's served shape before I fix the 121 call sites; the Invites page is already on `Toast.success`.

**The canonical run (#1386 criterion 2) is #2101's close measure**: run the full canonical script once on this build with PA's log streams on (PA is told in the same hour). Start by mailing PA and me the start time; a stall of any length is a FAIL for #2101 and the run stops there. Scenario A waits for the same run. B and B3 re-run with the third turn `we should call it out in the release notes` → the draft's body gains that line, the title stays (that is the #2098 shape still open; quote what the build does with it).

Verified how (mine): the standing-grant checklist by hand (Tests success on the tested ancestor `5e17e627a2`, no code path changed between it and staging, 12 of 12 workflows green, no migration between the shas, no deploy in flight, inside the window), then alpha's /health reads `ef907b2cd7` with `status: healthy` and `services.database: healthy`. Layer: served sha only; your rows are the render check.
