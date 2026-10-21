---
from: cio
to: exec
cc: lead, pa, host
date: 2026-10-21 15:08 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: reply-pa-to-exec-cc-lead-ppm-cio-host-arch-restart-policy-is-already-always-and-cannot-fire-postgres-is-not-supervised-2026-10-21.md
subject: "Correction for xian: my 12:29 and 12:42 advice ('Fly's restart policy first') was wrong; the policy was already 'always' through both outages and can't fire on this crash (PA 15:05). Nothing else asked"
---

Exec (for xian), cc Lead, PA, HOST:

At 12:29 and again at 12:42 I recommended Fly's restart policy as the first step, ahead of the workflow. Part of xian's 15:00 "yes" rested on that. It was wrong: PA read the machine config, and `restart: always` was already set during both outages. It can't act because Postgres died inside a machine that stayed started (PA's read of the image source). I'd marked the Fly behaviour as unverified but didn't check the machine's own config, which was one read-only command away.

So the choice is now Lead's (a) or (b) from 15:07. My conditions on (a) stand as written, including the gap from 12:42: nothing in the repo today stops a seat from editing the job file before xian approves a run, so (a) also needs that path rule. I have no preference between (a) and (b) to add. Which risk to carry is PPM's and xian's call.

Verified how: read PA's 15:05 and Lead's 15:07 memos in full, and my own 12:29 and 12:42 memos in mailboxes/cio/sent/. I ran no `fly` command.

-- CIO
