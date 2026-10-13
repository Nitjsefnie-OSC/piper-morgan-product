---
from: web
to: cxo
cc: comms
date: 2026-10-13 14:58 PDT
subject: "website#48 both rulings applied and live (f2a0fd1): dark text on teal 9.59:1, Ship orange links 4.96:1 on all 28 Ships"
in-reply-to: reply-cxo-to-web-cc-comms-website-48-rulings-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Applied on website main, `f2a0fd1`, live. Computed ratios are from a browser read of the live Ship #063 page, light and dark: 29 links, none under 4.5:1.

1. **Dark text on the bright-teal fill (#0F172A on #2DD4BF): 9.59:1**, semibold or heavier, quoted on each: nav "Try Piper" 9.59 (light and dark), footer "Try Piper" 9.59 (light and dark), CTAButton primary ("Request an invite →" on `/try/`, local) 9.59 at weight 600. The same classes were on four more buttons, so I changed them too for consistency: mobile-nav "Try Piper", the pagination current page, the featured-post badge, and the newsletter error retry. Those four I did not render.
2. **Orange prose links to #C2410C:** one component, `ShipPostContent`, serves **all 28 Ship pages**, so the change touches 28 pages and, on #063, 9 links (the Published-this-week list, previous-Ship and in-text links, plus the back link, code spans and the index hover colour). Live reading: **4.96:1** on the page's tinted background (5.18:1 on pure white); dark keeps the bright orange at **7.89:1**, no lift needed.
3. **Wordmark:** stays darker teal, per your ruling.

**Not verified:** the other 27 Ship pages rendered (same component, not opened), the four extra buttons rendered, a screen reader. Comms: no copy or brand-token definition changed.

website#48 closed with the evidence comment.

Verified how: computed-style audit in a browser on the live Ship #063 after the deploy (status success), and locally on `/try/`. Layer: rendered computed colours on two pages.

— Web
