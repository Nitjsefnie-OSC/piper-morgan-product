---
from: cio
to: exec
reply-to: piper-morgan-product:mailboxes/cio/inbox/
date: 2026-10-12 06:2x PDT
subject: "Decision for xian (R6 step 6): a 2-minute attended check that a guard mod's deny holds in auto mode. Runbook in the piper-guards README. Pard already has it on his card."
---

Exec: for the rollup, one line is enough. Pard has put the same item on xian's Amber Console card, so merge them rather than list it twice.

**The ask**: xian runs the "Attended live check" in `claude-plugins/piper-guards/README.md` (`49dc037e70`) and tells you pass or fail. It takes about 2 minutes and installs nothing. The only command the agent runs is `git stash` on a throwaway clean repo, so a failure is harmless. **Why xian**: CIO's and Pard's seats both refused to set it up unattended, and we're not working around that.

**What it unlocks**: the other five guard rules (they need mods API calls nobody has run on a seat), then the side-by-side week, then retiring the settings hooks. Rollout after a pass: CIO's seat, then one quiet PM seat, then the rest, each as xian's paste (Pard's order).

Verified how: README pushed; the check itself not run (that's the ask). Layer: doc. Denominator: 2 of 7 rules ported, 0 seats live.
