---
from: ppm
to: exec
cc: lead, cxo, arch
date: 2026-10-17 1535 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2072 admitted (Class 3), gate 6 -> 7, ledgered; DECISION FOR XIAN: admit #2077 (token field may autofill the Piper password and send it to GitHub) as Class 2?"
---

Exec, cc Lead, CXO and Arch:

**1. #2072 admitted, on xian's word relayed by Lead** (15:09, "I agree with PPM's recommendation"). Your ruling of record supersedes the relay if it differs.
- Milestone MVP. The body carries the Gate class 3 line, and the ledger has the seventeenth entry: 6 -> 7 open MVP, 0 days moved.
- It closes when, on alpha with the grant revoked:
  - the standup and the work-focus reply say GitHub can't be read (#2076, on Production and gated through #2072; it rides tomorrow's first promotion);
  - "what's connected?" doesn't say connected (the renderers are live on `118241587e`);
  - CXO accepts it served.
- Class 3 means it's disclosed if still open at partner start, not a must-close. The must-close set is still #2064 alone.

**2. A decision only xian can make: admit #2077 to MVP as Class 2 (Security, credential exposure)?**
- **What:** PA filed it. On Settings → GitHub the token input is `type="password" autocomplete="off"`, and Chrome ignores that. The browser can fill the field with the saved Piper sign-in password. If the user presses Reconnect or Update, the Piper password goes to GitHub's API as a token.
- **Evidence:** on card A1 today xian saw a masked value in the field. The page's own code doesn't set that in this state. It is unverified whether it was autofill: PA's one-line length check hasn't been run.
- **My recommendation: admit.** It is a latent credential leak to a third party, and xian's 16:18 "latent risks count" puts known latent security risks inside the design-partner bar. If admitted, it joins #2064 as a must-close item.
- **Cost:** about one line. CXO (15:32) says `autocomplete="new-password"` is the right fix.
- **Closing condition if admitted:** that attribute live on alpha with its test, plus either PA's check reading 0 on a browser with a saved Piper password, or the attribute quoted from the served page with that limit named.
- **For now** I've placed it on Production with the admission asked, the same way #2072 waited.

Arch: does Class 2 (credential exposure) fit, in your reading? If you see it otherwise, say so and I'll change the ask.

Also ledgered on the review page: #2031 closed (CXO 15:32), and #2073 is closed (Lead, a2e001492a).

Verified how: `gh issue view 2072` shows milestone MVP with the class line in the body; `gh issue view 2077` shows Production; the criteria line reads 7 open MVP, none missing from the order doc, 0 unmilestoned. The template line is quoted from PA's issue, not re-read by me. Nothing served by me.

— PPM
