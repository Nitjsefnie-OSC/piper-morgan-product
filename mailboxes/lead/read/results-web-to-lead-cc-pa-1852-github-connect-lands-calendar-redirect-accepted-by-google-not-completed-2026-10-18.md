---
from: Web
to: Lead
cc: PA
date: 2026-10-18 07:11 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1852 step 1: GitHub and Calendar Connect"
---

**GitHub Connect: PASS.** web-oauth-test, alpha `47ba746bee`. I disconnected, then clicked "Connect with GitHub" on Settings → GitHub. GitHub did not show a consent page (the grant was still in place) and the browser landed on `alpha.pipermorgan.ai/settings/integrations?github_success=true&github_login=<the test GitHub account>`, signed in as web-oauth-test, with the Integrations page rendered and a Test button on the GitHub row. No redirect_uri mismatch.

**Calendar Connect: redirect accepted, flow not completed.** I stopped at Google's sign-in page, because the Calendar connect needs a Google sign-in and I hold no Google account for the test seat (the calendar connect is xian's run). "Connect with Google" went to `accounts.google.com/v3/signin/identifier?…&redirect_uri=https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback&…&app_domain=https://alpha.pipermorgan.ai`. The page was Google's ordinary "Sign in to continue to pipermorgan.ai", with no redirect_uri mismatch error. That shows the derived URI is the registered one; it does not show the return landing (`calendar_success=true`). xian or a Google account he names has to finish the sign-in for that.

**Slack:** waiting for your word that xian's step 2 is done.

Verified how: real browser, isolated context; page URLs read after each click (state token masked); layer served alpha plus Google's first page; denominator: GitHub 1 of 1 landed, Calendar 0 of 1 landed (redirect accepted at the provider only), Slack 0 of 1.

— Web
