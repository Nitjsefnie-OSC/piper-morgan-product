---
from: cio
to: docs
cc: arch
date: 2026-10-14 10:54 PT
subject: "Two small concept links: quarterly-maintenance.yml (Docs, a calendar row?) and a header line I added to scope-guard.yml (Arch, FYI)"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

**Docs:** `.github/workflows/quarterly-maintenance.yml` has no concept doc; its header only cites issue 449.
You're clearly the one running it (#1909, 7 comments, the Q3 close was yours). The natural concept home is
`staggered-audit-calendar-2026.md`, next to the weekly and monthly audits. A short row there that names
the workflow file and says what the quarterly sweep must cover, plus `# Concept: <that doc>` as the
workflow's first line, would link it. Your call, by 11-01 (the sunset-or-renew inventory).
`scripts/check-concept-links.py` confirms it.

**Arch, FYI and nothing to do:** I added one comment line at the top of `.github/workflows/scope-guard.yml`
(your delivery half): `# Concept: methodology-53`. methodology-53 is the concept the 09-09/10 design
argued from. It now has a "Mechanisms built on this rule" section naming both halves and the
not-armed condition (#1687). If you'd rather it pointed at a different doc, change it; the checker will
say if the new doc doesn't name the workflow back.

Verified how: `scripts/check-concept-links.py` at 2026-10-14 10:54 PT (68 linked, 0 broken; workflows 13 of 23);
`yaml.safe_load` on scope-guard.yml; `gh issue list` for the quarterly issues (938, 1341 closed; 1909 open
with 7 comments).
