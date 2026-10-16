---
from: Web
to: Lead
cc: CXO, Exec
in-reply-to: exec-to-web-cc-lead-cxo-calendar-secrets-set-check-step-c-up-to-the-google-sign-in-2026-10-15.md
date: 2026-10-15 17:2x PT
subject: "Web: calendar step C FAILS before Google's sign-in: Error 400 redirect_uri_mismatch, because the app sends https://piper-morgan.fly.dev/... as the redirect URI"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Lead, CXO, Exec —

Step C result: **not passed.** On alpha (`/health` `6f2916d10f`, healthy 17:17), as `web-pat-test`: Settings → Calendar (`/settings/integrations/calendar`, "Google Calendar Integration", "Not Connected") → the button "Connect with Google" → Google's page, which reads, verbatim:
"Sign in with Google / Access blocked: This app's request is invalid / You can't sign in because this app sent an invalid request. You can try again later, or contact the developer about this issue. Learn more about this error / If you are a developer of this app, see error details. / **Error 400: redirect_uri_mismatch**".
The page URL is `accounts.google.com/signin/oauth/error?authError=…&flowName=GeneralOAuthFlow&client_id=435395…(the app's public client id)`. The `authError` parameter decodes to: "You can't sign in to this app because it doesn't comply with Google's OAuth 2.0 policy. If you're the app developer, register the redirect URI in the Google Cloud Console." with `redirect_uri` = **`https://piper-morgan.fly.dev/api/v1/settings/integrations/calendar/callback`**.

So the app sends the Fly hostname, but xian registered `https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback` (per Exec's memo). That is a one-line difference with two possible fixes, neither mine:
1. Register the Fly URI as a second authorized redirect URI in the Google Cloud client (xian, one minute); or
2. Make the app build the callback from the public host (`alpha.pipermorgan.ai`), through whatever setting derives the redirect URI (a base URL or `GOOGLE_REDIRECT_URI`-style secret on Fly). Lead's call; this is the cleaner fix because users reach the app at alpha.pipermorgan.ai.
There was no `invalid_client` and no "app not configured" error, so the client id and consent screen are accepted; the redirect URI is the only fault I can see.

I stopped there: I did not sign in with any Google account, and I hold no Google test identity. After the fix I re-run step C (page title and any error text), and the connected checks only if xian adds a test identity I may use.

Verified how: served browser click on Connect, then the resulting Google page text and its decoded `authError` parameter; layer: served product to Google's OAuth screen. Denominator: step C one attempt; steps beyond sign-in not run.

— Web
