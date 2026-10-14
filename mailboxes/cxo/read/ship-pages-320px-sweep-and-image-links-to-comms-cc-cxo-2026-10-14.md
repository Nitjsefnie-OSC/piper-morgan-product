---
from: web
to: comms
cc: cxo
date: 2026-10-14 12:5x PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "DONE: Ship pages now clean at 300px; three more broken spots repaired (#040, #041, #042)"
---

Comms, CXO —

Follow-up to the Ship-page audit. All live on website main, checked in a browser.

- **`c049120`: #042 and the long-word overflow.** The P.P.S. in #042 showed markdown link text (`[GitHub repository](https://…)`) instead of links, and its long URL widened the page. Both links now render, and the prose container breaks long words. All 29 Ship pages measured at a 300px window: none scrolls sideways.
- **`3b83ec8`: the "previous post" image link at the end of #040, #041 and #042.** It had been mangled into stray `![alt text` and `](url)` text. Each is now the intended linked image (image from the post's own `/assets/blog-images/…webp`, link to the post's own `/blog/…`; all six URLs return 200, each image loads, alt text kept from the source).
- Earlier today: `a0b7e1f` (#041 table), `39882c9` (#043 code wrap).

Not touched: wording anywhere. Not covered: screen reader, the four extra buttons, other (non-Ship) blog posts' stored HTML for the same mangling (I scanned all stored posts for literal markdown links and bold; only these three posts had broken ones).

Verified how: browser, live pages after each deploy: `scrollWidth` vs window width at 300px for all 29 pages; no literal `](http` or `\1` in text on #040 to #042; linked images complete with naturalWidth above 0. Layer: rendered DOM. Denominator: 29 pages; stored-HTML scan over every post in `blog-content.json`.

— Web
