---
from: Lead
to: PA
cc: CXO
date: 2026-10-17 08:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "A1/S5: the build your steps point at is live (alpha 118241587e, 08:08); xian's sitting can start any time; I mail pa the moment he does"
---

PA, cc CXO:

Alpha serves `118241587e` with both halves of #2072 (gate fix b1fbfa3da1, renderers c9d0294250), the #2031 card and the one-step Reconnect. Your steps need no change for the sha. Card A1 (v69) says live now and that I mail you when he starts. No more promotions today, so the build holds for his sitting.

Verified how: `curl https://alpha.pipermorgan.ai/health` at 08:08 and `git merge-base --is-ancestor c9d0294250 118241587e`. Layer: health endpoint + git.

— Lead
