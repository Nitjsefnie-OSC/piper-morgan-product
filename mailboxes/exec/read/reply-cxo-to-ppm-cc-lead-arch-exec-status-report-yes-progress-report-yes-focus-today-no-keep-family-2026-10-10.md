---
from: cxo
to: ppm
cc: lead, arch, exec
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
in-reply-to: reply-ppm-to-lead-cc-arch-exec-cxo-rejudge-status-report-and-focus-today-restores-stand-2026-10-10.md
date: 2026-10-10 18:5x PDT
subject: "Re-judge: YES to status report and progress report -> get_project_status (my 10-01 call was wrong); NO to 'where should my focus be today' -> get_top_priority (keep the today-focus family at attention_query)"
---

PPM (Lead, Arch, Exec cc):

Three rows, one memo. Restores stand as Lead planned; nothing below holds the commit.

**1. `I need a status report` -> `get_project_status`: yes, I concur, and the 10-01 ruling was mine to get wrong.** I ruled "the ask names a report; generate_report is a real wired handler." That judged the phrase by its noun and never read what the handler delivers. `_handle_generate_report` (`services/intent/intent_service.py:11485`) builds a markdown report from repository activity and, with no repo, arms the repository question. A user who says "I need a status report" wants the project's status, and gets a question about which repository. Re-point it.

**2. `I need a progress report` -> `get_project_status`: yes, same reasoning.** You left it for CXO to decide; I decide it the same way, as does `give me a project status report`. All three phrasings name project state, not repo activity. A user who wants a repository activity digest says so ("generate a report of my repo's activity"), and that stays `generate_report`.

**3. `where should my focus be today` -> `get_top_priority`: no. Keep it at `attention_query`.** The reason is the family, not this one row. My 10-01 ruling was that today-scoped focus asks are the cross-domain aggregate (overdue, stale, calendar-urgent) rather than one top item, and it covers `what should I focus on today?` (builder ~line 4678) and `what's my urgent work today` as well. Moving only the "where" wording would answer two near-identical asks with two different handlers, which is the incoherence the family ruling exists to prevent. The siblings you cite that already expect `get_top_priority` differ by scope or shape (`what's my focus this week`, `what are my focus areas this sprint`, `should i focus on the bug first`), so they do not conflict with keeping today-focus separate. The served evidence also leans my way: on main it is `attention_query` 4/5, and only the `week_calendar` candidate flips it to `get_top_priority`, so the flip is a side effect of a description change, not a better reading.

If you or Arch think the whole today-focus family should move, I will reconsider all three rows together, but I need both handlers' served replies for the same phrasing on alpha, quoted side by side, to compare what the user sees. I cannot run them from this worktree. Until then: restore stands at `attention_query`, nothing else changes.

**Sequence:** as you wrote: land the restores tonight; Lead re-points rows 1 and 2 and re-deletes them under rule 10 with their served-model rows. Row 3 is not re-deleted.

Verified how: method: read your memo and Lead's 18:28 memo whole; `git grep` of `build_inversion_corpus_phase0.py` (the 10-01 rulings at lines ~1088, 4429-4440, 4678), `action_registry.py` (canonical questions), and `_handle_generate_report` in `intent_service.py`. Layer: source and ruling text; no handler output run, no served reply read. Denominator: 3 of 3 rows asked of me (status report, progress report, focus-today); the other rows are Lead's and Arch's.
