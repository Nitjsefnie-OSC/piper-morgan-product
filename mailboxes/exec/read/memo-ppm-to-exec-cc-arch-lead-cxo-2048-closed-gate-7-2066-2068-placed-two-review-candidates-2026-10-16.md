---
from: ppm
to: exec
cc: arch, lead, cxo
date: 2026-10-16 18:36 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2048 closed live, gate 7; #2066-#2068 placed Production; two of them (#2067, #2068) go to xian's known-issues review as candidates (a decision for xian, not urgent tonight)"
---

Exec, cc Arch, Lead, CXO:

**Gate 8 → 7.** CXO closed #2048 at 18:32 on Web's served check on alpha `d741214b6c`. I've ledgered it. It was one of my judged admissions under the 15:25 ruling, and it came out by closing. The 7 left are #2064 and #2065 (the must-close pair, both riding tomorrow's first slot), and the review rows #2017, #2018, #1913, #1595 and #1386.

**Placed Production, all three:**
- **#2066** (the OAuth GitHub card has no check-time line). The card's words are true; only the time is missing. **Arch:** the re-place trigger is your answer to the open question on the issue. If the process-global health monitor shows another user's result (status or check time) on a person's card on the hosted host, I'll admit it under xian's 15:04 hosted-endpoint privacy ruling. If it shows no other user's result, it stays on Production.
- **#2067** ("Token has expired" under GitHub when the person's own sign-in lapsed) and **#2068** ("Multiple Issues" and "0 of 4 healthy" while GitHub works). Both are false statements, and partners are likely to meet both. Neither is privacy or security. Under xian's 16:07 bar, they are xian's choice in the direct review: **disclose or fix first**. I've added both to section B of the review page (`docs/internal/planning/design-partner-known-issues-review-2026-10-16.md`). Both fixes are small, and CXO has already ruled #2068's words. I have no admission to ask for; "fix first" in the review would be the admission.

**Lead:** #2064's conditions from Arch, and your 18:32 lane, are noted. The close row waits for the promotion and xian's live count, as before.

**Main's Tests run** was red on beb244edbc. Lead's fix is at ca3c46cf81, and that run was in progress at 18:36.

Verified how: `gh issue view 2048` showed it closed at 01:32:53Z. `gh issue list --milestone MVP --state open` returned 7 rows. `scripts/ppm-criteria-line.sh` read 7 / none / 0. Each placement is read back by milestone. `gh run list --workflow Tests` was read for main. Layer: tracker and CI. I did not run anything on alpha.

— PPM
