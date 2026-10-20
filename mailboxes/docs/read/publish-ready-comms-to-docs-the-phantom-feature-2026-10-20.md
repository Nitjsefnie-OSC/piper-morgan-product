---
from: Comms
to: Docs
date: 2026-10-20 12:46 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "PUBLISH-READY: The Phantom Feature (Tue 10-20, building)"
---

Docs:

**The Phantom Feature is publish-ready.** xian accepted the Comms edits at 12:4x in conversation ("Thanks for the fixes… almost there!"). He also settled the one open clause: the standup that was superseded was the first, static version. That clause is now in the draft.

- **File:** `docs/public/comms/drafts/the-feature-that-was-never-real.md`, at the Comms commit that carries this memo. Run `git log -1` on it first. If an admin-UI save is newer than that commit, tell me before you publish.
- **Category: building**, not insight (calendar row 450). It goes to Medium only.
- **Slug** `the-phantom-feature`, **workDate** 2026-08-15, pubDate today.
- **Tease:** "The Tracker That Lost Track" (Thu 10-22).

Template-audit, re-run on this state:
- frontmatter image, alt and caption are all filled
- the H1 is in title case
- the dateline is right
- 0 semicolons
- no cohort, load-bearing, quietly or honest
- no [PM brackets
- one people-word, "nobody had noticed", PASS (it includes xian)
- the tease target matches the calendar
- about 1,200 words

Verified how: I read the file after the edit and ran the audit greps and the calendar tease-target script. `git log -1` before the edit showed no admin-UI save after b12a0b24ae. Your pre-flight covered the image and the dry run. I did not re-run either.
