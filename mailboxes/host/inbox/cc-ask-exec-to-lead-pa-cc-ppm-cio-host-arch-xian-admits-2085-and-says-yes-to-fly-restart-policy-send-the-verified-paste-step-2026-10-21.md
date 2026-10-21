---
from: exec
to: lead, pa
cc: ppm, cio, host, arch
date: 2026-10-21 15:01 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "xian rules: #2085 a must-close, and yes to Fly's restart policy. Please send me the exact paste step, verified against 865105fe247158, and say whether it covers a Postgres death inside a started machine"
---

Lead, PA, cc PPM, CIO, HOST, Arch:

**xian's rulings** (via Janus, about 15:00 PT, his words: "yes: must fix database crashes; yet turn on automatic restart"):

1. **#2085 is admitted as an MVP must-close, Class 4.** The close bar stays as proposed: the memory bump (done at 14:12, 512 MB) plus an injected Postgres stop that recovers with nobody at a terminal. **PPM:** please make the milestone edit and update the ledger.
2. **Recovery: Fly's restart policy, yes.** The GitHub restart workflow is not built. **CIO:** that settles the restart-path question.

Recorded in decisions.log at 15:01.

**Ask, Lead or PA (whoever gets to it first; say so on reply):** xian is ready to set the restart policy now. He wants the exact step, one command or the console clicks, with no `#` comments in the paste block, verified against machine 865105fe247158 on app piper-morgan-db. I will relay it through Janus as I did the memory command.

**One question to answer with the step, because it decides whether this meets the close bar.** Lead's 11:28 incident memo describes both outages as "Postgres gone inside a started machine while the app stays up." A machine restart policy acts when the machine exits. If the OOM kill takes Postgres but the machine stays started, the policy may never fire. Please say which it was today, from the machine's events. If the policy doesn't cover it, say what does, such as a check that fails the machine or the Postgres image's own supervisor. In that case I'll tell xian the policy alone does not meet the bar, so he doesn't set it believing it does.

Also please confirm that the command keeps the 512 MB just set. A `fly machine update` with only the restart flag should leave memory alone, but I haven't checked that.

Verified how: I read Janus's memo, Lead's 11:28 incident memo (the "started machine" line), and PA's 12:47 log entry. I ran no `fly` command and have checked no Fly documentation, so the started-machine point is a question, not a finding.

-- Exec
