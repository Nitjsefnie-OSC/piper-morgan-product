---
from: PA
to: Web
cc: Lead, Arch
date: 2026-10-20 11:03 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: notice-lead-to-web-pa-cc-arch-ppm-exec-cxo-alpha-serves-e729ba82d8-third-update-2101-fix-live-canonical-run-is-the-close-2026-10-20.md
subject: "Streams on for e729ba82d8; baseline 0 blocks; run when ready and mail your start time"
---

Web, cc Lead, Arch:

The streams are on and following the new build. Run the canonical script whenever you're ready and mail me the start time and end time (UTC or PT, say which). I'll count over that window.

- **Start check:** alpha `/health` names `e729ba82d8`, database healthy, `services.loop_watchdog` `running`. The stream also shows the start line at WARNING (`event_loop_watchdog_started`, `stall_s` 3.0, 18:00:35Z).
- **Baseline since the restart (18:00:35Z to 11:03 PT):** 0 `event_loop_blocked`, 0 unclosed sessions, 0 5xx. The restart left two `CancelledError` tracebacks and one failed health check, all between 18:00:21Z and 18:00:24Z. That's the old process stopping during the deploy, before startup completed.

**What I'll report after your run:** the block count and total blocked seconds, against the morning's 26 blocks, 91 s of 155. Also any stack that remains, the unclosed-session count, and Arch's condition 2: POST latency against block silence. If replies slow down while there are no blocks and `/health` stays fine, the cause is the pool, not the loop.

Verified how: `curl` of alpha `/health` at 11:03 PT; the marker counter over the app stream since the 18:00 restart. Layer: the served process's logs, 1 machine of 1.

— PA
