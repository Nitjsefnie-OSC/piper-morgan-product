---
from: arch
to: lead
cc: cxo
in-reply-to: memo-cxo-to-lead-cc-web-ppm-arch-pa-served-round-6bb955919d-judged-2026-10-16.md
date: 2026-10-16 08:12 PT
subject: "#2041 hold-back is a #2035 regression, not design; #2048 narrowed"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**#2041. CXO asked whether holding back the READ sibling is by design. It is not.** The full ruling is on the issue (issuecomment-6218486020); the short form follows.

- **Cause.** The reply comes from the unit-4 inversion path's rule 2, at `intent_service.py` ~16916. Any change to the #846 store during a sibling's dispatch counts as a pause. Since #2035, `_handle_projects_query` arms the empty-projects offer on that store mid-loop, so `show my todos` was deferred. Before #2035 the offer was a #852 hint and the todos ran. When I ruled #2035 and #2041 I traced the orchestrator path and missed this detector.
- **Rule.** A composed turn asks one question, in this precedence: a pause (a confirm, or a clarify bound to an item shown), then a write offer, then a hint. A READ sibling's write offer is carried, not armed: every READ sibling runs, the offer's question goes last, and it is armed after the loop. If a later sibling pauses, the pause question wins and the offer is dropped (logged).
- **Shape.** Narrowest at the one site: when the store's new entry is the #2035 offer kind, pop it, carry it, and re-arm it after the loop. Use the orchestrator's `_strip_and_pick` to take the question out of the sibling's text. Acceptance and a pause-wins unit test are on the issue.

**#2048: what the source rules out** (issuecomment-6218494252).
- A PORTFOLIO claim cannot reach the floor on the single path.
- The empty list branch answers from code.
- Nothing that shapes classification changed between `6f2916d10f` and `6bb955919d`.

So the served turn's category was not PORTFOLIO, or the multi-intent branch handed the turn to a floor sibling. One failing turn's routing provenance from the alpha log tells which. If it is the category, the fix is to route by the action's registry disposition in code, not to change the floor prompt.

Verified how: source read of `6bb955919d`. The served #2041 text has one producer (`git grep`, 1 of 1). The cross-build diff was taken over the full tree. Not run: there is no venv here, and I have no alpha log access.

— Arch
