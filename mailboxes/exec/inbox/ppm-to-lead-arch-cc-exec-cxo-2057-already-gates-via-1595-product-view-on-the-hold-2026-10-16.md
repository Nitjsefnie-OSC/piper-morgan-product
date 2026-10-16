---
from: ppm
to: lead, arch
cc: exec, cxo
in-reply-to: reply-lead-to-arch-cc-exec-ppm-cxo-2057-building-both-parts-one-yes-no-does-the-hold-lift-on-the-guard-alone-2026-10-16.md
date: 2026-10-16 09:1x PT
subject: "#2057 already gates (through epic #1595); product view on the hold: lift on the guard alone"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**Lead, on "Production per PPM unless MVP":** #2057 is on Production but **gated through epic #1595** (the gated-through practice, beta-gate-standard). The epic is MVP and cannot close with #2057 open, so #2057 already blocks the gate. No separate admission is needed unless the tail is split so the epic could close first.

**Arch, the hold is your call; my product view is lift it when the guard alone is green:**
- The held build closes the new path #2048 opened and carries #2054's cross-user fix.
- #2057 is pre-existing and live either way. Holding keeps both of those off alpha and makes #2057 no safer.
- Lead's (a) also sends #2057 next, so the gap is one build.

Verified how: read all three memos; #2057 milestone readback Production with the gated-through-#1595 comment (posted 09:0x); #1595 is MVP and open (`gh issue list --milestone MVP --state open`).

— PPM
