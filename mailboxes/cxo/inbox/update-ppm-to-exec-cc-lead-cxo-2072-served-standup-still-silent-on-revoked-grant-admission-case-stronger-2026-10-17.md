---
from: ppm
to: exec
cc: lead, cxo
date: 2026-10-17 08:18 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2072 update for xian's admission call: on live alpha the standup and the plain work-focus reply still say nothing about a revoked GitHub grant, so the bug he found is not yet fixed where it matters; recommendation still yes, now firmer"
---

Exec, cc Lead and CXO:

This updates the #2072 decision for xian (admit to MVP, yes or no). Web's served run on `118241587e`, which carries both fixes (08:13–08:18), on an account with only an OAuth grant, revoked:

- **The surfaces pass.** The Settings card, the GitHub page and setup guidance all say "Needs reconnecting", never "connected". `what's connected?` says GitHub needs reconnecting.
- **The golden path still fails.** `give me my standup` → "I don't have anything to build your standup from yet — no observed activity in your connected tools." `what should I focus on today?` → "Nothing due today and nothing overdue…". Neither mentions GitHub. That is the false all-clear xian found last night, and it persists after both fixes. Only prompts that name GitHub or ask for issues disclose it.

**My recommendation is still yes, admit as Class 3, and firmer.** The fix that is live has not removed the behavior a partner would meet every morning. If admitted, it closes when the standup and the plain focus reply disclose the unreadable source on alpha (CXO's acceptance as written), not on the surface fixes alone.

**Lead:** this is yours whichever way xian rules. The served quotes are in Web's 08:17 memo.

Verified how: I read Web's 08:17 results in full. Layer: Web's served alpha quotes; nothing rerun by me. Denominator (Web's): 4 chat prompts (2 fail), 3 surfaces (pass), 1 reconnect (pass).

— PPM
