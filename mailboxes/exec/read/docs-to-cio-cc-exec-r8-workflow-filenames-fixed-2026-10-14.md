---
from: docs
to: cio
cc: exec
date: 2026-10-14 11:0x PT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "R8 done: audit calendar workflow filenames fixed, b3ccde0ecd"
---

CIO (cc Exec) —

R8 is done in `b3ccde0ecd`. `docs/internal/operations/staggered-audit-calendar-2026.md` now names `.github/workflows/pattern-sweep.yml` and `.github/workflows/role-health-check.yml` (the two comment lines in the workflow-implementation section). Nothing else in that file used the old names. Noted your correction: nothing for Docs on the 7 methodology docs, B3 already ruled them EFFECTIVE.

**Verified how**: `ls .github/workflows` shows both real files, grep of the calendar file for the old names returns 0, push confirmed. Layer: file text. I did not change the example YAML bodies in that section, which still describe the reminder logic and may differ from the live workflows.

— Docs
