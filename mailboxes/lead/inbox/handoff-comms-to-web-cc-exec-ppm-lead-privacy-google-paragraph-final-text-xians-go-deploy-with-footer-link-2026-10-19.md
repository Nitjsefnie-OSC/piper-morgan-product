---
from: comms
to: web
cc: exec, ppm, lead
date: 2026-10-19 15:20 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "/privacy: xian's go (15:2x). The final text is §1 of the draft, as written. Deploy it with a footer Privacy link, then quote the live sentences and the footer href back"
---

Web, cc Exec, PPM, Lead:

xian said "go" on the draft as written (Exec's 15:17 ruling). The final text is §1 of `docs/internal/planning/comms/privacy-google-user-data-draft-2026-10-19.md`. Paste it verbatim, with no rewording. Website file `src/app/(public)/privacy/page.tsx`, under "Your Piper account":

1. **(a) Replace** the "Services you connect" sentence "If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there when you ask." with "If you connect GitHub, Slack or Notion, Piper reads and writes there when you ask. Google Calendar is read-only (see below)." Keep the sentences that follow it (passwords, encrypted access, GitHub disconnect) as they are.
2. **(b) Add** the five-paragraph "Google Calendar." block right after "Services you connect", in the page's existing bold-lead style. The last paragraph links "Google API Services User Data Policy" to https://developers.google.com/terms/api-services-user-data-policy.
3. **(c)** "Last updated" stays "October 2026".
4. **Footer:** add **Privacy → /privacy** to `src/components/Footer.tsx`. It isn't there today. xian's go covers it. Put it wherever reads naturally.

**Please quote back**, from the served page after deploy:
- the replaced sentence;
- the first and last sentences of the Calendar block;
- the Limited Use link's href;
- the footer's Privacy href on the homepage.

PPM ledgers it, and #2087's submission waits on it.

**Lead:** your `has_email` log change (lane 2092) keeps the paragraph true as written ("asks Google … for your Google account's email address"). If the scope is ever dropped or shown in Settings, tell me and I'll bring the one-clause change to xian.

Verified how: Exec's 15:17 ruling read in full; the draft §1 re-read; Lead's 14:49 confirmations read (two scopes, no raw-event writer). The live page last read today at 14:4x (`c8fbb15`).

— Comms
