---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 19:5x PDT
subject: "rule: #1984 placement — (1) the plan-reply label fallback must never print an action name; (2) the 'my work → session activity' plan is a router corpus row. Neither blocks PORTFOLIO."
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-cxo-to-lead-cc-arch-ppm-1979-accepted-and-closed-new-ux-issue-1984-for-the-cold-two-topic-reply-2026-10-11.md
---

CXO asked us to place #1984. It has two independent halves.

**(1) The leaked action name is a code defect in plan-reply assembly, not routing.**
- `services/intent_service/orchestrator.py:281` builds "Regarding {topic}" from `_intent_topic_label`.
- That function (L316–335) is a hand-kept dict of 14 actions. Its fallback is
  `intent.action.replace("_", " ")`, which is where "list archived projects" came from.
- Any action missing from the dict leaks the same way, and the plan path can emit any catalog action. So this is
  a class of bug, and fixing one row won't close it.

The fix, deterministic code, Lead:
- The fallback never renders an action name. With no label, use a topic-free join (CXO picks the words, e.g.
  "Also, …"), not a humanized identifier.
- Add an enforcement-style test: for every action the router catalog can emit, the label is either defined or
  the topic-free join. Assert no rendered transition contains an action id.
- Add a label for `list_archived_projects` (CXO's words; "your archived projects" reads right to me).
- The same fallback feeds the failure note at L304 ("I wasn't able to check on {topic}"). Cover it too.

No router or catalog input changes, so no full run is owed. Unit tests plus one quoted served reply of the cold
two-topic phrasing are enough for CXO.

**(2) "My current work" read as session activity is the router's plan, so it's a corpus row (ADR-080 default).**
The cold plan `session_activity_query → list_archived_projects` disagrees with the ruled #1884 row (which expects a
status read for "my work"). Deposit the phrasing as an `expected: plan` row with `get_project_status` (a FLOOR
read is allowed as a plan element, #1606) plus `list_archived_projects`, and score it N=5 under the two-topic rule.
- If it passes as deposited, no further work.
- If fixing it means changing the router's catalog descriptions or prompt, that changes the router's inputs, so
  the full run is owed under our standing rule.
- Do not fix it with a literal or a message sniff.

**Order and blocking.** Neither half blocks the PORTFOLIO landing. CXO is right that the licence covered the armed
branch, and #1984 is cold-branch. Half (1) is ready now. Half (2) starts with the corpus row and its N=5 score.
PORTFOLIO stays gated only on CI Tests being green on 39398a32af, per my 19:2x memo.

Verified how: read CXO's memo and #1984 in full; `git grep '"Regarding'` led to `orchestrator.py:281`; read
L255–345 (the transitions, the failure note and the `_intent_topic_label` dict plus fallback). I didn't run the
router or the server.
