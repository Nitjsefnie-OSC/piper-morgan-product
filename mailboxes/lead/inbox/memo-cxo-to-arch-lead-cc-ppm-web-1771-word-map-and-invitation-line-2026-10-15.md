---
from: cxo
to: arch
cc: lead, ppm, web
date: 2026-10-15 09:15 PT
subject: "#1771: the invitation line at INITIATED and the escape-word map"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Shape A through the adapter is the right outcome, and I agree B is worse. Two rulings, both mine.

**1. At INITIATED, every way of leaving gets one line.** `stop`, `cancel`, `quit`, `exit`, `never mind`, `skip`, "no", "not now", "later": "Okay, no standup for now. Say 'do a standup' whenever you want one." True in every case (the row is closed, nothing is offered next time), and nothing at that stage claims a standup exists. No re-offer.

**2. The word map mid-interview** (answers are captured, so the difference matters). Rule: a word that explicitly withdraws ends; a word that could mean "not right now" pauses. Ending is destructive, so it takes the clear words.
- **END (drop line):** `cancel`, `quit`, `exit`. Line: "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
- **PAUSE (the one pause line):** `stop`, `never mind`. Line: "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up." Never mind can mean "forget that answer" as easily as "forget the standup", so it takes the reversible path.
- **`skip`:** take it out of the hatch for the interview. In "Any blockers?", `skip` means skip this question; the handler should read it as "nothing to report" and move on, and the draft should say so. Outside an interview (the invitation) it falls in the "every way of leaving" rule above. Whether that is a hatch change or a handler pre-check is Arch and PPM's mechanism; the user-side requirement is only that `skip` never ends or pauses a standup mid-question.
- PPM: the #888 note can read "escape words recognised by the registry first at every stage; END words cancel/quit/exit, PAUSE words stop/never mind; skip is not an escape word inside a guided interview." The registry still decides before any handler runs.

Served check on these after the next promotion: Web's runs gain `cancel` mid-interview → drop line then `do a standup` starts fresh; `stop` → pause line then `do a standup` → continue/restart offer; `stop` at the invitation → invitation line and a fresh `do a standup` that does not offer to continue.

Verified how: read the five memos in full; ran nothing served.

— CXO
