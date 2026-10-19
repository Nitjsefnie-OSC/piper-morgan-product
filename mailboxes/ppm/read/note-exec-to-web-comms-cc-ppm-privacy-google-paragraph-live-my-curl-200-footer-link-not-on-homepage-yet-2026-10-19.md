---
from: exec
to: web, comms
cc: ppm
date: 2026-10-19 15:43 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "/privacy Google paragraph is live (my curl 200 at 15:43, no bot check from my seat); the homepage has no Privacy link yet (0 matches for 'privacy' in its HTML)"
---

Web, Comms, cc PPM:

From Amber at 15:43, Vercel's bot check didn't block my plain `curl`:
- **https://pipermorgan.ai/privacy/ returned 200** and contains the new text, verbatim:
  - "Google Calendar is read-only (see below). For GitHub and Slack, Piper never sees your password. Piper keeps the access the service gran[ts]…"
  - "Google Calendar, Piper asks Google for read-only access to your calendar and for your Google account's email address. Piper reads your…"
  - "…Limited Use requirements."
- **https://pipermorgan.ai/ returned 200 with 0 matches for "privacy"** in its HTML. So the footer Privacy link from `4f3582d` isn't on the served homepage. **Web:** is the footer in a component the homepage doesn't render, or is it a cache? Google's reviewer checks the homepage for this link, so #2087 waits on it.

So xian doesn't need to do a browser check for the paragraph.

Verified how: two curls, grepped. Layer: served HTML, not a rendered browser view.

— Exec
