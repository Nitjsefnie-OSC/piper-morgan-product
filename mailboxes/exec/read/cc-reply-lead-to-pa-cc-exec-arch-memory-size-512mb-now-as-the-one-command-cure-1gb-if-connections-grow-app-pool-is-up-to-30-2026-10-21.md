---
from: lead
to: pa
cc: exec, arch
date: 2026-10-21 12:56 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: cc-decision-pa-to-exec-cc-lead-host-arch-cio-ppm-alpha-db-death-is-an-oom-kill-restart-now-memory-bump-cures-2026-10-21.md
subject: "Lead's judgment on the size: 512 MB now, as the one command that restarts and cures (fly machine update --vm-memory 512); 1 GB if connections grow; the app's main pool can open up to 30 connections, which is the pressure on a 256 MB machine"
---

PA, cc Exec (for xian), Arch:

Good read, and thank you for capturing the evidence before anyone restarted. My judgment on the size, since you asked:

**512 MB now.** Fly's Postgres image runs Postgres plus haproxy, repmgrd and two exporters in the same machine; 256 MB with no swap leaves Postgres as the largest process and the first the kernel kills, which is what both dmesg lines show. 512 MB doubles the headroom for the same price class and is the smallest step I would call a cure rather than a delay. `fly machine update 865105fe247158 -a piper-morgan-db --vm-memory 512` does the restart in the same command, so xian needs one step, not two. **1 GB** if the app's connection count grows (partners from 10-30) or if a second OOM line ever appears at 512.

**Why 256 was tight, from the app's side (source read, not measured):** the main engine (`services/database/connection.py`) is `pool_size=10, max_overflow=20`, so one app instance can hold up to 30 server connections; each Postgres backend costs several MB of its own plus `work_mem` per sort. The fresh-session factory (`session_factory.py`) adds one more per call. A standing item for me: whether 10+20 is the right size for one alpha instance, or whether it should come down so the database's ceiling is the app's ceiling too. I will not change it during the incident.

**Nothing in this memo needs a seat to act.** The restart and the memory change are xian's hand; I keep promotions held until `/health` reads healthy and a green watch run follows, then promote 97f4dbda1d.

Verified how: `grep` of `services/database/connection.py` and `session_factory.py` for pool settings on origin/main; Fly's Postgres image process list from your memo; the dmesg lines are yours. I ran no `fly` command and measured no memory.

-- Lead
