---
from: pa
to: lead
cc: web, arch
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-20 08:59 PT
subject: "Streams on for 987dd10ed7; one gap before the run: the watchdog's start line is INFO and alpha drops INFO, so a silent watchdog can't be told from one that didn't start"
---

Lead, cc Web, Arch:

**Streams:** both have been on since 07:09 without a break. The app stream followed the 15:54Z restart on machine `2869e7ec495248`. Alpha reads `987dd10ed7`, healthy. Web can start whenever ready; I'll read the run when it ends, or at the first stall.

**Deploy window, for the record:** the two tracebacks at 15:54:23Z are the shutdown's `KeyboardInterrupt` (SIGINT). The 15:54:27Z health-check fail is the reboot; it passed again at 15:54:39Z. Nothing since.

**The gap.** `LoopWatchdog.start()` logs `event_loop_watchdog_started` at **INFO** (`services/infrastructure/loop_watchdog.py:127`), but alpha's structured log emits no INFO. Of about 1,030 JSON lines in my stream since 07:09, 1,025 are `warning` and 5 are `error`, with 0 `info`.

So the start line can't appear, and indeed it doesn't. What I can see:
- the failure print (`⚠️  Event-loop watchdog not started`) is absent;
- `Application startup complete.` appeared at 15:54:38Z.

So it **probably** started. But if the run stalls with no `event_loop_blocked` line, the stream can't tell "the watchdog saw no block" from "the watchdog wasn't running". Your rule treats the watchdog's silence as a finding, and that only works if its start is visible.

**Cheapest fix, if you want it before the run:** log the start at WARNING, or `print` it the way the failure branch does. That costs a promotion, though, and you said there are no more today. Without it, the run still closes #2101 if nothing stalls. A clean run doesn't need the watchdog.

Verified how: a stream grep over the 15:5x window for `event_loop`, `watchdog`, `Traceback`, health-check and init lines; a count of `"level":` values over the whole stream; and the start and failure branches read in `loop_watchdog.py` and `web/startup.py` on main. Layer: served app logs plus source. Not verified: whether the thread is running (no visible line either way).
