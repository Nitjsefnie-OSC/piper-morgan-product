# Rule-7 attribution, #2132/#2133 lane (claude/lead-2132r), 2026-10-22

Lane catalog changes:
- new op `compare_documents` (READ, read_referent);
- new op `decline_batch_issues_from_meeting` (READ, no flip group);
- `analyze_data`'s description narrowed to repository activity;
- `analyze_document`'s description rewritten, with an args sentence ("Put the name the user gave in args: title = their words for it").

**Full runs, same minute** (router: anthropic claude-haiku-4-5):
- main 484/542 asserted;
- candidate 492/555.
- **Shared rows:** 6 improved, 9 worsened, net −3 (`inversion_report_diff.py`).
- **New rows:** 11/13 MATCH; 2 CLARIFY ("What does this document say?", "Make tickets for each action item from the standup").

**×6 attribution, same minute:**

| phrase | main | candidate | no-new-ops variant | no-description variant |
|---|---|---|---|---|
| modify the status document | update_document ×6 | CLARIFY ×6 | CLARIFY ×6 | CLARIFY ×6 |
| show priorities for this sprint | get_top_priority ×6 | prioritize ×6 | prioritize ×6 | prioritize ×6 |
| any old prs lying around | stale_prs ×6 | list_prs ×6 | stale_prs ×6 | stale_prs ×5 |
| are we behind upstream at all | local_git_status_query ×6 | CLARIFY ×5 | CLARIFY ×5 | local_git_status_query ×6 |
| what did we make earlier | session_activity_query ×6 | NONE ×6 | CLARIFY ×6 | session_activity_query ×6 |
| what meetings are coming up | week_calendar ×6 | meeting_time ×6 | week_calendar ×6 | meeting_time ×5 |
| Analyze this document | CLARIFY ×6 | analyze_document ×6 | analyze_document ×6 | CLARIFY ×6 |

Not attributed (they wobble on main too): "what's the most critical thing" (3/3 on main), "what are my active projects", "show today's assignments".

**Verdict: the candidate FAILS rule 7.** Six rows are candidate-attributed. Two of them flip under either half alone, so the perturbation is not one change. The description half is what moves "Analyze this document" (the target row). Held; not landed.

Files:
- full runs: `rule7-2132-candidate-full.md`, `rule7-2132-main-full.md`;
- ×6 runs: `rule7-2132-candidate-x6.md`, `-main-x6.md`, `-main2-x6.md`, `-noops-x6.md`, `-nodesc-x6.md`.
