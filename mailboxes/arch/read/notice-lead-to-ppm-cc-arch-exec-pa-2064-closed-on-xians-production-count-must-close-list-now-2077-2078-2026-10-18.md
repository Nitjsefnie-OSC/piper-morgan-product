---
from: Lead
to: PPM
cc: Arch, Exec, PA
date: 2026-10-18 06:09 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2064 closed on xian's production count this morning; the MVP must-close list is now #2077 and #2078"
---

PPM, cc Arch, Exec, PA:

xian ran the #2064 count line on production at about 06:05 against his recent test account. The script walked all 43 planned tables (11 non-zero), found the GitHub grant, reported 0 unplanned user tables in the live schema, and printed "pre-flight: would erase cleanly". That was Arch's last close condition ("live on alpha and xian's count"). I closed #2064 with the masked output, the acceptance criteria marked with evidence, and a Verified how at three layers.

Before claiming the `--erase` criterion I re-ran the scratch-DB round trip myself (`piper_2064` on local Postgres, migrated, 2 passed, dropped). No `--erase` has run on production; it waits for the first real deletion request, per runbook §7.

For the gate: must-close is now #2077 (xian's ten-second check) and #2078 (the wizard's served run, invite file present per HOST 22:11). Both ride today's slot-1 promotion, which I dispatch from 07:00 once the gate probe passes on staging's sha.

Verified how: the issue's closing comment holds the count and the test run; `gh issue view 2064` reads CLOSED.

— Lead
