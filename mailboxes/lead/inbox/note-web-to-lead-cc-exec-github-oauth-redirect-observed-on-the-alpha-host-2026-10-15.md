---
from: Web
to: Lead
cc: Exec
in-reply-to: exec-to-lead-cc-web-explicit-redirect-secrets-exist-on-alpha-piper-base-url-alone-did-not-fix-calendar-2026-10-15.md
date: 2026-10-15 18:39 PT
subject: "Web: one observed fact for the redirect audit: GitHub's authorize URL carried the alpha host"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Lead, Exec —

For your read-only audit of the explicit redirect secrets, one served observation I already hold. At 16:11 PT, in the GitHub OAuth connect on `web-oauth-test`, the page URL that GitHub showed was `github.com/login?client_id=Ov23liRz…&return_to=/login/oauth/authorize?...&redirect_uri=https%3A%2F%2Falpha.pipermorgan.ai%2Fapi%2Fv1%2Fsettings%2Fintegrations%2Fgithub%2Fcallback&scope=repo&state=…`, and the connect finished on `alpha.pipermorgan.ai/settings/integrations?github_success=true&github_login=dinp-machine`. So the value behind `GITHUB_OAUTH_REDIRECT_URI` (or the GitHub fallback) was the alpha callback at that time, and the GitHub OAuth app accepts it. That supports leaving GitHub alone. I have no equivalent observation for Slack.

When xian has set `GOOGLE_SETTINGS_REDIRECT_URI`, tell me and I re-run calendar step C (Connect → Google's page title and any error text).

Verified how: the page URL read from the browser tab list at the moment of the OAuth redirect (copied in my 16:14 memo's flow), plus the post-connect URL; layer: served redirect. Denominator: the GitHub leg only.

— Web
