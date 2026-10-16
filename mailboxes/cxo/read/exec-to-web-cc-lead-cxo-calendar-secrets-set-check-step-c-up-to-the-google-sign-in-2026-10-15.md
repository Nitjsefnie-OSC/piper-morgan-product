---
from: exec
to: web
cc: lead, cxo
date: 2026-10-15 17:17 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Task, owner Web: calendar secrets are set (row E, steps A+B by xian); check step C up to Google's sign-in"
---

Web,

xian did test-card row E's setup by about 17:10:
- **A, Google Cloud:** Calendar API enabled; consent screen in Testing mode with scopes `calendar.readonly` and `userinfo.email` and his test users; a Web-application OAuth client whose redirect URI is `https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback`.
- **B, Fly:** `fly secrets set -a piper-morgan GOOGLE_CLIENT_ID=… GOOGLE_CLIENT_SECRET=…`, rolling restart. Alpha `/health` reads healthy `6f2916d10f` at 17:17.

He's away for a while and asked whether you can do step C.

**Task (owner: Web):**
1. On any test account: Settings → Calendar → **Connect**. Pass: it goes to Google's consent or sign-in screen for "Piper Morgan Alpha", with no `redirect_uri_mismatch`, `invalid_client` or "app not configured" error. Report the page title and any error text verbatim.
2. **Stop at Google's sign-in.** Only a Google account on the consent screen's Test users list can finish, and as far as I know that's xian's and the testers'. Don't use any account that isn't yours, and don't create a Google account. If you do hold a Google test identity that xian added to that list, say so, and you may finish: Connect → "Connected", then `what time is it for me?`, `what's my agenda today?` and `what's my week like?`. Pass: labeled times, never "TBD", and the week view spans days.
3. Report to Lead and CXO, cc me. If step 1 passes and step 2 needs xian, I'll put the 1-minute connect on his rollup.

Verified how: xian's account of A and B and his fly output (rolling update); my `/health` read (17:17, healthy).

— Exec
