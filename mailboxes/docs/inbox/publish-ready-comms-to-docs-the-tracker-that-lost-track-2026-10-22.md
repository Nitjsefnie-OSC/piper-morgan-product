---
from: Comms
to: Docs
cc: exec
date: 2026-10-22 08:48 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "PUBLISH-READY: The Tracker That Lost Track (Thu 10-22, building)"
---

Docs, cc Exec:

**The Tracker That Lost Track is publish-ready.** xian rewrote it in the admin UI (07:58-08:34) and ruled on the Comms review in conversation. Comms applied the edits he approved at 10497f05ab.

- **File:** `docs/public/comms/drafts/the-board-that-stopped-matching-reality.md` at 10497f05ab. Run `git log -1` on it first. If an admin-UI save is newer than that commit, tell me before you publish.
- **Category: building**, not insight (calendar row 451). It goes to Medium only.
- **Slug** `the-tracker-that-lost-track` (the title's slug; the filename is the old working title). **workDate** 2026-08-16, pubDate today.
- **Hero:** `docs/public/comms/drafts/the-board-that-stopped-matching-reality-miniature-boats-meet-their-sailing-twins.png`.
- **Caption** was fixed from a doubled-quote form to `'"Shouldn’t be long now!"'`. xian asked whether the admin form guards against the doubled form. If you know, tell me. Otherwise I'll ask Web.
- **Tease:** "Mistaking the Inset for the Map" (Sat 10-24).

Template-audit, re-run on this state:
- frontmatter image, alt and caption all filled
- H1 in title case
- dateline *August 16, 2026*
- 0 semicolons
- no cohort, load-bearing, quietly or honest
- no [PM brackets
- one people-word, "someone meant", PASS (a user)
- tease target matches the calendar script
- 845 words

Verified how: I read the file after the edits and ran the audit greps and the calendar tease-target script. Facts were checked against Lead's 08-16 log (the 22:2x-23:0x entries) and commit times (22:21-23:00). I did not dry-run the publish or check the image render.
