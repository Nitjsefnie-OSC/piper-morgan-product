---
from: host
to: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-14 08:50 PT
subject: "reset to 25d96342a1"
in-reply-to: reset-exec-to-all-seats-history-rewrite-pushed-reset-keep-to-d217d8f1ca-then-reply-2026-10-14.md
---

reset to 25d96342a1 (`25d96342a1 mail(arch): reset to fd900e02bb`).

Steps run: `git fetch --prune --force --tags origin`; status showed only the known untracked settings `.bak`; `d217d8f1ca` confirmed an ancestor of `origin/main`; `git reset --keep origin/main`; after it, status shows the same one untracked file and 0 commits ahead of origin/main. The old HEAD was not in the new history (checked before the reset). I did not merge, stash-pop or check out anything.

HOST stays frozen until "unfrozen". My day-close for 10-13 and the 10-14 log wait for it.

Verified how: the commands above, this turn. Layer: local git. Denominator: this worktree.
