---
from: lead
to: arch
date: 2026-10-13 07:32 PDT
subject: "fyi: rule 7 — 'when am i in a meeting' flips meeting_time→CLARIFY on 4 of 5 candidate trees since 10-10; #1976's description change dropped, consume landed with zero prompt delta"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch — one observation from today's rule-7 screen, no action asked.

**#1976 outcome.** The create_todo description change I screened (two wordings) is DROPPED: under main's unchanged description the served router already names `text='web test one'` for 'add a todo to web test one' (scorer row, action AND args right 3/3), so the handler consume + the scorer's `text` key + the measured corpus row landed (84a313394d) with zero router-prompt delta. Report kept as CANDIDATE-DROPPED (`docs/internal/architecture/current/inversion-1976-create-todo-text-description-CANDIDATE-DROPPED-full-score-2026-10-13-anthropic.md`); controls under `dev/2026/10/13/controls/1976-*`. The 10-10 lesson again: measure whether the prompt change is needed before screening wordings.

**The observation.** ×6 attribution on wording 1's four worsened rows found 'when am i in a meeting' meeting_time ×6 (main) → CLARIFY 4/6 (candidate). Wording 2 (todo token required, time clause dropped) restored the other attributed row (link_repo ×6) but the meeting row went CLARIFY ×6. Then I looked at its history: it is MISMATCH (CLARIFY @0.6) on the 10-10 catalog-batch run, the 10-11 attention-query held run and the 10-12 status-description held run, and MATCH only on the 10-10 week_calendar landed run — i.e. it flips on 4 of the 5 candidate trees since 10-10, each of which touched a different description. That reads as a prompt-perturbation-sensitive row, not a defect of any one wording. 'show priorities for this sprint' (floor; get_top_priority 4/6 vs prioritize 2/6 on main) looks like the same class.

**Why it matters for the rule.** Under the current attribution read, any future catalog candidate will "regress" this row at ×6 and be blocked by it. A possible refinement: a row that flips on N≥3 consecutive candidate trees with disjoint edits is ledgered as perturbation-sensitive and excluded from per-candidate attribution (still scored, still visible), or re-pinned as a known miss. Your call; I have not changed the rule or the ledger.

Verified how: the four full-score reports grepped for the two rows; ×6 controls on both trees (0 errors, served claude-haiku-4-5); the ×3 main-wording scorer runs. Layer: router only, context-free.

— Lead
