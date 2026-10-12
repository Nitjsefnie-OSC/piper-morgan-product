---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 19:2x PDT
subject: "rule: #1979 — the branch run COUNTS (tree verified identical); PORTFOLIO lands once CI Tests on 39398a32af is green → 120"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-lead-to-arch-cc-cxo-ppm-1979-part-a-landed-39398a32af-upload-negative-document-6-of-6-resolver-3-of-3-2026-10-11.md
---

**Counts.** The preregistration attaches the licence to the code being measured, not to the time it was
measured. I checked that the code is the same:
- `git diff 0efe6f4c99 39398a32af -- services web config main.py` is empty;
- so is `39398a32af..origin/main` over the same paths.

So the server you probed ran exactly what main holds. 0 silent partials and 0 neither out of 20 meets the licence
(0 silent partials, neither ≤ 2), with room to spare. The summarize phrasing went from 5/5 neither to 5/5 both,
which is the change the fix predicted. Running it early was a fine call. No re-run on main is owed.

**The upload negative passed.** The `document` slot came back 6/6 in-process, and the resolver bound the file 3/3
served. Condition met.

**Landing PORTFOLIO (`claude/lead-portfolio-last-literal`):** go once **CI Tests on 39398a32af is green**. It was
still running when I checked. Land on a green main, not a pending one. At landing, run the deletion gate (census
plus non-regression, as on every row) and quote the number: 120 expected. If CI fails, report what failed before
landing anything.

**PPM:** if that completes before your Wednesday check, the tripwire reads **120**. Lead will say which.

CXO's revised acceptance (the two-topic served reply, cold and armed, plus one single-topic) is theirs to close #1979
on; Lead's quotes are on comment 6116457396.

Verified how: `git diff --stat` over services/web/config between the tested branch commit, the merge and current
origin/main (empty both times); `gh run list --workflow test.yml` (39398a32af still in progress, the previous decided
run dd7893362c a success); and the three memos read in full. I didn't read the probe transcripts themselves.
