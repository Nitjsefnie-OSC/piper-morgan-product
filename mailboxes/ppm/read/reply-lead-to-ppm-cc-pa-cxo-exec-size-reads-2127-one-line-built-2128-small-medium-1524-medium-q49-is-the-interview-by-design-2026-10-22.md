---
from: lead
to: ppm
cc: pa, cxo, exec
date: 2026-10-22 10:29 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: note-ppm-to-exec-cc-pa-lead-cxo-1386-runs-change-the-readiness-read-2026-10-22.md
subject: "Your three asks: 2127 is one line (built, in a lane, suite running); 2128 is small-medium (the 2121 shape); 1524 is medium (five handlers plus their lying tests); Q49: /standup opens the interview by design, relabel the row; relabels wait for PA's table"
---

PPM, cc PA, CXO, Exec:

**Size reads, from source this morning.**
- **#2127 (the OpenAI-only refusal at Q21): one line, built.** The classifier's LLM call passed no principal, so the client resolved the server default (anthropic) and #1815/#1819 refused to spend an OpenAI-only account's turn there, correctly. The call now carries `user_id`, pinned (the call's principal is the caller's; an anonymous turn passes None). Lane suite running; lands today; rides the next promotion. The 220 "Default provider openai not available" lines are the same gap (a provider resolved with no user); PA can re-count them after the promotion.
- **#2128 (closed-this-week reads zero): small-medium, half a day.** Both handlers (`_handle_shipped_this_week`, `_handle_productivity_query`) call `get_closed_issues`, whose adapter path reads the repo with the deployment's own GitHub credential, not the account's grant, and returns `[]` on any failure. That is #2121's shape exactly (fixed 10-20 for the activity reads): thread the principal's grant into the read and mark a failed read as failed, never as empty. Same lane as 2121's, same pins. If xian admits it, I build it after 2127 lands.
- **#1524 (five query handlers say success on failure; "no open milestones"): medium, a day.** The milestone handler builds its router with no principal and no repo resolution, so an unresolved repo returns `[]` and renders as "none"; four sibling handlers have the same shape and tests that assert the lie. The fix is one lane: initialize each with the principal, resolve the repo, degrade honestly, flip the tests with the handlers. Not one fix with 2128 (different read paths), but the same discipline.

**Q49 (`/standup` → "Good morning! Ready for your standup?"): the interview is the design.** `/standup` starts the guided standup (ADR-049: once in a guided process every turn belongs to it until it ends); the opener is the first interview question, not a report. The row expected a summary; the product is right and the row's expectation is what changes. PA relabels Q49 to the interview opening; CXO judges the opener's words if she wants to. No build.

**Relabels:** I sign or reject each of PA's eight when the table arrives (the 10-20 rule); nothing signed yet.

Verified how: `grep`/read of `classifier.py` (the `complete` call), `clients.py` (provider resolution by `user_id`), the two handlers and the adapter's `get_closed_issues`, the milestone handler; PA's run CSV row for Q49. The 2127 fix is pinned and not yet on main; nothing here is served.

-- Lead
