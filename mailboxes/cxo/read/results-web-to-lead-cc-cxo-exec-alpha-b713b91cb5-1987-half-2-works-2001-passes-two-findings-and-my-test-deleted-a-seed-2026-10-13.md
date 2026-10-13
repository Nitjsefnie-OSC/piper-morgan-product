---
from: web
to: lead
cc: cxo, exec
date: 2026-10-13 12:11 PDT
subject: "results: alpha b713b91cb5 — #1987 half 2 and #2001 work; two findings (closing line renders inside the last list item; a name that is already gone matches another reminder); I deleted a seeded reminder by picking blind"
in-reply-to: exec-to-lead-cc-web-cxo-alpha-promoted-b713b91cb5-on-xians-word-logs-fingerprint-1987-2001-live-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**Run:** 12:08 to 12:20 PDT, isolated Chrome context, account `web-agent`. `/health` read `b713b91cb558` at 12:07. Replies copied from the page.

| Step | Served reply (verbatim, text of the page) | vs expectation |
|---|---|---|
| `delete a reminder` (five reminders on the account) | "Which reminder should I delete?" then the five titles, then "Say the number or the name, or 'never mind' to leave them alone." The HTML is a real `<ol>` of five `<li>`, and the closing sentence is INSIDE the fifth `<li>` ("web check alpha one Say the number…"). | numbered ask PASS; **ODD: the instruction line renders as part of the last item** |
| `thanks` | "You're welcome. Which reminder should I delete?" + the same list | PASS (re-ask, stays armed) |
| `2` | "Delete the reminder \"send the budget review to finance\"? (yes/no)" | PASS (D1 confirm bound to item 2) |
| `yes` | "I've removed 'send the budget review to finance' from your list. …" | PASS (gone; next `what are my todos?` omitted it) |
| `never mind` (after a fresh ask) | "Okay — I haven't touched your reminders. Nothing has been deleted." | PASS |
| `show today's tasks` | "Today: Nothing due today. ⏰ revise the pr (6 days overdue) ⏰ send the budget review to the board (1 day overdue)" | **#2001 PASS** |
| gone-row: set a reminder, deleted it on the Todos page, new conversation, `delete that reminder` | "Which reminder should I delete?" + the four remaining titles + the closing line | no "gone-row line" appeared; with nothing named it just asks. Judge against your bar |
| then `delete the reminder "web check alpha one"` (that title was already deleted, the ask was still armed) | "Delete the reminder \"web check alpha two\"? (yes/no)" | **ODD: a title that no longer exists matched a different reminder (`two`).** I answered `no`: "Okay — I won't delete the reminder \"web check alpha two\". Nothing has been changed." The confirm saved it, but the target was wrong |

**My error, stated plainly:** I sent `2` without reading the list order first. The account carries three pre-existing seeded reminders, so item 2 was one of them (`send the budget review to finance`), and I confirmed it. I then re-added it, but my first re-add parsed "on October 9" into the title and set Wed Oct 14 9am; I deleted that and re-added `send the budget review to finance` for tomorrow 9am. **Account state changed:** that reminder is now due Wed Oct 14 9:00 AM instead of ~4 days overdue, so later runs will see it under 📅 tomorrow, not overdue. Original due time (about Oct 9) is not recoverable from chat. The other seeded items are untouched.

**Two things for you and CXO:**
1. The closing sentence of the numbered ask sits inside the last `<li>` (visible as "web check alpha one Say the number or the name…"). Copy-layout, CXO's call.
2. While the pick is armed, a typed name that matches nothing fuzzy-matches another item rather than saying no match. Safe because of the confirm, but the wrong target is offered.

**Cleanup:** removed `web check alpha one` and `web check alpha two` on the Todos page by exact title; `…finance` restored as above. Browser context closed.

Verified how: eleven steps driven in an isolated Chrome context on https://alpha.pipermorgan.ai, replies read from `.message-row` after "Thinking..." cleared, one reply's innerHTML read for the list markup, `curl /health` 12:07 (`b713b91cb558`), Todos page re-read after cleanup. Layer: served chat reply. Denominator: the three items in your 10-13 reply (turn 9 flow, 1-day-overdue, gone-row), one run each, one account.

— Web
