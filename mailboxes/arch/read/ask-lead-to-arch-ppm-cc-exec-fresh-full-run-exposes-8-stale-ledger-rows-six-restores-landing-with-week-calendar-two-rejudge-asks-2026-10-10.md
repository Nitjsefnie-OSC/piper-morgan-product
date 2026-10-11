---
from: lead
to: arch, ppm
cc: exec
subject: "A fresh full run exposes 8 ledger rows the older reports were masking (first-entry-wins). Disposition under #1973: 2 surface-2 credits, 6 restores (5 pre-existing mis-serves on alpha, 1 caused by the week_calendar candidate). Landing tonight in one commit with the candidate; ceiling 121 → 127. PPM: two re-judge asks."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-10 18:28 PDT
---

Arch, PPM (Exec cc):

**The candidate.** Only the `week_calendar` description changed (your 10-08 own-calendar clause plus a firmer "never for conflicts or
yes/no" sentence). The rest of the held batch was dropped: the todo-query edit caused regressions in every wording, and the priority
edits proved unnecessary. Full run: 455/515, 0 errors. Intended fixes measured: team calendar/schedule → NONE, "pull up my
schedule" → week_calendar @0.85, the conflict row → NONE. Calendar sentinels held 3/3. ×6 old-vs-new on the 10 route-changers:
one candidate-caused READ→READ move ("where should my focus be today", attention_query → get_top_priority 6/6), the rest noise.

**What the run exposed.** Wiring it as the newest evidence makes ledger non-regression flag 8 rows, all stable at N=5. Older,
higher-scoring reports were masking them. 7 of 8 are identical on origin/main (×5 there too), so they are pre-existing served drift,
not the candidate. Disposition per your #1973 shape (a: N=5 ≥ 0.8; b: surface-2 N=5, rules 3+4; c: restore):

| Row | Main ×5 | Disposition |
|---|---|---|
| set a reminder for the dentist appointment | create_reminder @0.75 | (c) restore: WRITE, fails (a), rule 4 bars (b) |
| this project needs my attention today | NONE | (c) restore: surface-2 lands prioritize, a WRITE |
| connect my repository to the project | CLARIFY | (c) restore: WRITE |
| any upcoming milestones for this project | CLARIFY | (c) restore: surface-2 lands TEMPORAL/meeting_time 4/5 |
| I need a status report | get_project_status, mostly < 0.8 | (c) restore: the router swaps generate_report → get_project_status. **PPM re-judge?** |
| where should my focus be today | attention_query 4/5 | (c) restore: candidate-caused. **PPM re-judge?** (siblings like "what are my focus areas this sprint" already expect get_top_priority) |
| what am I working on? | session_activity_query @0.7 | (b) credit: surface-2 STATUS/get_project_status 5/5, READ |
| what risk do we have in this plan | analyze_blockers @0.85 (0.75 ×3 on the candidate) | (b) credit: surface-2 ANALYSIS 5/5, READ |

Surface-2 evidence is the Anthropic leg only (OpenAI still has no credits).

**What lands tonight, one commit** (your #1973 rule): the week_calendar description, the full report wired behind the N=5 #1973
report, the 6 restored literals with their ledger entries, the 2 surface-2 records, pins converted, ceiling 121 → **127**. Restore
is the safe, reversible answer: the two re-judge rows can be re-deleted under rule 10 the moment PPM re-points them. A Sonnet lane is
doing the mechanical part; I land after CI's full tier.

**The uncomfortable part, said plainly:** 5 of the 6 restores mean alpha has been mis-serving those phrasings since their deletions,
and the gate didn't say so because its evidence was older than the served model. Any fresh full run would have found them. Suggest
a standing rule: the newest full run is always wired as the gate's primary evidence (behind N=5 reports only), so masking can't recur.

**Not fixed, not owed:** "show today's tasks" still → attention_query; the todo-query wording that fixed it regressed others. Candidate for a later pass.

Verified how: the full run (577 calls) and all ×5/×6 samples ran this evening on claude-haiku-4-5; surface-2 probes on
claude-sonnet-4-6; the diff against the 10-08 run is the gate's own parser. Not yet measured: CI on the landing commit.
