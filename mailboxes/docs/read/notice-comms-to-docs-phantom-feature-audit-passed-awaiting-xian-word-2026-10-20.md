---
from: Comms
to: Docs
date: 2026-10-20 12:21 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Heads-up: The Phantom Feature (pubDate today) passes template-audit, publish-ready pending xian's word on Comms' final edits"
---

Docs:

Today's post, "The Phantom Feature" (`docs/public/comms/drafts/the-feature-that-was-never-real.md`), has xian's final voice pass (admin UI, 12:04).

What Comms did on it:
- Fact fixes and copyedits at 12:08.
- A footer-tease timing fix at 12:20.
- Template-audit against that state, which passes:
  - frontmatter image, alt and caption are all filled
  - H1 is in title case
  - dateline "August 15 – October 19, 2026"
  - 0 semicolons
  - no cohort, load-bearing, quietly or honest
  - no [PM brackets
  - one people-word, "nobody had noticed", PASS (it includes xian)
  - the tease targets "The Tracker That Lost Track" (Thu 10-22), which is correct
  - about 1,200 words

**Not yet publish-ready.** xian is reviewing the Comms edits and may change one clause ("...both of which have long since been largely superseded"). Comms will send the publish-ready memo, or the changed lines, as soon as he answers. Until then, run `git log -1 -- <draft>` before you start, because he edits in the admin UI.

Verified how: read the file at HEAD after the last admin-UI save (d3789a8388) and the Comms commits after it. Ran the audit greps and the calendar tease-target script on that state.
