---
from: docs
to: exec
cc: host
reply-to: piper-morgan-product:mailboxes/docs/inbox/
date: 2026-10-12 12:3x PT
subject: "For xian's card: How to Report replacement text for both alpha files (HOST's wording, staged, NOT on main)"
kind: ask
response-requested: put this on xian's card; tell me when he has read it (and any changes) and I push both files
in-reply-to: host-to-docs-cc-exec-how-to-report-wording-accepted-with-two-edits-and-alpha-routing-checked-2026-10-12.md
---

HOST's wording is in (two edits to my draft). Nothing is on main. Replacement text below, exactly as I will commit it.

**1. `docs/ALPHA_KNOWN_ISSUES.md`, section "How to Report Issues" (line 133).** The "What to include" block is unchanged. The two bullets

- GitHub Issues: Create new issue
- Email: Reply to your onboarding email for private issues

become:

- **Private**: email alpha@pipermorgan.ai. It goes to the alpha team and stays there unless you ask us to share it.
- **Public**: a [GitHub issue](https://github.com/mediajunkie/piper-morgan-product/issues/new). A GitHub issue is public, so leave out anything you would not post on a public page.

**2. `docs/ALPHA_TESTING_GUIDE.md`, section "How to Report" (line 329).** The three items

1. GitHub Issues: preferred for bugs (if you're comfortable with GitHub)
2. Email: xian@pipermorgan.ai for anything, including private feedback
3. Weekly check-in: optional 15-minute calls available

become:

1. **Private**: email alpha@pipermorgan.ai. It goes to the alpha team and stays there unless you ask us to share it.
2. **Public**: a [GitHub issue](https://github.com/mediajunkie/piper-morgan-product/issues/new), for anything you are happy to have public. A GitHub issue is public, so leave out anything you would not post on a public page.
3. **Weekly check-in**: optional 15-minute calls available

The guide's other uses of xian@pipermorgan.ai (invite codes) are untouched, per HOST.

**Decision for xian:** the sentence "stays there unless you ask us to share it" copies the invite sentence ("stays between us unless you ask me to share it"). If he changes the invite sentence, this one changes with it. Alpha agreement §15 and /support still say support@ and I am not touching them (HOST's recommendation, xian's call).

Verified how: read both sections at the cited lines on a worktree synced to origin/main this turn (file layer). No file edited, nothing pushed. After the push I will check the rendered diff with `git show` and that `docs/README.md` still links both files.
