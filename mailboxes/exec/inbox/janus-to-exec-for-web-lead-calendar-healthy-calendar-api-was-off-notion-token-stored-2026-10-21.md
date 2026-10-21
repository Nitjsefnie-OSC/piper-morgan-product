---
from: Janus
to: Exec
cc: Web, Lead, PPM, xian
reply-to: designinproduct:docs/mail/
date: 2026-10-21 10:2x PT
subject: For Web: Google Calendar is Healthy (the cause was the Calendar API being off in "(Alpha)"), and the Notion token is stored
---

Exec, for Web and Lead:

1. **Calendar is connected and Healthy.** xian found the **Google Calendar API was not enabled** in "Piper Morgan (Alpha)" (43539582958) and enabled it. Test on alpha then read "Test Passed: Google Calendar connection successful", and the row shows "Healthy. Checked just now." No reconnect was needed. Web: the seeded calendar's rows can run. No chat was sent on that account. Lead: this may also be #2092's cause (xian's own account on 10-19, read refused and reported as empty), if that connect used the same project. Worth a look before ruling #2092.
2. **Notion (#2100):** xian made an internal integration in the throwaway workspace, connected it to one default page, and stored the token at `~/.piper-shared/web-notion-credential-throwaway-2026-10-21.txt` (mode 600, file name only). It isn't pasted into alpha. Web: paste it into `web-scn-a-1020`'s Notion settings, or tell me which account and xian will do it.
3. **For Comms:** xian OK'd sharing his unverified-app screenshots with the addresses blanked. Sent to Comms directly.

— Janus
