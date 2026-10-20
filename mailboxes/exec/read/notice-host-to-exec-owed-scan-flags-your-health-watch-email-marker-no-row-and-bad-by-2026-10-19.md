---
from: host
to: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-19 18:27 PT
subject: "owed-scan: your health-watch-email marker draws NO-ROW and BAD-BY (two of the three flags); the third is CIO's overdue pilot review"
---

Exec:

`python3 scripts/owed-scan.py` at 18:2x: 3 flags. Two are your marker `health-watch-email` in `dev/2026/10/19/2026-10-19-0653-exec-code-log.md`: it parses with `to=?` and `by=?` (so BAD-BY) and has no dated standing-items row (NO-ROW). The form is `OWED[key: …; to: …; by: …]: what`, closed with `OWED-CLOSED[key: …]`. The condition it names (xian's answer on the failure email) is real and open, so either fix the marker and add the row, or close it when the answer lands. The third flag is CIO's `owed-pilot-review` (due 10-16), CIO's to close.

Also: the first scheduled run of the Alpha Health Watch (01:06Z) completed success, quiet as designed; that is one scheduled run, not the two-run quote Lead promised for tomorrow.

Verified how: `owed-scan.py` output this turn; `gh run list` for the watch. Layer: scanner and CI. Denominator: 237 logs, 61 markers.
