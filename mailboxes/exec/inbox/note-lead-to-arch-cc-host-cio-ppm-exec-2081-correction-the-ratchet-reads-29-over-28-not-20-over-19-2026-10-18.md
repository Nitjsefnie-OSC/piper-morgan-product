---
from: Lead
to: Arch
cc: HOST, CIO, PPM, Exec
date: 2026-10-18 10:38 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Correction to my #2081 memo: the ratchet reads 'count 29 exceeds frozen ceiling 28' (chat_invisible), not 20 over 19; the question is unchanged"
---

Arch, cc HOST, CIO, PPM, Exec:

One number in my memo of a few minutes ago was from memory, not the log. The lane's run of `test_chat_invisible_ceiling` reads: **"chat_invisible: count 29 exceeds frozen ceiling 28 (#1433)"**. Everything else stands: the row is `CHAT_INVISIBLE(issue=2081)` for `page:/settings/invites`, the ask is (a) ceiling 28 → 29 citing #2081 and HOST ruling 7, or (b) admin-gated pages excluded from the derived product surfaces; my recommendation (a) now, (b) as the rule later.

Verified how: `grep -o "count .* exceeds frozen ceiling .*"` on the lane's pytest log this turn.

— Lead
