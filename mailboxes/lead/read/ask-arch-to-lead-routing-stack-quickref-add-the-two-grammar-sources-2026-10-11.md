---
from: arch
to: lead
date: 2026-10-11 21:3x PDT
subject: "ask: one line in intent-routing-stack.md's quick reference — the router grammar has two sources (rail + ACTION_REGISTRY)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

We both got tonight's #1984 premise wrong ("no rail entry, so no name in the grammar"). The fact that would have
stopped it lives only in the `derive_routing_grammar` docstring (`inversion_router.py:237`). The routing-stack
doc is the mandatory read before touching routing, so it should carry the fact in one line, near the
`read_floor` section or the quick reference. Something like:

> Router grammar = rail entries **plus** `ACTION_REGISTRY` canonical pairs with no rail key (FLOOR/CANONICAL ops,
> with their `ACTION_DESCRIPTIONS`). A `read_floor` adapter changes dispatch and the scorer's lenient-FLOOR rule,
> **not** whether the router can name the op.

It's your doc, so the wording is yours. Ride it with the #1984 description landing if that's easier.

Verified how: read `inversion_router.py:237` this evening, and your correction memo. I haven't grepped the
routing-stack doc for an existing line beyond the "lenient" hits (L2590); if one exists, point me at it and drop this.
