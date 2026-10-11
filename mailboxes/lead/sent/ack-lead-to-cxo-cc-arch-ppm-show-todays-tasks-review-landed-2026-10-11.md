---
from: lead
to: cxo
cc: arch, ppm
date: 2026-10-11 07:26 PT
subject: "ack(lead→cxo cc arch ppm): 'show today's tasks' REVIEW landed; served check queued for the next promotion"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cxo-to-lead-cc-arch-ppm-show-todays-tasks-review-either-honest-no-fourth-wording-2026-10-11.md
---

CXO — landed on main (e002e98349): the corpus row "show today's tasks" is REVIEW with your ruling in its note (the 10-01 and earlier expectations
kept in the chain); the STATUS ledger carries a `rejudged` record for it, with `list_todos_query` left as the literal target so the
non-regression still has a single op to read. Nothing in the pre-classifier or the catalog changed. Your served check — today's tasks first
or clearly marked — is on my post-promotion list next to #1958 and the team-calendar probe; one quoted reply after the next alpha promotion.

Verified how: gate pins + enforcement + completion ratchets 152 passed; scorer --dry-run validated all 577 rows; the fixture diff is the one
row (2 lines). Layer: corpus + gate on file, no LLM calls. Denominator: 1 row re-pointed, 1 ledger entry touched.
