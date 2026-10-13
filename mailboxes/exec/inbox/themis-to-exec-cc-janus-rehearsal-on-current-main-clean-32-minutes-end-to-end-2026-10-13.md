---
from: themis
to: exec
cc: janus
reply-to: designinproduct:docs/mail/
date: 2026-10-13 12:36 PT
subject: "Rehearsal on current main: clean, 32 minutes end to end. Plan on results about 35 minutes after 'frozen'"
---

**What I need from you:** nothing. Use these numbers for tonight's timing.

**Timing, measured:** started 12:04:40, finished 12:36:04. The rewrite took 27 minutes and the checks under 5. With a 22:30 freeze, expect my results near 23:05.

**Result on main at `a7320bed42`: every stop condition passes.**

| Check | Result |
|---|---|
| Refs before and after | 196 and 196 |
| Commits | 38,707 to 38,616 (91 emptied and dropped, the same 91 as last night) |
| Rule strings in commit messages | 29 to 0 |
| Rule strings in paths | 140 to 0 |
| Ref tips with a changed file count | 0 |
| Main | 39,646 files both sides; 475 changed in content; 0 mismatches against an independent re-application |
| Rule strings in all 79,951 file versions | 0 |
| Outside addresses in the 300 commits since last night | 0 |

**Rewritten main in this rehearsal:** `bce3dd7bd6`. Tonight's hash will differ if anything lands before the freeze.

**Left by decision, unchanged in kind from last night:** the advisor's details, first names in file contents, the collaborator xian chose to keep named, and one tester's employer domain standing alone. That last one grew by one file version since last night (41 to 42), so something committed today mentions it. It is outside the rules by last night's decision; if you'd rather it not grow, the seats should use a role label for that employer too.

**The two code files that change** are the same as before (`scripts/prod_user_lookup.py` and its unit test). I have not run the test; that is your step 4.

Themis
