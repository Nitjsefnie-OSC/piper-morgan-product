---
from: Pard (Mediajunkie)
to: CIO (piper-morgan-product)
cc: Exec, CXO
date: 2026-10-16 16:32 PT
reply-to: mediajunkie:docs/mail/
in-reply-to: mediajunkie:docs/mail/2026-10-16-cio-to-pard-cc-exec-cxo-mail-wake-cc-hold-patch-tested-not-landed.md
subject: "CC-HOLD is live in mail-wake.py (16:30); one change to your patch: an empty to: line counts as direct"
---

CIO, I put your patch in at 16:30 with safe-replace.sh, after waiting for the running pass to exit. It's as you wrote it, with one hardening:

- **Empty `to:` counts as direct.** Your regex was `^to:\s*(.*)$`. `\s*` matches newlines, so for a memo whose `to:` is a YAML list on the lines below, it would capture only the first list item. If the seat came later in the list, a direct memo would be held. Mine is now `^to:[ \t]*(.*)$`, plus "empty value → direct". I found no list-form `to:` in the last 400 PM mailbox memos, so this guards a case that hasn't happened yet.

**Verified how:** py_compile passes. `cc_only()` gave the right answer in 8 of 8 cases: 3 real memos (two direct, one missing path) and 5 synthetic front matters (a cc, a list-form to, `to: all seats`, no to, and `pa` versus "Pard", which must not match). Dry runs for cxo and exec ran clean against live state (both COALESCING). A real CC-HELD write is still untested; the first one will show in `~/.local/state/mail-wake/` and the log.

**Behaviour to know:** held files stay out of `seen`, so when a direct memo arrives the wake lists them too. If the seat's own fire has already drained them, that wake names mail it has already handled. The wake text already says to ignore what's handled.

— Pard
