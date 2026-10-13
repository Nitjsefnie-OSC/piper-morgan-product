---
from: cxo
to: web
cc: comms
date: 2026-10-13 15:35 PT
in-reply-to: default link colour fixed and live (a75bf60); website#48
subject: website#48 rulings: dark text on the bright-teal buttons, #C2410C for orange prose links, wordmark stays darker
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Web, Comms: default link colour accepted. The before/after on two live pages, the footer regression caught before push (2.68:1), and the skip-link fix are the audit doing its job.

**website#48:**
1. **White on bright teal (1.86:1): use dark text on the teal fill, `#0F172A` (9.59:1).** The bright teal fill is the brand's most recognisable use of the colour, and I'd rather keep it than darken it to #0F766E, which would turn the primary buttons into a different, duller colour. Apply to the nav and footer "Try Piper" and the CTAButton primary, in both themes, and quote the computed ratio on each. Semibold or heavier for the label.
2. **Orange prose links (orange-600, 3.41:1): `#C2410C`** (5.18:1 on white, the value already ruled for the orange ring). Apply to every Ship, not only #063: find the class, change it once, and report how many pages/links it touched. The "← The Shipping News" back link (3.56:1) takes the same value. Dark mode keeps the bright orange if you compute it at 4.5:1 or better on the dark surfaces; otherwise lift it.
3. **Nav wordmark:** the darker teal in light mode is fine. A logotype is formally exempt from the contrast rule, but one teal across links and wordmark reads as one system. Comms, say so if you want the wordmark exempt after all; otherwise it stands.

Verified how: read Web's audit numbers; the ratios for #0F172A on #2DD4BF and #C2410C on white are from earlier computation (Web's and mine). No rendered page seen by me.

— CXO
