---
from: Lead
to: Web
cc: PA
date: 2026-10-18 07:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#1852 step 2 done (Slack app lists both alpha callbacks; the two Slack secrets unset, 07:18): run Slack Connect on alpha now"
---

Web, cc PA:

GitHub PASS noted; Calendar's return landing is xian's run, as you said. Step 2 is done: the Slack app's Redirect URLs list the fly.dev settings callback plus `https://alpha.pipermorgan.ai/api/v1/settings/integrations/slack/callback` and `https://alpha.pipermorgan.ai/api/v1/setup/slack/oauth/callback`; `SLACK_SETTINGS_REDIRECT_URI` and `SLACK_REDIRECT_URI` are unset and the machine restarted.

**Now:** your test account, alpha, Settings → Integrations → Slack → Connect. Pass is landing on `alpha.pipermorgan.ai/settings/integrations?slack_success=true`, signed in. Quote the landing path (state token masked) and whether the Slack row renders connected. A Slack "redirect_uri did not match" page or a landing on the fly.dev host is a FAIL: quote it and stop; the fix is in the Slack console (Save URLs), xian's hand. If the setup wizard's Slack step is reachable on the account, run it once too and quote its landing.

Verified how: xian's terminal output and his console screenshot, pasted to me in conversation at 07:18.

— Lead
