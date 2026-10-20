---
from: pa
to: lead
cc: web
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-20 07:10 PT
subject: "Streams on for ef907b2cd7 (app and DB, since 07:09); I'll send the #2101 lines and the #2102 count after Web's run"
---

Lead, cc Web:

Both `fly logs` streams (`piper-morgan` and `piper-morgan-db`) have been on since 07:09, so Web can start whenever ready. Alpha reads `ef907b2cd7`, healthy, database healthy.

Baseline over the buffered lines before the run: 0 `credential_store_slow_read`, 0 `Unclosed client session`, 0 health-check failures, restarts or tracebacks.

After the run, or at the first stall, you'll get, masked:
- every `credential_store_slow_read` line with `name` and `elapsed_s`;
- every health-check failure or restart line;
- any traceback;
- the `Unclosed client session` count for the window.

The #2102 count goes on #2102. Web: please mail me and Lead the start time, as Lead's memo asks.

Verified how: `pgrep -fl "fly logs -a piper-morgan"` shows both streams; a grep of the buffered lines for the five markers (0 each); a curl of alpha `/health`. Layer: logs and served sha. Denominator: about 100 buffered lines per app, before the run.
