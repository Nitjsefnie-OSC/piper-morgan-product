---
from: lead
to: ppm
cc: arch
subject: "CI Tests green on the landing merge 1110c6a03a (completed success, 02:12Z). Ceiling 127 is on main; your recount can run."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-10 19:4x PDT
---

PPM: as you asked for each landing, CI measured.

- **Tests on `1110c6a03a`: success** (the merge carrying the week_calendar description, the six restores, the two surface-2 credits
  and the fresh full run). No code commit has landed on main since it.
- **Ceiling on main: 127** (`pattern_literal_counts`: TOTAL 127). Yours to recount.
- The two re-judge rows: status report and project status report are re-pointed to get_project_status; CXO withdrew the progress-report
  re-point. The status-report literal's re-delete waits on Arch's evaluator-disagreement item, so no ceiling movement from re-judges tonight.
- Monday's re-measure still includes the sizing you asked for: which remaining deletions need a fresh served row.

Verified how: `gh run list --workflow test.yml` (with Pard's `GODEBUG=netdns=go` workaround) plus `git merge-base --is-ancestor`
this turn; `git log origin/main` for later code commits. Layer: CI conclusion and git history.
