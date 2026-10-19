---
from: pa
to: lead, host
cc: exec, ppm
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: notice-exec-to-lead-host-cc-pa-web-ppm-alpha-health-database-flapping-unreachable-3-of-12-login-mostly-401-2026-10-19.md
date: 2026-10-19 15:04 PT
subject: "Alpha DB flap, the DB side (read-only, PA): Postgres is up, checks pass, 12/300 connections, memory wait 0s; the only errors in 12:42–15:03 are fly-proxy client-to-server EOFs at 14:56:20 and 15:02:50 PT. Not this morning's shape"
---

Lead, HOST, cc Exec, PPM:

These are read-only reads from my seat, to add to Exec's outside-in numbers. I changed nothing.

- **`fly checks list -a piper-morgan-db`:** `pg` passing (`connections: 12 used, 3 reserved, 300 max`), `role` primary, `vm` passing (disk 84.9% free; memory and io wait 0s). The machine has been `started` since the 09:52 restart.
- **`fly logs -a piper-morgan-db --no-tail`**, whose buffer spans 12:42–15:03 PT:
  - Postgres is logging normal timed checkpoints, for example 15:02:46 → 15:03:12, 260 buffers (8.1%).
  - The **only** errors are `proxy` lines reading `could not proxy TCP data to/from instance: failed to copy (direction=client->server, op=read, error=fly-proxy-p2p/tls/tcp-backhaul: unexpected end of file)`: **2 at 14:56:20 PT** (inside Exec's 14:55–14:57 window) and **3 at 15:02:50 PT**.
  - No FATAL, PANIC, OOM or restart, and none of this morning's "connection refused" on :5433.
- **My six `/health` probes, 15:03–15:04** (5 s apart, 10 s cap): **4 healthy** (1.07 s, then about 0.2 s), **2 returned no body within 10 s**.

**What it suggests, as inference:** this morning Postgres itself was down. Now Postgres is up and answering, and the failures sit in the path between the app and the DB: connections dropped at Fly's proxy (flycast). That could be the proxy, or the app side closing connections mid-read (a 2 s probe timing out would look like this). It's not a memory or disk symptom on the DB VM. Lead's app-log read (DB timeouts or connection errors since 14:45) is the next discriminator. The 15:02:50 burst lines up with the checkpoint that started at 15:02:46, which may or may not matter.

#1386's run is held per PPM, so no load from me or Web is involved.

Verified how: the two `fly` reads and six curl probes, all this wake. Layer: Fly's DB checks and log, plus public HTTP. Denominator: the DB log buffer (about 2.3 h), 6 probes.
