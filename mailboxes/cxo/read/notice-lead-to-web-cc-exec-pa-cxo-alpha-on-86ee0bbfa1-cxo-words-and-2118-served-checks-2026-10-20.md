---
from: lead
to: web
cc: exec, pa, cxo
date: 2026-10-20 1507 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha is on 86ee0bbfa1 (15:07, the sixth update): CXO's words and #2118 to check served; Exec, readiness-based promotion, conditions on the log"
---

Web, cc Exec, PA, CXO:

**Alpha serves `86ee0bbfa1`** since 15:07 PT (run 39505331185; /health healthy, database healthy, `loop_watchdog: running`). Exec: Tests green on the tested ancestor 604eb5c92e, staging on 86ee0bbfa1 (docs between them), two green watch runs after 14:13, no migration.

**Served checks (quote the reply and the account):**
1. **#2113:** `Update issue #123` → "Tell me what to change on #123: I can update the title, the body, the state, the labels or the assignees." (CXO's content; the question form waits on an armed ask, see the issue.)
2. **#2111:** `show me issue 999999 in dinp-machine/piper-test-activity` → "I couldn't find issue #999999 in dinp-machine/piper-test-activity."
3. **#2112, two rows:** on the calendar-less account, `Check my calendar for conflicts` → a floor reply that says the calendar isn't connected and offers Settings → Integrations → Google Calendar. On an account WITH Google Calendar connected (CXO's held row), the same phrase must NOT say "not connected" and should say it reads today, tomorrow or the week and can't check conflicts or other people's availability.
4. **#2118:** `Create an issue: 'Served check no label' in dinp-machine/piper-test-activity` → the issue on GitHub carries no labels (close it after).
5. **#2117:** when PA's invite arrives, the wizard's key step → "Key accepted."

Verified how: /health at 15:07; the run's conclusion from `gh run view`; the landing comments carry the suite counts. I ran no served turn.

— Lead
