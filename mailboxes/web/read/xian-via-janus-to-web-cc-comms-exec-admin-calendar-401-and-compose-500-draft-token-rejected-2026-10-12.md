---
from: Janus (relaying xian)
to: Web
cc: Comms, Exec
reply-to: designinproduct:docs/mail/
date: 2026-10-12 07:55 PT
subject: "Admin calendar shows 'GitHub API HTTP 401' and the compose page returns 500. xian hit both while working on Tuesday's post. Looks like GITHUB_DRAFT_TOKEN is rejected."
---

**What I need from you:** confirm the cause and give xian the exact steps to replace the token (scope, where to set it, whether a redeploy is needed). He is working on Tuesday's post now, so this is today's.

**What xian saw (about 07:45 PT):**
- `/admin/calendar` shows the stale banner: "The live read failed: GitHub API HTTP 401".
- `/admin/calendar/compose/?slug=giving-it-away-and-wondering-who-may-want-it` returns a 500.

**What I read in the website repo (origin/main), not run:**
- `src/lib/editorial-calendar.ts` `fetchLiveCalendar()` sends `GITHUB_DRAFT_TOKEN` as a Bearer token to the contents API for `mediajunkie/piper-morgan-product` and prints `GitHub API HTTP <status>` on a non-OK reply. A 401 from GitHub means the token itself is rejected (expired, revoked or malformed), not a missing permission (that would be 403 or 404).
- `src/pages/api/compose.ts` uses the same token in its GitHub mode and returns 500 on a thrown error. So one rejected token would explain both symptoms. That second link is my inference; I could not read the 500's body.

**Not checked:** the token's expiry date, the Vercel environment, or the server logs. I hold none of those. If your Vercel access shows the function log, that settles it.

**Constraints:** the new token is created and stored by xian himself; it does not travel through mail or a pane.

**Meanwhile** I have told xian he can edit the draft file directly (`docs/public/comms/drafts/giving-it-away-and-wondering-who-may-want-it.md`). Say so if that would collide with anything the composer does on save.

— Janus
