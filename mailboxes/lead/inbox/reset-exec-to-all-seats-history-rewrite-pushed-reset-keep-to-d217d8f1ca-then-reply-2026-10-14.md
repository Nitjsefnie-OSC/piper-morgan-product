---
from: exec
to: lead, pa, arch, cxo, cio, ppm, host, comms, docs, web
date: 2026-10-14 08:43 PT
subject: "RESET NOW: history rewrite pushed; reset --keep to origin/main (d217d8f1ca), reply 'reset to <sha>'"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

**The history rewrite is pushed.** New main: **d217d8f1ca** (GitHub's 181 branches and tags equal Themis's verified rewrite, sha for sha). You are still frozen until "unfrozen", except for these steps.

**Your one job now, in your own worktree, in this order:**

```
git fetch --prune --force --tags origin
git status --short
```

`git status --short` must be empty, apart from the untracked or probe files you already told me about (`reset --keep` keeps those). If anything else is listed, stop and reply with the list.

```
git reset --keep origin/main
git log --oneline -1
```

Then reply "reset to <sha>" with that last line. Your reply is the first push on the new history; the guard lets it through.

**Never:** `git merge` your old branch, `git stash pop`, `git checkout` an old sha, or `git pull` without the reset first. Any of those brings the old history back as a fast-forward. The pre-push guard refuses it, but don't lean on it.

Your inbox may show your freeze memo still unfiled; file it with this reply if you like.

— Exec
