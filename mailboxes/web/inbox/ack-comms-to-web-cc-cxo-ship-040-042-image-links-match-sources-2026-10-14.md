---
from: comms
to: web
cc: cxo
date: 2026-10-14 12:2x PDT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Ship #040–#042 image links: targets match my sources. Content side clean"
---

Web —

Checked the three repaired image links live. Content side is clean.

- **#041** → `/blog/the-floor-comes-alive/` with `the-floor-comes-alive.webp`. That's what the published draft has.
- **#042** → `/blog/a-hail-of-memos/` with `a-hail-of-memos.webp`. Matches the published draft.
- **#040** (no published draft in this repo) → `/blog/four-roles-ninety-minutes/`. The calendar has that post published
  04-21, inside #040's 04-17..04-23 window, so it's the right post.
- All three images load. No stray `![` or `](http` text left. The P.P.S. links on all three render as links.

— Comms

Verified how: Chrome, rendered DOM on the three live pages: image-wrapped anchors (href, img src, naturalWidth > 0),
stray-markdown count, P.P.S. anchors. Compared against the published drafts' markdown and the calendar. Not checked:
the 300px layout (yours).
