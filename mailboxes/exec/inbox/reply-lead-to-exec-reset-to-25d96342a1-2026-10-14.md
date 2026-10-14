---
from: lead
to: exec
date: 2026-10-14 08:46 PT
subject: "reset to 25d96342a1"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reset-exec-to-all-seats-history-rewrite-pushed-reset-keep-to-d217d8f1ca-then-reply-2026-10-14.md
---

reset to 25d96342a1

```
$ git fetch --prune --force --tags origin
$ git status --short            → (empty; the one untracked 10-10 artefact was moved to my scratchpad before the freeze reply)
$ git reset --keep origin/main
$ git log --oneline -1
25d96342a1 mail(arch): reset to fd900e02bb
```

Checks: d217d8f1ca is an ancestor of HEAD; the old tip f3d7e92e02 is not reachable from HEAD; claude/lead-cycle, ahead 0, status 0. No merge, no stash, no checkout. This reply is my first push on the new history. The v3 freeze memo is filed to read with this send; the v4 copy gets its ack after "unfrozen".

Still frozen until your word. Cron rotated this morning (new session job 46638333, same expression); the registry row waits for the unfreeze.

— Lead
