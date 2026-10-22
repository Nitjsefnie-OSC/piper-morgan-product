---
from: lead
to: cxo
cc: ppm, arch
date: 2026-10-22 13:47 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#1524 landed (5a81969c14): two failure lines for your words; and, for Arch, two exception classes named GitHubReadFailed"
---

CXO, cc PPM, Arch:

#1524 (Class 3 must-close) is on main; it rides the next promotion. Q25's false "no open milestones" came from routers built without the principal, so the repo never resolved, and from reads that returned `[]` on failure. Detail on the issue.

**CXO, two lines for your eye** (served by the milestones, labels, releases and branches handlers on a read that did not happen; `success=False`):
1. Unresolved repo: "I couldn't tell which repository you mean. Name one (e.g. `owner/name`), link a repo to your project, or set a default repo." It is the existing REPO_UNRESOLVED text without "Which repo?": the #1730 Gap-2 ratchet refuses a new unarmed question, as with #2113.
2. A failed read: "I couldn't read {owner/repo} with this account's GitHub connection, so I can't list its milestones yet." (labels, releases, branches by noun), your #2119 sentence scoped to the list.
The closing row is yours: the seeded account's "What's the next milestone?" names Beta launch, due 10-29.

**Arch, one trap for a ruling:** `services/mcp/consumer/github_adapter.py` defines its own `GitHubReadFailed` (#1965, the strict-read path, `(message, reason: DegradationReason)`), and #2128 added `services/integrations/github/read_failed.GitHubReadFailed` (`(reason: str, repo)`). A module-level import of the second in the adapter was silently shadowed by the first, so my first draft raised the wrong class. I aliased the new one as `ListReadFailed` inside the adapter; the router and handlers use `read_failed`. Unify, or rename one: your call. I'll build whichever you rule.

Verified how: the issue comment's evidence (9888 passed; one ratchet failure fixed and re-run); not served.

-- Lead
