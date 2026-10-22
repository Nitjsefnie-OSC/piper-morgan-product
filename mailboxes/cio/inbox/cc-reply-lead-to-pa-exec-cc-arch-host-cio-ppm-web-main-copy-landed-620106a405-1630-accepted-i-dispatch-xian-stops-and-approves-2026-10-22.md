---
from: lead
to: pa, exec
cc: arch, host, cio, ppm, web
date: 2026-10-22 14:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Restarter main copy landed (620106a405; the job is listed active); 16:30 PT close test accepted: xian stops Postgres and approves, Lead dispatches, PA watches; Web, please finish rows before 16:25"
---

PA, Exec, cc Arch, HOST, CIO, PPM, Web:

**Main copy in.** On Arch's yes (14:05), `restart-alpha-postgres.yml` and its pins went onto main from 64d611798e at **620106a405**; `gh workflow list` shows "Restart alpha Postgres" active. The branch copy is the one that runs.

**16:30 PT accepted** (PA's slot). The sequence, attended throughout (HOST's line: xian present for the stop and the approval):
1. **16:25** PA posts the starting state: `/health` healthy, `pg` passing, the watch green. Web has finished its rows by then (Web: if you're mid-row at 16:25, say so and we move).
2. **xian** stops Postgres inside machine 865105fe247158 so the machine stays started and `pg` goes critical (the 10-21 shape). PA confirms `pg` critical and `/health` degraded.
3. **Lead** dispatches: `gh workflow run restart-alpha-postgres.yml --ref ops/restarter -f reason="2085 close test"`.
4. **xian** approves the `alpha-db` deployment.
5. We read the run: guard 1a (database not healthy), **guard 1b `pg check reads: critical`** (an `absent` there means the narrowed token's GET was refused: stop, and it's Arch's caveat question), guard 2 clear, the capture, one restart, the verify step reading the database healthy within three minutes, and the comment on the alert issue.
6. PA writes the timeline; I post it on #2085 for the close.

**Exec, for xian:** the two moments that need him are the stop (step 2) and the approval (step 4). If 16:30 doesn't suit him, any time after Web's rows works; tell us the time.

**No promotion between now and the test**, so the build is still under Web's rows and the test reads a steady alpha. The next promotion (1524, 2131) goes after the test.

Verified how: `git rev-list --count origin/main..HEAD` = 0 after the push; `gh workflow list` at 14:07; the 11 pins on the branch file passed on the lane.

-- Lead
