# Google Cloud project map and the one-project end state (#2087)

**Owner:** Lead (map); **decision:** xian. **Written:** 2026-10-22 from source on main and the console facts relayed 10-21 (Janus via Exec, Web's read of the authorize URL). No secret values were read; client ids are named by project only.

## 1. What Piper uses Google for

Only **Google Calendar** (read-only). Source has no Google sign-in, no Gmail or Drive client, and no other Google API. `accounts.google.com` appears only in the Calendar OAuth handler.

| Piece | How it picks its Google client | Where that client lives |
|---|---|---|
| Calendar connect from the setup wizard | `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` env (alpha: Fly secrets); fallback `IntegrationConfigService.get_google_client_id()` (local config) | **"Piper Morgan (Alpha)"**, project 43539582958 (Web read the authorize URL's `client_id`, 10-21 09:18) |
| Calendar connect from Settings → Integrations | same handler, same env | same |
| Token refresh and every calendar read | `google_calendar_adapter` builds credentials from the same `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` env | same |
| Calendar API (the service the reads call) | enabled per project | **enabled in "Piper Morgan (Alpha)"** by xian, 10-21 (the cause of #2092's false empty) |
| Legacy single-user env leg | `GOOGLE_CALENDAR_CREDENTIALS`, `GOOGLE_CLIENT_SECRETS_FILE`, `GOOGLE_TOKEN_FILE` (local development) | not a per-user connection; `integration_status_service` reports it as `via=env` |
| Branding, domain verification (`pipermorgan.ai`), data-access (scope) submission (#2087) | n/a (console work) | **"Piper Morgan"**, project 538609082609, Design in Product account |

**OAuth parameters alpha sends** (source, confirmed by Web 10-21): scopes `calendar.readonly` and `userinfo.email`; offline access; consent prompt. Redirect URIs: `{PIPER_BASE_URL}/api/v1/setup/calendar/oauth/callback` (override `GOOGLE_CALENDAR_REDIRECT_URI`) and `{PIPER_BASE_URL}/api/v1/settings/integrations/calendar/callback` (override `GOOGLE_SETTINGS_REDIRECT_URI`); alpha's base is `https://alpha.pipermorgan.ai`.

**Audience (console, relayed):** "Piper Morgan": In production, External. "Piper Morgan (Alpha)": set In production by xian 10-21 (was Testing, which caused the 7-day token expiry and the 100-user allowlist). Both unverified, so partners see "Google hasn't verified this app" and a 100-user cap applies.

**Unverified by me:** staging's and production's `GOOGLE_CLIENT_ID` (secrets I can't read); whether any other client exists in either project.

## 2. Why it matters

Verification is **per project**. All of #2087's verification work sits in "Piper Morgan", which serves no client alpha uses. If that verification completes, partners connecting on alpha still see the unverified screen for the Alpha project's client, and the consent screen still names "Piper Morgan (Alpha)". Comms' Calendar line quotes that name ("Go to Piper Morgan (Alpha) (unsafe)") and is marked "recheck at send" for exactly this reason.

## 3. The one-project end state: options

**(A) Move alpha to a new OAuth client in "Piper Morgan" (538609082609).** *Recommended.*
- Steps (xian's console, then one attended secret set):
  1. In "Piper Morgan": enable the Google Calendar API; create an OAuth client (type Web application) with the two redirect URIs above on `https://alpha.pipermorgan.ai`.
  2. Set alpha's `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` Fly secrets to the new client, generated and piped so nothing prints (HOST or PA with xian present; the app restarts once).
  3. Everyone with a connected calendar reconnects once (refresh tokens are bound to the client that issued them). Today that is the test accounts and xian.
  4. Retire the Alpha client (or the whole Alpha project) after a week of clean connects.
- **For:** the verification work already lives there; one account owns brand, domain and scopes; once verified, the consent screen says "Piper Morgan". Moving now costs only test reconnects; after partners join, every partner reconnects.
- **Against:** an attended secret change and a restart; the project belongs to the Design in Product account, so the app's Google identity sits with that business (xian's call whether that is the right owner).

**(B) Keep the Alpha project and redo verification there.**
- **For:** no secret change, no reconnects.
- **Against:** branding, the `pipermorgan.ai` domain proof (Search Console ownership under the Piper Morgan account) and the data-access submission start over, and the review clock restarts; two projects remain unless "Piper Morgan" is deleted.

**(C) Leave both as they are.** Not an end state: verification in "Piper Morgan" never reaches alpha's users.

## 4. Recommendation

**(A), before 10-30**, because the reconnect cost is lowest now. Verification does not need to finish first: the submission stays in "Piper Morgan" and applies to the new client when approved. After the switch, HOST's send check reads the consent screen's app name on the morning of any invitation, and Comms' line changes from "Piper Morgan (Alpha)" to whatever the served screen shows.

**Lead's part if xian picks (A):** none in code (the client is env-driven); I verify after the switch that both connect paths complete on a test account and that a calendar read returns events, and I post the result on #2087.
