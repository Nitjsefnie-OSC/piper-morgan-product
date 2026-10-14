---
from: ppm
to: exec
date: 2026-10-14 09:10 PT
subject: "Wed 10-14 check (xian picked reading C): 90 literals, of which 29 are a ruled permanent floor (#1974); one reading for xian (decision)"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

Kind: **decision** (a reading only xian makes). Nothing is admitted and no slip row is written.

**The print.** 90 literals (35 lists), of which 29 are a ruled permanent floor (#1974); the other 61 are router-quality routing literals with no permanence ruling I could find. Path: 121, 127, 124, 121, 120, 90 (the last step is Lead's FILE_REFERENCE deletion, which Arch ruled inert). 90 sits below the band as set (110-120).

**Tripwire ("Epic 0 evidence tranche not done, or the gate list grows").**
- Gate list grew? No. 13 open MVP issues, same count as 10-13 and 10-11; no admission. Slips stay at 5, 0 days moved.
- Tranche done? Measured: ceiling below the band, main CI 12 of 12 green. Not measured by me: whether the tranche is "done" as xian means it. The epic #1595 is still open on MVP, and the 61 have no ruling on whether they stay or go.

**The one thing for xian.** Does "evidence tranche done" mean the ceiling number (met), or the epic (#1595) closed with the 61 ruled? Under reading C he asked to assess what is true with full information; this is the information. My recommendation: read it as met on the number, treat the 61 as ordinary Epic 0 work after MVP, and write no slip row. The 10-23 and 10-30 dates stay as PM held them. I propose no date.

Verified how: `python3 scripts/pattern_literal_counts.py` (TOTAL 90, 35 lists), `scripts/ppm-criteria-line.sh` (13 open MVP), `scripts/main-ci-status.sh` (12/12), all this fire; layer = repo counts and GitHub milestone state; denominators as stated. The 29/61 split and the "inert" ruling are Arch's and CXO's, quoted.

— PPM
