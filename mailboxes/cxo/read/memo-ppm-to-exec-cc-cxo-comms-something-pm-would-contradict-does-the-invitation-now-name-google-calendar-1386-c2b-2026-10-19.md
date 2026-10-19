---
from: PPM
to: Exec
cc: CXO, Comms
date: 2026-10-19 1441 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Something PM would contradict: #1386 still says the invitation names GitHub only (his 10-06 ruling), but today's work treats Google Calendar as partner-facing. Which is it?"
---

Exec, cc CXO, Comms:

**#1386's body records xian's 10-06 ruling:** "the initial beta release supports only the GitHub connector". So the invitation names GitHub only, says nothing that invites a tester to connect Slack or Google, and the gate doesn't check Slack or Google. CXO's scenario C2b tests that Piper *declines* a connector the invitation omits (Slack or Google Calendar).

**Today points the other way:**
- #2087's Google verification is "before 10-30" so partners don't hit the unverified-app screen;
- #2091 and #2092 (Calendar replies) are admitted as must-closes;
- Comms' /privacy draft discloses Calendar data use.

If Calendar is in the beta, criterion 6 changes, and C2b has to probe Slack only, not Calendar.

**The question for xian:** does the design-partner invitation now name Google Calendar alongside GitHub? Or is Calendar connectable but unadvertised (in which case why is the verification before 10-30)?

I've held Web's C2b turn until he answers; the rest of the #1386 run goes ahead. I'll amend #1386's body and criterion 6 to whatever he says.

Verified how: `gh issue view 1386` (body, "What changed" and criterion 6); CXO's 10-07 refresh doc (C2b row); today's admissions and the #2087 thread. A source and record read; no new ruling.
