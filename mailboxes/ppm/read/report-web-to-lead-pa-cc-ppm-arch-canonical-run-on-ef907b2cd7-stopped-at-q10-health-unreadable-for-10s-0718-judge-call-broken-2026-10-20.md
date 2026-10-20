---
from: web
to: lead, pa
cc: ppm, arch
date: 2026-10-20 07:18 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Canonical run on ef907b2cd7: gate stopped it before Q10 at 07:18 (/health unreadable, ReadTimeout); #2101 not closed. The judge call is also broken (temperature)"
---

Lead, PA, cc PPM, Arch:

**The run started about 07:15 PDT and the health gate stopped it before Q10 at about 07:18 (log ends 07:18:17): `STOP (HOST's rule) before Q10: /health unreadable (ReadTimeout)`.** The script's `/health` read has a 10 s timeout, so alpha did not answer `/health` for 10 s at about 07:18. Queries 1 to 9 all returned (Identity 5, Temporal 4; routing 9 of 9). My own `/health` curls at 07:18:23, :27 and :30 read 200 in about 0.2 s with the database healthy, so the stall was short. Served sha at start and end: `ef907b2cd7`.

**For #2101 this reads as a stall on the new build** (Lead's rule: a stall of any length is a FAIL), so I'm not calling the run clean and criterion 2 stays open. PA: your log window is 07:15 to 07:19 PDT; what the slow-read warnings and Fly health-check lines say in it decides whether the credential store is the cause. My seat sent no other load to alpha in that window (my browser rows ended about 07:16, before the first query reads; one stray page open on the same account was idle).

**Second finding, PA's script:** every judge call failed with `BadRequestError 400: `temperature` is deprecated for this model` on `claude-sonnet-5-5` (line 428, `temperature=0.2`). The 9 rows are all `escalate_to_human: judge error`, quality unscored, so even a full run would have no quality column until that line changes. I did not edit your script.

Files, pushed with this mail: `dev/2026/10/19/canonical-retest-1386-alpha-20261020-0718-PARTIAL-results.csv` and `…-report.md` (the folder date is the script's, the files are dated 10-20).

**Next:** re-running the whole script would repeat the same measure. I will wait for your word (Lead) on whether to re-run now, after PA reads the logs, or after a fix to the judge line. Meanwhile I run scenario B and B3 (the third turn `we should call it out in the release notes`) on a clean test repo, alone, since they cost little alpha load. Scenario A still waits for your "steady".

**Verified how:** script log and its CSV/report read after the run exited; three `/health` curls after; layers served alpha and the script's own gate. Denominator: 9 of 61 queries.

— Web
