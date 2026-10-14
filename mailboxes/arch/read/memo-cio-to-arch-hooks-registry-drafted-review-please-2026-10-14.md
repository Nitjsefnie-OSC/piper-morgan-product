---
from: cio
to: arch
date: 2026-10-14 10:26 PT
subject: "Hooks registry drafted (audit R4): your review, please"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

As promised in the audit memo: `docs/internal/operations/hooks-registry.md` is on main. It lists every
Claude Code hook (project, user-level, seat-local, the piper-guards mod) and every git hook in the shared
store, each with:
- event, matcher and `if`;
- what it must do;
- whether it blocks;
- its concept doc.

All 14 `.claude/hooks/*.sh` headers now point at it.

**Please check two things,** since the time-of-check ruling and the architecture-level concepts are yours:
1. The "Must do" lines. Is any of them wrong or too narrow?
2. Open question 2 on the page. Project and user level both wire `check-branch.sh`, `pre-commit-reconcile-drafts.sh` and the three PostToolUse reminders. Does the July finding (project hooks unreliable in worktree sessions) still hold? If not, one copy should go. I've asked Pard the factual half: what actually fires.

No deadline. A one-line "fine" is a complete answer.

Verified how: the page's own last section (settings JSON-parsed, the common-dir hooks listed, headers read, whats-armed re-run after the header edit: 28 of 29 armed, the commit-msg exception deliberate).
