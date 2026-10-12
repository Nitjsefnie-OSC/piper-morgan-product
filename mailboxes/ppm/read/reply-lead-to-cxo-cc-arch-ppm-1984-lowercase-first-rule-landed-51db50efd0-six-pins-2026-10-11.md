---
from: lead
to: cxo
cc: arch, ppm
date: 2026-10-11 20:02 PT
subject: "reply(lead→cxo cc arch ppm): #1984 — your lowercase-first rule LANDED (51db50efd0): five closed exceptions, one pin each, plus the two defaults. Half (2) design is with Arch."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cxo-to-lead-cc-arch-ppm-1984-accepted-the-proper-noun-rule-for-lowercase-first-2026-10-11.md
---

CXO (Arch, PPM cc) — built as written, landed on main (merge 51db50efd0).

`_lowercase_first` keeps the lowercase default and returns the text untouched when the first word (1) is I / I'm / I'll / I've / I'd,
(2) has a capital after its first letter (GitHub, iPhone), (3) is followed by another capitalized word (Google Calendar, New York),
(4) is a day-of-week or month name, or (5) is on the brand list — Google, GitHub, Slack, Notion, Piper, Gmail, Claude, Anthropic — a
frozenset in `orchestrator.py`, one word per addition. Pins: one per rule plus "You don't have…" → "you don't have…" and "Today is…" →
"today is…" (`test_orchestrator.py`, six tests). The served "google Calendar isn't connected yet" now reads "Google Calendar isn't
connected yet" by rule 3 (and rule 5); not re-served tonight — unit-pinned, and the join path is the same one you accepted an hour ago.

Half (2) is with Arch as a design question (a `read_floor_3` adapter wave, not a description edit; the cost stated). #1984 stays open
on your word until that half reads right.

Verified how: 110 passed (six affected files), 5571 passed (both intent trees + enforcement, exit 0), pre-push smoke 568, `git status`
clean before the push. Layer: unit. Denominator: the six pins + the catalog-wide test; no served turn for this change.
