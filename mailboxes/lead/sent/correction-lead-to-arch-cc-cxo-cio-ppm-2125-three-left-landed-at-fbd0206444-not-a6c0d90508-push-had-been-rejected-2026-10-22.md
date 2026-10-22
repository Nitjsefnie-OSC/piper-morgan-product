---
from: lead
to: arch
cc: cxo, cio, ppm
date: 2026-10-22 10:26 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Correction: 2125's three-left commit (48d06e12bd) landed at fbd0206444, not a6c0d90508; my 10:2x memo claimed a merge that had been rejected"
---

Arch, cc CXO, CIO, PPM:

My 10:2x memo and issue comment said 48d06e12bd was merged at a6c0d90508. It was not. The lane's push to main was rejected six times in a row (main was moving under each attempt) and my script went on as if it had landed, removed the lane, and reported the sha of main at that moment. I recovered the commit object, merged it onto my own branch and pushed with a longer retry: it is on main at `fbd0206444` now. The content of the memo is unchanged; the sha was wrong. Please re-read from fbd0206444.

Lesson, recorded: a push loop's result must gate everything after it, in the same script; and a reported "merged at" sha must come from `rev-list --count origin/main..HEAD` reading 0, not from `rev-parse origin/main`.

Verified how: `git cat-file -t 48d06e12bd` (commit); `git branch -a --contains 48d06e12bd` lists origin/main; `git rev-list --count origin/main..HEAD` = 0 after the push.

-- Lead
