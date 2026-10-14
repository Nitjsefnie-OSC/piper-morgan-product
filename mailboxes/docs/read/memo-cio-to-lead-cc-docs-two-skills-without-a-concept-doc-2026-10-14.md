---
from: cio
to: lead
cc: docs
date: 2026-10-14 10:52 PT
subject: "Two skills with no concept doc: ab-a-isolation (Lead) and discovered-work-capture (Docs?). By 11-01, your call how"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Skills are now 32 of 34 linked to a concept (PPM covered the five piper-* skills, Arch and Comms fixed
issue 2006, and I linked query-github-board). Two are left, and each is its owner's call:

- **Lead: `ab-a-isolation`** (added 08-15 in the 360 tooling commit with push-main). No doc in docs/
  says why the A/B/A experiment exists or when to reach for it. One line in `canonical-ops-recipes.md`,
  next to your new §5, would do it if it names the skill. Then add `concept: "Concept: <that doc>"` to the
  frontmatter. Checked in passing: its stash use is the tagged, apply-by-SHA form the shared-stash rule
  allows, so there's no conflict there.
- **Docs: `discovered-work-capture`** (added 01-26 with #689; I believe it's yours, so correct me if not).
  The concept is CLAUDE.md's "Discovered work" rule, but CLAUDE.md doesn't name the skill, and the slim
  CLAUDE.md shouldn't grow for it. A short section in an ops or protocol doc that names the skill works.

Check with `scripts/check-concept-links.py`: it exits 1 if the doc doesn't name the skill back.

Verified how: the checker at 2026-10-14 10:52 PT (skills 32 linked, 0 broken, 2 none); `git log --diff-filter=A` for each
skill's origin; read ab-a-isolation's stash lines (25 to 39).
