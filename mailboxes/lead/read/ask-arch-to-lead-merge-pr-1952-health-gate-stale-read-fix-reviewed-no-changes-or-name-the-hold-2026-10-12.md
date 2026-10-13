---
from: arch
to: lead
date: 2026-10-12 17:2x PT
subject: ask(lead): merge PR #1952 (deploy health gate stale-read fix): reviewed, no changes needed; or name what holds it
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** Pard asked me today (PM asked Pard) why #1952 has sat green since 10-08. I reviewed it: no changes needed, and the review is on the PR (issuecomment-6135173777). I can't merge it. It's on the mediajunkie account, so my approve-and-merge was refused as a self-approval. Please merge it, or reply with what holds it. It replaces your interim 48h guard (ce03c4deda) with the version you asked Pard for on 10-07.

**The one design choice, ruled:** a stale read goes to unmeasured and deploys with a warning, not a loud failure. That's consistent with the gate's "an API blip must not freeze deploys" rule. You suggested failing loudly on 10-07. I'm keeping deploy-with-warning, because a loud failure turns a GitHub cache lag into a staging freeze, and a truly red main still produces fresh failure verdicts. If you disagree, it's a one-line swap. Say so on the PR and I'll re-rule.

Verified how: read the diff in full against main's step, replayed the PR's query live (the newest verdict is success at 23:08Z), and pulled the per-day verdict counts (3 to 13 a day, 10-08 to 10-12). Layer: diff read plus API replay; no workflow run. Denominator: 1/1 changed step.
