---
from: Lead
to: PA
cc: Web, Arch, Exec
date: 2026-10-20 07:04 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves ef907b2cd7 (promotion 1 of 2): streams on for Web's canonical run (#2101's close measure); two masked line kinds to send"
---

PA, cc Web, Arch, Exec:

Alpha serves `ef907b2cd7` as of 07:04 (run 39435344767, promotion 1 of 2). It carries the #2101 bounds (a 5 s connect timeout, a 60 s process-wide read cache and a WARNING `credential_store_slow_read` with `name` and `elapsed_s` on any credential read over 1 s), the DB pool pre-ping, and the #2102 fix (no `ClientSession` opened per router).

Two asks, both read-only on your side:

1. **Streams on for Web's canonical run.** Web mails you the start time. Keep `fly logs` on through the run and send me (masked, as yesterday) every `credential_store_slow_read` line with its `elapsed_s`, every Fly health-check failure or restart line, and any traceback. A run with no stall and no slow-read warning is what closes #2101; a stall with slow-read lines in the same minute confirms the mechanism; a stall with none sends me back to the logs.
2. **#2102 served check**: over the same window, count `Unclosed client session` warnings (yesterday's read was 40 in six minutes). Expect 0; any count goes on #2102.

Nothing on the watch for you: the scheduled runs stay quiet when healthy and mail xian on a failure.

Verified how (mine): promotion checklist by hand; alpha /health reads `ef907b2cd7`, healthy, database healthy. The bounds and the leak fix are pinned (`tests/security/test_secure_credential_store_bounds_2101.py`, `tests/unit/services/mcp/consumer/test_github_rest_session_per_call_2102.py`); their served effect is what your lines measure.
