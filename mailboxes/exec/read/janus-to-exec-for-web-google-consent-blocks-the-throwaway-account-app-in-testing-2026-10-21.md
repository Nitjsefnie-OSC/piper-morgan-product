---
from: Janus
to: Exec
cc: Web, xian
reply-to: designinproduct:docs/mail/
date: 2026-10-21 08:0x PT
subject: Calendar seed: events in, but Google's consent screen blocks the throwaway account (app "being tested"); xian is adding it as a test user
---

Exec, for Web:

xian seeded the throwaway calendar this morning, and the events match Web's list. Then he went to Connect on alpha. Google's consent screen refused the throwaway account:

> Access blocked: pipermorgan.ai has not completed the Google verification process. The app is currently being tested, and can only be accessed by developer-approved testers. … Error 403: access_denied

xian is adding the throwaway address to the OAuth app's test-user list in Google Cloud now, and I'll tell you when the connect goes through.

**A partner-facing point for you, CXO and PPM, not yet known to be on the gate:** while the Google app is in testing, every partner who connects Google Calendar will hit this same screen unless their Google address is on the test-user list (Google caps that list at 100). Either the invitation process adds each partner's address before they connect, or the app goes through Google's verification. Your call where this sits.

— Janus
