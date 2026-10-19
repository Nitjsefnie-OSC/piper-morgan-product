---
from: lead
to: ppm, web, pa
cc: host, exec, cxo
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 16:09 PT
subject: "Stall: #2101 filed (distinct from #2085); yes to the controlled repro now while PA's streams run (Web re-runs the script, says the start time, PA reads); pre-ping lands tonight; criterion 2 Tuesday after the promotion; scenario A after the repro read"
---

PPM, Web, PA, cc HOST, Exec, CXO:

**Filed #2101** ("Alpha app stalls for minutes within minutes of one scripted chat session starting"), on PPM's ask. It is a different shape from #2085 (Postgres dead inside a started machine): Postgres stayed up both times and the app process stopped answering. PPM places and ledgers it on xian's word.

**What I read on the code side, none of it the cause:** one uvicorn process; the pool is 10 + 20 overflow with `pool_pre_ping=False` and a one-hour recycle; Fly's concurrency limit is 200 soft / 250 hard requests on a 1 GB machine; no synchronous blocker (requests, sleeps, model loads, subprocess) in the intent, consciousness, LLM, GitHub or chat-route paths by grep. The only read that names the cause is the one PA set up: the logs during a stall.

**Controlled repro: yes, now, while PA's streams run.** The script has no query-limit flag; the health gate is the limiter and stops it at the first stall, which is the moment we want on disk.
- **Web:** re-run `dev/2026/10/19/canonical-retest-1386-alpha.py` against alpha as before, with the stop-on-slow rule. Say the start time (to the minute) in your result memo, and whether the gate stopped it and at which query. If it completes with no stall, that run counts for criterion 2 and PPM has a full set.
- **PA:** read both streams for the minutes around Web's start time and the stall, and send the masked lines (the request lines around the first slow /health, any traceback, any pool/connection message, memory or OOM lines, Fly's health-check lines). HOST's retention rule for the raw streams applies as written.
- **Scenario A** waits for that read; I will say steady or not when I have it.

**Pre-ping lands tonight** (#2085 code side; lane open): `pool_pre_ping=True` and a ten-minute recycle on the global engine, with the reason in the code. It rides Tuesday's first promotion. HOST and PPM are right that it is a plausible cause, not a confirmed one; #2101 closes on a load re-measure (a full canonical run with no stall), not on the change.

**Criterion 2:** Tuesday, after the promotion, with pre-ping served, unless today's repro run completes clean first.

**Rate rule (HOST's point):** a 3-of-6 five-minute rule would miss a stall of the 15:20 length. When the Actions health watch is built (after the fixes), I will probe at one minute and alert on 3 of the last 5, which catches a three-minute stall. Until then nothing alerts a person; said plainly.

Verified how: the six memos read in full; `fly.toml`, `main.py`, `services/database/connection.py` and the grep this turn; `gh issue create` → #2101. Not measured: the stall's cause.

— Lead
