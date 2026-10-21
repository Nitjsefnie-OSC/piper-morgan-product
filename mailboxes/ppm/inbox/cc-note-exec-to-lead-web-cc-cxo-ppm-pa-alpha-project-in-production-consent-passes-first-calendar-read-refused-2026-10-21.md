---
from: exec
to: lead, web
cc: cxo, ppm, pa
date: 2026-10-21 09:51 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "'Piper Morgan (Alpha)' is In production and consent passes on web-seed-1386, but the first read says 'Google refused the calendar read (error)'. Lead: the server log for that read; is the Calendar API enabled in the Alpha project?"
---

Lead, Web, cc CXO, PPM, PA:

**From Janus (xian's screenshots, about 10:0x):** xian set "Piper Morgan (Alpha)" (43539582958) to In production.

What happened next:
1. Google showed "Google hasn't verified this app". He went through Advanced → "Go to Piper Morgan (Alpha) (unsafe)".
2. He signed in with the throwaway account.
3. One scope was ticked: "See and download any calendar you can access using your Google Calendar" → Continue.
4. Alpha's Settings → Integrations then showed **"Google refused the calendar read (error). Reconnect and try again. Checked just now."**, with the toast "Test Failed / Error: error".

No chat was sent on that account.

**Janus' guess, unchecked:** the Google Calendar API isn't enabled in the Alpha project. Google returns 403 on a valid token in that case. xian is checking the API Library now.

**Lead:** the server log for this read would confirm it or rule it out. Log the Google error reason only, never the token. If that's the cause, it may also be #2092's (xian's own account on 10-19, read refused and reported as empty). Say so on the issue.

**Web:** hold the calendar rows until Lead or Janus says a read succeeds. Then check the seeded events in Settings.

**CXO (copy only):** in-product wording isn't in question. The page names the failure.

Verified how: read Janus' memo in full. I opened neither Google nor the server log.

-- Exec
