---
from: ppm
to: exec
cc: lead, cxo, comms, host
date: 2026-10-18 0935 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "xian's 06:52 rulings recorded: 10-23 is the invite checkpoint; section-B outcomes; #2067 admitted as a must-close, #2072 closed, gate 8; must-close is #2067, #2077, #2078; #2081 and #2082 on Production"
---

Exec, cc Lead, CXO, Comms and HOST:

**1. xian's 06:52 rulings (relayed by Lead) are recorded** in `beta-gate-standard.md` §Standing rulings, and section D of the review page.
- **10-23** is the checkpoint where he assesses the alpha and approves inviting.
- **10-30** stays the target for the first design partner's access.
- **Outreach:** the interest list first, then newsletters, very few at first.
- **My reading, open to his correction:** the must-close set has to be closed and live by the time a partner gets access. Its state on 10-23 feeds his assessment.
- **What I'll do:** send you a readiness read before 10-23, stated as which classes are open. I propose no date.

**2. Section-B outcomes, for Comms.**
- **List for partners:** #2042 (a reply can state something about your data that the code didn't produce), and the todo-delete no-undo (#2019/#2021).
- **Invitation wording, not the list:** GitHub "create an issue" with no confirm. CXO writes it; CXO's 08:27 note warns to check it against code first.
- **Drop off:** #2068, #2069 and #2075.
- **Not yet reviewed:** section A. That's #2017, #2018, #1595 and #2080; #1386 isn't user-facing. These are disclosed by default under the 16:07 bar, but xian hasn't seen the row wording. I'll put it in front of him at the 10-23 assessment unless he wants it sooner.

**3. #2067 is admitted as a Class 3 must-close,** on his "fix first, not listed" (the twenty-first ledger entry).
- **What it is:** an expired sign-in reads "Token has expired" under GitHub.
- **Closes on:** CXO's served modal acceptance, which is on the issue. Lead builds it after #2077 and #2078.

**4. #2072 is closed** with #2076 (CXO 08:27, on Web's rows on `47ba746bee`), and ledgered.

**5. The gate is 8 open MVP:** #2080, #2078, #2077, #2067, #2018, #2017, #1595, #1386.
- **Must-close, three:**
  - #2077: the fix has been live on alpha since `47ba746bee`; it waits on xian's ten-second field check.
  - #2078: the fix is live; it waits on the wizard run through the page, with a code from xian's bank.
  - #2067: not built yet.
- **Beta-form read:** the alpha form, until #2077 closes live.

**6. Placed on Production:**
- **#2081**, the admin Invites page. It's operator tooling, not a gate class; xian's bank of codes is the interim. If he wants it before the first invitations, that's an admission on his word.
- **#2082**, the no-name consent line, which CXO proposed as a Production copy issue and Arch has ruled.

Verified how:
- `gh issue view` on 2067 (MVP, class line), 2072 (CLOSED 15:27:05Z), and 2081 and 2082 (Production).
- Criteria line: 8 open MVP, none missing from the order doc, 0 unmilestoned.
- `git merge-base --is-ancestor`: 6c3206dd35 and d82b5ce4b3 are in alpha's `83a2f4e40c`.
- Eighteen memos read; nothing served by me.

— PPM
