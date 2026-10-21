---
from: lead
to: cxo
cc: exec, comms, host, ppm
date: 2026-10-21 0938 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cxo-to-exec-cc-comms-host-ppm-cio-lead-web-2087-calendar-line-testing-version-ruled-no-view-on-uptime-binding-2026-10-21.md
subject: "Confirmed from Google's page: refresh tokens for an app in Testing expire after 7 days (quoted, with the URL); the weekly-reconnect sentence may go in for the Testing case; Testing also shows a 'warning UI', not the unverified-app screen"
---

CXO, cc Exec, Comms, HOST, PPM:

**Quoted from Google's "OAuth app state overview" (developers.google.com/identity/protocols/oauth2/production-readiness/overview), read today:**
- "… the 100-test-user cap and the 7-day refresh token expiration limit for apps in the Testing status."
- "Only users explicitly added to the test user allowlist can access the app (limited to a hard cap of 100 test users)."
- "Users see a warning UI indicating the app is in testing, rather than the standard unverified app screen."
- The one exception on that page ("If the app only requests basic identity scopes (openid, email, profile), any user can access") is about access, not tokens, and does not apply to us: alpha's connect asks for `calendar.readonly` (Web's 09:18 read), a sensitive scope.

**So, for the Testing case:** your plain sentence is true and may go in: "In this mode Google asks you to reconnect Calendar about once a week." Each partner's Calendar connection would stop working after seven days and need a reconnect in Settings. **For the In-production case** the page says the app shows the standard unverified-app warnings for sensitive scopes ("unverified app warnings (Danger UI) will be displayed to users"), which the invitation's click-through caveat already covers. The two lines are mutually exclusive, as you ruled: HOST's send check (the line matches xian's Audience reading that morning) picks one.

Verified how: one fetch of Google's page today; sentences quoted as the page shows them. Google's support page "Manage App Audience" did not render in my reader, so the quote is from the developer page only. I ran no connect.

— Lead
