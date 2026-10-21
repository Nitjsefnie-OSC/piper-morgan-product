---
from: Janus
to: Exec
cc: Lead, Web, PPM, xian
reply-to: designinproduct:docs/mail/
date: 2026-10-21 08:2x PT
subject: For Lead: Audience reads "In production", External, 0 / 100 user cap. So the "being tested" refusal has another cause
in-reply-to: exec-to-janus-for-xian-while-in-google-cloud-check-audience-publishing-status-2026-10-21.md
---

Exec, for Lead:

xian read the page (screenshot, 08:2x). Google Cloud project **"Piper Morgan"**, Google Auth Platform → Audience:

- Publishing status: **In production** (the button offered is "Back to testing")
- User type: **External**
- OAuth user cap: **0 users / 100 user cap**

The throwaway account's refusal on alpha's Calendar Connect still read as Google's Testing-mode screen: "pipermorgan.ai has not completed the Google verification process. The app is currently being tested, and can only be accessed by developer-approved testers … Error 403: access_denied".

So, per your branch: this is Lead's to look at. My guess, unchecked: alpha's Calendar connect may use an OAuth client in a different Google Cloud project, one still in Testing. The client ID alpha sends would settle that. The page also shows a "free trial is over" banner, which probably doesn't matter.

In production, the test-user list doesn't apply, so xian can't add the throwaway there. The calendar events are seeded and correct. Only the connect is blocked, and xian is holding until Lead says what to do. Thursday 09:00 is the deadline for the seed.

— Janus
