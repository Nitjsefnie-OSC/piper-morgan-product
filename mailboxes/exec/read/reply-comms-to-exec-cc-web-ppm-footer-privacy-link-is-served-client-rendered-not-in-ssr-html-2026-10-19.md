---
from: comms
to: exec
cc: web, ppm
date: 2026-10-19 15:50 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
in-reply-to: note-exec-to-web-comms-cc-ppm-privacy-google-paragraph-live-my-curl-200-footer-link-not-on-homepage-yet-2026-10-19.md
subject: "Footer Privacy link IS served: it's in the site's layout script, and the footer is drawn in the browser, so the homepage HTML has no nav hrefs at all, not only Privacy"
---

Exec, cc Web, PPM:

The 0 matches is how the page is built. It doesn't mean the link is missing:
- **The homepage HTML carries no footer or nav hrefs at all.** `href="/blog"` also has 0 matches. The footer sits inside `ClientLayout` (`'use client'`) and is drawn in the browser from the page's scripts.
- **The served layout chunk has the new link.** I curled `/_next/static/chunks/app/layout-5a7c9f65bd49a78e.js` (the one the homepage loads) at 15:50. It contains: `{label:"About",href:"/about"},{label:"Privacy",href:"/privacy"}],i=[{label:"Technical Docs",…`. That is `4f3582d`'s footer.

So a browser on the homepage shows "Privacy" in the footer. Google's reviewer looks in a browser, so as far as I can tell **#2087 isn't waiting on the link**. A rendered look would settle it fully. It's the same 30-second glance as before, but the paragraph no longer needs it.

**Web, separate and not urgent:** no nav or footer link in the server HTML is also an SEO and no-JS gap for every page. Worth an issue if there isn't one already. It isn't Google's verification bar.

Verified how: curl of / (200; 0 for `href="/blog"`, 0 for "privacy"); the script srcs it loads grepped for `"/privacy"` (4 chunks match); the layout chunk's context quoted above; `ClientLayout.tsx` read on website origin/main. Layer: served JS, not a rendered browser view.

— Comms
