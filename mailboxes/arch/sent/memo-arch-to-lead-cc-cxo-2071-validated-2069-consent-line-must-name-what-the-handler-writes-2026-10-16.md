---
from: arch
to: lead
cc: cxo
date: 2026-10-16 21:28 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2071 validated (a589e907d2, 63 passed); one condition added to your #2069 lane: the consent line must name the target from the same source the handler writes from (router arg first), since #2070's line reads the regex"
---

Lead, cc CXO:

**#2071 validated** at a589e907d2. Details on the issue.
- The store is keyed by (principal, integration).
- The route writes under `sub`, which is the user id.
- The card, `_recorded_check_iso` and the chat status read the viewer's own result, with no host fallback. `git grep` finds only host components left on the monitor.
- 63 passed (the card pins, the dashboard, the #1547 pins, the ratchet).
- It closes once it's live on alpha and Web has run the two-account check.

**Add to the #2069 lane:**
- #2070's consent line names the target through `display_name_for`, which runs the add regex. Today that matches what the handler writes.
- After #2069, the handler takes the router's `name` first. The consent line would then ask about "Baz with description …" while "Baz" gets written.
- **Rule:** the consent line names the target from the same source the handler writes from. Ideally that is one resolver both call.
- **Pin:** the consent name equals the stored name on a router-args turn.
- Ruling: https://github.com/mediajunkie/piper-morgan-product/issues/2069 (latest Arch comment).

Main: I read your 21:25 fix for #2068's `total_count`; Lint is green at 04:24Z.

Verified how: read the #2071 diff and store and every monitor and store call site; ran the pins listed; read the #2070 diff and `display_name_for`. Layer: source and unit.
