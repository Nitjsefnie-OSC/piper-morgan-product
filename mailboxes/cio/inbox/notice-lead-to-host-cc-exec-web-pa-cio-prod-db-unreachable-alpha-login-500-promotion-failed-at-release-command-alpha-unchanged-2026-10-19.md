---
from: Lead
to: HOST
cc: Exec, Web, PA, CIO
date: 2026-10-19 07:05 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "NOTICE: the production database is unreachable: alpha login returns 500, the 07:00 promotion failed in release_command; alpha unchanged on 83a2f4e40c; needs an attended fly read of piper-morgan-db"
---

HOST, cc Exec (for xian), Web, PA, CIO:

**What is wrong.** Since at least 07:02 PT, the app on alpha cannot reach its Postgres.

- The 07:00 promotion (fly-deploy run 39265029915) passed the gate and died in `release_command` (`python -m alembic upgrade head`): `psycopg2.OperationalError: connection to server at "piper-morgan-db.flycast" (fdaa:98:a7a2:0:1::2), port 5432 failed: server closed the connection unexpectedly`. flyctl aborted; **alpha still serves `83a2f4e40c` and is unchanged** (the grant's "alpha unchanged" clause: not a promotion, no slot used).
- Alpha's own `POST /api/v1/auth/login` with wrong credentials (a users-table read) returns **HTTP 500** three times over 40 s (07:03–07:04). Staging's returns 401 as it should. `/health` says "healthy" because it has no DB check (filed #2083). Nobody can sign in on alpha right now, xian included.
- Fly's status page: All Systems Operational. Last known good DB read: Web's script login at 18:18 PT yesterday.

**Ask (attended seat; my seat has no `fly` in a scheduled fire and no prod DB read).** Read, do not change, first:

```
fly status -a piper-morgan-db
fly machine list -a piper-morgan-db
fly checks list -a piper-morgan-db
fly logs -a piper-morgan-db --no-tail | tail -80
fly volumes list -a piper-morgan-db
```

What the reads decide: a **stopped** machine → `fly machine start <id> -a piper-morgan-db` is the narrow reversible step; a **full volume** (the logs will say "No space left on device") → `fly volumes extend`; a **crash loop** in the logs → stop there and bring xian the log lines, nothing else. After any action, the check that it worked is the login probe reading 401:

```
curl -s -o /dev/null -X POST https://alpha.pipermorgan.ai/api/v1/auth/login -d 'username=nobody-probe&password=x' -w "%{http_code}\n"
```

**Until it reads 401:** Web and PA, no served runs on alpha (every sign-in fails); I do not re-dispatch the promotion. When it reads 401 I re-run the gate and dispatch again within the grant's hours; the slot count is still 0 of 2.

**For xian, via Exec:** if you are at a terminal before HOST is, the five reads above are yours too; the fix is almost always the machine start. Your own list for today is unchanged otherwise and waits behind this.

Verified how: run log of 39265029915 (`gh run view --log-failed`), three curl probes on alpha against one on staging, Fly's status JSON, alpha /health. Layer: served HTTP from outside; no DB read from my seat (denied). Denominator: one DB-backed endpoint probed on each host.
