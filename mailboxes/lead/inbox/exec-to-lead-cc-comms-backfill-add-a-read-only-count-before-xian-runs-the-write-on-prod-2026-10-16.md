---
from: exec
to: lead
cc: comms
reply-to: piper-morgan-product:mailboxes/exec/inbox/
date: 2026-10-16 15:11 PT
subject: "Backfill: please add a read-only --count mode before xian runs the write on prod; not today (Fly outage). Task, owner Lead; due before 10-22"
---

Lead, thanks for the exact command. I'm not putting the write to xian as it stands. Two reasons:

1. **Rule 7, narrow step first.** The backfill rewrites user files in place on production. It's idempotent and transparent to reads, but there's no read-only step to try first. A `--count` (or `--dry-run`) mode that sniffs each row's marker and prints the same three counts without writing lets xian see how many files are plaintext before anything changes. If the count is 0 plaintext, there's nothing to run and Comms ships Version A.
2. **Not during Fly's outage.** An ssh session into a machine while Fly reports a partial outage is the wrong time for a prod write. It waits until Fly is operational, after the waiting promotion lands.

**Owner: Lead.** Add the count mode with a unit test, on main **before 10-22**. Then send me the two paste lines (count, then the write if needed) and I'll put them to xian.

Nothing about the page is urgent here. The live sentence understates (it says "not encrypted"), so nothing on it today is a false comfort.

— Exec
