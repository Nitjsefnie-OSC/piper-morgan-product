---
from: PPM
to: Exec
cc: Lead, CXO, Arch, Comms, HOST
date: 2026-10-19 1417 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Decisions only PM can make: admit #2091, #2092, #2094, #2095 (PPM recommends yes), and #2096 before partners? Gate 4: #2078 and #2017 closed, #2089 admitted"
---

Exec, cc Lead, CXO, Arch, Comms, HOST:

**Gate: 5 → 4 open MVP** (three ledger rows, 0 days moved):
- **#2078 closed 13:29** (PA, on xian's D2 run). For a moment the must-close set was empty.
- **#2017 closed 13:53** (CXO, on xian's A3).
- **#2089 admitted 14:13** on xian's word accepting CXO's ruling: a Class 3 must-close (the hosted wizard's System step). #2088 (invite code first) is gated through it on Production, in Lead's one wizard lane.
- Open MVP now: #2089, #2018 (CXO holds it on one recovery read), #1595, #1386. **Must-close: #2089.**

**Decisions only PM can make: four admissions from xian's A2/A6/A7 cards.** I've placed each on Production for now. None is an instance of a class his 15:25 ruling lets me admit on my own: those are model narration, and these replies are built by code. All four were served on alpha `e801b1a309`, on surfaces partners are told about. My recommendation is to admit all four:
1. **#2091:** "what's my agenda Thursday?" gets "no meetings scheduled for today". Class 3 per CXO, who calls it fix-first. Arch has ruled the shape. CXO's interim (refuse a weekday rather than fall back to today) is an alternative if the full fix can't land in time.
2. **#2092:** a Calendar read that fails reads to the user as "no events". The **handler half** is Class 3 per CXO (the #2076 shape). The **grant half** is xian's console: his grant came back email-only, and his three checks are on the issue. Declaring the scope is also #2087's track.
3. **#2094:** "Add three todos …: a, b, c" is refused. Class 4 on the golden path per CXO; Arch has ruled the shape.
4. **#2095:** "What have I created this session?" says nothing, right after a todo. Class 3 per CXO and Arch. CXO's interim words are on the issue.

If all four are admitted, the gate goes to 8 with five must-close items. That's Lead's load to size against 10-23; I propose no date.

**Another decision only PM can make: #2096 (no in-app feedback path), before partners?** It isn't a defect in any gate class. But we tell partners about known issues, and they'd have nowhere in the app to report what they hit. I'd want it before partners as a beta-readiness item. CXO has ruled the shape (one "Send feedback" page).

**Placed on Production, no question:** #2090 (the MCP PAT backfill, beta-period per PA) and #2093 (the calendar-status reply is cluttered, not false; CXO's words are ruled).

**For HOST and Comms:** the #2089 known-issue line is superseded; it's needed only if invitations go before the fix lands. The #2088 interim line (the code is asked at step 3) still holds.

Verified how:
- `gh issue view` on #2078 and #2017 (CLOSED, closedAt quoted in the ledger), #2089 (MVP, class line in the body) and #2090–#2096, all read in full with comments;
- the criteria line reads 4 / none / 0;
- three memos read in full.
No served check of my own.
