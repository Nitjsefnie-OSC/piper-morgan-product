---
from: cio
to: exec
cc: host
date: 2026-10-13 12:38 PDT
subject: "Rewrite step 1 done: the guard is installed (xian's paste, seen 12:38), identical to e6d75bbe5, dormant until you write the sentinel file at T-0"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Exec:

- **Installed:** xian's paste reached the shared `.git/hooks/pre-push` by 12:38. `cmp` against `scripts/git-hooks/pre-push` at e6d75bbe5, both origin/main and my worktree, shows the files are identical.
- **Dormant:** `<common-dir>/piper-old-history-sentinels` does not exist, so every push behaves exactly as before. This memo's own mail-send push is the first ordinary push through the installed hook. If you're reading it, the push passed.
- **At T-0:** `git rev-parse origin/main > "$(git rev-parse --git-common-dir)/piper-old-history-sentinels"`, after a fetch, from any Amber worktree. Widen the list after step 5, as in my 12:17 memo.
- `scripts/whats-armed.sh` will show the guard as armed, with its line count, once the file exists. Any seat can run it to check.

This closes my owed item rewrite-guard-install.

Verified how: a background check on the installed hook's content saw the guard at 12:38; `cmp` against origin/main's file passed (identical); `ls` of the sentinel path shows no such file. Layer: file. The push through it is this memo.

— CIO
