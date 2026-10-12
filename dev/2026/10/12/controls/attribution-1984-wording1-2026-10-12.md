# #1984 half (2) — wording 1 (40b3c95b33) full run + ×6 attribution — 2026-10-12 07:0x PT

Full run on the candidate tree merged with main d296221de5 (c84a039451):
`inversion-1984-status-description-full-score-2026-10-12-anthropic.md` — 475/529 asserted, 593 calls, Haiku 4.5 592/593,
1 ERROR (an API error on "what's the current status"; ×6 below reads get_project_status 6/6). Diff vs main's newest report
(`inversion-week-calendar-description-full-score-2026-10-10-anthropic.md`, `scripts/inversion_report_diff.py`): shared 513,
old MATCH 455 → new 460, **13 improved** (incl. the target rows: "what am I working on?", "tell me what I'm working on",
"show my active work", "quick check, working on now?" → get_project_status; "list my projects", "what are my active projects"
→ manage_portfolio), **8 worsened**, 7 route-changed. The #1984 row reads PLAN[get_project_status→list_archived_projects] (MATCH).
Shared-subset gate vs the 08-12 baseline: 1 named regression left ("analyze the file I uploaded", identical on 10-10 and 10-11 —
pre-existing); the other two named on 10-10 ("list my projects", "what am I working on?") now MATCH.

×6 attribution, clean origin/main worktree (79eeea87c7) vs the candidate tree, same phrases, same minute, Haiku 4.5 (48 + 48 calls;
`ctl-1984-worsened-main-2026-10-12.md`, `ctl-1984-worsened-candidate-2026-10-12.md`):

| row | expected | main ×6 | candidate ×6 | read |
|---|---|---|---|---|
| let's analyze the risk here | analyze_blockers | analyze_blockers ×6 | CLARIFY ×6 | **ATTRIBUTED** |
| are we behind upstream at all | local_git_status_query | local_git_status_query ×6 | analyze_commits ×5, CLARIFY ×1 | **ATTRIBUTED** |
| tasks I'm actively working on | list_todos_query | list_todos_query ×5, session_activity_query ×1 | session_activity_query ×6 | **ATTRIBUTED** |
| what projects am I working on | list_projects | list_projects ×6 | get_project_status ×6 | **ATTRIBUTED** ("what they are working on" pulls it) |
| show priorities for this sprint | floor (get_top_priority) | get_top_priority ×3, prioritize ×3 | prioritize ×6 | main already split; candidate hardens the rail side — borderline |
| what's the current status | get_project_status | get_project_status ×4, CLARIFY ×2 | get_project_status ×6 | improved (the run's ERROR was transport) |
| I need to remember to submit my timesheet | create_todo | create_reminder ×4, create_todo ×2 | create_reminder ×6 | main already mostly wrong — served-model drift, not attributed |
| when am i in a meeting | meeting_time | CLARIFY ×6 | CLARIFY ×6 | pre-existing drift (the fragile row), not attributed |

Also ×6 both trees on the one deposit row scored for the first time this run, "show me when we shipped the API" (expected
check_completion_status): shipped_this_week ×6 on BOTH trees — a pre-existing known miss of the 10-11 COMPLETION_HISTORY deposit,
not this candidate's.

**Verdict: wording 1 is NO-GO** under Arch's condition (4) — four attributed regressions (one ANALYSIS survivor, one QUERY, two
STATUS-neighbourhood rows the "what they are working on" clause pulls into status). Not landed.
