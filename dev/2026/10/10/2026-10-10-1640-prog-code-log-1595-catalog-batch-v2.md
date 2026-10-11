# Session log: prog-code, #1595 catalog batch v2 (model Sonnet 5 / 5.5)
- Setup: scratch worktrees on held branch and origin/main; router screen via inversion_phase1_shadow_score.py --phrase.
- Baseline (main) sentinels 3/3 each recorded (40 calls). Main: "pull up my schedule"->meeting_time, "show the team calendar"->week_calendar (targets genuinely failing).
- Isolation: week_calendar held wording alone caused "conflict"->week_calendar@0.72; todo-query description edit (any wording tried) caused "when am i in a meeting"->CLARIFY and priority rows -> attention_query. get_top_priority/prioritize edits not needed for sprint target (main text gives get_top_priority@0.85).
- Candidate 2 (week_calendar only, strong conflict disclaimer): all regressed rows fixed, 3/4 targets; "show today's tasks"->attention_query on main todo text.
- Candidates 3-5 restored todo-query edit: fixes today's tasks but CLARIFY/priority regressions return.
- Calls used: 250/250 (cap reached). Reboot at ~15:00 interrupted; scratch lost, branch survived.
- Branch left at candidate-2 wording. Discovered issues filed: none.
