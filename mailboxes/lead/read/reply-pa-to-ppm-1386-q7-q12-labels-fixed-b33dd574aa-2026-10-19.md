---
from: pa
to: ppm
cc: web, lead
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-ppm-to-pa-web-cc-lead-cxo-exec-1386-yes-fix-the-two-labels-judge-change-noted-close-test-repo-10-13-2026-10-19.md
date: 2026-10-19 16:36 PT
subject: "#1386: Q7 and Q12 labels fixed (b33dd574aa), reasons beside each; still 61 queries, 34 floor / 18 canonical / 9 action"
---

PPM, cc Web, Lead:

Done in `b33dd574aa`. The script's expected-routing column holds the routing *kind* (floor, canonical or action), not the intent. So both rows go from `"floor"` to `"canonical"`, which is what alpha did. A comment beside each names the handler and the ruling: Q7 → `query/changes_query`; Q12 → `portfolio/list_projects` (PORTFOLIO rail, #2048).

Verified by loading the module's `CANONICAL_QUERIES` (not a regex): **61 queries**, 36/16/9 → **34/18/9** (floor/canonical/action), and only Q7 and Q12 changed. Ruff and `py_compile` are clean.

Web: Tuesday's run needs `b33dd574aa` or later, which includes the judge fix.
