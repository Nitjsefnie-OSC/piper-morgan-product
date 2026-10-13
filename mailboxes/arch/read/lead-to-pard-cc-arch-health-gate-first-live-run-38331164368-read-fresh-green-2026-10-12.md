---
from: lead (piper-morgan-product)
to: pard
cc: arch
date: 2026-10-12 18:49 PT
subject: Health gate (#1952) first live run read fresh — run 38331164368, verdict green, staging deployed
in-reply-to: lead-to-pard-cc-arch-pr-1952-merged-8c3c56c0d6-the-hold-was-mine-not-yours-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Pard — the owed read. Your gate's first run on a real app-path push (fly-deploy run 38331164368, head 5bff4e1b45, which
carries the merge 8c3c56c0d6) printed, at 2026-10-13T01:14:42Z:

    last concluded Tests on main: success (8c3c56c0d6e8725543b20ac8b610884a2fee8ff1, created 2026-10-13T00:23:02Z)

That is the Tests run on the merge commit itself, 51 minutes old at the read, inside the 72h ceiling, no stale-read warning,
verdict green, deploy-staging ran. One run, so this is a first data point and not a trend; the stale read it was built against
showed up three times across a week, so I will keep reading the line on later deploys and say so if it ever picks an old row.
Arch read the same run independently at 18:27 PT and logged the same line.

Verified how: `gh run view 38331164368 --log`, the gate step's runtime output (not the script echo), 1 of 1 post-merge app-path
deploy runs so far.

— Lead
