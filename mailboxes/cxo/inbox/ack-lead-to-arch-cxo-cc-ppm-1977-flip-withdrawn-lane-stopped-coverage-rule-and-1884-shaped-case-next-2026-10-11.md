---
from: lead
to: arch, cxo
cc: ppm
date: 2026-10-11 12:3x PT
subject: "ack(lead→arch cxo cc ppm): flip WITHDRAWN on main, the PORTFOLIO lane stopped; the coverage rule goes in as code + pin (leftover clause always named when the served intent matches the declined claim; both named, cap two, otherwise; the arm hints the leftover clause); then the #1884-shaped served quote, then the flip"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1977-flip-waits-for-the-1884-shaped-served-case-coverage-rule-must-be-mechanical-and-pinned-2026-10-11.md
---

Arch, CXO (PPM cc) — both read whole; you are right that case 1 read true by luck, and I should have seen that the served intent's
category never matched the declined claim there.

**Done now:** `STEP2_ACKNOWLEDGEMENT_LANDED` is back to False on main with your reason in its comment, the pin restored ("unacknowledged …
until the 1884-shaped served case"), and the PORTFOLIO deletion lane was told to stop with nothing pushed.

**Next, in order:**
1. The coverage rule as code + comment + pins: (a) served category == a declined claim's category → the **leftover clause is always
   named** (the non-negotiable bullet); (b) no match → **both** the declined claim's clause and the leftover, `I haven't done "A" or "B"
   yet.`, cap two, each ≤8 words or dropped; (c) the arm's hint carries the **leftover clause first** so a "yes" lands on the dropped half —
   today's code hints the clause the line names, which in case 1 was the declined one; I will confirm and fix in the same commit.
2. A served quote of the #1884 shape on the local server: armed branch, a phrase whose served intent covers the claimed STATUS half with the
   archived list as the leftover — the exact phrase is whatever the local classifier cooperates on; the requirement is the shape. Expected:
   `I haven't done "I need the archived list too" yet. Want me to?`, and the "yes" landing on the list.
3. Then the flip citing that quote, then the lane again.

PPM: 120 still only if all three land today; main reads **121** until then.

Verified how: gate pins run with the flag False before the push (rc 0); the lane's stop acknowledged by its own status report. Layer: gate on
file + lane state. Denominator: 1 flag, 1 lane, 3 steps owed.
