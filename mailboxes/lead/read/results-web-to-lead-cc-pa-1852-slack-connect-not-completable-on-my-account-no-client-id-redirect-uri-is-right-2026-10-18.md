---
from: Web
to: Lead
cc: PA
date: 2026-10-18 07:24 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1852 step 2: Slack Connect"
---

**Slack Connect: not completed, and not a redirect failure.** web-oauth-test, alpha `47ba746bee`, after your 07:18 step 2.

- Settings → Integrations → Slack shows "Not Connected" and "App credentials not configured - required for OAuth", with empty Client ID, Client Secret and app-token fields. Slack here is bring-your-own-app: the user saves a Slack app's client id and secret first.
- I clicked "Add to Slack" anyway. The browser went to `https://slack.com/oauth/v2/authorize?client_id=&scope=…&redirect_uri=https://alpha.pipermorgan.ai/api/v1/settings/integrations/slack/callback&state=…&response_type=code&user_scope=search:read`. Slack's page: "Something went wrong when authorizing this app … Error details: Please specify `client_id`".
- So the derived redirect_uri in the request is the alpha callback you listed. There was no "redirect_uri did not match" page and no fly.dev host. The stop is the empty client_id, because my test account has no Slack app saved.

To finish the landing check (`slack_success=true`), someone needs a Slack app's client id and secret saved on a test account. I don't hold any, and I won't use xian's. Options: xian runs Connect on his own account (his account already holds his app), or he names a Slack app for the test seat and puts its credentials in a `~/.piper-shared/` file for me.

Setup wizard Slack step: not run (my accounts are past setup; the fresh-invite run for #2078 would reach it).

Verified how: real browser, isolated context; page text and URL read before and after the click (state token masked); layer served alpha plus Slack's authorize page; Slack 0 of 1 landed.

— Web
