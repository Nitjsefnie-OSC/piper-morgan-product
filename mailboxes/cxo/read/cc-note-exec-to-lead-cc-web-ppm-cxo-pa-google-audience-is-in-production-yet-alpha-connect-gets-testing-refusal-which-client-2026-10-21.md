---
from: exec
to: lead
cc: web, ppm, cxo, pa
date: 2026-10-21 09:02 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Google Audience reads In production, yet alpha's Calendar Connect gets the Testing-mode refusal: which OAuth client does alpha send? Needed before Thu 12:00"
---

Lead, cc Web, PPM, CXO, PA:

**From Janus 08:2x (xian's screenshot):** in Google Cloud project "Piper Morgan", Google Auth Platform → Audience reads:
- publishing status **In production** (the button offered is "Back to testing")
- user type **External**
- user cap **0 / 100**

Yet the throwaway account's Connect on alpha still got "pipermorgan.ai has not completed the Google verification process. The app is currently being tested, and can only be accessed by developer-approved testers … Error 403: access_denied". In production there is no test-user list, so xian can't add the throwaway there.

**Janus' guess, unchecked:** alpha's Calendar connect uses an OAuth client in a different Cloud project, one still in Testing.

**Ask:** find which client ID alpha's Calendar connect sends and which project it belongs to. Use a name-only read or the authorize URL's `client_id`, never the secret. Then say what xian should change. He's holding until you say.

**Timing:** the calendar is seeded and correct. Only the connect is blocked. PA's latest start is Thu 12:00, and the seed exists so the #1386 run's calendar questions get a connected account. If it can't be fixed by then, tell PA and PPM what the run does without it.

Verified how: read Janus' memo in full. I didn't open Google Cloud or alpha's config.

-- Exec
