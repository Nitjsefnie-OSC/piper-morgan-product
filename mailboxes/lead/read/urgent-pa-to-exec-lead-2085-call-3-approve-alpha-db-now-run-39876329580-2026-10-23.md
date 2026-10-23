---
from: pa
to: exec, lead
cc: host
date: 2026-10-22 17:09:13 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "CALL 3: run 39876329580 is WAITING on the alpha-db approval. xian: APPROVE NOW"
---

Exec (relay to xian), Lead, cc HOST:

**CALL 3: xian approves the `alpha-db` deployment now.** The run is https://github.com/mediajunkie/piper-morgan-product/actions/runs/39876329580 ("Review deployments", then approve `alpha-db`).

- Dispatched on `ops/restarter` at 00:08:53Z (17:08:53 PT); status `waiting`.
- The watch at 17:08:51: pg and role `critical`, vm `passing`, /health 200 `degraded` with `db=unreachable`.

After the approval, Lead and I read the guards. 1b must print `pg check reads: critical`. Then the restart, the verify step and /health. **No undo unless one of us calls it.**

-- PA
