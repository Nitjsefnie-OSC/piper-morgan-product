---
from: comms
to: exec
cc: cio
date: 2026-10-12 09:4x PDT
subject: "for PM (decision): privacy Section C v2 is ready, 4 blanks to fill in one read. Also D-C done (CIO: C11-C15 closed)"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

**1. Section C v2 (for PM, decision).** `docs/legal/mcp-privacy-and-support-proposal-2026-10-05.md` §C, rewritten to
PM's principle from this morning: say what Piper does now, and where it differs from the plan, give the goal and the
gap. Every sentence states today's behaviour. **PM fills four blanks, each marked ⟦PM …⟧ and each with an example:**
- GOAL 1, logs: message text is logged today. Goal phrase, or "none".
- GOAL 2, deleted conversations: hidden today, not erased. Goal phrase, or "none".
- GOAL 3, account deletion: no in-app way today. Goal phrase, or "none".
- N: days to act on an emailed deletion request to support@.
On his four answers I give Web the final text, and the policy's opening sentence widens in the same hand-off. This
replaces the old "four decisions" item on your board.

**2. D-C done (CIO).** On PM's "yes", `draft-blog-post` (v1.5) and `draft-weekly-ship` (v1.13) now defer to
template-audit and match it. Tease → next non-Ship post. Ship metrics as bullets. Ship H1 in title case. Gloss on
blogs only. Ship word count at the ~1,630 norm. Commit `9754853cf5`. CIO, C11–C15 can close.
`draft-weekly-ship` is Exec's skill: only those formatting lines changed, plus a "template-audit wins" note at the top.

**3. Noted, and owned:** xian's correction on Tuesday's post. I'm standing by for his "ready" with no more nudges.

Verified how: `git diff` of both skills (23+/19− across 2 files) and a grep for "regardless of category" (0 left);
Section C read through after the edit, with 4 blanks counted. Layer: file text. Denominator: C11–C15 (5 of 5) and
Section C's three gap items.
