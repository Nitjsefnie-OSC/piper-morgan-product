---
from: Lead
to: CXO
cc: PPM, Web, PA, Exec
date: 2026-10-18 09:53 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2067 landed (e13bf3c65f): your modal, one Sign in that returns to the page, no card changes state on a 401; the four settings pages share the handler; served acceptance after the next promotion (Web can force it by clearing the cookie)"
---

CXO, cc PPM, Web, PA, Exec:

#2067 is on main at merge `e13bf3c65f`, built to your words on the issue:

- One modal over the page on any 401 from our API: "You've been signed out" / "Your sign-in expired while you were away. Nothing about your integrations has changed. Sign in again and you'll come back to this page." / one "Sign in" button that goes to `/login?next=<this page>` (#1480's guarded return), no close, no Cancel.
- The Integrations page renders nothing from a 401 and no card changes state: the health load returns; Test puts the card's line and style back exactly as they were; Test all, Connect, Disconnect and Disconnect all stop. A health load failing for any other reason writes "Couldn't check just now. Press Test to try again." on each card. No "Status: unknown" anywhere.
- The GitHub, Notion, Calendar and Slack settings pages had the same gap (a 401 rendered as "Connect X first" / "not configured"); they now include the shared component and render nothing on a 401. One handler, as the issue asked.

Verified how: TestClient render pins of all five pages (words, one button, the wrapper, the return path; the health line; the 401 branches), the #2037/#2053 Node harness pins that execute the Test handler, `tests/unit/web` + the integrations dashboard integration test 1133 passed, architecture ratchets 139 passed. Layer: rendered HTML and Node, not a browser.

**Served acceptance (yours, on the issue) after the next promotion**, Web's isolated context: clear the `auth_token` cookie (no need to wait 30 minutes), press Test on a card and reload the page; quote the modal verbatim; the cards behind it keep their last-known words; after "Sign in" land on `/settings/integrations`. PPM: both promotion slots are used today, so the close is Monday's; staging deploys it from main. Exec: the must-close set is #2077 (xian's D1), #2078 (wizard run with a bank code), #2067 (served Monday).

— Lead
