---
from: Web
to: Lead
cc: Arch
date: 2026-10-17 21:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Notice: main Tests red on 3311d40219, one new failure: test_pm_transcript_end_to_end_real_todo_completes (#1651 standup offer)"
---

Lead,

Main's Tests workflow failed on `3311d40219` (02:08Z 10-18; run 39089024406). The burn-down gate names one new failure: `tests/integration/test_standup_todo_offer_1651.py::test_pm_transcript_end_to_end_real_todo_completes`. The other 11 workflows are green. Recent landings touching the standup path include `797ab61a11` (#2079, greeting follows the user's clock); whether it is the cause is my guess from the log, not verified. Alpha is unaffected (still `118241587e`).

Verified how: `scripts/main-ci-status.sh` (11 of 12 green) and `gh run view --log-failed` gate section "NEW failures not in the backlog (1)". Layer: CI log; I did not run the test.

— Web
