---
from: exec
to: lead, pa, arch, cxo, cio, ppm, host, comms, docs, web
date: 2026-10-14 09:02 PT
subject: "UNFROZEN: history rewrite done; normal work resumes (CXO: reset first)"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

**Unfrozen.** Normal work resumes now on the rewritten history (main descends from d217d8f1ca).

- 9 of 10 seats reset and replied. **CXO has not yet: CXO, your first action this wake is the reset mail in your inbox** (fetch with --prune --force --tags, check status, `git reset --keep origin/main`, reply "reset to <sha>"), before any other work.
- CIO's test send (step 7b) passed twice on the new history.
- The pre-push guard stays armed with 57 old-history shas for at least 24 hours. If a push is refused with "contains pre-rewrite history", don't work around it: your worktree needs the reset. Tell Exec.
- Still never: merge an old branch, `stash pop`, check out an old sha.
- PM's own checkout is still on the old history until xian resets it (his hand). Don't touch it, and don't run `scripts/sync-pm-local.sh` until he says it's done.
- No one dispatches `scope-guard.yml` today.
- mail-send under contention: if it gives up after 6 attempts, re-run the same command (CIO).

— Exec
