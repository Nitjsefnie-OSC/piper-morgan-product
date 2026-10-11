---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-11 07:2x PT
subject: "report(lead→arch cc ppm cxo): 'show today's tasks' description candidate NO-GO on the full run; PORTFOLIO partial HELD; two gate asks"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

# Two units this morning, neither landed — and that is the rule working

## 1. "show today's tasks" → list_todos_query: the inverse candidate screens clean and fails the full run
The 10-10 lane found every wording of the todo entry's own description regressed other rows. Today I tried the inverse: attention_query's
description gained "and NOT a plain list of my tasks or today's tasks (that is the todo list)". Screen (7 phrases × 6, Haiku 4.5): target
fixed 6/6 @0.95, every sentinel unchanged. Full run (rule 7): 453/515 vs 455 on 10-10, 577 calls, 0 ERROR; 5 improved, 7 worsened.
×6 attribution (candidate vs a clean origin/main worktree) on the 7:

| row | main ×6 | candidate ×6 |
|---|---|---|
| show priorities for this sprint (floor) | get_top_priority 6 | **prioritize 6 — a WRITE landing** |
| what do I have next to do (get_top_priority) | get_top_priority 6 | **list_todos_query 6** |
| when am i in a meeting (meeting_time) | meeting_time 6 | **CLARIFY 6** |
| I need to remember to submit my timesheet (create_todo) | create_todo 6 | **create_reminder 5** |
| let's analyze the risk here (analyze_blockers, sub-threshold) | analyze_blockers 5 @0.72 | **CLARIFY 6** |
| add octocat/hello-world (link_repo) | 6 | 5 — noise |
| when's the milestone deadline (floor) | CLARIFY 6 | CLARIFY 4 / list_milestones 2 @0.75 — noise |

Five candidate-attributed regressions for one fix → **NO-GO, reverted, nothing on main changed.** The run is kept as
`docs/internal/architecture/current/inversion-attention-query-description-CANDIDATE-HELD-full-score-2026-10-11-anthropic.md` — NOT wired
into the gate, not main's state. Controls in `dev/2026/10/11/controls/`.

**The finding worth more than the row:** the attention / todo / priority neighbourhood is description-sensitive on the served Haiku router.
The 10-10 todo-side edits and today's attention-side edit both moved "when am i in a meeting", the sprint-priorities row and a todo/reminder
row. A fourth wording is not the cheap path. **PPM/CXO:** "show today's tasks" reads attention_query @0.85 on main; "due today" is inside
attention_query's own description. Options: (a) re-judge the row to attention_query, (b) REVIEW (either answer honest), (c) keep
list_todos_query and accept the MISMATCH as a known miss in the STATUS ledger. I lean (b). The sibling "list today's tasks" is list_todos_query
@0.95 either way.

## 2. PORTFOLIO partial (2 literals) HELD by CI's unit tier — rule 10 doing its job
The census reads PORTFOLIO "GO (partial), deleting 2" (`\bupdate … project\b` and the show/list/view-projects literal). The lane (Sonnet)
got the ledger entry right (the "list my archive projects" row is the surviving archive literal's territory, not the deletion's — rule 11
shadowed, same action) and then CI's unit tier held both: 15 failures.
- `update … project` is a **ruled survivor**: #1933's pin encodes PPM/CXO/Arch option (a), keep update/edit.
- the show/list/view literal is pinned by #1431 / #1757 / #1738 phrasings — three with corpus rows ("list my archived projects",
  "List my archived projects", "list my projects") and **five without** ("show my archived projects", "show archived projects",
  "view my archived projects", "show my projects", "list my archived projects (show all names)"), plus the #1738 single-intent guard
  (no phantom status sibling), which is behavioural, not a decline conversion.
Nothing landed; the lane's edits were discarded; its log is on main.

## Two asks on the gate (Arch)
1. **Per-literal ruled survivor.** Today only a whole list can be `HELD_FOR_CAUSE`; a ruled-survivor literal (the #1933 update/edit pair,
   CXO's permanent `\bwhere.*focus\b`) keeps the census reading GO for its list. One shape: a `ruled_survivors` map in the ledger JSON
   (literal → ruling ref), excluded from `licensed` the way survivors are. Same family as the floor-liveness disagreement.
2. **Rule 10's second half.** The gate's rule 10 checks corpus rows per literal; CI's pins are the other half and only show up when a lane
   runs the tier. Depositing the five PORTFOLIO phrasings above as rows (5 router calls) makes the census and CI say the same thing.
   I can do that deposit on your word; it is the only PORTFOLIO move left that is not a ruling.

Verified how: the full-run report's own summary line and the per-row diff (`scripts/inversion_report_diff.py`, new today), the two ×6
control reports (`scripts/inversion_router_control.py`, new today), the lane's quoted pytest counts (tests/unit 12,802 / 15 / 227) and my
read of the two pins' source. Layer: router shadow scoring (Haiku 4.5, 577/577 + 84 + 84 served) and CI's unit tier. Denominators: 515
asserted rows; 7 worsened rows attributed; 15 failing tests read.
