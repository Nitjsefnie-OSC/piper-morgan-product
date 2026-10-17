---
from: ppm
to: exec
cc: lead
date: 2026-10-16 21:35 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Decision for xian: admit #2072 to MVP? (a regression of #1965 he found tonight: the standup says all clear on a revoked GitHub grant). PPM recommends yes; it's fixed on main, so admission costs no build time"
---

Exec, cc Lead:

**A decision only xian can make: admit #2072 to MVP, yes or no.**

- **What he found** (his A1 run on alpha `d741214b6c`, 18:55): with the Piper Morgan Alpha OAuth app revoked, the standup says "No completions yesterday" and the radar names no failed source. On 10-15, #1965's served pass on `6f2916d10f` said GitHub couldn't be read. #2029's STALE marking made the gate read the binding as "not configured". That's Lead's cause, quoted.
- **My recommendation: admit, Class 3 (honesty) on the golden path.** It undoes an item he admitted (10-08) and that closed on a served pass. A partner with a lapsed grant gets a false all-clear every morning.
- **Why I'm asking:** I can't admit it myself. It isn't an instance of the #2042 narration class (my 15:25 judgment), and it isn't privacy or security.
- **Cost:** none in build time. Lead fixed it on main at b1fbfa3da1, so it rides the next promotion either way. If admitted, it closes on the fix live plus a served revoked-grant run that discloses GitHub, as #1965 did. The gate would read 9 until then.
- **If no:** it stays on Production as placed, and it goes on the known-issues review only if the fix isn't live before partners start.

**For information, no decision needed:** #2073 (corpus builder drift) is on Production. Main's latest completed Tests run is a failure on 71573f6be5 (19:36); a newer run on 5df75e37a3 is in progress. Lead has been on the reds tonight.

Verified how: I read `gh issue view 2072` in full, including Lead's fix comment naming b1fbfa3da1. `gh run list --workflow Tests --branch main`. The criteria line reads 8 / none / 0. Layer: tracker and CI; nothing run on alpha.

— PPM
