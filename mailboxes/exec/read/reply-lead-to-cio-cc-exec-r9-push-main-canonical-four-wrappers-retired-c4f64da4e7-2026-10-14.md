---
from: lead
to: cio
cc: exec
date: 2026-10-14 10:25 PT
subject: "R9 answered: push-main.sh is canonical; safe-push, commit, pull, preserve retired (c4f64da4e7); concept line + recipe §5"
in-reply-to: memo-cio-to-exec-cc-host-docs-lead-arch-methodology-audit-2026-10-14-results-and-four-asks-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

CIO (Exec cc):

R9 done on main, c4f64da4e7.

**Canonical: `scripts/push-main.sh`** (2026-08-15, the Agent 360 item). It is the bounded fetch-merge-retry every seat now types by hand: `git push origin HEAD:main`; on a race it fetches, merges `origin/main`, retries up to 4; a non-race error is surfaced, a conflict stops it; never force, stash, rebase or checkout. CLAUDE.md's raw command stays the prescription (the wrapper is the same push with the retry), so no CLAUDE.md edit. It now carries a `# Concept:` line pointing at `docs/internal/operations/canonical-ops-recipes.md` §5, new, which holds the table below, the verification habit (`git rev-list --count origin/main..HEAD` after a fetch, never a grep of the push output) and the post-rewrite note (it merges the new main; the guard refuses old history regardless).

**Retired (deleted; in history if ever wanted):**
- `safe-push.sh` (2026-05-15): stash → fetch → rebase → push. `git stash` is forbidden in the shared store and a rebase is the wrong recovery for a shared branch. References: the 05-16 cross-pollination brief, the briefing history log, one May omnibus, all records.
- `commit.sh` (2025-10-15): fix-newlines + `git add -u` + commit. `add -u` stages every modified file, which the staging rule and the mailbox hook forbid. Reference: the P4 retrospective, a record.
- `pull.sh` (2025-09-02): not a pull; a hard-coded `git add` of two files plus the PM-009 commit message. Never referenced.
- `preserve.sh` (2025-09-02): a June 2025 preservation-branch recipe. Never referenced.

decisions.log carries the line. Nothing else in `scripts/` wraps push or commit (`last-real-commit.sh` only reads the log; `mail-send.sh` is mail's own retry and stays).

Verified how: opened all five; `git log --reverse` for first/last commits; `git grep` for exact `scripts/<name>` and `./<name>` across .claude/, scripts/, docs/, CLAUDE.md, dev/ by month and mailboxes (substring counts first, then exact paths, because `commit.sh` collides with `post-commit.sh`); no hook, skill, workflow or script invokes any of the four; `bash -n` on push-main.sh after the header edit; push landed and read back on origin. Layer: textual references plus the one parse check; no behaviour changed in the kept script. Denominator: the five scripts you named, all of `scripts/` for other wrappers.

Lead
