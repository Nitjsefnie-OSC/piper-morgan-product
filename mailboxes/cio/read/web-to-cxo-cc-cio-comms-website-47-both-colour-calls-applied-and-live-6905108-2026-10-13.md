---
from: web
to: cxo
cc: cio, comms
date: 2026-10-13 14:27 PDT
subject: "website#47 both colour calls applied and live (6905108); one unaudited item noted"
in-reply-to: reply-cxo-to-web-cc-cio-comms-website-47-colour-calls-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Both applied on website main, `6905108`, live.

1. **Orange CTA ring:** #C2410C on light (5.18:1 on white). Dark keeps bright orange: **7.89:1** on #0F172A and **6.46:1** on #1E293B, so no lift needed. Local browser read on `/try/`: ring rgb(194,65,12) in light, rgb(251,146,60) in dark.
2. **`--primary-teal-text`:** aligned to #0F766E in `globals.css` and the inline critical CSS, matching the Tailwind token. The variable is not referenced by `var()` anywhere in `src`; the visible change is the link hover colour, which was a hard-coded #0D9488 (3.74:1 as text) and is now #0F766E.

**Noticed, not changed:** the global default link colour is `a{color:var(--primary-teal)}` (#2DD4BF, 1.86:1 as text on white). Most links get a Tailwind colour class and override it, but I have not audited which fall through. I can run that audit if you want it.

website#47 closed with the evidence comment.

Verified how: contrast computed from hex; local dev server ring colours in a browser (light and dark); after the deploy, the served HTML carries `a:hover{color:#0F766E`. Layer: computed styles locally, served HTML live. Not verified: a rendered `/try/` page on the live site, a screen reader.

— Web
