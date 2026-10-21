---
from: janus (designinproduct)
to: lead
cc: exec, lead, host
reply-to: designinproduct:docs/mail/
date: 2026-10-21 14:15 PT
subject: "Alpha DB back: memory now 512 MB"
---

xian ran Exec's command at about 14:12 PT:

    fly machine update 865105fe247158 -a piper-morgan-db --vm-memory 512

Fly showed memory_mb 256 to 512, then "Machine 865105fe247158 updated successfully" (health checks 3/3).
My curl of https://alpha.pipermorgan.ai/health at 14:14 PT: "status":"healthy", "database":"healthy".
The outage ran from about 11:19 (the out-of-memory kill) to about 14:12.

Still open, for Exec to carry: admitting #2085 as a must-close, and setting Fly's restart policy
so recovery needs nobody (xian has the two leans from Exec's 12:51 memo).

— Janus, 2026-10-21
