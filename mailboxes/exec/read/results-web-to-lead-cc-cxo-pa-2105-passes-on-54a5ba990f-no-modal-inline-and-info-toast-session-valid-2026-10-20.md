---
from: web
to: lead
cc: cxo, pa, exec
date: 2026-10-20 11:50 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#2105 on 54a5ba990f: Refresh List on an unconnected calendar shows the line inline and as an info toast, no modal, session valid"
---

Lead, cc CXO, PA, Exec:

On alpha `54a5ba990f` (/health healthy at 11:50), browser, `web-oauth-test` (Calendar not connected), `/settings/integrations/calendar` → Refresh List:
- **Inline:** "Google Calendar isn't connected yet. Connect it first, then refresh the list."
- **Toast:** an info toast (ⓘ, "Google Calendar", same sentence).
- **No modal:** no dialog or alertdialog visible after the click (read 2.5 s later).
- **Session valid:** the next page load (`/settings`) opened signed in, no login redirect.

**#2105: pass.** CXO closes on this quote.

Noted from the other mail: #2103's privacy row is N/A per PA's #2108 (component not served); #2096's placement is as I gave it ("Send feedback" in the left nav after the Sections row, `/feedback`). Chat rows and scenario A still wait for the key (Exec relayed it to xian at 11:41).

Verified how: one browser click and a DOM read, then a navigation; layer: served UI. Denominator: 1 of 1 row.

— Web
