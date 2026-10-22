---
from: pa
to: exec, lead
cc: host
date: 2026-10-22 16:23 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#2085 close test, starting state GREEN; CALL 1: xian runs step 1 (the pg_ctl stop) at 16:30"
---

Exec (relay to xian), Lead, cc HOST:

**Starting state** (PA's read-only watch, sampling every 10 s):
```
16:23:04 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
16:23:16 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
```
- The database machine's checks read pg, role and vm **passing**.
- Alpha `/health` returns 200, healthy, `ded184e4ad`, database healthy.
- No earlier run of the restarter exists; `gh run list` is empty.

**CALL 1, xian at 16:30:** step 1 on his card, the `pg_ctl stop` line, in a plain Terminal. Expect "server stopped".

**Next from me (CALL 2):** "pg reads critical, dispatch now", once the watch shows `pg=critical` and /health degraded. Until then, don't dispatch. Guard 1a would refuse a healthy database.

-- PA
