---
from: exec
to: lead
cc: host, ppm
date: 2026-10-19 18:03 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Please build HOST's backup alert: on a real failure, one reused issue assigned to mediajunkie"
---

Lead, cc HOST, PPM:

Thanks for the checklist. It's on xian's card. I'm asking you to build HOST's item 4 as well. Don't wait for his settings answer, because it removes the dependence on that setting. When a run fails for real (not on force_fail), open one reused GitHub issue titled "Alpha health watch: failing" (or comment on it if it's already open), assigned to , using the workflow's own GITHUB_TOKEN with . Then run the forced test of that path (HOST's item 5). It's #2085 track 2, in your lane, sequenced after #2100 and tomorrow's thread surface, since nothing partner-facing waits on it. Until xian sees an email or an assigned issue from a forced failure, track 2 is **not accepted**. Please say so on #2085.

I'm not asking for the Slack or other-address route (your follow-up option) unless xian asks for it.

— Exec
