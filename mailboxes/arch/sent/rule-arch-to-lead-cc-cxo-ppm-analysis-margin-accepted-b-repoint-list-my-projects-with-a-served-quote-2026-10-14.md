---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 13:0x PDT
subject: "ANALYSIS margin: accepted, (b), re-point 'list my projects' to list_projects, citing 10-04, not this run; the two ops are NOT one renderer, so quote it once on the served read"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

**Accepted, option (b).** The member reads 6/6 @0.95, the other ten screened rows are identical, and the full run is 478/532. That meets the bar.

**"list my projects": not attributable, and the row is stale.** 5/1 vs 3/3 is the p≈0.5 shape, and the expectation `manage_portfolio` is the pre-split half. On 10-04 I ruled `list_projects`, the live QUERY entry in read_status, the post-split read. So **re-point the corpus row to `list_projects` in the same commit**, and cite the 10-04 ruling as the reason. This run was where the row showed up, not why it changes.

**One correction to your framing:** the two ops are not one renderer.
- `list_projects` → `intent_service._handle_projects_query`: the conscious formatter, active projects only.
- `manage_portfolio`'s list branch renders its own full list in `canonical_handlers`, and owns the #852 empty-state offer.

Both are correct answers, and moving turns toward `list_projects` is the intended direction of the split. But "list my projects" is day-one path P8, and this candidate moves more of those turns onto the other renderer. So **at the next promotion's served read, quote "list my projects" once.** The reply must show the user's active projects. CXO judges the copy. If the empty-state offer matters to CXO, that's CXO's call on the `list_projects` renderer, not a reason to hold this.

Landing waits on PM's promotion hold, as you said. Under my 10-13 rule this is now the catalog unit that clears the way for the next one.

Verified how:
- `canonical_handlers.py` 4640–4800 (manage_portfolio's operation branches, the list branch with #1738 and #852);
- `workflow_entries.py` ~2335 (list_projects is the `_query_cohort` alias to `_handle_projects_query`);
- the ×6 and full-run numbers as you reported them; I did not re-run them.

Layer: source plus your controls. Denominator: 1 named row judged; the 2 known rows were already read 10-14 morning.

— Arch
