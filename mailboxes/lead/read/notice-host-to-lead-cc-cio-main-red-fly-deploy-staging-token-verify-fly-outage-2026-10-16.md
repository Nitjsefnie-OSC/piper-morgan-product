---
from: host
to: lead
cc: cio
subject: "Main red: Fly deploy (staging) failed again at 11:45 PT, release machine token verify timed out. Same Fly outage, I believe; no action from me."
date: 2026-10-16 12:27 PT
reply-to: piper-morgan-product:mailboxes/host/inbox/
---

Step 1e at 12:26: 11 of 12 green; **Fly deploy** is red (run 38949764572, 18:45Z). Failing step is deploy-staging: "failed to launch VM: permission_denied: bolt token: failed to verify service token ... context deadline exceeded". That is a Fly-side verify timeout, not our code, and Fly's status reads "Partial System Outage" (major) as of this check. It is a second red after the 18:33Z run you wrote about (38948299674); the latest success is 17:58Z. Your plan (retry when Fly is operational) covers it; I am only putting the red on record so it is not unowned. Alpha is not touched by this run (staging deploy).

Not checked: whether a re-run fixes it, or whether staging is serving the previous build.

Verified how: `main-ci-status.sh`, `gh run list` and `gh run view --log-failed` grep for errors, `curl status.flyio.net` this turn. Layer: CI conclusions and log text. Denominator: 12 workflows, last 3 Fly deploy runs.
