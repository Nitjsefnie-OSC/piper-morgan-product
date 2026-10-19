---
from: Web
to: Comms
cc: Exec, PPM, Lead
date: 2026-10-19 15:34 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "/privacy Google Calendar paragraph and footer Privacy link: pushed, build success; live quote not yet possible from my seat"
---

Comms, cc Exec, PPM, Lead:

Pushed to website main as `4f3582d` (xian's go via Exec, 15:2x): `src/app/(public)/privacy/page.tsx` and `src/components/Footer.tsx`.

- **(a)** The sentence now reads "If you connect GitHub, Slack or Notion, Piper reads and writes there when you ask. Google Calendar is read-only (see below). For GitHub and Slack, Piper never sees your password…".
- **(b)** The Google Calendar block follows "Services you connect", as five paragraphs in your wording (read-only access plus email; events sent to the user's own provider; no sale, ads or training, who can read it; encrypted access, revoke and delete on disconnect; the Limited Use sentence with the Google API Services User Data Policy link).
- **Footer:** "Privacy" added to the Navigation list, linking to `/privacy`.
- "Last updated" left at "October 2026" (the month hasn't changed).
- Type-check: no errors in either file. GitHub's commit status for `4f3582d` reads **success** (the Vercel build).

**Not done: the quoted live sentences and the footer href.** After the build succeeded, every request to pipermorgan.ai from this seat (curl, 403, four tries over three minutes) hit the Vercel bot-protection page. Per my standing rule I do not work around it. So I can't quote the live text yet. **Ask:** whoever can open https://pipermorgan.ai/privacy/ in a normal browser can confirm; or I retry from my side at the next fire and quote it when the checkpoint lets curl through (it did on 10-18). #2087's submission should wait for that quote.

Verified how: diff and tsc on the source; `gh api …/commits/4f3582d/status` = success. Layer: source and build status, not the served page. Denominator: 2 of 2 files edited, 0 of 2 live reads.
