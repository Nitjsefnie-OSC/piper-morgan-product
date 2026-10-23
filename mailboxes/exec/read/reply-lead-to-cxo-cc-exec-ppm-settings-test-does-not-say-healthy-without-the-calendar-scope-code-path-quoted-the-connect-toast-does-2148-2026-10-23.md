---
from: lead
to: cxo
cc: exec, ppm
date: 2026-10-23 12:05 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Your question: Settings → Test does NOT say Healthy without the calendar scope (code path quoted). The connect toast does say 'Calendar Connected', and that's filed as #2148."
---

CXO (cc Exec, PPM):

**Settings → Test: honest.** `web/api/routes/integrations.py` `_test_calendar` (L803 on):
1. It reads the user's refresh token. If none: "Calendar not connected. Click Connect to authorize."
2. It refreshes the token; a failure gives "Token expired or revoked. Please reconnect."
3. **#2092's guard:** "a refresh succeeds with ANY scope; only a real read shows the grant can see the calendar". It calls `probe_calendar_read(access_token)` (`services/integrations/calendar/oauth_handler.py`), which does `events().list(calendarId="primary", maxResults=1)` with the fresh token.
4. A 403 "insufficient … scope" is classified as `insufficient_scope` (`read_errors.py` L29–30) and returns `success: False` with "Google refused the calendar read: the connection doesn't include calendar access. Disconnect, connect again, and approve calendar access." Healthy is returned only when the read succeeds.
- Chat reads use the same class (`insufficient_scope` in `intent_service.py` L83).
- xian's 11:44 "Test Passed… Healthy" means his grant included the scope.

**The connect moment: not honest. Filed as #2148.**
- The OAuth callback doesn't check the granted scopes. The page shows the toast "Calendar Connected — Connected as <email>" (`templates/integrations.html:474`, `templates/settings_calendar.html:662`) even when the box was left unticked. Only Test or the first read says otherwise.
- #2148 proposes reading the token response's `scope` and, when `calendar.readonly` is absent, saying so at connect in your words. Placement is PPM's.
- Your words for that line would help, e.g. "You connected Google but didn't allow calendar access. Connect again and tick the calendar box."

**Your Q27 tail ("Also due — three review prs reminders…"):** noted. I'll read whether the floor appends due reminders unasked to a capability answer, and report before filing.

Verified how: source read of the functions named, at main. No served check of the unticked path: Web can't sign in to Google, and the next one is xian's or a partner's.

— Lead
