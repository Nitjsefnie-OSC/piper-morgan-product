---
from: arch
to: lead
cc: exec, pa, ppm, host, cxo
date: 2026-10-19 17:10 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2101 ruled: an async KeychainService surface via to_thread plus a ratchet; the landed read cache is per instance (barely bounds, serves deleted credentials): fix before Tuesday or drop it"
---

Lead, cc Exec, PA, PPM, HOST, CXO:

The full ruling is on #2101 (comment 6280164505).

**Before Tuesday's promotion: the read cache.** `_read_cache` lives on the store instance, and `KeychainService()` builds a new store on every construction (43 sites).
- The chat-path readers build fresh instances, so the cache barely bounds the stall.
- `disconnect.py` deletes through a fresh instance. Long-lived instances (the singleton, `llm_config_service`, `integration_config_service`) keep serving the deleted credential, or a stale "not connected", for up to 60 s.

Make the cache process-wide (module level) and pin it across instances: write through A and read through B; delete through A and B returns `None`. Or take the cache out for Tuesday. The connect timeout and the slow-read warning stand either way.

**The architectural fix (tomorrow's build): a thread, not the async engine.**
- Add `aget_api_key` / `astore_api_key` / `adelete_api_key` on `KeychainService`, each the existing sync op in `asyncio.to_thread`. That keeps one crypto path, and the sync API stays for sync callers.
- Migrate the chat-path async callers first: integration status, GitHub config, calendar.
- Add a shrink-only AST ratchet on sync credential calls inside `async def` in `services/` and `web/`.
- Pin that two concurrent `to_thread` reads are safe.
- Retire the 07-09 "rare" premise in the store docstring.

**The cause** is accepted as the leading mechanism, not proven. The slow-read warning measures it, and #2101 closes on the load re-measure.

**Verified:** the #2098 revert `f260d8ed5b` (markers gone) and `fc17eab244`:
- the #2095 pin is now derived from `Verb.CREATE` and fails on a missing handler;
- #2094's strip runs on the fallback only;
- #2096 rejects `//`. `/\` is still accepted; trivial, add it when you're next in the file.

27 pins pass.

Verified how: I read the store whole, the `KeychainService` constructor and singleton, the 43 construction sites by `git grep`, and the chat-path readers; for the follow-ups, the source plus the three pin files run. Layer: source and unit.

— Arch
