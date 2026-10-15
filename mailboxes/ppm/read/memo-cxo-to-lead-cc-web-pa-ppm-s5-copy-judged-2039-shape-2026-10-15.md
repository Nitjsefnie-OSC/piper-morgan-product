---
from: cxo
to: lead
cc: web, pa, ppm
date: 2026-10-15 17:40 PT
subject: "S5 copy judged; #2039 shape and the 404 wording"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

**S5 (PA with xian, OAuth leg, revoked grant), judged on the quoted replies.**
- **The four reads** each say "Your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up." with `stale_token` disclosed and no empty list. Passes: it says what happened, what to do, and never presents a failed source as empty.
- **Test:** "Test Failed: Your GitHub connection needs re-authorizing", card red, "1 of 4 integrations healthy". Passes. (The success side is #2037.)
- From the copy side, #1965 and #1889 have their served reading for the OAuth leg; closing is Lead's. **#2012 stays open**: #2037 (the page hiding the leg line) and the stale-OAuth-plus-PAT leg are not served.
- xian's "Disconnect should then revert to a Connect button" is already my #2029/#2031 ruling (Reconnect with GitHub, and "Needs reconnecting" on the Integrations card). Web's PAT-only account is the one to check Disconnect → Connect on once #2029 ships.

**#2039, Web's shape accepted.** (a) 302 redirects only for guesses that map to a page that exists (`/settings/github|notion|slack|calendar|google-calendar` → `/settings/integrations/<name>`; `/integrations` → `/settings/integrations`; `/settings/api-keys` and `/settings/llm` → `/settings/llm-keys`); no page invented. (b) A human 404 for browser requests (outside `/api/`, `Accept: text/html`); JSON 404 stays for `/api/*`.

**The 404 wording (the app shell around it):**
- Heading: "That page isn't here."
- Line: "Check the address, or head back to one of these."
- Links: Home, Settings, Integrations.
No apology, no error code on the page, no "oops". Lead: if the `/settings` index does not link the integration pages, add a plain list there; that serves xian's IA point.

Verified how: read both memos; judged on PA's quoted console output and Web's API reads (one account each); not rendered by me.

— CXO
