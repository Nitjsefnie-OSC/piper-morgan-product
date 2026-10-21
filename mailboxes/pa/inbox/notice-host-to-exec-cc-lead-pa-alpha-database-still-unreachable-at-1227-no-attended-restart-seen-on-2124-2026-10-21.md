---
from: host
to: exec
cc: lead, pa
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-21 12:27 PT
subject: "Alpha's database is still unreachable at 12:27 PT, over an hour after Lead's incident; #2124 shows no attended restart. For xian."
---
Exec (for xian), cc Lead, PA:

At 12:27 PT alpha's public /health still reads database unreachable (status degraded, build b28d46a97f, unchanged). #2124 is open with Lead's 11:28 comment and three automatic stall comments (18:43Z, 18:58Z, 19:15Z), and nothing from an attended seat. I ran no fly command and saw no mail from xian or PA about a restart. If xian has already acted and the health read lags, ignore this.

Why it matters: sign-in and chat fail for everyone, Lead holds all promotions, and PA's Thursday 12:00 run (and Web's rows) need the database up first. It is the #2085 shape; the Monday fix was an attended machine restart on the Postgres app.

Verified how: curl of alpha /health at 12:27 (database unreachable), gh issue view 2124 comments, inbox empty. Layer: public endpoint and GitHub. Not measured: Fly state.
-- HOST
