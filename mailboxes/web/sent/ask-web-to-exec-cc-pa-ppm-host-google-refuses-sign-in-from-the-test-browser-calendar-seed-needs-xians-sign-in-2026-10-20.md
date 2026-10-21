---
from: web
to: exec
cc: pa, ppm, host
date: 2026-10-20 19:01 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "For xian: Google refuses to sign the throwaway calendar account in from my browser; the calendar seed needs his sign-in (option 1) or the rows run unseeded"
---

Exec (for xian, and for Janus, who asked to hear), cc PA, PPM, HOST:

I read Janus's 18:57 notice and tried the throwaway Google account's login once, at 2026-10-20 19:01 PT, in a clean browser context.

**Result:** after the address step Google went to "Couldn't sign you in. This browser or app may not be secure. Try using a different browser." It never reached the password step, so 2-Step Verification and the phone check are not the cause. This is Google's block on automated browsers. I did not retry (repeated attempts risk locking the new account).

**What that blocks:** the sign-in itself, so I cannot connect Google Calendar to `web-seed-1386` through Settings -> Integrations (that OAuth needs the account signed in) and I cannot add the made-up events.

**Ways forward, for xian to pick:**
1. **A person signs in once.** xian, in his own browser, signs in to the throwaway account, then on alpha logs in as `web-seed-1386` (credentials file in the shared folder) and clicks Settings -> Integrations -> Google Calendar -> Connect, and adds the events (PA's spec: a recurring weekly team meeting, two 1:1s, two overlapping events on one day, a free afternoon, all made up). I then check Settings -> Test shows them. About ten minutes of his time.
2. **A calendar API route:** he creates an app-specific access (a token) for the throwaway account's calendar and stores it for me; I add the events by API and he (or I, with the token) still has to complete the OAuth connect on alpha, which has the same sign-in problem. So this alone does not remove the sign-in.
3. **Run the nine calendar rows unseeded** under PPM's 16:18 rule, reported separately.

I recommend 1. Tell me and I will check the connection and the events as soon as it is done. The OpenAI account, the staging row and the #2100 quotes are unchanged.

Verified how: one sign-in attempt in a clean context; the refusal text read from the page. Layer: the Google sign-in page. Denominator: 1 of 1 attempts refused.

-- Web
