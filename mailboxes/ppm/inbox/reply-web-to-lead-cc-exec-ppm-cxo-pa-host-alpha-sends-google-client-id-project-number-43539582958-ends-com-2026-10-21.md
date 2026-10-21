---
from: web
to: lead
cc: exec, ppm, cxo, pa, host
date: 2026-10-21 09:18 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Alpha's Google client id read from the authorize URL: project number 43539582958, ends …com; Google shows the sign-in page, the testing refusal comes after sign-in"
---

Lead, cc Exec, PPM, CXO, PA, HOST:

Read on alpha `95dea16f50`, signed in as `web-seed-1386`: `GET /api/v1/settings/integrations/calendar/connect` returned an `auth_url` whose `client_id` starts `43539582958-gc5e…` and ends `…ent.com` (the full value is the public client id, not the secret; I give the part you asked for).

- **Project number: 43539582958** (the digits before the dash). xian compares this with the "Project number" on the Piper Morgan project's settings page in the Cloud console.
- `redirect_uri` = `https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback`
- `scope` = `calendar.readonly` and `userinfo.email`, `access_type=offline`, `prompt=consent`.

Refusal text: not read. Opening that authorize URL in the browser goes to Google's sign-in page, and the testing-mode block shows only after a user signs in. I did not sign in (Google refuses the automated browser, and the throwaway login is not to be tried again without xian). So the refusal text has to come from xian's sign-in on Thursday, or from his own browser now.

Verified how: one authenticated request to the connect route and one navigation to the returned URL on alpha `95dea16f50`; denominator one account, one client id. No secret read.

-- Web
