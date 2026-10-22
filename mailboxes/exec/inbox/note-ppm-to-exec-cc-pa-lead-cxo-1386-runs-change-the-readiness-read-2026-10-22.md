---
from: ppm
to: exec
cc: pa, lead, cxo
date: 2026-10-22 1019 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#1386 runs change this morning's readiness read (information for xian's 10-23 decision, plus an admission only he can make): the gate's own test missed both bars; the invitation names Anthropic only; I propose #1524 and #2128 as Class 3"
---

Exec (for xian's 10-23 read), cc PA, Lead, CXO:

This corrects this morning's readiness read. **I wrote that the best case tonight was one must-close open (#2085), "plus #1386 waiting on the run's read and sign-off". That understated #1386.** PA's run (10:12 end mail) missed both of criterion 2's bars, so #1386 is a real item to 10-30, not a sign-off. The detail and my ruling are on #1386 (comment 6346811165).

## 1. What the run showed (PA's figures, which I recounted from the CSV)

| | Run 1, Anthropic, seeded | Bar |
|---|---|---|
| Routing | 53/61, 86.9% | ≥ 90%: miss |
| Expected-pass | 24/42, 57.1% | ≥ 75%: miss |

- **Of the 18 expected-pass rows not judged PASS, 16 are MARGINAL and 2 FAIL.** Ten of the 16 MARGINALs carry the judge's own mode "Correct": right data, marked down on how it was said.
- **Hard failures fell:** 7 FAIL on 10-20's run, 3 today (all 61 rows).
- **Unseeded rows route at 91.7%;** the routing misses come from the seeded rows.
- **The good news: the calendar reads work on a served account for the first time.** Q8, Q34, Q35 and Q61 list the seeded events. That bears on #2092; its close is still Web's row and CXO's read.

## 2. My ruling (criterion 2's acceptance criteria are mine)

The bars don't move. The third box ("each waived with rationale, or filed, fixed and re-run") is what's left:
- **Routing:** relabels only where the routing design says so. PA proposes each row and Lead signs it (10-20 rule).
- **MARGINAL rows:** waived only with a reason from **CXO**, who reads the served reply as an experience. Every report shows the raw 57.1% beside any waived figure.
- **Rows that state something false about the user's data can't be waived.**

**For xian, the 10-30 question on #1386 is: will CXO's reads waive most of the MARGINALs, or do the answers have to improve and be re-run?** Routing looks closable by relabels. The honesty rows below need fixes either way.

## 3. A proposal only xian can make: admit two issues as Class 3

The run's seed made two false answers visible on GitHub, the beta's shipped surface:
- **#1524** (served at Q25): "You don't have any open milestones right now", when the repo has "Beta launch" due 10-29. Lead's 10-22 source read traces it to a router built with no user context; an unresolved repo returns `[]`, rendered as "none".
- **#2128** (filed now, at Q51 and Q41): "Issues/PRs Closed: 0" and "Light week" in a week with a merged PR and two closed issues. The same run's Q17 read "19 issues closed" from the same repo. The cause is unverified.

This is the shape of #2092, a false empty about the user's own data, which xian admitted as Class 3. **PPM proposes admitting both to MVP as Class 3 must-closes.** That would make the gate 10 open (7 must-close). Both stay on Production until xian rules. **Lead:** a size read on each would help xian decide. If #2128 shares #1524's cause, it may be one fix.

## 4. The invitation's provider line: Anthropic only (decided by the 10-20 bar)

The OpenAI run failed on two counts:
- a missing-key refusal at Q21, because the classifier sent an OpenAI-only account's turn to Anthropic (**#2127**, placed Production);
- expected-pass 42.9 points below the Anthropic run on matched rows.

It was one run and there's no rerun, because Q21 is a product defect. The checklist row is updated. OpenAI can be named after #2127 closes and a new run passes.

## 5. Asks

- **CXO:** read the 16 MARGINAL rows (and Q49) in `dev/2026/10/19/canonical-retest-1386-alpha-20261022-1004-results.csv`, and say for each whether it's acceptable for a partner. That's the waiver reason the criterion needs.
- **PA:**
  - the triage table for the 8 routing misses, as on 10-20;
  - a disposition for Q17 (file it, or name an existing issue);
  - check Q7 and Q29 ("No activity detected since yesterday") against the repo's events for that day. If they're false, they join #2128.
- **Lead:**
  - sign or reject PA's relabels;
  - the size read on #1524 and #2128;
  - your design line on Q49 (`/standup` opens the interview).

I still owe tonight's update after Web's calendar rows. It will fold this in, so xian reads one state.

Verified how:
- Read PA's 10:12 end mail in full.
- Recounted the expected-pass set from the Run 1 CSV (42 rows, `known_pathological` False: 24 PASS, 16 MARGINAL, 2 FAIL) and the verdict counts on 10-20's CSV.
- Read the rationale for Q17, Q37 and Q49, and #1524's 10-22 served-instance comment.
- `gh issue create` for #2128.
- `gh issue view` on #2127 and #2128: both on Production.

I ran no turn and read no handler source.

-- PPM
