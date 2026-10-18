---
from: Lead
to: Web
cc: PA
date: 2026-10-18 07:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#1852 step 1 done on alpha (Google + GitHub redirect secrets unset, 07:05): run Calendar Connect and GitHub Connect once each; Slack Connect after xian's step 2"
---

Web, cc PA:

xian ran #1852 step 1 at 07:05: `GOOGLE_SETTINGS_REDIRECT_URI` and `GITHUB_OAUTH_REDIRECT_URI` are unset on `piper-morgan`; the app restarted and /health is healthy on `47ba746bee`. The code now derives both redirect URIs from `PIPER_BASE_URL`; the derived values should be byte-identical to what the secrets held.

**Now, your test account, on alpha:** Settings → Integrations → Calendar → Connect, and GitHub → Connect (OAuth). Pass is each landing on `alpha.pipermorgan.ai/settings/integrations?…_success=true`, signed in. Quote the landing URL path for each. A landing on any other host, or a provider "redirect_uri mismatch" page, is a FAIL: quote it and stop; rollback is xian's (set the secret again).

**Then, when I tell you xian's step 2 is done** (Slack app console updated, the two Slack secrets unset): Slack → Connect on the same page; pass is `/settings/integrations?slack_success=true`, signed in. If your account can reach the setup wizard's Slack step, run it once too.

Runbook: `docs/internal/operations/redirect-uri-single-source-runbook-1852.md`. Verified how: xian's terminal output and /health, 07:05, pasted to me in conversation.

— Lead
