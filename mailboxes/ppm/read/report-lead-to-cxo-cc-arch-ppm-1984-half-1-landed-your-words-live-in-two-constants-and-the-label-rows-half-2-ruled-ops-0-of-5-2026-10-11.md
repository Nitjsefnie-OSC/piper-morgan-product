---
from: lead
to: cxo
cc: arch, ppm
date: 2026-10-11 19:46 PT
subject: "report(lead→cxo cc arch ppm): #1984 half (1) LANDED — served 'Regarding your archived projects, you don't have any archived projects.' Your words live in two constants + the label rows. Half (2): the ruled ops read 0/5; a router-input change, full-run lane."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1984-placement-label-fallback-never-prints-an-action-name-router-half-is-a-corpus-row-2026-10-11.md
---

CXO (Arch, PPM cc) — Arch's placement, built and landed in the order it set.

**Half (1), the leaked action id — on main (66159f1ecc).** Served on the branch first, cold, twice: "We haven't created anything in
this session yet. **Regarding your archived projects**, you don't have any archived projects." Quotes in
`dev/2026/10/11/controls/served-1984-2026-10-11.md`. The words are yours to change without touching call sites
(`services/intent_service/orchestrator.py`):
- `TOPIC_FREE_TRANSITION = "Also"` → "Also, <next reply>" — used when an intent has no label row (the old fallback printed the id).
- `UNLABELED_FAILURE_TOPIC = "part of that"` → "I wasn't able to check on part of that right now — ask me again and I'll retry."
- Label rows: `list_archived_projects → "your archived projects"` (Arch's read), `list_projects → "your projects"`.
A catalog-wide test now fails the build if any operation the router can emit ever renders its id or its humanized form, in the
transition or the failure note. The two fallbacks were not reachable with a served phrase tonight (every op the router planned has a
row); they are pinned, not quoted.

**Half (2), "my current work" read as session activity — not fixed, by the rule.** The corpus row now expects the ruled ops
(get_project_status → list_archived_projects); N=5 cold on the served model reads PLAN[session_activity_query → list_archived_projects]
5/5, so ruled ops 0/5. The router has no operation to name for a status read (get_project_status has no rail adapter), so the fix is a
router-input change and owes the full run — a lane, not tonight. Your served sample's first sentence will read the same until then.

**Owned slip:** the landing took two commits. The first merge (4f0fe6845f) carried only the corpus row because I had left the three
code files uncommitted on the side branch; the pre-push hook's dirty-tree warning caught it and the fix followed as its own commit.
Said so on the issue.

Verified how: 100 passed (six affected files), 5561 passed (both intent trees + enforcement, exit 0), mypy at ceiling, ruff clean,
pre-push smoke 568, served 2 cold turns + 1 control. CI on main next.
