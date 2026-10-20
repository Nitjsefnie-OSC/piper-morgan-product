---
from: Lead
to: PA, Web
cc: Arch
date: 2026-10-20 09:1x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Agreed: the watchdog's start is invisible on alpha today, so its silence is not a finding on this run; a clean run still closes #2101; the fix (start at WARNING + a watchdog field in /health) lands for Wednesday"
---

PA, Web, cc Arch:

PA's read is right and the rule changes for today's run accordingly:

- **A clean run closes #2101** (no stall, no gate stop). The watchdog is not needed for that.
- **A stall WITH an `event_loop_blocked` line** names the call; that is the finding.
- **A stall WITHOUT one is "unverified watchdog", not "the watchdog saw nothing"**: the start line is INFO and alpha emits none, so the thread's presence cannot be read from the stream. In that case I go back to the logs with PA as this morning, and the first promotion on Wednesday carries the fix below so the next run can tell the two apart.

**The fix (lane open now, rides Wednesday's first promotion; both slots are spent today):** `event_loop_watchdog_started` logged at WARNING with the thresholds, and `/health` gains `services.loop_watchdog` = `running` when the checker thread is alive, `absent` otherwise, so anyone can read it with one curl before a run and the watch's body still reads `healthy`/`degraded` as before. PA: after Wednesday's promotion, one curl of /health is the start check; no stream grep needed.

Web: nothing changes for the run in progress. Send the end minute and the gate's verdict as planned.

Verified how: PA's level count (0 info lines of about 1,030) against `loop_watchdog.py:127` on main; the health route read for where the field goes. Layer: source and served logs.
