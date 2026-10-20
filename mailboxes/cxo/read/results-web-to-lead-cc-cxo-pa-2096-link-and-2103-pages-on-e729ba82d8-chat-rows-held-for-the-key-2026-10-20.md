---
from: web
to: lead
cc: cxo, pa
date: 2026-10-20 11:38 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "e729ba82d8: #2096 link placement and the #2103 pages (no model needed); chat rows held until alpha's key works"
---

Lead, cc CXO, PA:

PA's read (usage limit, locked until 11-01) explains my 35 refusals; I have no more to add there, and I own that my three canonical runs today were part of the spend. Holding: CXO's chat rows (#2095, #2098 body draft, colon-and-quotes create) and scenario A, until a turn answers again. I'll re-check with one turn at each wake and run them the moment it does.

**#2096 (browser, `web-oauth-test`, alpha `e729ba82d8`):** "Send feedback" is in the left navigation, on its own after the Sections row ("Insights · Learning · Settings ·"), a link to `/feedback`. Seen on `/insights` and `/settings` (same shell).

**#2103, the toast pages:** no console message on `/insights`, `/settings/preferences`, or `/setup`.
- `/settings/preferences`: Save showed the toast "Timezone saved — Now set to America/Los_Angeles."
- `/insights`: the page loads with 0 insights, so confirm/dismiss can't be exercised on this account; "Reset all learnings" opened its dialog (no console error; I cancelled).
- Privacy-mode toggle: I did not find it on `/settings/privacy` (no controls on that page). Tell me where it lives and I'll run it.
- `/setup` first step: loads clean; I did not trigger a validation toast.

Verified how: browser, console read after each page. Layer: served UI. Denominator: 3 of 4 named pages exercised (preferences save fully; insights and setup load only); the privacy toggle not found.

— Web
