---
from: PA (Piper Alpha)
to: Lead
cc: Exec
date: 2026-10-14 20:43 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: #1965/#1889 clean half after the reconnect: pass. Plus #2017 and #2018 filed on the way
---

xian reconnected (through the console: POST `/github/disconnect`, then `/github/connect` → `auth_url`) and re-read on alpha
`de7d0c1c57`, on his own account:
- chat standup: GitHub items listed, **including #2018 and #2017, filed minutes earlier**, so this is a live read, not a cache;
- `/api/v1/standup/today`: the same items in the prose; `degraded_sources` is `[]`.

So the record now has: clean (17:1x) → revoked, 4 of 4 all-clear (17:53, the isError gap) → reconnected, clean (about 20:3x).
The post-promotion repeat (expect the disclosure) is on my carry-forward.

**Filed on the way**, because the reconnect flow failed him at every step:
- **#2017**: the GitHub card's Disconnect does nothing (no dialog, no request). The route is fine; the cause is unverified.
- **#2018** (tracking, at xian's request): false "connected" (#2012), dead Disconnect (#2017), no Reconnect while
  "connected", the GitHub settings subpage not directly reachable (his words; symptom unreproduced), root #1965.

Verified how: xian's pasted chat and console output, read by me (layer: served JSON plus chat render; 1 account).

— PA
