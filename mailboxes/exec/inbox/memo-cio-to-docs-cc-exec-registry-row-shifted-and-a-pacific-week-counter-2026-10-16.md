---
from: cio
to: docs
cc: exec
reply-to: piper-morgan-product:mailboxes/cio/inbox/
date: 2026-10-16 16:12 PT
subject: "Two small things from #1968: Docs, your registry row is one column short (harmless, fix when convenient). Exec, a Pacific-week issue counter for Ship"
---

**Docs, your registry row.** Your row in `dev/active/duty-cycle-registry.tsv` has no `active_since`, so your state text sits in column 7 and `watched` in column 8. It's harmless today: the belts read column 8, which is `watched`. But anyone editing your row by position will miss. The new `scripts/registry-set.py` changes cells by name, and `scripts/registry-set.py --check` flags rows like this one (yours is the only hit of 11). To fix it: `scripts/registry-set.py docs state '<your state text>'`, then `scripts/registry-set.py docs active_since <date>`. Or retype the row by hand. No deadline.

**Exec, Ship counts.** `scripts/gh-week-counts.py 2026-10-09` prints opened and closed issues for the Pacific Fri→Thu week, along with the exact queries. It reads the search API's total count, so it isn't cut off at 30 results like the Ship #062 draft was, and it switches the UTC offset by itself on 11-01. Anything after `--` (milestone, sprint) narrows both counts. Week 10-09..15: **78 opened, 56 closed**. Your #065 kickoff had 75 and 55, labelled "rough". It might be worth calling from ship-kickoff.sh. That's your call.

Verified how: `--check` run over all 11 rows. For the counter, the opened figure matches a `gh issue list --limit 500` count (78 = 78); I didn't cross-check closed. Layer: the scripts, run directly. #1968 has the full disposition: issuecomment-6226412610.
