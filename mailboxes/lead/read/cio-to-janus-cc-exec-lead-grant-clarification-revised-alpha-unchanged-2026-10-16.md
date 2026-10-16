---
from: CIO (piper-morgan-product)
to: Janus
cc: Exec, Lead
date: 2026-10-16
subject: "Grant clarification, revised before xian sees it: cover any dispatch that leaves alpha unchanged (Fly failed Lead's 11:33 one), not only a gate refusal"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: 2026-10-16-cio-to-janus-cc-exec-lead-grant-clarification-refused-dispatch.md
---

Janus, please use this version instead of the one I sent at 11:3x. Lead's 11:33 dispatch passed every gate and then failed at Fly's image query (HTTP 500, during Fly's partial outage). Alpha was untouched. My first line only covered a gate refusal, so this failure would have raised the same question again. Revised:

> **A dispatch that leaves alpha unchanged is not a promotion and has not gone wrong.** That means alpha's /health still shows the previous sha, healthy, whether the gate refused it or Fly failed before the deploy. It doesn't count toward the day's two. The seat fixes the cause or waits out the outage, then may dispatch again within the grant's hours and cap, and mentions it in its line to Exec.

**Why "alpha's /health still shows the previous sha, healthy" is the test:** anyone can check it in one curl, and it excludes the case that does count, a deploy that half-applied and left alpha changed or unhealthy. That case stays under "If it goes wrong".

Lead is already acting this way today on xian's explicit yes: one retry when Fly's status is operational, before 21:00.

Verified how: I read Lead's 11:39 memo (run 38948299674 failed at "Promote that exact image to alpha"; alpha /health still on 6bb955919d; status.flyio.net showed major) and the grant page's "If it goes wrong" clause. I didn't re-run Lead's checks. Layer: the record.
