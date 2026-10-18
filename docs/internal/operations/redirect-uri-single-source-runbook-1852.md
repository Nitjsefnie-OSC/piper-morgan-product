# Redirect URIs from one source: `PIPER_BASE_URL` (#1852 runbook)

**Owner of every step: xian** (each step is `fly secrets` or a provider console; agent seats are denied both).
**Approved:** xian, 2026-10-18 in conversation with Lead ("your proposal makes sense"). Lead wrote the proposal on #1852 (comment of 2026-10-15) and this page turns it into commands.

## What this does

Four redirect URIs are set by hand as Fly secrets. The code already derives each one from `PIPER_BASE_URL` when the secret is absent, and `PIPER_BASE_URL` is the alpha host. After this runbook the base URL is the only place a host lives; a future host move is one secret plus the provider consoles.

| Secret | Code fallback when unset | Provider console must list |
|---|---|---|
| `GOOGLE_SETTINGS_REDIRECT_URI` | `{PIPER_BASE_URL}/api/v1/settings/integrations/google/callback` (`settings_integrations.py`) | already lists it (xian set it to this value on 10-15) |
| `GITHUB_OAUTH_REDIRECT_URI` | `{PIPER_BASE_URL}/api/v1/settings/integrations/github/callback` (#2043, on alpha since `118241587e`) | already lists it (the alpha OAuth app, cutover 09-22) |
| `SLACK_SETTINGS_REDIRECT_URI` | `{PIPER_BASE_URL}/api/v1/settings/integrations/slack/callback` (`settings_integrations.py:377`) | **not yet**: the Slack app lists the fly.dev URL |
| `SLACK_REDIRECT_URI` (also the wizard's fallback) | settings: as above; wizard: `{PIPER_BASE_URL}/api/v1/setup/slack/oauth/callback` (`setup.py:1325`) | **not yet** |

Every `fly secrets unset` restarts the app once. Batch the names in one command where the steps allow.

## Step 1. Google and GitHub, any time (no observable change)

Both derived values are byte-identical to the secrets' current values, so nothing a user sees changes and no console changes.

```
fly secrets unset -a piper-morgan GOOGLE_SETTINGS_REDIRECT_URI GITHUB_OAUTH_REDIRECT_URI
```

**Check** (anyone, after the restart): `curl -s https://alpha.pipermorgan.ai/health` healthy; then Web runs Calendar Connect and GitHub Connect on alpha once each and reports the landing page (`/settings/integrations?…_success=true`, signed in).

## Step 2. Slack, in this order (the fix this issue asks for)

1. **Slack app console** → *OAuth & Permissions* → *Redirect URLs*: **add** both, keep the existing fly.dev entry for now, Save:
   - `https://alpha.pipermorgan.ai/api/v1/settings/integrations/slack/callback`
   - `https://alpha.pipermorgan.ai/api/v1/setup/slack/oauth/callback`
2. **Unset the two Slack secrets** (one restart):
   ```
   fly secrets unset -a piper-morgan SLACK_SETTINGS_REDIRECT_URI SLACK_REDIRECT_URI
   ```
3. **Served check** (Web, on alpha, Web's test account): Settings → Integrations → Slack → Connect; pass is landing on `alpha.pipermorgan.ai/settings/integrations?slack_success=true`, signed in. If the Slack wizard is reachable on the account, run its Slack step once too (it now sends the setup callback path, which the old shared secret got wrong).
4. **Remove** the `https://piper-morgan.fly.dev/api/v1/settings/integrations/slack/callback` entry from the Slack app's Redirect URLs.
5. **Docs** (Lead or Docs): `docs/SLACK_APP_SETUP.html` line 228 shows the fly.dev callback as the URL to register; replace it with the alpha settings callback and add the setup callback.

## Step 3. Record

- Comment on #1852 with the date of each step and Web's landing quotes; close #1852 when step 2.3 passes (`close-issue-properly`).
- The cutover runbook's §9b "pending provider registrations" entry for Slack is then done; note it there.

## If something goes wrong

- A Slack Connect that lands on the fly.dev host or a Slack "redirect_uri did not match" error means step 2.1 did not save or step 2.2 ran before it. Re-add the URLs in the console; no secret needs to come back.
- Rollback for any provider is to set the secret again to the alpha URL (`fly secrets set -a piper-morgan NAME=https://alpha.pipermorgan.ai/api/v1/...`); the values are in this table, not bearer credentials.

Verified how (Lead, 2026-10-18): fallbacks re-read from source on main (`web/api/routes/settings_integrations.py`, `web/api/routes/setup.py`, `web/api/routes/settings_integrations.py` GitHub handler at #2043); the Slack console's current Redirect URLs are xian's read, not mine.
