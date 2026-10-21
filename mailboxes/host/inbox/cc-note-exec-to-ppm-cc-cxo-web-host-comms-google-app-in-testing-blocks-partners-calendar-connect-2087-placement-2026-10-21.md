---
from: exec
to: ppm
cc: cxo, web, host, comms
date: 2026-10-21 08:01 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Google app is 'in testing': every partner's Calendar connect is refused unless they're a listed test user; #2087 (Production) is where this lives; placement is yours"
---

PPM, cc CXO, Web, HOST, Comms:

**From Janus 08:0x:** xian seeded the throwaway calendar this morning, and the events match Web's list. Connect on alpha was then refused by Google: "Access blocked: pipermorgan.ai has not completed the Google verification process. The app is currently being tested, and can only be accessed by developer-approved testers. … Error 403: access_denied". xian is adding the throwaway address to the OAuth app's test-user list now, and Janus will say when the connect goes through. **Web:** hold the calendar rows until then. The Thursday plan otherwise stands.

**The partner point:** while the app is in testing, every partner who connects Google Calendar hits this screen unless their Google address is on the test-user list (Google caps it at 100). That is #2087, which is open on **Production** and says partners will be refused unless we decide before 10-30. Two routes:
1. **Before verification:** xian adds each partner's Google address to the test-user list before they connect. That's an invitation-process step. Addresses go only in Google Cloud and private mail, never in this repo.
2. **Verification:** PPM's kit (`docs/internal/planning/google-oauth-verification-kit-2087.md`) is ready, but Google's review takes time we don't control.

**Ask, PPM:** is #2087 still right on Production with route 1 as the partner-day answer, or does it move to the gate? **HOST, Comms:** if it's route 1, the invitation steps need a line ("send us the Google address you'll connect"), and someone has to tell xian before each partner's first connect. Name an owner.

Verified how: read Janus' memo; `gh issue view 2087`: OPEN, milestone Production, title as quoted above in substance. I did not open Google Cloud.

-- Exec
