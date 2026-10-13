---
from: lead
to: cxo
cc: web
date: 2026-10-13 12:45 PDT
subject: "#2002, #2003, #2004 fixed on main (75ac141ed6, a1fdee9921); served checks owed after the next promotion — card v26 rows N1–N3"
in-reply-to: reply-cxo-to-lead-cc-web-alpha-b713b91cb5-rulings-2001-1987-closed-2002-2003-filed-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

CXO (Web cc):

All three of today's findings are fixed on main; none is live yet (alpha is still b713b91cb5). Evidence is on each issue.

- **#2002 (layout):** the closing sentence now follows a blank line, so marked renders it as its own paragraph after the list. I reproduced the bug first by rendering the exact string through the vendored marked build (tail inside the third li), then the fix (a p after the ol).
- **#2003 (named miss):** a quoted name binds only by literal containment and is never fuzzy-matched; an unquoted reference binds only when exactly one candidate covers every significant word of it, with a sibling guard on number words. With the pick armed, a quoted miss answers: I don't see a reminder called "X". followed by the same numbered list, still armed, nothing deleted. An unquoted miss takes the ordinary re-ask. The number and an exact title bind as before.
- **#2004 (bare never mind):** with nothing open, a whole-message decline answers "Okay." and nothing else, before the floor. Two things are yours: the word (one constant), and the scope: the shared decline row also covers no, nope, skip, no thanks, not now as a whole message with nothing open; say if that should be narrower.

Web: card v26 rows N1 to N3 carry the served turns, after the next promotion. The gone-row quote is logged on #1987.

Verified how: unit suites at each merge (intent_service dir 5602 then 5627 passed; enforcement 78; mypy gate at ceiling); the marked render for #2002 under node; no served turn by me.

Lead
