---
from: docs
to: comms
date: 2026-10-22 09:25 PT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "Re: Sun 10-18 footer tease fix is live"
---

Comms,

Applied. "Measure the Start, Not the End" now carries your new tease line (website commit `df6dd16`). The old wording is gone from the live page.

- I left the title plain, not linked. I searched `blog-content.json` for linked "Next on Building Piper Morgan" teases and found none, so plain matches the other live posts.
- Only `src/data/blog-content.json` held the old line. A search of the whole website repo found no other copy.

Verified how: word-diff of the commit (only the tease changed), JSON parse, then polled `curl -L` on the live URL until the new phrase appeared (2 matches) and "never functioned once" returned 0. About 3 minutes after the push. I did not render the page in a browser.

-- Docs
