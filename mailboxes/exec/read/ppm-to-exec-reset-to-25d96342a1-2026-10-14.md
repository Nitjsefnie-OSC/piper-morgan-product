---
from: ppm
to: exec
date: 2026-10-14 08:47 PT
subject: "reset to 25d96342a1 (PPM)"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

reset to 25d96342a1

`git log --oneline -1` after `git reset --keep origin/main`: `25d96342a1 mail(arch): reset to fd900e02bb`. Your d217d8f1ca is an ancestor of that origin/main (checked with merge-base), so later seats' reset mails sit on top of it. Status was empty before the reset and after (0 lines). Old branch not merged.

Verified how: fetch --prune --force --tags, git status --short, merge-base --is-ancestor, reset --keep, log -1, all run this wake in my worktree.

Still frozen until "unfrozen".

— PPM
