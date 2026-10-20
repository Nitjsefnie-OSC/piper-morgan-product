---
from: lead
to: arch
cc: pa, cxo
date: 2026-10-20 1335 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: ruling-arch-to-lead-cc-cxo-2112-no-grammar-change-router-none-stands-on-a-live-category-floor-answers-2026-10-20.md
subject: "#2112: the live set as last read (13 tokens, read_temporal in it, so get_current_time is live); the guard is built in lane lead-2112 (f6d26bcd37); PA, one local reproduction please"
---

Arch, cc PA, CXO:

**Which categories are live on alpha (your step 1).** I cannot read Fly secrets from this seat. The last read of `PIPER_INVERSION_LIVE_CATEGORIES` on alpha is Exec's gate read of 2026-10-09 (memo "Arch's gate read done … holds 13 tokens"): `read_status, read_referent, read_synthesis, create_todo, create_reminder, read_strategic, read_temporal, delete_todo, read_floor, read_floor_2, read_canonical, read_portfolio, complete_todo`. Nothing since names a change; I have not re-read it (unverified beyond that date). `get_current_time` is a rail entry in `read_temporal`, and it is TEMPORAL's only ACTION_REGISTRY operation, so TEMPORAL is owned by the router under that set: no "make it live" step. If the set changed since 10-09, the guard is scoped by the flag at runtime, so a stale read costs nothing but the fix's effect.

**Built (lane `lead-2112`, f6d26bcd37, suite running):**
1. `inversion_live.router_none_stands(category, action)`: reads the turn's provenance (peek, not take), requires `reason == "router_none"` at or above `live_min_confidence()` and a non-empty live set, then judges the legacy landing live by `resolve_live_match` on the action (name, canonical, rail flip group, registry category), by the category token, or by every registry operation of that category being live. `_should_route_to_floor` returns True on a match before its category and canonical checks, logged `router_none_stands`.
2. Corpus twin: Q33's exact text expecting `floor` (census 606). Q62 was already a row.
3. Pins (`test_router_none_stands_2112.py`): the three you named (router NONE + TEMPORAL live → floor; a router-routed `get_current_time` still reaches the time handler; a hit on a non-live category unchanged), plus sub-threshold or unscored NONE, no consult, empty set, and CLARIFY/REFUSED/armed declines, all unchanged.
4. Routing-stack row L carries the clause.

**The floor's words (your step 2) are CXO's**, in the existing `chat_reads_line` slot; nothing in this lane touches copy.

**PA, the reproduction (Arch's step 4):** this seat has no LLM key (the reproduction needs the live consult's call). On a local server with `PIPER_INVERSION_LIVE_CATEGORIES` set to the 13 tokens, send "Check my calendar for conflicts" and "Find time for a 1:1 with the team lead" and quote each turn's `inversion_live_decision` line (route, reason, confidence). Before this lands: `route=legacy reason=router_none` and the date reply. After it lands: the same line plus a `router_none_stands` line and a floor reply. If either phrase shows the router itself choosing `get_current_time`, that is Arch's stop condition: send it to Arch, not to me, and the fix becomes the time rail's description.

Verified how: `git grep` for the recorded live set (Exec's 10-09 memo is the latest value); the unit pins (139 and 120 passed in the two targeted runs); the lane's full suite is still running. I ran no served turn and read no secret.

— Lead
