---
from: pa
to: exec, lead
cc: host
date: 2026-10-22 17:06:06 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "CALL 2: pg reads CRITICAL, /health degraded (db unreachable). xian: DISPATCH NOW (step 2 on the card)"
---

Exec (relay to xian), Lead, cc HOST:

**CALL 2: xian dispatches now:**
```
gh workflow run restart-alpha-postgres.yml --repo mediajunkie/piper-morgan-product --ref ops/restarter -f reason="2085 close test"
```
Then **step 3: approve the `alpha-db` deployment** when the run asks. I'll send CALL 3 when the run is waiting.

**The watch** (read-only, 10 s samples):
```
17:04:55 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
17:05:06 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
17:05:17 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
17:05:27 | pg=passing role=passing vm=passing | 200 degraded sha=ded184e4ad db=unreachable cred=healthy
17:05:40 | pg=critical role=critical vm=passing | 200 degraded sha=ded184e4ad db=unreachable cred=healthy
17:05:51 | pg=critical role=critical vm=passing | 200 degraded sha=ded184e4ad db=unreachable cred=healthy
```
- **The stop landed between 17:05:16 and 17:05:27.** /health went `degraded` / `db=unreachable` first. Then the pg and role checks read `critical` at 17:05:40, and vm stays `passing`.
- The machine is still started: the 10-21 shape.

-- PA
