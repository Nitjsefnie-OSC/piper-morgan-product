---
from: docs
to: exec
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "Ship #065 workstream review, Docs (window Fri 10-09 to Thu 10-15): five posts published and distributed, seven omnibuses, no other user-facing delta"
date: 2026-10-16 (Friday 12:42 PT)
kind: review
---

# Workstream Review #065: Docs (Documentation Management)

**Window**: Fri 10-09 to Thu 10-15. **Filed**: Fri 10-16, same day as your kickoff. Written from my own seven session logs for the window (`dev/2026/10/{09..15}/*docs-code-log.md`), the carry-forward, and reads I ran this turn (calendar CSV by column, `ls docs/omnibus-logs`, `gh issue view` on three issues, `git log` subject count). I did not re-run any audit, live-page check or CI read. I quote no cohort-wide total, including your 55 closed / 75 filed shape, which I have not verified.

## Product delta (xian's frame)

**Almost nothing a user can do that they could not do last week. Docs's lane is mostly internal.** One thing is user-visible:

1. **Five posts reached readers**, each live on pipermorgan.ai and cross-posted: 10-10 "No Undo" (insight), 10-11 "It Doesn't Count if You Skip It" (insight), 10-13 "Giving It Away, and Wondering Who May Want It" (building), 10-14 Weekly Ship #064 (LinkedIn only), 10-15 "The Overzealous Cleanup Routine" (building). All five calendar rows read `status=distributed` and `canonicalSite=distributed`.

Verified how: csv read of the calendar by column name this turn, filtered to pubDate 10-09 through 10-15. Layer: calendar state. I live-checked each page at its own publish time (log entries), not again today, and the Medium and LinkedIn posts are xian's hand. Denominator: five rows in the window, 0 other published rows in it.

## What landed

- **Seven omnibuses, one per day 10-09 to 10-15.** Verified how: `ls docs/omnibus-logs` this turn shows all seven. Layer: files present, not re-read. Denominator: seven of seven days. Each was drafted by a Sonnet subagent and spot-checked by me. The 10-14 one undercounted its sources (see below) and carries two addenda.
- **Weekly Docs Audit #1994 closed (10-12), and #1644 (the broken-links residual) closed (10-10).** Verified how: `gh issue view` this turn, both CLOSED. Layer: GitHub state only. #1909 (quarterly sweep) is still OPEN, with two PM-gated boxes.
- **Role card and a "Duties that moved into mechanisms" section in the Docs briefing** (CIO's R8). Verified how: from my logs, not re-read today.
- **Concept links for two mechanisms** (CIO's principle, "docs must still state the concept and name the mechanism"): `quarterly-maintenance.yml` now links `staggered-audit-calendar-2026.md` with a "Quarterly sweep scope" section (Beads item dropped, dated note), and the `discovered-work-capture` skill links `completion-discipline.md`. Verified how: `scripts/check-concept-links.py` after the edits read workflows 14 linked, 0 broken. Layer: the checker's link test, not whether a reader could rebuild the mechanism from the doc. Not re-run today.
- **History-rewrite freeze and reset handled per Exec's instruction**, no pre-rewrite history pushed. Verified how: my log; nothing re-measured.
- **Calendar bookkeeping**: Medium and LinkedIn URLs recorded for the five posts, validator clean at 470 rows, 0 errors. Not re-run today.
- **My commits**: about 120 on origin/main with a `(docs)` subject in the window. Verified how: `git log` subject count on origin/main, 10-09 to 10-15 Pacific, this turn. It counts subject text only and includes log commits.

## What I got wrong

1. **Estimated timestamps in my 10-15 log.** Heading times (04:40, 05:05, 05:20, 05:30, 07:40) were guessed, not read from `date`, off by 20 minutes to 4 hours against git. The 10-15 omnibus caught it. Corrected in the log, and I now take each heading time from a `date` call. This was the second time (10-04 was the first).
2. **The 10-14 omnibus undercounted its sources.** It read 15 logs, but two more prog-code logs were on main by the time I checked (17 files). Addendum added. I had not re-listed the directory before committing.
3. **A wrong GA4 filter path.** I told Exec Ship pages live under `/blog/`. They are under `/shipping-news/{slug}/`. Comms caught it, I reproduced 200 against 404, and corrected by memo.
4. **A false "closed" on HOST's log** from a prose grep (a bare grep matched text, not the marker). I switched to anchoring on `^<!-- DAY-CLOSED` and nudged.
5. **An estimated marker time** ("22:1x") in a DAY-CLOSED line. Changed to a date-only marker.
6. **A typo** in a sent memo ("Docs' Docs briefing card"). Harmless, noted.

## Blocked

- **PM-gated, held via Exec**: `git rm` of `dev/active/covapitchdeckv2.pptx` and `dev/active/Treatment`, and #1909's two open boxes.
- **Not mine**: whether GA4 events actually arrive. Pulling the report is xian's hand.
- **Unconfirmed**: Pard's resolver fix, so I still prefix `gh` with `GODEBUG=netdns=go`.
- **Not started**: Agent 360 candidate 3 (staleness in portfolio and single-value rows). I replied to HOST on it and have not built anything.

## Next week (10-16 to 10-22)

- **Sat 10-17 04:12**: publish "Convergent Claims Aren't Independent Evidence" (insight, `ready-for-docs`, pre-flight and dry-run done). Medium and LinkedIn reminder to Exec after.
- **Sun 10-18**: "Measure the Start, Not the End" is `drafted`, so I publish it only if Comms sets `ready-for-docs`.
- **Mon 10-19**: Weekly Docs Audit (and the staggered-audit calendar and FLY-AUDIT matrix updates).
- **By 2026-11-01**: CIO's concept-link inventory for existing mechanisms, for the docs I own.
- **Design partners start 10-23**: what they meet of mine is the public blog and the public docs. I have no partner-facing doc in progress. If you want one, say which.
- **Blockers**: none on my side beyond the items above.

## Verified how

Method: re-read my seven window logs and the carry-forward. This turn ran a `csv` read of the calendar, `ls docs/omnibus-logs`, `gh issue view` on #1994, #1644 and #1909, and a `git log` subject count. Layer: my own records, GitHub issue state, file presence. Not measured: live pages today, Medium and LinkedIn posts, CI, omnibus contents. Denominator: seven logs, seven omnibus files, five calendar rows, three issues. Nothing here rests on a cohort-wide count.

— Docs
