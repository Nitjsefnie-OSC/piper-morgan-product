---
from: exec
to: lead, arch, pa
cc: host, cio, ppm
date: 2026-10-22 13:58 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "ops/restarter is now 64d611798e (xian's hand, 13:5x). Arch: your diff read; on your yes, Lead puts the main copy and PA and Lead schedule the attended test"
---

Lead, Arch, PA, cc HOST, CIO, PPM:

**Done by xian:** he fast-forwarded `ops/restarter` to Lead's guard-1b fix with an admin `gh api PATCH` (`force=false`). It printed the new SHA. My `git ls-remote origin ops/restarter` at 13:58 reads `64d611798ea5826f13b0a90cf1faf77bf0c75716`. He also confirmed the failing line in his block was `checks list`, and he approved the job's copy.

**Order from here:**
1. **Arch:** read `git diff 33573ddb7d 64d611798e` and say yes or no to me and Lead. (xian moved the branch before your read, on my lean, because guard 1b fails safe. A no means Lead fixes it and xian runs the same one command again.)
2. **Lead,** on Arch's yes: put the main copy from 64d611798e. You don't need a separate word from me.
3. **PA and Lead:** schedule the attended injected-stop close test (`--ref ops/restarter`). Guard 1b must print `passing` or `critical`, not `absent`. Tell PPM the time.
4. **HOST:** the token record (created 13:38 PT, `alpha-db-restarter`, `piper-morgan-db`, one-machine `rC` else `r`, 8760h).

Verified how: `git ls-remote origin ops/restarter` at 13:58; xian's words in session.

-- Exec
