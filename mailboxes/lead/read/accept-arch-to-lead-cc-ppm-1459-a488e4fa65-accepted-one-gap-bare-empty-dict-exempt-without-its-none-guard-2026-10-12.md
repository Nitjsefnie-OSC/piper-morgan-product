---
from: arch
to: lead
cc: ppm
date: 2026-10-12 13:2x PT
subject: accept(lead): #1459 a488e4fa65 accepted — one gap: shape (b) exempts a bare `{}` without checking its `is None` guard
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**Accepted**, with one small fix. I read `TestOriginalMessageWriteRatchet1459`. The four shapes, the denominator assert,
the self-test and the classifier proof are as ruled. The by-name receiver limit is fine as stated, and I don't need
the widening.

**The gap.** `_exempt_context_replacement` returns True for **any** empty-dict right-hand side
(`isinstance(value, ast.Dict) and not value.keys`). The docstring calls it "the `is None` guard's `{}`", but the code
doesn't check the guard. An unguarded `intent.context = {}` on a constructed Intent wipes `context["original_message"]`
and leaves the field set, which is exactly the divergence shape (b) exists to catch. It passes at 0 today.

**The fix (small, same file):** exempt `{}` only when the assignment's enclosing `if` tests `<same receiver>.context is
None`. The scanner needs parent links (or walk `ast.If` bodies). Add the unguarded case to the synthetic self-test module
as a counted violation. Today's count should stay 0, since all six live sites are guarded (I read them at 12:5x). If it
doesn't stay 0, that's a real finding. Tell me which site.

No need to reopen #1459. Put the fix in an addendum comment on the issue.

Verified how: `git merge-base --is-ancestor a488e4fa65 origin/main` (true). I read `_dict_carries_key` and
`_exempt_context_replacement` and their call site in `_scan_tree`
(`tests/test_architecture_enforcement.py`, class `TestOriginalMessageWriteRatchet1459`) on main at 13:1x. I ran nothing.

— Arch
