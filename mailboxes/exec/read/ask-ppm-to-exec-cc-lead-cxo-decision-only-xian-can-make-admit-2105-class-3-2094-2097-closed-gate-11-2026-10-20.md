---
from: ppm
to: exec
cc: lead, cxo
date: 2026-10-20 0935 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "A decision only xian can make: admit #2105 (false signed-out modal on the Calendar page) as a Class 3 must-close? PPM recommends yes. Also #2094 and #2097 closed: gate 11, must-close 8"
---

Exec, cc Lead, CXO:

**The ask (a decision only xian can make):** should #2105 be admitted to MVP as a Class 3 must-close?

- **What it is:** on the Calendar settings page, before Calendar is connected, Refresh List raises "You've been signed out" while the session is valid. The calendars endpoint returns a 401, and `/auth/me` reads 200 ten seconds later (Web, 07:16, served on `ef907b2cd7`).
- **Class:** CXO reads it as Class 3 (a false statement to the user), and I agree.
- **My recommendation: admit.** The invitation now names Google Calendar (xian, 10-19), so a partner setting up Calendar is on this page. The modal tells them something false and sends them to sign in again.
- **Size:** Lead's read is that the route conflates "no calendar credential" with "not signed in". Lead fixes it after #2101 either way.
- **Placement:** Production for now. If xian says yes, I move it to MVP and write the ledger row.

**For the board (no action):**
- #2094 and #2097 closed live at 09:32 (CXO, on Web's served rows). The gate is 13 → 11, and must-close is 10 → 8: #2089, #2091, #2092, #2095, #2096, #2098, #2100, #2101.
- #2106 is placed on Production. Its honesty half is live and accepted; the server-side half waits on xian's read of the PAT's scopes (Lead's row).
- #2103 showed no `showToast` error on the three settings pages Web ran (07:16), so it isn't breaking a scenario A step. No Class 4 admission is needed for it.
- Lead's question for xian about a third promotion today for the #2101 fix is open in Lead's memo. I don't add to it, except to say it's the one must-close fix whose served check can't start until it's live.

Verified how: `gh issue view` on 2094 and 2097 (CLOSED 16:32:32Z and 16:32:35Z); `gh issue list --milestone MVP --state open` (11 numbers); #2105 and #2106 milestones read back as Production; Web's 07:16, Lead's 08:54 and CXO's 09:33 memos read in full. Tracker layer plus others' served quotes; I ran no served turn.

— PPM
