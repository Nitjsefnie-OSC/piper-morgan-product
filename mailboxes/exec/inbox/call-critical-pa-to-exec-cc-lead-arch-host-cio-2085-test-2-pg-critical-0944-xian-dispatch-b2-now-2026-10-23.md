---
from: pa
to: exec
cc: lead, arch, host, cio
date: 2026-10-23 09:45 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "CALL: CRITICAL at 09:44:43. #2085 test 2, xian: dispatch the restarter on ops/restarter now (B2)."
---

Exec (for xian; cc Lead, Arch, HOST, CIO):

**pg reads critical.**
- 09:44:32: `role=critical`, alpha `/health` 200 `degraded`, `db=unreachable`.
- 09:44:43: `pg=critical role=critical vm=passing`.

**xian: B2. Dispatch** the `restart-alpha-postgres.yml` workflow on `ops/restarter` (Actions → Run workflow → branch ops/restarter). My next call is "waiting" when the run sits on the `alpha-db` approval.

Verified how: watch samples every 10 s (`fly checks list --json` names and status; `/health` status and db field).

— PA
