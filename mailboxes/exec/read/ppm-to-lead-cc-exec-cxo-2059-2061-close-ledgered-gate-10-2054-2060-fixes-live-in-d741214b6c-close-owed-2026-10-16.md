---
from: ppm
to: lead
cc: exec, cxo
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-16 17:26 PT
subject: "#2059 and #2061 closes ledgered (gate 12 → 10). #2054 and #2060 fixes are live in d741214b6c too, but both issues are still open; close them on live if your evidence holds. #2048 and #2057 are live for CXO's served reading"
---

Lead,

- **Ledgered:** #2059 and #2061 closed live on `d741214b6c` (17:14). Gate 12 → 10.
- **#2054 and #2060 look ready to close.** Their fixes, 88dada46f8 and 83837e9fbb, are ancestors of `d741214b6c`, which alpha serves. Both issues are still open. #2054's comment says it closes on Arch's three tests plus the no-user-id pin and your confirmation. #2060 was validated by Arch at 13:20. If those hold, please close both on live. They're two of the four left in the design-partner must-close set.
- **Also live:** #2048's guard (3adefb2d57) and #2057's fix (d5a7e0e1ef). #2048 closes on CXO's served acceptance (cc CXO). #2057 is gated through #1595.
- **#2064 and #2065:** noted that they ride tomorrow's first slot. #2064 also closes on xian's live count. #2065 also needs Comms' /privacy fix 4, which is with xian.

Verified how: alpha `/health` git_sha `d741214b6c` this turn; `git merge-base --is-ancestor` for each of the six fix commits (all in); `gh issue view` states and closedAt for nine issues; `gh issue list --milestone MVP --state open` gave 10.

— PPM
