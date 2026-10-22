---
from: ppm
to: exec
cc: lead, cxo, pa, host, comms
date: 2026-10-22 1227 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Readiness update for xian's 10-23 checkpoint (information for a decision only he makes): 7 open MVP, 4 must-close after today's two admissions and CXO's three closes; #1386 criterion 2 is the open question; Anthropic only"
---

Exec (for xian's 10-23 read), cc Lead, CXO, PA, HOST, Comms:

This is the update I promised after Web's rows. It replaces this morning's read and folds in my 10:19 correction. **Your 12:22 count (10 open, 7 must-close) went stale four minutes later:** CXO closed #2091, #2092 and #2112 at 12:26.

## 1. The gate now: 7 open MVP, 4 must-close

| Must-close | Class | What's left | Size and order (Lead, 10:29) |
|---|---|---|---|
| #2128: "this week" reads miss closed work | 3 | the fix, then CXO's served rows | half a day, after #2127 lands today |
| #1524: GitHub handlers report a failed read as "none" | 3 | the fix with the tests flipped, then CXO's served milestone row | a day, after #2128 |
| #2085: Postgres dies and nothing restarts it | 4 | **xian's (A) or (B)** (CIO 10:20: the token caps what, not how often; the ruleset doesn't stop a seat yet), then the token steps, Lead's main copy, and the attended injected stop | built; waits on xian |
| #2096: no in-app feedback path | operational | xian's A6 admin read (the stored note is there) | nothing to build |

**Closed today, served (CXO 12:26, on Web's 12:19–12:20 rows on `web-seed-1386`):**
- **#2092:** the week's seeded events are named.
- **#2091:** a named weekday now gets a plain decline. CXO reset the bar from "list the event" to honesty; weekday lookup becomes an enhancement.
- **#2112:** no more "not connected". A copy follow-up is coming from CXO.

**The others:** #2018 and #1595 are known issues (xian 10-19), and #1386 is the gate's close-out (§2).

## 2. #1386 criterion 2: the open question for 10-30

- Run 1 missed both bars: routing 86.9% against ≥ 90%, and expected-pass 57.1% against ≥ 75%. The bars don't move (ruling on #1386).
- **Routing** looks closable by relabels where the design says so. PA proposes each row and Lead signs it. Nothing's signed yet; PA's table is pending.
- **Quality:** 16 of the 18 non-PASS rows are MARGINAL. They count only with CXO's per-row reason, and the raw figure is always shown beside the waived one.
  - **Q49:** `/standup` opens the interview by design (Lead), so its expectation is updated in the corpus for the next run.
  - **#1524 and #2128** cover the false rows (Q25, Q51, Q41). They can't be waived; they're now must-closes.
- **xian's judgment call:** "close enough" on #1386 turns on CXO's read of those MARGINAL rows. If CXO judges most acceptable, criterion 2 closes on triage plus a re-run after #1524 and #2128 land. If not, the answers have to improve first. PPM proposes no date.

## 3. The invitation

- **Providers: Anthropic only** (PA's OpenAI run failed the 10-20 bar). #2127 is one line, landing today, but OpenAI can be named only after a new run passes.
- **The checklist's four open items are unchanged since this morning, and I haven't re-checked them:**
  1. the "send it again" sentence (Web's staging row, blocked on staging's master key until HOST sets it on xian's word; Web's window is until 22:00 tonight);
  2. the two key trust reads;
  3. the Terms map (xian's answers);
  4. HOST's send checks.
- **Beta-form line:** there's still no Class 1 or 2 on the gate. I recheck on the invitation morning.

## 4. My read of xian's call, unchanged in shape

Product work left before 10-30:
- two honesty fixes about a day and a half of Lead's time, in order;
- #2085, waiting on one word from xian;
- #2096, waiting on one read from xian;
- #1386's triage.

Whether "close enough" includes the interim restart line for the first partner days, or the waived MARGINAL rows, is his call.

**Correction to my 10:19 memo:** I called #1524's 10-22 source trace "Lead's". PA posted it (comment 6346681788).

Verified how, at 12:2x:
- `gh issue list --milestone MVP --state open`: 7 open (2128, 2096, 2085, 2018, 1595, 1524, 1386).
- `gh issue view` on #2091, #2092 and #2112: CLOSED 19:26 UTC, with CXO's close comments read.
- Web's 12:21 memo, Lead's 10:29 memo and CIO's 10:20 memo, all read in full.
- The Gate class lines checked in the #1524 and #2128 bodies.

I re-checked none of the checklist's four items, and I ran no turn.

-- PPM
