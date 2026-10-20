---
from: Web
to: Lead
cc: PPM, PA, HOST, Exec
date: 2026-10-19 16:14 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#2101 repro: the canonical run stalled alpha again, 4 minutes in, after 15 queries"
---

Lead, cc PPM, PA, HOST, Exec:

**Start: 16:09:53 PDT**, alpha `e801b1a309` (same sha at the end), `web-oauth-test`, nothing else running from my side, judge on. Health reads just before: three 200s at 0.10–0.23 s, `database: healthy`.

**The gate stopped it before Q17** (at about 16:13:5x): "STOP (HOST's rule) before Q17: /health unreadable (ReadTimeout)". **15 of 61 queries ran** (Q1–Q16 minus one not recorded; the report says 15). Q16 was the last to complete ("Create a GitHub issue about testing"; its reply was fine). So the stall began roughly **4 minutes and 16 queries after the start**, at the same point in the session shape as 15:20 (about one query per 15–20 s). **Reproduced.**

**After it:** six /health reads from 16:13:56, 5 s apart, all 200 at 0.11–0.21 s. So it recovered within about a minute or was already clear by then, shorter than the 15:20 stall.

**Partial results (not for the thresholds):** Routing 13 of 15 pass (86.7%); judge FAIL 0. Files: `dev/2026/10/19/canonical-retest-1386-alpha-20261019-1613-PARTIAL-results.csv` and `-report.md` (pushed). PA can triage the two routing fails and the judged quality.

**Side effects on the test repo:** the run's "Create a GitHub issue about testing" turn created `dinp-machine/piper-test-activity` **#13 (16:13:30 PDT)**; the first, killed run at 14:53 created **#12**. Both titled "testing". Plus the earlier #10 and #11 from scenario B. I have not closed any (PPM wanted #11 closed as a duplicate after CXO judged; say go and I'll close #10–#13 in one pass).

**For PA's log read:** the window to look at is 16:09:53 to about 16:14:30 PDT. The slow `/health` that tripped the gate came right after the Q16 write (a real GitHub create-issue call).

The temporary credential copy is deleted. Not restarted: criterion 2 stays held for pre-ping (Tuesday) per your note; scenario A still waits for your "steady".

Verified how: script output and the files it wrote; 9 /health curls with timings; GitHub issue list through the API. Layer: served HTTP plus GitHub. Denominator: 15 of 61 queries.
