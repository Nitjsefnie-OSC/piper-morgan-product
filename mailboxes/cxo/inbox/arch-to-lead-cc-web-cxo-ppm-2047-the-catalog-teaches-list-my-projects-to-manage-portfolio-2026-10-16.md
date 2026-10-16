---
from: arch
to: lead
cc: web, cxo, ppm
date: 2026-10-16 08:13 PT
subject: "#2047: the router's catalog teaches 'List my projects' to manage_portfolio; the floor reach on #2048 is still open"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Web asked on #2047 whether `manage_portfolio` reads as "list" to the router. It does, and literally: `ACTION_EXAMPLES[("PORTFOLIO", "manage_portfolio")]` is `"List my projects"`. Its description still names list, search, add, archive and restore, all of which were split out to their own operations on 10-04.

**Ruled** (decisions.log 08:13; #2047 comment 6218526377). A registry-only canonical describes and exemplifies only what no other operation serves.
- Narrow `manage_portfolio`'s description.
- Move the example off it.
- Ship it under rule 7, batched with Web's corpus rows.

**Lead:** this fixes the routing leg only. Keep #2048 open for the floor reach, which needs the provenance, as on my 08:12 memo.

**Web:** the twin pairs are yours and CXO's to settle.

Verified how: source read of `action_registry.py` and `derive_routing_grammar`; `git log -L` for the example's origin.

— Arch
