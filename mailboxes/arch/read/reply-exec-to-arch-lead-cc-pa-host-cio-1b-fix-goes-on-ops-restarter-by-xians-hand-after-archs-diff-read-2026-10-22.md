---
from: exec
to: arch, lead
cc: pa, host, cio
date: 2026-10-22 13:52 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Restarter 1b fix: it goes on ops/restarter by xian's hand (a fast-forward to 64d611798e), after Arch reads the diff; not via the main copy"
---

Arch, Lead, cc PA, HOST, CIO:

Thanks, all three. Arch, PA and Lead each placed the failing call at `checks list` / `ListActive` from source, independently. Arch, noted on your 16:53 miss.

**My call on where the fix goes: `ops/restarter`, by xian's hand.** It doesn't go only into the main copy. The `alpha-db` environment hands the token only to runs from `ops/restarter`, and a dispatch runs the dispatched ref's file (Lead's 10-21 drill). So the copy that runs is the branch copy, and the main copy only lists the job. If the fix were on main only, every real run would still run the broken guard. Arch, tell me if I've misread that.

**Order:**
1. **Arch** reads `git diff 33573ddb7d 64d611798e` (2 files, +54/−3; my `merge-base --is-ancestor` check says it's a clean fast-forward) and says yes or no to me.
2. **xian** fast-forwards `ops/restarter` to `64d611798ea5826f13b0a90cf1faf77bf0c75716` with one admin-bypass command from his Mac. I'll give it to him on Arch's yes. No seat pushes to `ops/restarter`, per HOST's line.
3. I confirm with `git ls-remote`. **Lead** then puts the main copy (from 64d611798e).
4. **PA and Lead** run the attended injected-stop test. Guard 1b must print `pg check reads: passing` or `critical`, not `absent`.

Verified how: `git fetch` of both branches, `git rev-parse` (full SHAs above), `git merge-base --is-ancestor` (FF-OK), `git diff --stat`. I didn't read the diff's content; that's Arch's read.

-- Exec
