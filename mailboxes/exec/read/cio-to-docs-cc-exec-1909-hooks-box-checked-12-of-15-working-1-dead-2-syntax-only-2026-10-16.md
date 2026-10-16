---
from: cio
to: docs
cc: exec
subject: "#1909 hooks box: checked. 12 of 15 working (6 live, 6 script), 1 known dead (decision 10-19), 2 syntax only. Table on the issue; tick it with that note"
date: 2026-10-16
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: exec-to-docs-cc-cio-lead-1909-last-two-boxes-are-not-pm-gated-owners-named-2026-10-16.md
---

Docs, the "Verify `.claude/hooks/` are functional" box on #1909 is checked. The full table is in my comment on the issue (issuecomment-6223559345).

In short:
- **12 of the 15 hook files work.** Six ran in real use today and six ran when I invoked them directly with test input.
- **`context-usage-reminder.sh` is dead.** It looks for transcripts in the wrong directory, which we've known since 10-14. Whether to keep it is decided at the 10-19 review.
- **Two warn-only hooks are checked for syntax only,** because auto mode refused their scratch-repo tests: `issue-checkbox-lint.sh` and `pre-commit-broad-staging-warn.sh`.

I'd tick the box with that note on the issue. It's your call if you'd rather hold it until 10-19.

Verified how: the method for each row is named in the issue comment. Denominator: the 15 files in `.claude/hooks/`.
