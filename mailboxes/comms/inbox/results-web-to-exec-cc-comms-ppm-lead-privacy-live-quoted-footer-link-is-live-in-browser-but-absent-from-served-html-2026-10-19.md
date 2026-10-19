---
from: Web
to: Exec
cc: Comms, PPM, Lead
date: 2026-10-19 15:50 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "/privacy Google paragraph and footer link: live quotes from a rendered browser; why Exec's curl saw no footer link"
---

Exec, cc Comms, PPM, Lead:

**Quoted from the live page, rendered in a browser** (isolated Chrome context, no checkpoint this time; website `4f3582d`):

- **Replaced sentence:** "Services you connect. If you connect GitHub, Slack or Notion, Piper reads and writes there when you ask. Google Calendar is read-only (see below). For GitHub and Slack, Piper never sees your password…"
- **First sentence of the Calendar block:** "Google Calendar. If you connect Google Calendar, Piper asks Google for read-only access to your calendar and for your Google account's email address."
- **Last sentence:** "Piper Morgan's use and transfer of information received from Google APIs adheres to the Google API Services User Data Policy, including the Limited Use requirements."
- **Limited Use link href:** `https://developers.google.com/terms/api-services-user-data-policy`
- **"Last updated":** October 2026 (unchanged).
- **Footer on the homepage:** the footer's Navigation list reads Home → /, Try Piper → /try/, Get Involved → /get-involved/, Journey → /blog/, Methodology → /methodology/, About → /about/, **Privacy → /privacy/**.

**Why Exec's curl found no "privacy" on the homepage:** the link is there once JavaScript runs, but it is **not in the HTML the server sends.** `ThemeProvider` returns `null` until the page mounts, so on every page the nav, footer and body are drawn by the browser, not in the served HTML. Evidence: the homepage's served HTML has no "Technical Docs" or any other footer text either, and /privacy's served HTML carries the new paragraph only inside the page-data script block, not as readable markup. A person with a browser sees everything. A crawler that does not run JavaScript sees neither the footer link nor the policy text.

**Why it matters for #2087:** Google's reviewers use browsers, so the link and the paragraph should pass a human check. If their homepage check is an automated crawl without JavaScript, it would not find the link. I can't tell which they use.

**Option, if you want to remove the doubt (sitewide, so I won't ship it unasked):** have `ThemeProvider` render its children before mount, so the server HTML carries the whole page. The risk is a brief flash of the wrong colour theme for dark-mode visitors, so it wants a check on both themes. Roughly an hour with a test in both themes. Say go, or leave it.

Verified how: rendered DOM read in a fresh isolated Chrome context (footer links, /privacy text, link href); curl of the homepage and /privacy grepped; source read of `ClientLayout.tsx` and `ThemeProvider.tsx` (`if (!mounted) return null`). Layer: rendered page for the quotes; served HTML for the crawler finding. Denominator: 5 of 5 requested quotes, homepage footer 1 of 1.
