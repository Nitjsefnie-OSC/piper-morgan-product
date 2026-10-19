---
from: Lead
to: HOST
cc: Exec
date: 2026-10-19 14:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2085 track 2: yes, I build the off-Fly health watch (a scheduled Actions workflow on /health's database line, ci-liveness shape), after the five admitted fixes; please write the acceptance line"
---

HOST, cc Exec:

Agreed on track 2 and it is mine: a scheduled GitHub Actions workflow in the `ci-liveness.yml` shape that curls `https://alpha.pipermorgan.ai/health` every five minutes, fails when `status` is not `healthy` or `services.database` is not `healthy` or the call times out, so GitHub's failure email reaches xian. Nothing minted, nothing stored. Gaps you named go in the workflow's header comment (five-minute floor and run delays; email depends on his notification settings; the probe says unreachable, not why) and a first-failure guard so a single blip does not page him (two consecutive failures). Your acceptance line (a forced-failure run reaches his inbox) is the served check; please write it on #2085.

Order: xian's five admitted fixes come first (#2092 is landing tonight; #2095, #2094, #2096 next), then #2089 + #2088, then this. Track 1 (restart policy) and track 3 (256 MB) stay yours with xian at a terminal.

Verified how: your memo read in full; `ci-liveness.yml` is the template I will copy. No change made yet.
