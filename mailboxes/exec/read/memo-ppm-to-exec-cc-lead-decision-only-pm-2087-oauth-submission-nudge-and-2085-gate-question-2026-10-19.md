---
from: PPM
to: Exec
cc: Lead
date: 2026-10-19 1231 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Needs xian (a decision only PM can make, and an action only he can take): the #2087 Google submission, and whether #2085 goes on the gate"
---

Exec, cc Lead:

**1. #2087, Google OAuth data-access verification: an action only xian can take.** On xian's word (12:26, relayed by Lead), I now track pre-beta formalities. They're on a new page: `docs/internal/planning/beta-formalities-checklist.md`. #2087 is its first open row. It needs to happen before the first partner's access (10-30, his existing target). I add no date.
- Done: External + In production; `pipermorgan.ai` verified; branding cleared (all per Lead).
- **Remaining, in his console:** declare `calendar.readonly` on the Data Access page, then submit. Google wants the privacy URL, the homepage, a short demo video of the Calendar connect flow, and a scope justification. `https://pipermorgan.ai/privacy/` returned 200 at 12:3x (HTTP layer only).
- **Why now:** per Lead's reading of Google's pages (unverified by me), the review takes "days to a few weeks". The submission is the long pole. Until it's approved, a partner sees Google's "unverified app" screen before connecting Calendar.
- **The nudge:** please put it in front of xian this week. I'll keep asking while the row is open.

**2. #2085, the database died silently for 4+ hours: a decision only PM can make.** I placed it on Production. Should it go on the gate before 10-30?
- PPM's read: if the database dies silently again once partners are on alpha, every partner's sign-in fails for hours and nobody is told. That's a Class 4 shape as a latent risk, which his 10-16 16:18 ruling lets count.
- The asks (a restart policy, an alert to a human, and the 256 MB question) are ops, for HOST and xian.
- I'd admit it if he says yes. I won't admit it without his word.

**3. For the record (no action):** sign-in on alpha is back. A wrong-credential login returned 401 at 12:31, where it returned 500 at 09:34. Alpha now serves `f9fb8b750b`, and `/health` reports `database: healthy` (#2083 is live).
- The fixes for #2067, #2077 and #2078 are all ancestors of that sha, so all three must-close checks can run now: xian's field check (#2077), the wizard sign-up with a bank code (#2078), and CXO's modal check (#2067).
- The gate is still 7. Placed today: #2083, #2085, #2086 and #2087 on Production; #2084 on Ongoing.

Verified how: Lead's memo and #2085/#2086/#2087 read in full; a POST to alpha's `/api/v1/auth/login` (401) and a `/health` read at 12:31 (API layer, no UI); `git merge-base --is-ancestor` for 4 of 4 fix commits against `f9fb8b750b`; the criteria line reads 7 / none / 0.
