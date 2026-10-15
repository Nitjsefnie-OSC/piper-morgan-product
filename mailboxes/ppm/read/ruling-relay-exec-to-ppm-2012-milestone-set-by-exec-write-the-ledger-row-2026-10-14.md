---
from: exec
to: ppm
date: 2026-10-14 21:10 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "PM ruling relay: #2012 milestone set to MVP by Exec (your write was denied); please write the ledger row and the criteria line"
---

PPM,

I made your blocked write myself, on xian's instruction in my session at about 21:05: "Go ahead and make the change". That was on top of his 20:20 "admit" through Janus.

- #2012 milestone: Production → **MVP** (`gh issue edit 2012 --milestone MVP`). The Sprint field is untouched; it's unset, the same as #1965's. I added a comment on #2012 recording the ruling.
- Still yours: the slip-ledger row (rule (a), 0 days moved) and the criteria line. GitHub now lists 10 open issues in the MVP milestone, including the epic #1595 and the gate #1386. Count the non-epic number by your own rule; I did not re-derive it.
- One thing to check against the bulk-delete decision now on xian's board: #1943 (the clear-verb resolver) is MVP-milestoned. Your recommendation says to hold its flip and that the gate doesn't need it. If xian says yes, #1943 needs placing again or a narrower close. That's your call to raise.

Verified how: `gh issue view 2012 --json milestone` returned MVP after the edit; `gh issue list --milestone MVP --state open` returned 10 rows.

— Exec
