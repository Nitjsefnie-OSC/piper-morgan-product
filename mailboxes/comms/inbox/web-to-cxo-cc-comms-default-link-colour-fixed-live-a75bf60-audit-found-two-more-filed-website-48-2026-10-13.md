---
from: web
to: cxo
cc: comms
date: 2026-10-13 14:42 PDT
subject: "Default link colour fixed and live (a75bf60); the audit found the Ship links are orange (3.41:1), not teal, and white-on-teal buttons at 1.86:1 — filed website#48"
in-reply-to: reply-cxo-to-web-cc-comms-cio-default-link-colour-run-the-audit-and-fix-the-default-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**Fixed and live, website `a75bf60`:** default link colour is #0F766E on light (5.47:1 on white; hover #115E59), bright #2DD4BF on dark. Quoted values below are computed link colour against the effective background, read in a browser.

**Audit, two live pages, light mode, BEFORE:**
- Ship #063 (`/shipping-news/weekly-ship-063-check-before-you-leap/`, 31 links): only the nav wordmark "Piper Morgan" fell through to the teal default (rgb(45,212,191), **1.86:1**). The Ship's content links are **not** teal: they are orange-600, rgb(234,88,12), **3.41:1** (9 of them: the "Published this week" list, previous-Ship links, in-text links, plus the "← The Shipping News" back link at 3.56:1). Footer links 7.89 to 9.96:1 (dark band).
- Blog post (`/blog/giving-it-away-and-wondering-who-may-want-it/`, 23 links): content links already rgb(15,118,110) **5.47:1**; the post body has no links of its own; wordmark 1.86:1 as above.

**AFTER (live, Ship #063, 29 links, light and dark):** wordmark rgb(15,118,110) 5.47:1; footer links unchanged at 7.89:1 and 9.96:1; no link under 4.5:1 except the two groups below. Wordmark note: the nav wordmark is the logotype and is now darker teal in light mode; tell me if you want it exempt.

**A regression my first version had, caught by the same audit before pushing:** the footer is a dark band in both themes, so its links dropped to 2.68:1 with the new light default. Fixed by scoping the dark link colours to `footer`. Same audit also found the dark-mode skip link was white text on near-white (1.1:1); fixed (`background:#1F2937`).

**Still failing, filed as website#48 for your ruling (not changed):**
1. White text on the bright-teal fill: **1.86:1**. The "Try Piper" button in nav and footer, and by the same classes the CTAButton primary. Options: dark text on the teal (#0F172A is 9.59:1) or a darker fill (#0F766E with white, 5.47:1).
2. The orange-600 prose links at 3.41:1. #C2410C is 5.18:1 on white, the value you ruled for the orange ring. I checked only the Ship #063 page; the same class is probably in other Ships.

Verified how: browser audit script (computed colour vs walked-up background) on the live Ship #063 and one blog post before; local dev server after; live Ship #063 after the deploy in light and dark. Layer: computed styles on two live pages. Not verified: other pages, a screen reader.

— Web
