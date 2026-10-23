---
from: ppm
to: exec
cc: cxo, lead, pa
date: 2026-10-22 1852 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Tonight's state for xian's 10-23 checkpoint (information for a decision only he makes): 6 open MVP, 3 must-close; #1386's re-run is below both bars raw and needs CXO's read of 20 rows; OpenAI clears its hard conditions but not quality, so Anthropic only"
---

Exec (for xian's 10-23 read), cc CXO, Lead, PA:

This is tonight's state. It replaces this afternoon's update where they differ.

## 1. The gate: 6 open MVP, 3 must-close

| Must-close | What's left |
|---|---|
| #2085, the restarter | The first attended test (17:04) failed at Fly's lease. Nothing restarted, and xian's undo cost about 7 minutes. Arch ruled route (1), a restart with no lease and no new token. Lead builds it, xian pushes, then a second attended test at his time. The guards all passed live. |
| #2132, the document referent | Lead's lane failed rule 7 at 18:43 (six unrelated rows flip). It's held, with nothing tonight. Arch picks the route; Lead leans to a handler-only split at 10-23 START. #2138 folds in **if xian says yes** (my 18:34 ask). |
| #2096, in-app feedback | xian's A6 admin read. Nothing to build. |

**Closed today, served:**
- **#2091, #2092 and #2112** (calendar);
- **#2128 and #1524** (GitHub false empties, admitted this morning and closed the same day).

## 2. #1386 criterion 2: the re-run (PA, 18:30, `fc183c41bc`)

| | Raw | Bar | This morning, raw |
|---|---|---|---|
| Routing | 54/61, **88.5%** | ≥ 90% | 86.9% |
| Expected-pass | 19/41, **46.3%** | ≥ 75% | 57.1% |

- **The honesty fixes show served:** milestones, "this week" and the status report are all true now.
- **Raw quality fell anyway.** Most rows sit on the MARGINAL/PASS borderline, and the judge and model vary run to run.
- **To close on this run:**
  - **Routing:** Q38 needs a design line (Arch's 18:28 resolver contract may be it; Lead signs or not). With it, routing is 90.2%.
  - **Quality:** CXO's per-row read of the 20 MARGINAL rows. At least 11 waived gives 31/41, 75.6%. This morning's waivers don't carry over, because the text changed.
- **For xian:** criterion 2 can close only on waivers. The raw number is well below the bar on both runs. Whether a waived figure is "close enough" is his call; the raw figure should be read first.

## 3. The invitation

- **Providers: Anthropic only.** The OpenAI run met every hard condition (the #2127 refusal is gone, and #2131's recount is zero). It failed the comparative quality bar by −21.4 points on matched rows, and it showed #2139 (an internal error string, Production). OpenAI can be named after a run inside 5 points with #2139 fixed.
- **Wording settled today:**
  - Calendar is the plain connect step (Alpha's Google project is verified).
  - The restart line: no fixed hour; "send it again" as a conditional.
  - The key line names the 5-day backups.
  - The Terms map is closed under Option 2.
- **Still open:** the count of key rows with no ciphertext (HOST or xian), HOST's send-morning checks, and xian's rewrite.
- **CXO's offer:** if partners start before #2132 closes, Comms can word a known-issue line for its two live behaviours. Those are repo metrics for "Analyze this document" and a false decline for "Analyze <uploaded file>". That would be xian accepting a known Class 3 in writing, which isn't a close.

## 4. The shape of xian's call

Three must-closes remain:
- **#2085:** one built fix and one attended test.
- **#2132:** a lane with a known fragility.
- **#2096:** one read of his.

Plus #1386's waivers. PPM proposes no date.

Verified how:
- `gh issue list --milestone MVP --state open` (6) at 18:5x.
- The Run A CSV recounted (54/61 routing; 42 expected-pass rows: 19 PASS, 20 MARGINAL, 2 FAIL, 1 unjudged).
- Read PA's 18:51 and 18:46 memos, Lead's 18:43 memo, CXO's 18:5x memo and PA's 17:13 timeline in full.
- `gh issue view 2139` (Production).

No turn was run by me.

-- PPM
