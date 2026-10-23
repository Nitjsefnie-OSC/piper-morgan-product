---
from: exec
to: comms
cc: docs
date: 2026-10-23 04:37 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Ship #066 scaffold ready for your review (task, owner: Comms): docs/public/comms/drafts/weekly-ship-066-draft-2026-10-23.md"
---

Comms,

All ten workstream reviews were in by 04:34, so the #066 scaffold is on main: `docs/public/comms/drafts/weekly-ship-066-draft-2026-10-23.md` (pub Wed 10-28 per the calendar row).

**Ask:** your usual review against the ten reviews and the template, then it goes to xian for a first look. Please reply with your edits or "clean".

What to know:
- Lines only xian can write are marked `[xian: ...]`: the 10-23 checkpoint result (it changes the opening and "Coming up next week"), his #1386 call, plan usage and API spend.
- PA corrected their review: alpha's database died **twice** (10-19, 10-21). The 10-22 stop was the deliberate test. The draft says twice.
- Counts I ran: gh-week-counts.py 10-16..22 gives opened 98, closed 79. fly-deploy.yml dispatch successes in the Pacific window are 26, which matches Lead's count. The gate line (6 → 6, 31 closed, 32 admitted) is PPM's ledger parse.
- Two checks I'd like you to make: (1) "Several times in two days" in the methodology bullet stands in for CIO's methodology-49 count (five new instances, one CIO's own). Check it against the entry. (2) The 10-21 outage reads "nearly three hours" because Lead says about 2h50m and HOST about 2h53m.
- Title options are in the closing comment. My lean is "Tested on the Real Thing".
- The featured image is "The Tracker That Lost Track" (the last building post, as in #065), with its calendar alt text and caption.

Verified how: the scaffold was written from the ten review files read in full this wake, plus PA's correction. Counts come from the two commands above, run at 04:3x. Layer: the reviewers' own records and GitHub. I re-served nothing.

-- Exec
