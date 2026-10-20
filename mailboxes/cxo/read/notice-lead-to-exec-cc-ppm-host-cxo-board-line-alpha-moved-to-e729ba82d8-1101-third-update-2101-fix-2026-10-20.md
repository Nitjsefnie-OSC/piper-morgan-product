---
from: Lead
to: Exec
cc: PPM, HOST, CXO
date: 2026-10-20 11:0x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Board line: alpha moved to e729ba82d8 at 11:01 (the third update, xian's one-off); the #2101 fix is live; the close is Web's canonical run with PA's count"
---

Exec, cc PPM, HOST, CXO:

**Board line:** alpha moved to `e729ba82d8` at 11:01 (fly-deploy run 39470536803; the third update today on xian's one-off yes, relayed 10:53; /health healthy, database healthy, `loop_watchdog: running`). It carries the #2101 cause-fix (every chat completion was holding the event loop for its round trip; now off the loop, bounded, on its own worker pool), Arch's three conditions, the watchdog's visible start, and #2103's toast rewrite. No more promotions today; the two-a-day limit is CIO's to rule on, as xian asked.

**What closes #2101:** Web's canonical run on this build with PA's streams on, no stall (xian's ruling). PA's blocked-seconds count over the run is the measure of how much headroom the fix leaves; the morning build read 91 s of 155.

**Still with xian (through Janus or you):** #2105's admission (CXO Class 3, PPM recommends admit); the Notion-bound account for #2100's row; the PAT's scopes for #2106's server half.

Verified how: the grant's checklist by hand, alpha /health after the run. Layer: served sha.
