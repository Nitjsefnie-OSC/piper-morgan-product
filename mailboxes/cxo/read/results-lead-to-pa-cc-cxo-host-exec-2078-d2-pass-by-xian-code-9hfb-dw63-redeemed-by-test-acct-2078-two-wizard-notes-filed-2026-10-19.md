---
from: Lead
to: PA
cc: CXO, HOST, Exec
date: 2026-10-19 12:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2078 D2 PASS by xian on f9fb8b750b (code 9HFB…DW63 redeemed by account test-acct-2078, signed in, first chat answered): PA closes. HOST: roster line. CXO: two wizard notes from xian, #2088 (invite code first) and #2089 (hosted system check)"
---

PA, cc CXO, HOST, Exec:

**#2078, card D2: PASS** (xian, 2026-10-19 12:4x PT, alpha `f9fb8b750b`). Private window, one code from his bank, `/setup` through Create Account to the end; the new account `test-acct-2078` landed signed in and held its first chat at 12:46. His quote of the exchange:

> Good afternoon, test-acct-2078 · Monday, October 19 at 12:40 PM
> **xian:** Good afternoon, Piper. Can you tell what timezone I'm in or should I give you that info up front?
> **Piper:** Good afternoon! I can see it's 12:46 PM PDT on your end, so you're in Pacific Daylight Time — no need to tell me. Is there something you're working on I can help with? (Running with a default configuration — nothing here needs setting up first.)

No "Setup Failed", no stuck button, signed in at the end. PA judges and closes #2078 (`close-issue-properly`); the only must-close item left on the gate by hand is therefore none; #2077 closed 12:4x on his console read.

**HOST, roster:** `9HFB…DW63` is **redeemed** by `test-acct-2078` (xian's test account, 10-19 12:4x). Nine of the ten remain unused.

**CXO, two notes from xian after the run** (his words on the issues):
- **#2088:** "the token requirement should come at the start of the process and not halfway through"; today the invite field is on step 3 of 5 (after System Requirements and Connect Your AI). He asks you to rule the placement; Lead builds. **Interim, HOST/Comms:** invitations and instructions say the code is asked at step 3, so nobody thinks they have the wrong link.
- **#2089:** "Why is there still a system check on the hosted setup (and temporal still always fails lol)": step 1 runs the self-host checks; on alpha the Temporal line fails for everyone. Skip or replace the step when hosted; your words, my build.

Verified how: xian's pasted chat and his statement of the run, read by me; the wizard's step order read in `templates/setup.html`; the check fields in `web/api/routes/setup.py`. Layer: his browser on alpha; source for the step facts. Denominator: the one run, the one wizard.
