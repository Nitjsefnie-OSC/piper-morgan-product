---
from: Comms
to: Docs
cc: exec
date: 2026-10-21 07:13 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "PUBLISH-READY: Weekly Ship #065, The Truth About State (Wed 10-21, ship)"
---

Docs, cc Exec:

**Weekly Ship #065 is publish-ready.** xian made his final pass in the admin UI (06:46–07:00, five saves ending 2228f63f5e). He then approved the Comms fixes in conversation at 07:1x, and they are applied:
- three grammar and wording fixes;
- "a couple of weeks ago" in the P.S.;
- the API-spend bullet reordered;
- commas before two "but" clauses;
- one tense fix.
He declined "at peak" on the 88%, and kept "close them as fast as we find 'em" as his voice.

- **File:** `docs/public/comms/drafts/weekly-ship-065-draft-2026-10-18.md`, at the Comms commit that carries this memo. Run `git log -1` on it first. If an admin-UI save is newer than that commit, tell me before you publish.
- **Category: ship.** It goes to LinkedIn. The slug follows #064's pattern: `weekly-ship-065-the-truth-about-state`, under `/shipping-news/`. The calendar row (458) has pubDate today.
- **Hero:** frontmatter `piper-ship.png`, with the alt filled and the caption empty (Ship convention). The External section's inline image is The Overzealous Cleanup Routine's `.webp`, and it returns 200.

Template audit, run on this state, with the Ship calibration applied (caption, tease, word count, short-form glosses and #NNN marked N/A by convention):
- **Frontmatter:** image and alt are filled.
- **H1:** title case.
- **Dateline:** *October 9–15, 2026*.
- **Headings:** none at `###`.
- **Word checks:**
  - 0 semicolons.
  - No cohort, load-bearing, honest, CoS, `<!--` or [PM.
  - The one "quietly" is inside a quoted pattern title (line 89). PASS.
- **People-words:** 1 match, "A rule nobody checks is just a wish". PASS, because it's generic.
- **Footer:** the previous Ship link to #064 resolves, and the phase tag is present.
- **Links:** all 9 unique links return 200 (curl -L).

Verified how: I read xian's word diff from 55d4f53d82 to 2228f63f5e in full, and checked its new facts:
- the $200/month credit: xian's 10-09 memo via Janus;
- "I would not use this product": Arch's 10-05 log.
I applied the edits by exact string match (8 of 8 matched once), re-ran the audit greps and curled every link. Before the edit, `git log -1` showed no save after 2228f63f5e.

-- Comms
