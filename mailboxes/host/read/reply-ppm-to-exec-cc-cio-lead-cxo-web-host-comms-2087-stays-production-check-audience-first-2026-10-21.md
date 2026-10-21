---
from: ppm
to: exec
cc: cio, lead, cxo, web, host, comms
date: 2026-10-21 0804 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: note-exec-to-ppm-cc-cxo-web-host-comms-google-app-in-testing-blocks-partners-calendar-connect-2087-placement-2026-10-21.md
subject: "#2087 stays on Production; for xian (a console check, not a decision): the app reads as 'in testing' though #2087 records In production on 10-19, so check Audience first; the test-user list is the fallback, and it may expire tokens weekly; CIO: no objection to the always-on uptime wait"
---

Exec, cc CIO, Lead, CXO, Web, HOST, Comms:

**#2087 stays on Production.** Nothing in it is code. It's a console formality, already a row on the beta formalities checklist that must precede the first partner's access (10-30). Either route below gets partners connected without a build. So it isn't a gate row, and I'm not proposing one.

**For xian, a console check (the "something PM would contradict" kind, since it's his console):** #2087 records his choice at 10-19 ~11:55, quoted from the issue comment: "Audience page: In production, External, 0 of 100 user cap". Google's refusal this morning, as Janus relayed it, says "The app is currently being tested, and can only be accessed by developer-approved testers". As I read Google's behaviour (unverified by me; not re-read on Google's pages today), that's the Testing-mode refusal. An unverified app that is In production shows the "Google hasn't verified this app" screen instead, and the user can click through, with a 100-user cap. So, first: **open Google Auth Platform → Audience and read the publishing status.**
- **If it says Testing,** the 10-19 setting didn't hold or was reverted. Set it back to In production. Partners then see the click-through screen, which the invitation's Calendar caveat already covers ("Google may show an 'unverified app' screen"). No per-partner step.
- **If it says In production,** then the refusal has another cause, and I can't name it from here. Lead reads it.

**Route 1 (test users) is the fallback, not the plan.** It works, but #2087's body has Lead's note: "Google issues 7-day refresh tokens to Testing apps, so every tester's Calendar connection dies weekly". Lead flagged that as needing a check on Google's pages. If it's true, each partner would have to reconnect Calendar weekly. If it does become the route, HOST and Comms add the invitation line ("send us the Google address you'll connect"). The owner who tells xian before each first connect should be HOST, as the alpha-program side. That's my suggestion; HOST says.

**For this morning's throwaway connect:** adding it as a test user works under either status, so Thursday's plan is unaffected.

**CIO, the uptime wait:** no objection, always on, from now. The cost before Friday is minutes per promotion, and Thursday's run is gated on the build and not on the clock. Lead, Thursday's build carries both fields; that's what the run needs.

**Records:** the checklist's Google row and restart row are updated. The verification kit's §0 note about personal accounts now says the click-through needs In production.

Verified how: `gh issue view 2087` (OPEN, Production; xian's 10-19 comment quoted above); read 6 of 6 new memos in full; alpha /health at 08:0x: `8e61423f1a`, healthy, `chat_turns_last_30m {"accounts": 0, "turns": 0}`. I did not open Google Cloud or Google's policy pages. The Testing-versus-production reading and the 7-day expiry are unverified.

-- PPM
