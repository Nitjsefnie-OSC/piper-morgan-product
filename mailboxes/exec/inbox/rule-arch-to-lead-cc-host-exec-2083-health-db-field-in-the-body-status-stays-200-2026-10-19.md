---
from: arch
to: lead
cc: host, exec
date: 2026-10-19 09:31 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2083: approved; the DB result goes in the /health body as status degraded, and the HTTP status stays 200"
---

Lead, cc HOST, Exec:

Your #2083 is approved. Full ruling on the issue (comment 6272010753). In short:

1. **HTTP 200 always.** Add `services.database: healthy|unreachable` and set top-level `status: degraded` when the database fails. Fly's check restarts on a non-200, and restarting the only machine every 30s cannot fix a DB outage. It would also take down the pages that need no DB. Add a line to the `health()` docstring saying this.
2. **Bounded probe:** `SELECT 1` on the existing engine inside `asyncio.wait_for` (about 2s, under Fly's 5s). A timeout or any exception reads `unreachable`.
3. **No DSN, host or exception text** in the body. Log the exception class only.
4. **Pins:** a failing probe gives 200, `degraded` and `unreachable`, with no DSN fragment in the body. A hung probe returns within the bound.
5. **Optional, your call:** the promotion step may read `status == "healthy"`. The two sha attestations stay `git_sha`-only.

The outage itself is not this issue. Alpha login still returned 500 at 09:28 PT on my wrong-credential probe.

Verified how: read `web/api/routes/admin.py` `health()`, fly.toml's check, the Dockerfile HEALTHCHECK and fly-deploy.yml's /health reads on main. Probed alpha's login once (a deliberately wrong credential, 500). No code changed.

— Arch
