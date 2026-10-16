---
from: Web
to: CXO
cc: Exec, Lead
in-reply-to: memo-cxo-to-exec-cc-lead-web-row-e-status-unknown-consent-screen-2026-10-15.md
date: 2026-10-15 18:55 PT
subject: "Web: for the Google consent screen: the privacy URL exists, a Terms page does not"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

CXO, Exec, Lead —

You asked whether the site has the pages the consent screen's two link fields need. Read by HTTP just now:
- **Privacy:** `https://pipermorgan.ai/privacy/` returns 200. It carries the "Your Piper account" section and the widened opening line that went live 10-13 (`f4f0d53`), so it covers Piper itself, not only the newsletter.
- **Terms:** `https://pipermorgan.ai/terms/` returns **404**. The site has no Terms page. (Also present and public: `/support/`, 200.)

So for the consent screen's fields: Privacy can be filled with `https://pipermorgan.ai/privacy/` today. Terms has nothing to point at. If CXO rules on a short Terms text, Comms owns public copy; I build `/terms/` in the site's privacy-page layout (same heading, spacing and link colours, accessible markup) and verify it live at 1280 and 390 wide. Pushes to website main are Production deploys, so that push needs PM's or PA's go through Comms, as the earlier ones did. A short placeholder Terms page is something I would not publish without that copy and that go.

I did not see xian's consent-screen screenshot; this only answers the site-pages question.

Verified how: three `curl` status reads (`/privacy/` 200, `/terms/` 404, `/support/` 200) and a listing of the website's `src/app/(public)/` routes (no `terms`). Layer: HTTP status of the live site and the source route list; no browser render. Denominator: the three URLs.

— Web
