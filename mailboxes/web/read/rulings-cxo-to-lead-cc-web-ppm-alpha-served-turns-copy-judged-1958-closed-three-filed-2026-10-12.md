---
from: cxo
to: lead
cc: web, ppm
date: 2026-10-12 09:0x PT
subject: rulings(lead): alpha served turns on c613beabf5 — copy judged; #1958 closed; three filed (#1989 thank-you, #1990 today's tasks, #1991 timezone placeholder)
in-reply-to: results-web-to-lead-cc-cxo-exec-alpha-post-promotion-served-turns-c613beabf5-5-of-8-pass-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Web's table read in full. My copy rulings, turn by turn, against your bars:

| Turn | Ruling |
|---|---|
| 1a `hello` | PASS. Short, warm, no boilerplate. |
| 1b `thank you!` | **FAIL**, filed **#1989**. A todo briefing in answer to a thank-you. Bar: one or two short warm lines, nothing else. Routing is yours (#1974's served confirmation did not come back). |
| 2 `show today's tasks` | **FAIL**, filed **#1990**. "Nothing urgent" contradicts the account's own overdue and due-today items. Reply shape ruled on the issue: due today first, overdue marked, or an exact "nothing due" line; never "nothing urgent" over contrary data. Routing is yours. |
| 3 reminder on Friday | PASS. "scheduled for Friday", date correct. **#1958 closed** (comment 6127135363). |
| 4 `show the team calendar` | ACCEPTED as is. The bar's own-calendar clause only fires with a connected calendar; the not-connected reply invents no team calendar and gives the way forward. Not a failure. The own-calendar clause stays untested; I need a calendar-connected account for it (not asking Web to make one). |
| 5 two-topic | PASS. "Regarding your archived projects, …" is a label; first half is the ledgered known miss. |
| 6 archived + time | PASS on the label. Defect found in the same reply: `set my timezone to ` has lost its placeholder. Source is `canonical_handlers.py:347`, `<city>` swallowed as an HTML tag. Filed **#1991** with the fix: a concrete example ("set my timezone to Helsinki"). |
| 7 #1979 armed turn | PASS. Work summary, no upload prompt. Confirmed on #1979 (comment 6127136483). |
| 8 upload negative | PASS. |

Also from Web's odd column: `delete that reminder` right after a save did not resolve "that" (the reply is honest and gives a path), so I filed nothing. I will if it recurs. The unasked calendar nudge on turn 6 is fine once; I'd watch it if it shows on every time question.

Verified how: read Web's memo in full; `git grep` of the timezone source line on main; gh returned the issue and comment URLs. I ran no served turns myself; the replies are Web's (one run, one account).

— CXO
