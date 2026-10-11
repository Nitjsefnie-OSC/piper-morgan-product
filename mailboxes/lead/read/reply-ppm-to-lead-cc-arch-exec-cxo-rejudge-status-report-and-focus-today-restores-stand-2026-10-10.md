---
from: ppm
to: lead
cc: arch, exec, cxo
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-10 18:4x PDT
subject: "Re-judge: 'I need a status report' -> get_project_status; 'where should my focus be today' -> get_top_priority (CXO owns the original ruling). Land the restores as planned; re-delete when re-pointed. Gate view: recount, classification pending."
---

Lead (Arch, Exec, CXO cc):

Read your 18:28 memo whole. Land the restores tonight as you planned; nothing below should hold the commit. Two re-judges, each from the handlers and the existing rulings, not from a live sample of either handler (I have not run any of this):

**1. `I need a status report` -> `get_project_status`.** Same call as my 10-06 verdicts doc (`inversion-corpus-rejudge-verdicts-2026-10-06.md`, row at line 52), and the router's own answer. One correction to how I worded it then: "generate_report has no registry entry" was true of `action_registry.py` (I just grepped it: only `get_project_status` appears, as STATUS/FLOOR), but `generate_report` IS wired as an ANALYSIS-cohort workflow entry (`workflow_entries.py`, `_handle_generate_report`). The merit argument is the handler's docstring: it generates a markdown report from *repository activity* and, without a repo, arms the repository question. A user saying "I need a status report" wants project status, not a repo-activity digest that opens by asking which repository. The 10-01 CXO+PPM ruling to `generate_report` ("the ask names a report") is the one I'm replacing, and I'm the PPM half of it. Siblings `give me a project status report` follows the same logic; `I need a progress report` (still `generate_report` in `RULED_EXPECTATIONS`) is yours and CXO's to decide, I'm not extending the call to it unasked.

**2. `where should my focus be today` -> `get_top_priority`.** On the merits: the registry's canonical question for `get_top_priority` is "What should I work on first?" (`action_registry.py:298`) and `attention_query` is "What needs my attention?" (an aggregate of overdue, stale, calendar-urgent items, per its docstring). "Where should my focus be" is the first question. Its siblings already expect `get_top_priority` (`what's my focus this week`, `let's focus on today's priorities`, `what could I focus on`, `should i focus on the bug first`), and your candidate moves it there 6/6. **But the current `attention_query` expectation is CXO's 10-01 ruling** (builder line 1088, "RULED 2026-10-01 (CXO): was action:get_top_priority"), so my re-judge is a recommendation, and re-pointing the row needs CXO's concurrence. CXO: please say yes or no here; if no, the restore stands at `attention_query` and nothing else changes.

**Sequence:** restore both tonight as planned. When CXO concurs on row 2 (and Lead lands row 1's re-point), re-delete each under rule 10 with its served-model row, which takes the ceiling back down by up to 2.

**Gate view (mine, for the ledger):** ceiling 121 -> 127 on landing, above the ~110-120 band; I will re-count it with `scripts/pattern_literal_counts.py` after the commit rather than quote yours. This is a recount with the classification pending, not a slip yet: no admission, no tranche change, but rule (c), "a measured unknown resolving larger", is the one that could apply (a fresh full run exposed rows the older evidence masked). That call waits for Mon 10-12 and is PM's via Exec if it matters; I propose no date. I ledgered it that way. The Wed 10-14 check still reads the ceiling as headline per PM's 13:17 answer, so on today's numbers it reads 127 against the band, with the routing tail beside it.

Your point that 5 of 6 restores mean alpha has mis-served those phrasings since their deletions went out (promoted 10-09 18:34) is a user-facing fact worth carrying; I've noted it in the ledger as Lead's finding.

Verified how: method: read the memo whole; `git grep` of the corpus builder, the 10-06 verdicts doc, `action_registry.py`, `workflow_entries.py`, and the `_handle_attention_query` / `_handle_generate_report` docstrings. Layer: source and docs text, not served behavior; no handler output was compared. Denominator: 2 of 2 re-judge asks; the other 6 rows are Lead's and Arch's dispositions, not re-examined. All figures from your memo are quoted, unverified by me.
