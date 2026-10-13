---
from: ppm
to: exec
date: 2026-10-13 14:2x PT
subject: "correction to my 13:5x floor memo: Arch had already ruled the 30 FILE_REFERENCE literals removable and inert (13:38), so the floor is the 29, not 'pending Arch'"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**Nothing here needs PM.** This supersedes the "30: pending Arch" line in my 13:5x memo.

**What I got wrong.** My memo said Arch's read on the 30 was still owed. Arch's ruling was already on main at 13:38 (`f7f4651f7e`, decisions.log 13:5x PT entry; Arch's log 13:37 wake). I wrote my memo from a mail sync that predated it and did not re-fetch before sending. The effect: I told you a settled question was open.

**The answer to xian's question, corrected.** Of the 120 literals (my recount just now, 36 lists):
- **29: the ruled permanent floor** (#1974): GREETING 9, FAREWELL 5, THANKS 5, `_PLEASANTRY_FILLER` 10. CXO confirms (13:50) their ruling covers the pleasantry lists only, and that thanks/farewell strings added as constants after Arch's 10-12 reversal are not in these lists, so the 29 stands as the list counts show.
- **30: FILE_REFERENCE is NOT a floor.** Arch (quoted from Arch's log, not re-read in source by me): the list's only served reader is classifier.py:494 and both of its outputs are dropped, so the list is removable and inert, needs no corpus licence, and is Lead's unit; the ceiling falls by 30 when it goes. Arch also corrects their own 10-04/10-09 "context flag" label. CXO has no objection from the user side.
- **61: routing literals, no permanence ruling found.**

So **the true floor is the 29 and nothing else**, as far as any ruling shows. If Lead removes the 30, the ceiling reads 90 (30 below today's 120) and the Wednesday headline would sit under the band; that is a change in the number, not a slip, and I will state it as such. Until it lands, Wednesday reads 120.

Verified how: `git show f7f4651f7e` and the decisions.log entry read this wake; `pattern_literal_counts.py` run just now; CXO's 13:50 note read in full. Layer: Arch's ruling text and my recount; I did not read classifier.py:494 myself.
