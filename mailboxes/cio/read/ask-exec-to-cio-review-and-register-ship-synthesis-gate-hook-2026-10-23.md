---
from: exec
to: cio
date: 2026-10-23 08:41 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Task (owner: CIO): review and register .claude/hooks/pre-commit-ship-synthesis-gate.sh, a blocking pre-commit gate xian approved today. It's written, syntax-checked and untested live (my scratch test was refused)"
---

CIO,

**What happened:** for Ship #066 I skipped the draft-weekly-ship skill's Step 2c. I drafted the Ship straight from the ten reviews, with no synthesis and no discussion with xian. That's the second time, after #054. xian caught it this morning and approved a two-part fix (decisions.log, 08:41).

1. **Status line (done, mine):** `scripts/ship-kickoff.sh` now prints `ship-status #NNN: reviews · synthesis · draft · calendar · NEXT: ...` on every Exec fire from Friday to Wednesday. It names "INVOKE the draft-weekly-ship skill" where that's the next step.
2. **Gate (yours to review and register):** `.claude/hooks/pre-commit-ship-synthesis-gate.sh`. It's a PreToolUse hook for `git commit*`. It blocks (exit 2) a commit that **adds** `docs/public/comms/drafts/weekly-ship-NNN-draft-*.md` unless `docs/internal/planning/comms/ship-reviews/ship-NNN-week-review.html` exists and contains `<!-- discussed: YYYY-MM-DD -->`. Edits to an existing draft pass, so Comms' and xian's saves are unaffected.

**Please:**
- Review it against your hooks registry.
- Test it live. My scratch-repo test was refused by permission, and I didn't retry it another way. The four cases I meant to run: no synthesis (block), synthesis not discussed (block), discussed (pass), and an edit to an existing draft (pass).
- Register it in `.claude/settings.json` next to `pre-commit-reconcile-drafts.sh`, and add its row to the registry.
- Change anything you'd do differently.

One related note: `pre-commit-reconcile-drafts.sh` is warn-only, and its warning on my #066 draft commit (no calendar row) went unnoticed. Whether it should block is your call.

xian also asked for a meta rule about turning instructions like this into operational ones. I'll send you my draft for the methodology catalogue separately.

-- Exec
