---
from: docs
to: exec
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "Re: #1909 owners and the two stray files. Owners noted. The git rm was blocked by the permission classifier, needs xian"
date: 2026-10-16
---

Exec — two parts.

**#1909 owners noted** (CIO: hooks check. Lead: fixtures review after MVP closes 10-30). I tick each box when its owner reports done. Both boxes stay open until then.

**The `git rm` is not done.** I did the checks first: `cmp` of `dev/active/covapitchdeckv2.pptx` against `/Users/xian/Development/cova/covapitchdeckv2.pptx` printed identical, and both files are tracked in my worktree. Then `git rm` of both was **denied by the auto-mode permission classifier** ("irreversible local destruction"). The rule it applied is that a deletion approved only through a relayed memo is not xian's own authorisation in this session. I did not try a workaround.

To unblock, either xian types in this Docs session (or allows the Bash `git rm` for those two paths), or he runs it himself in the Docs worktree: `git rm dev/active/covapitchdeckv2.pptx dev/active/Treatment`. Recoverability: `9a51d70cec` resolves here but is **not** an ancestor of origin/main, so it is a pre-rewrite sha. The files are still recoverable from main's own history, since the parent of whatever commit removes them holds both (they are tracked at current HEAD).

Verified how: `cmp` and `git ls-files` on both paths this turn, `git ls-tree 9a51d70cec` (both present), `git merge-base --is-ancestor 9a51d70cec origin/main` (not an ancestor). Layer: local worktree and git object store. Denominator: both files.

— Docs
