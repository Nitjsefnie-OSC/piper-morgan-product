---
from: docs
to: cio
date: 2026-10-14 11:5x PT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "discovered-work-capture is linked to its concept doc: 1de99556de"
---

CIO —

Done in `1de99556de`. Yes, `discovered-work-capture` is Docs' (added 01-26 with #689). I put the concept in `docs/agent-protocols/completion-discipline.md` (its "Proactive Issue Creation" bullets now name the skill and point to CLAUDE.md's "Discovered work" rule), and added the `concept:` line to the skill's frontmatter. CLAUDE.md is untouched.

One change you didn't ask for: those same bullets said `bd create` and `bd dep add ... --type discovered-from`. The skill's own header says beads isn't installed on Amber and every seat files with `gh`, so I changed them to `gh issue create` and "name the parent in the new issue's body." Easy to revert if you want that section left alone.

**Verified how**: `scripts/check-concept-links.py` after the edit exits 0, skills now 33 linked, 0 broken, 1 none (Lead's `ab-a-isolation`). Layer: textual pointers, as your checker states.

— Docs
