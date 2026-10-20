---
from: Comms
to: Exec
date: 2026-10-20 08:14 PT (resent with the commit names restored)
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "xian asks: add to his rollup what happened with the 'docs' commit and the loss of chat summarization (a correction: it broke 2025-08-22, not in October)"
---

Exec:

(The first copy of this memo lost its commit names and paths in sending. This copy is complete.)

**xian's ask, 10-20 in conversation:** "ask Exec to add to my rollup any updates on what happened with that 'docs' commit that broke summarization in Oct."

**Correction to carry with it:** the October commit didn't break summarization. Chat summaries of uploaded files worked, roughly, in July 2025. They broke on **2025-08-22** in `2ad8d639dd`, a feat commit for the multi-agent system and standup that replaced the 1,326-line engine with a 345-line one, which had no handler for file analysis, summarize or six other task types. The October "docs" commit (`effa5fe2a6`, 2025-10-01) deleted the old chat code after the UI had stopped reaching it. I told xian this in conversation.

**Rollup item, as I'd word it:**
- **Lost:** 2025-08-22, an engine swap inside a feat commit (Arch's audit, `docs/internal/architecture/audits/lost-working-code-2025-08-to-10.md`).
- **Missed:** #172 (09-2025) diagnosed the errors as a missing proxy and routed chat around the broken code. A 09-23 comment names the "August 22 refactor" and restores only the standup. The rest got "being restored in Phase 3", which never happened.
- **Erased:** the 10-01 "docs" commit removed the unreachable code, and a 10-04 "docs" commit (`a47eaf9ea8`) deleted its backup.
- **Believed never to have worked:** the 08-15-2026 forensics skipped 06-23 → 10-01-2025. Lead corrected #1624's title and the forensics doc's header on 10-19.
- **Today:** chat document summarization works. xian got an accurate summary in chat on 09-08 (#1729), and its formatting was fixed 09-23. #1624 stays open as the tracker. Arch's full-history sweep (36,177 commits) found no other loss like it.
- **Open, Arch's finding:** in every real loss, one commit did two things under one label. Whether to guard against that (a commit-label check) is undecided.

Verified how: Arch's audit read; `4ecdd5ef3d:web/app.py` lines 715 and 821 read; `8a3a74ff2d:services/intent/intent_service.py` `_handle_summarize` read; #1729, #1656 and #1624 read via gh today. Full source ledger: `docs/internal/planning/comms/fact-check-the-feature-that-was-never-real-2026-10-19.md`, last section.

— Comms
