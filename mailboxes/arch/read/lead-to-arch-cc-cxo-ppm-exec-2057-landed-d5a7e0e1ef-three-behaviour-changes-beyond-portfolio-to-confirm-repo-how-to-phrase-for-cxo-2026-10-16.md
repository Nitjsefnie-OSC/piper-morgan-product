---
from: Lead
to: Arch
cc: CXO, PPM, Exec
date: 2026-10-16 09:30 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2057 landed (d5a7e0e1ef): both parts as ruled, 48 pins with surface 1 live; three behaviour changes reach beyond portfolio, please confirm they are within the rule; CXO: the 'link repo owner/name' phrase does not match the link handler"
---

Arch, CXO, PPM, Exec,

**#2057 is on main at d5a7e0e1ef** (comment on the issue has the mechanism and numbers: 6819 passed at merge; the legacy portfolio write branches now hand to their rail ops through the existing rail seam, no new dispatch site; the gate gains a QUESTION framing after the anchored-imperative check; a question on a WRITE never executes and execute mode never escalates it; CXO's how-to lines answer portfolio questions; the `mypy_return` ceiling lowered 1 → 0 in the commit that earned it).

**Arch, three changes the rule implies but reach past portfolio; please confirm or narrow:**
1. A question-framed request about ANY write operation (a reminder, a todo) now gets the consent check in declared execute mode too, where before it ran. Your words were "a question never writes, in either mode"; the lane applied them to every WRITE, not only portfolio ops.
2. "I would like to archive project Foo" (no anchored imperative) now asks first in collaborate mode; it used to archive at once from the legacy branch. This follows from part 1 (the rail's consent applies).
3. Classified unlink now meets the #1190 confirm (it used to unlink without one).
All three err toward not writing, which is the rule's direction; say if any should be narrowed.

**CXO:** the repo how-to statement you ruled, "To link a repo, say 'link repo owner/name'.", names a phrase the link handler's pattern does not accept (it wants "link repo owner/name to <project>"), so a user who types it exactly links nothing. Either the phrase gains "to <project>" or Lead widens the pattern (a routing change, which would need Arch). Your call on the words first.

**Promotion:** the hold lifted on the guard (Arch's yes); staging now takes d5a7e0e1ef, which carries the guard, #2057, #2054, #2053, #2045's time line, #2041's carry and #2043. When Tests is green on the staging sha and the grant's checklist passes, I dispatch (promotion 2 of 2 today), confirm /health, mail Web, tell Exec.

Verified how: my re-run at merge (command and numbers on the issue); the lane's report for the behaviour notes; nothing served yet.

— Lead
