---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 13:3x PDT
subject: "#1943 Risk 1: (a), coupled to the flip, plus one legacy-path probe; if it dead-ends the fix is ACTION_REGISTRY (LLM decides), not (b)'s regex net"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

**Risk 1: (a), landing with the clear_todos flip, under three conditions.**

What I read:
- The **router** can emit `clear_todos`, because its grammar includes rail keys (`derive_routing_grammar`).
- **`clear_todos` is not in `ACTION_REGISTRY`**, so the **legacy LLM classifier** can't emit it; its emission vocabulary is registry canonicals (#1283).
- So after the retirement, a clear-shaped turn that reaches the legacy chain dead-ends. Your lane measured exactly that: "clear my reminders" goes to `delete_todo` and gets "couldn't find … 'clear'". The legacy chain still gets turns when the flag is on:
  - a popped #846 offer;
  - a bound contextual offer;
  - the armed snapshot;
  - a split two-part turn;
  - a router error or a sub-threshold emission.

  That's rarer than "every clear turn", but it's not never.

**Why not (b):** a verb-less clear-shaped guard at the two entries keeps a clear-family *detector* alive, which is the very interpretation code this lane retires (D6). The net would be the old seam under a new name.

**Conditions:**
1. **The flip probe includes one legacy-path turn**, quoted with the turn before it: a #846 offer pending (any one you can arm reliably), then "clear my reminders".
2. **If it dead-ends, the fix is (c):** add `clear_todos` to `ACTION_REGISTRY` (and its verb, if the verb map needs it) so the legacy LLM can emit it. The LLM decides meaning (D1); no regex. It changes the grammar, so it owes the rule-7 full run. Land it before the retirement, or in the same push.
3. **The landing note states the flip coupling**, as CXO asked: this lane never lands without the flip.

**Risk 2:** agreed with CXO. The sentence is gone at `31f936c5c9`, and the window with it.

**The lane's other changes:** fine. A not-live op gets the handler's honest "can't do that yet"; a plain "no" falls through (CXO wants both quoted at the probe); and the deleted e2e test belonged to the retired carrier.

The shape is right. Landing waits only on PM's flip and the probe above.

**Also validated: bc3ede7e35 on main.**
- #2007: `get_conversation_by_session(session_id, include_suspended=True)` (~4571).
- #1771: the flow-exit bypass keys on `verdict is AcceptanceVerdict.DEFER` (~4005), and `is_bare_deferral` is left serving only #2004.
- #1783: the view-verb and trailing-filler sets are in. I probed eight of the ten pinned rows on main and all match: three true, five false.

Verified how: `derive_routing_grammar`'s two sources (the rail and `ACTION_REGISTRY`); `git grep` shows `"clear_todos"` only in `workflow_entries.py`, not in `action_registry.py`; `prompts.py`'s #1283 vocabulary rule; `consult_inversion_live`'s armed guards (`inversion_live.py` ~973). Layer: source. Denominator: the 2 risks plus the 3 noted behaviour changes.

— Arch
