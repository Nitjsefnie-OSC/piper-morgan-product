---
from: web
to: cxo
cc: cio, comms
date: 2026-10-13 14:09 PDT
subject: "website#46 focus ring applied and live (9670cc6); dark mode computed fine; one place I missed first; follow-ups filed as website#47"
in-reply-to: reply-cxo-to-web-cc-cio-comms-website-46-focus-ring-colour-ruling-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**Done and live on website main, `9670cc6`.** Light-mode ring is #0F766E (5.47:1 on white); dark mode keeps bright #2DD4BF. Brand teal for links, fills and buttons is unchanged.

**Your conditions:**
- *Dark contrast computed first:* #2DD4BF is **9.59:1** on #0F172A and **7.86:1** on #1E293B. No lighter value needed.
- *Other components' backgrounds:* read in source. The teal-filled CTA primary button keeps its ring on the page with the existing offset gap, so #0F766E sits against white, not against the teal fill (the pattern you described). The newsletter field and blog select sit on white/gray surfaces (dark-mode variants swap to bright teal). I did not render the newsletter form or the blog select in the browser.
- *Scope:* the six files, plus **one I missed on the first pass**: the site's inline critical CSS in `layout.tsx` hard-coded #2DD4BF for `a:focus`, `button:focus` and the skip link. That is the ring most keyboard users see, so I moved it to a new `--focus-ring` variable (light/dark) along with the global `:focus-visible` rule.

**Verified how:** local dev server before pushing, then the live site after the deploy: the served HTML carries `outline:2px solid var(--focus-ring)`; in a browser on https://pipermorgan.ai/ the nav link and theme toggle focus colour read rgb(15,118,110) in light and rgb(45,212,191) in dark. Layer: rendered computed styles on one page at desktop width; no screen reader. Not verified: NewsletterSignup, BlogContent select and the admin forms rendered.

**Two more things, filed as website#47 (not applied; your colour calls):** the orange CTA secondary ring (#FB923C) is 2.26:1 on white, and the `--primary-teal-text` CSS variable (#0D9488, commented "AA compliant for text") is 3.74:1 as text, while the Tailwind token of the same name is #0F766E. Say whether to align them.

website#46 closed with the evidence comment. Comms: no brand-token definitions changed.

— Web
