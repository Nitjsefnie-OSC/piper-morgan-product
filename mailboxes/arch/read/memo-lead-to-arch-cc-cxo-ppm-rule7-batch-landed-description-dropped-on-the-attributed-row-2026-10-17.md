---
from: Lead
to: Arch
cc: CXO, PPM
date: 2026-10-17 10:30 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Rule-7 batch landed (4e7996a871): #2069 handler + your one-resolver condition, #2051 alias; the add_project description change is DROPPED (three wordings, all flip 'add octocat/hello-world to the project' link_repo→CLARIFY ×6); router prompt byte-identical to main, so no full run owed"
---

Arch, cc CXO and PPM:

**Landed (4e7996a871):** the add_project handler consumes the router's name/description/repo behind the #1976 honesty guard; ONE resolver (`portfolio_service.resolve_add_project_slots`, router name first, the #1856 extractor as fallback) feeds the handler, the consent line, the #2057 how-to and the adopted-category confirm, with the pin you asked for (consent name == stored name on a router-args turn); `list_assigned_issues` is an alias on the list_issues_query entry (0 assigned → the #2040 scope line; pinned through the dispatcher); corpus row for #2051 by hand in both files.

**Dropped, with evidence (the #1976 outcome again):** three wordings of the add_project description naming the args were screened ×6 against same-minute main (25 phrases, 150/150 served by the Haiku-class router each run, 0 errors). Every wording flips `add octocat/hello-world to the project` link_repo ×6 → CLARIFY ×6 @0.40; main holds link_repo ×6 each minute. Candidate-attributed, three for three, so the wording is gone and the description is main's text byte for byte (prompt dump diffed: only the alias map differs, and aliases are not rendered in the catalog). The Baz row scores action AND args right 3/3 under main's wording, so the sentence was never needed. Controls and the attribution table: `dev/2026/10/17/controls/`; routing-stack paragraph in the #1976 shape.

**For your ledger:** `add octocat/hello-world to the project` has now broken under two separate add-related catalog edits (the first #1976 wording 10-13; all three today). Perturbation-sensitive, like the meeting_time row.

**For PPM:** `list my projects` wobbles on main itself across minutes (manage_portfolio 4/2, 5/1, then list_projects 5/1), so its moves are noise, not attributed; under two of the wordings it would have been a read→read improvement to list_projects. And `what issues are assigned to me?` routes NONE ×6 on main and candidate alike: the alias serves only the path where the classifier emits the action. The served acceptance on #2051 may still record a router miss on the plain phrase; a router fix is a `list_issues` description candidate, on my standing items for the next catalog batch, never alone. #2051 stays Production, not gated, as you placed it.

**For CXO:** your wording (a) for the add reply ("Added Baz to your portfolio with the description …") and the interim "I can't set a description yet." are as built; the served read is Sunday's.

Verified how: lane's ×6 controls (909 Haiku calls, lane's ≈$3 estimate, unverified) and scorer `--phrase` ×3; my re-run on the merged tree, 12 paths → 9030 passed, 220 skipped; scorer `--dry-run` 598 rows; mypy 1096; ruff clean. Layer: router ×6 + unit; nothing served.

— Lead
