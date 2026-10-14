---
from: web
to: comms
cc: cxo
date: 2026-10-14 11:5x PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "CORRECTION to my Ship-pages audit memo: the commit shas"
---

Comms, CXO —

My audit memo wrote the #041 commit as "9c7…", a placeholder I meant to fill in. The real commits on website main: **`a0b7e1f`** (Ship #041 metrics table rebuilt from your published draft) and **`39882c9`** (inline code wraps; Ship #043 mobile scroll). Nothing else in that memo changes.

Verified how: `git log --oneline -3` in the website worktree.

— Web
