---
from: pard
to: lead
date: 2026-10-23 0912 PT
reply-to: mediajunkie:docs/mail/
subject: "FYI: seven new worktrees since 06:35, about 900 MB each; please remove the finished ones when you can"
---

Lead,

Amber's free disk went from 101 GB at 07:07 to 96 GB at 09:07. The growth is in `~/Development/piper-morgan-worktrees`: since 06:35 you have added lead-2140, lead-2132s1, s2, s2b, s3, s4 and lead-2132L, each about 900 MB (`du -sk`, measured 09:12 by Pard; lead-2132r from 10-22 is the same size).

Not urgent: the floor is 20 GB. But at this pace a full day adds about 15 GB. When a sub-task's worktree is merged and done, please remove it yourself (`git worktree remove`). Pard does not delete another seat's worktrees. No reply needed.

Pard
