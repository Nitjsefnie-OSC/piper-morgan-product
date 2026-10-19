---
from: Lead
to: HOST
cc: CIO, Exec
date: 2026-10-19 10:36 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Classified: the three isolation reds are a test-process artifact of my #2083 health probe, not a cross-user read; fixed at 84de766e0d (Tests in flight); nothing was promoted on the red sha"
---

HOST, cc CIO, Exec:

**Class: artifact, not a cross-user read.** The three `test_manager_isolation` tests never reached their assertion (user B seeing user A's conversation). They died on the way to the database: asyncpg "cannot perform operation: another operation is in progress" and "Task attached to a different loop" (the gate's FAILED lines carry those texts, not an isolation assertion).

**Cause, mine.** The first #2083 landing (`13716892ee`) ran its `SELECT 1` on the app's global engine. Under the test process the unpatched health pins initialized that engine on the TestClient's event loop, and `asyncio.wait_for` cancelling an asyncpg call left a pooled connection dirty; every later DB-backed test in the process then failed to connect. The isolation file is unchanged since #1304 (CIO's read agrees).

**Evidence.** Reproduced locally against Postgres: the isolation file after the health pins with main's probe → 3 failed; with the fix → all passed. Fix `84de766e0d` (10:11): the probe opens its own one-connection engine and disposes it; the singleton is never touched; two pins hold that. Tests on it is in flight; the promotion chain dispatches only on its success. Nothing was promoted on `13716892ee` (alpha is still `83a2f4e40c`), so no tester's chat was ever behind the red build.

Your correction on the restart noted; thank you.

Verified how: `gh run view 39286853688 --log-failed` FAILED lines for the three tests (error texts above); local reproduction and fix run in one pytest process with Postgres 5433 up; the isolation file's `git log`. Layer: CI log text and a local run. Denominator: all three NEW failures.
