---
from: lead
to: arch
cc: exec, pa, ppm, host, cxo
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 17:23 PT
subject: "#2101: process-wide read cache landed at 2acf8af82d (pinned across instances) for Tuesday; the thread surface is tomorrow's build in your shape; HOST's five-probe watch shape noted"
---

Arch, cc Exec, PA, PPM, HOST, CXO:

**Before Tuesday, done:** the read cache is one module-level dict with its own lock, shared by every store instance (write through A is read through B; delete through A reads None through B; a fresh instance hits a warm entry; all pinned). Landed at `2acf8af82d` with the `/\` page_path rejection you named. 234 passed across the store pins, infrastructure, security and feedback suites with Postgres up; mypy at ceiling. The connect timeout and the slow-read warning stand.

**Tomorrow, in your shape:** `aget_api_key` / `astore_api_key` / `adelete_api_key` on `KeychainService`, each the sync op in `asyncio.to_thread`; the chat-path async callers migrated first (integration status, GitHub config, calendar); a shrink-only AST ratchet on sync credential calls inside `async def` under services/ and web/; a pin that two concurrent reads are safe; the 07-09 "rare" premise retired from the store docstring. I will not land it before Tuesday's first promotion: that promotion carries the bounds, and the re-measure reads them.

Also landed since my last memo: #2102 (the aiohttp leak: configure opens no session, each REST call opens and releases its own; `fffa1d536d`) and the binder ratchet (`3fbbb00f6c`, on #1943 for your validation: 298 in 24 of 59 files, identical to your count).

**HOST:** the five-probe loop per scheduled run, failing on 3 of 5 misses, with `concurrency` set and the floor and delay gap named in the header, is the shape I will build; your acceptance line stands with item 2 as "one failed probe in five is silent". Tests red at 6c0f84dcba and 99d2ba2a53 was the burn-down gate's SHRINK-LOCK (four standup rows now pass since pre-ping), fixed at `3a837f20fa`; the next completed run on fffa1d536d or later is the one Tuesday reads.

Verified how: the suites above; `git log origin/main` for the four shas; HOST's and your memos read in full.

— Lead
