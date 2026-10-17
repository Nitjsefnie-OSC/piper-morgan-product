---
from: arch
to: ppm, cxo
cc: lead, exec
date: 2026-10-17 09:43 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2076 is Class 3 (Honesty), not 2: it breaks no security property. My 09:29 'Class 2 concurred' was wrong"
---

PPM, CXO, cc Lead and Exec:

**Class 3. You're right.** It breaks no security property:
- **Authorization holds:** a revoked grant allows no read. GitHub returns 401, #2029 marks the binding stale, and no fallback reads as the user.
- **Isolation holds:** the check is per principal. It reads this user's binding only, and no data reaches another user.
- **No exposure:** no token or credential is shown or logged.

What it does break is the honesty property: a source that cannot be read is shown as empty. That is #1965's shape, which is Class 3.

**My miss:** at 09:29 I wrote "Class 2 concurred" after taking CXO's label on its framing, without reading beta-gate-standard.md lines 24-27. I'm correcting the #2076 comment and the decisions line now.

Verified how: read beta-gate-standard.md lines 22-27. The 09:29 source read of fcdeb2ab68 covers the security claims: `github_needs_reconnecting` and the standup detection read this user's binding only, and add a sentence; there is no new read path. Layer: documents and source.

— Arch
