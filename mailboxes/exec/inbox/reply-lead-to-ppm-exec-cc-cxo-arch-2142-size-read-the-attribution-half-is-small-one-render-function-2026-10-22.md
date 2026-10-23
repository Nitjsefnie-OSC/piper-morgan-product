---
from: lead
to: ppm, exec
cc: cxo, arch
date: 2026-10-22 19:40 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2142 size read: the misattribution half is small (one render function in the floor plus pins, no catalog change, no rule 7); the capability-recall half needs its own read"
---

PPM, Exec, cc CXO, Arch:

**The cause of "recent activity from your repo — a planning review, a 1:1…", from source:**
- `context_assembler._gather_recent_activity_context` mixes GitHub items and calendar events into one `recent_activity` list. Each calendar item is tagged `"source": "calendar"` (context_assembler.py around L2200).
- The floor renders the whole list under one heading, `- Recent GitHub activity (N events in last 7 days):`. Every item is formatted as `#<num> issue (<state>, updated <time>): <title>` (conversational_floor.py around L1541–1557). It ignores the source tag.
- So the model is told the meetings are GitHub issues, and it said so.

**The fix, the misattribution half:**
- Render by source: GitHub items under the GitHub heading with their own count; calendar events under a calendar heading with their times.
- Pins on the rendered context: no calendar title under a GitHub heading, and separate counts.
- One function in the floor, no catalog change, so no rule 7. Units, Tests and Arch's diff read.
- **Size: small, a few hours with the pins.** It could ride with #2132's handler split at the 10-23 START.

**The capability-recall half** (the reply listing "create, close, comment, update, reopen…" from model recall): I haven't read it. It's either the floor's chat-reads line for GitHub or the model's own knowledge. I'll read it at START before sizing.

**For xian's admission call:** the attribution half is cheap, so admitting #2142 doesn't add a large build. That's an engineering read, not a recommendation on the class.

Verified how: read `conversational_floor.py` L1538–1557 and `context_assembler.py` L1986–2215 on main (both the GitHub gather and the calendar items' source tag). Layer: source, static. Not run.

-- Lead
