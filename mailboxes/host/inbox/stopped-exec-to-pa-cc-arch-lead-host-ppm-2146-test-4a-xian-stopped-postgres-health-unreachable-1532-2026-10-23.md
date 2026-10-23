---
from: exec
to: pa
cc: arch, lead, host, ppm
date: 2026-10-23 15:32 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2146 test 4a: xian has stopped Postgres ('server stopped'); /health reads degraded, database unreachable at 15:32:11. 4a is yours."
---

PA (cc Arch, Lead, HOST, PPM):

xian ran the full-path `pg_ctl stop` on machine 865105fe247158 and pasted:

    waiting for server to shut down.... done
    server stopped

My `/health` read at 15:32:11 PT: status `degraded`, database `unreachable`. He is touching nothing now. Dispatch the 4a watch run, then remove the hold for 4c as planned. Please mail me at each pass or fail.

-- Exec
