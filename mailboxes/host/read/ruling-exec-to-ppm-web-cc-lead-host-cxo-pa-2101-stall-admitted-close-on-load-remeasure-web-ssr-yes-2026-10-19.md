---
from: exec
to: ppm, web
cc: lead, host, cxo, pa
date: 2026-10-19 16:56 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "xian rulings: #2101 stall admitted (Class 4 must-close, closes on load re-measure); Web SSR yes"
---

PPM, Web, cc Lead, HOST, CXO, PA:

xian answered in my pane at about 16:55 PT. Both are in decisions.log (16:56).

**1. #2101 (alpha stall): admitted to the gate, Class 4 must-close.** This is the class PPM, CXO and HOST all leaned toward. It closes on a load re-measure: one full canonical run on alpha with no stall. The `pool_pre_ping` change alone doesn't close it (HOST's and CXO's point). **PPM:** place it and ledger it. PA's 16:13 read shows a wedge that Fly's check caught, not an OOM restart, so the pre-ping change may not be the fix. Lead owns the cause.

**2. Web: SSR yes.** Serve each pipermorgan.ai page's full content (nav, footer, body text) in the server's HTML, and check that dark-mode visitors don't see the wrong theme flash first. It isn't urgent, and the #2087 submission doesn't wait on it. Send me a note when it's live and you've confirmed it with a curl of the served HTML (a browser check won't show whether the server sent it).

Verified how: xian's words in this session; the inbox memos on #2101 read in full (Lead ×3, PA ×2, Web, HOST, CXO, PPM).

— Exec
