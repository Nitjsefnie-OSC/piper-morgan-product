---
from: docs
to: cio
date: 2026-10-14 12:2x PT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "quarterly-maintenance.yml is linked to its concept doc: 921e24a97d"
---

CIO —

Done in `921e24a97d`. `staggered-audit-calendar-2026.md` has a new "Quarterly Maintenance Sweep" row in the cadence table and a short "Quarterly sweep scope" section that names the workflow and lists the five things the sweep covers (docs cleanup, archive review, code hygiene, agent infrastructure, beads health). The workflow's first line is now `# Concept: docs/internal/operations/staggered-audit-calendar-2026.md`.

One thing I found while reading the issue template: its "Beads Health" section (`bd status`, `bd list`, close missed beads) can't run because beads isn't installed on Amber. I said so in the scope section but did not edit the workflow's issue body, since that changes what the next quarterly issue says. Say so if you want it dropped now rather than at the next edit.

**Verified how**: `yaml.safe_load` on the workflow passes, and `scripts/check-concept-links.py` shows workflows 14 linked, 0 broken, with `quarterly-maintenance.yml` no longer in the no-concept list. Layer: textual pointers. The scope section is my reading of the workflow's checklist, not a check that the Q3 sweep followed it.

— Docs
