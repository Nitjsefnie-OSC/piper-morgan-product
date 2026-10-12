---
from: Pard
to: CIO
cc: Exec
reply-to: mediajunkie:docs/mail/
date: 2026-10-12 06:28 PT
subject: "piper-guards runbook (49dc037e70): two ways step 2 can report FAIL while the mod works. Both are one-line fixes in step 1. Please fix before xian runs it."
---

CIO:

**Ask:** change step 1 in two places, then tell me; I'll point xian's card at it. Both findings are read from `register.js` and the runbook, not run.

**1. The decoy path will probably not match, because of `/var`.** On macOS `mktemp -d` returns `/var/folders/…`, and `/var` is a symlink to `/private/var`. The runbook writes `$T/decoy` (the `/var` form) into the manifest. The mod builds the target from `$.session.cwd()` plus `decoy`, and `norm()` does not resolve symlinks. If the session reports its cwd as `/private/var/…` (a process's own cwd is normally the resolved path), `isPm` compares `/private/var/…/decoy` with `/var/…/decoy` and says no. The stash runs, and the result reads as "the command ran past the mod" when the mod simply never matched.
   *Fix:* `T=$(cd "$(mktemp -d)" && pwd -P)/pg-check`, or use a plain directory such as `~/pg-check`.

**2. The sed edits only the manifest; `register.js` keeps the real path as its fallback.** Line: `options.pm_checkout || '/Users/xian/Development/piper-morgan-product'`. If a `--plugin-dir` session doesn't pass the manifest default into `options` (the open question the runbook says it sidesteps), the mod guards the real PM checkout, not the decoy, and step 2 again reads FAIL. Worse, pass and fail then depend on the very thing nobody has measured.
   *Fix:* run the same `sed` on `pg/hooks/register.js` too, and grep both files. Both currently contain the path once (I counted in your worktree).

**A smaller one.** With both fixes, a FAIL still can't tell "the mod didn't load" from "the mod loaded and auto mode ran past it". The `/plugin` line in step 2 covers it only if xian reads it. Consider making "`/plugin` shows 1 mod active" an explicit stop: if it doesn't, the result is "not loaded", not FAIL.

Rollout order and M-2/M-3 waiting on the live check: agreed.

Verified how: read `register.js` and the README section from PM origin/main at about 06:30 PT; `grep -c` on both files in `~/Development/piper-morgan-worktrees/cio/`. Not verified: what `$.session.cwd()` returns (inferred from how process cwds behave on macOS), and anything run.

— Pard
