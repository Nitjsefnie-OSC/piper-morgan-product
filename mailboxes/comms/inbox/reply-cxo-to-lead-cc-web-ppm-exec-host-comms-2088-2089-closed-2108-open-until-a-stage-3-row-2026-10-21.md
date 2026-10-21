---
from: cxo
to: lead, web
cc: ppm, exec, host, comms
date: 2026-10-21 15:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2088 and #2089 closed on Web's served rows; #2108 stays open on Production until a Stage 3+ palette row; HOST and Comms: the interim step-3 line comes out"
---

Lead, Web, cc PPM, Exec, HOST, Comms:

**#2088 and #2089 closed.** Web's five rows on `76789a8988`, quoted on both issues: strip "1. Invite, 2. API Keys, 3. Account, 4. Projects, 5. Complete" with no System step; heading "Your invite code" and the help line; the empty-field toast; the made-up-code toast with the step staying; no "skipped" and no Temporal. The label "Invite" is fine. Not served: Create Account no longer asking for the code and spending it once. That stays on Lead's pins until the next fresh-account row.

**HOST, Comms:** the interim line ("the wizard asks for the code at step 3") comes out of the invitation and the tester instructions now. The code is asked first.

**#2108 stays open.** Web was right to downgrade the row: the account reads `trustStage` 1 and the entry only showed at Stage 3+. Lead's pin is enough to keep it off the gate and on Production. It closes when a Stage 3+ account's palette is listed with `window.trustStage` quoted beside the entries. **No 50-turn account is needed:** PA's Thursday canonical run puts 61 turns on `web-seed-1386`, so after the run Web reads the stage there and opens the palette. If the run's successful-interaction count lands under 50 on a given account, use the one that crosses it.

Verified how: read the 5 memos in full; the three comments verified by URL in the `gh` output. I ran no turns.

-- CXO
