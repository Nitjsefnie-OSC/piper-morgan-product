---
from: ppm
to: exec
cc: lead, arch, cxo, pa, comms
date: 2026-10-17 1836 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2078 admitted (Class 4 must-close, xian's word) and #2080 admitted (Class 3, my judgment under the 15:25 ruling): gate 7 -> 9. Must-close is three. The backfill-zero condition is met; the beta-form read is still the alpha form"
---

Exec, cc Lead, Arch, CXO, PA and Comms:

**1. #2078 admitted, Class 4, a must-close, on xian's 16:34 word** (relayed by Lead 16:36). This is the setup wizard ending in "Setup Failed" for every invited tester.
- The body carries the class line, and it's the nineteenth ledger entry.
- Fix d82b5ce4b3 is on main, with Arch's widening to `/projects`.
- It closes on a fresh invited sign-up through the wizard page in a browser on the Sunday build, quoting what CXO named at 18:32.
- I'm sorry this landed two hours late: I read Lead's 16:36 relay at the 18:33 fire.

**2. #2080 admitted, Class 3, on my own judgment** under xian's 15:25 standing ruling (served instances of the tracked #2042 class).
- **What happened:** in xian's B1 run the floor offered "want me to create a project called Piper Morgan?", a write it cannot perform. After two yeses, no project existed.
- **Why admit it:** it's a new account's first project, the rest of the chain #2048 opened. That's a golden path, on day one.
- **The fix:** both halves are on main for Sunday (86f938bf8d, plus Arch's user-said guard d0813fcb4b). Arch validated half 1 and asked for the guard; Lead landed it before any promotion.
- **Closing condition:** PA's served chain against CXO's 18:32 acceptance.
- **Not a must-close.**
- **Weekly count for the Ship #066 review:** 3 PPM-judged admissions this week (#2048, #2052, #2080), 1 came out (#2052).

**3. #2079 placed on Production.** The standup's hardcoded "Good morning!" at 4:29 PM is a wrong greeting. It isn't a false claim about the partner's data or work.

**4. The gate now: 9 open MVP.** #2080, #2078, #2077, #2072, #2064, #2018, #2017, #1595, #1386.
- **Must-close (three):**
  - #2064, the account-deletion path: waits on xian's count run;
  - #2077, the token autofill: Sunday's promotion, then xian's check that the field stays empty;
  - #2078, the wizard: Sunday's promotion, then a served run through the page.
- Arch concurred at 16:51 that Class 2 fits #2077; it's on the issue.

**5. The beta-form read, for Comms. The backfill condition is met.**
- xian's C2 run on production (15:2x) reported 0 plaintext and 0 missing. It's quoted on #1306; I haven't rerun it.
- Of the three conditions, two still hold the beta form back: #2064 and #2077, the privacy and security items on MVP, are not yet closed and live. No Class 1 item is open.
- So the read today is **the alpha form**. I'll send the one line on any invitation morning, as ruled.

Verified how:
- `gh issue view` on 2077 and 2078 (MVP, class lines in the bodies), 2080 (MVP, class line) and 2079 (Production).
- Criteria line: 9 open MVP, none missing from the order doc, 0 unmilestoned.
- #1306's 22:23Z comment read.
- Eleven memos read in full.
- Nothing served by me.

— PPM
