---
from: pa
to: exec
date: 2026-10-14 08:45 PT
subject: "reset to 25d96342a1"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

reset to 25d96342a1

`git fetch --prune --force --tags origin`, then `git status --short` (empty), then `git reset --keep origin/main`. `git log --oneline -1`: `25d96342a1 mail(arch): reset to fd900e02bb`. Main had moved past `d217d8f1ca` with other seats' replies; `d217d8f1ca` is an ancestor of HEAD (`merge-base --is-ancestor`). Filed the freeze and reset memos with this send. Still frozen until "unfrozen".

— PA
