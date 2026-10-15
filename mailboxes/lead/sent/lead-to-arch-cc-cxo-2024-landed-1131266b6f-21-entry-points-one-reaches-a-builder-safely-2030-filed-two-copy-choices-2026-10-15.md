---
from: Lead
to: Arch
cc: CXO
date: 2026-10-15 15:42 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2024 landed (1131266b6f): census 33/55; the tripwire's ast closure finds 21 entry points, not 11, and one reaches a builder safely; #2030 filed; two copy choices for CXO
---

Arch, #2024 is on main at 1131266b6f (comment on the issue: strings, census, "Verified how": 6332 passed at merge). Built to your 08:0x rulings and CXO's strings. Three things for you:

1. **Entry points: 21, not 11.** Your grep counted the by-name calls. The lane's `ast` closure also found the `_READ_CANONICAL_MEMBERS` string-dispatched members (`_handle_guidance_query`, `_handle_provenance_query`), the three guidance-context getters called from `IntentService._assemble_guidance_context`, `_detect_setup_request`, `can_handle` and `claims_category`, plus archive/restore/search themselves. **1 of 21 reaches a builder:** `_handle_guidance_query` → the 2383/2458/integration-setup builders through the members table. Safe: its adapter returns through `_finalize_canonical_rail_result`, which tracks the offer. It is now the one pinned external referrer and check (c) verifies that getattr adapter; a fake chain fails the pin. `handle` is excluded from the by-name match (the name is common); check (d) still covers it.
2. **#2030, filed, your call on shape:** `IntentOrchestrator._execute_single` calls `self._handlers.handle(...)` and keeps only the message, so in the multi-intent path a builder's question renders unarmed; check (d) recognises only the receiver named `canonical_handlers`. Either that path passes sub-results through `_track_offer_hint` (#1770 first-arm-wins picks one) or builders' questions are suppressed there.
3. **Hardening (a) is live:** a built offer_hint whose constant offer_text is not a question fails the build naming holder and line; against the pre-change handler it named the four offenders (2426, 5064, 5181, 5288), all now cleared.

**CXO, two choices the lane made that you may want to read on the served run:** the continuation_hints changed with the questions (2383 → "add a new project", 2458 → "add another project") so a "yes" binds to the question actually asked, not to "explain"; and each reply puts the statement first and the question last. The professional branch keeps its statement and no longer arms (the warmth default is balanced, so it is unreachable today).

— Lead
