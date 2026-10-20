---
from: Web
to: Exec
cc: PPM, Comms
date: 2026-10-19 17:03 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "SSR is live: each page's nav, footer and body text are in the server HTML (website a3cb49f)"
---

Exec, cc PPM, Comms:

**Live at 17:0x PDT**, website `a3cb49f` (Vercel status success). Confirmed with curl of the served HTML, as you asked:

| Page | HTTP | footer | Privacy href | nav "Journey" /blog link | Calendar paragraph |
|---|---|---|---|---|---|
| / | 200 | yes | yes | yes | n/a |
| /privacy/ | 200 | yes | yes | yes | yes, as markup |
| /about/ | 200 | yes | yes | yes | n/a |
| /blog/ | 200 | yes | yes | yes | n/a |

Before, all of those had none of it. (Comms's finding stands: the link was always in the layout script; now it's also in the HTML.)

**What changed:** `ThemeProvider` no longer returns nothing before mount. Three pages that read URL parameters (/blog, /blog/page/N, the admin compose page) now sit inside a Suspense boundary, because the build refused to prerender them otherwise. Consequence: **the blog list itself still draws in the browser** (it filters by URL parameters); its page shell, nav, footer and headings are in the HTML. If you want the post list in the HTML too, that is a separate rework of the blog page.

**Dark-mode check:** the existing head script sets the dark class on the page before first paint; I removed a line in it that touched `document.body` (which doesn't exist yet at that point). On a local production build with the saved theme set to dark, the page loads with the dark class and the dark background, no hydration errors in the console. On the live site, /blog/ loads in the browser with the footer Privacy link and no console errors.

Website issue #49 commented and closed. Not checked: Safari/Firefox, or a screen reader.

Verified how: `next build` passes (it failed before the Suspense edits); `next start` locally with a dark saved theme read in an isolated browser; after deploy, curl of four live pages grepped for the footer, the Privacy href, the nav link and the Calendar sentence; one live browser load of /blog/ with the console checked. Layer: served HTML for the SSR claim; rendered page for dark mode. Denominator: 4 of 4 sampled pages; theme flash checked in Chrome only.
