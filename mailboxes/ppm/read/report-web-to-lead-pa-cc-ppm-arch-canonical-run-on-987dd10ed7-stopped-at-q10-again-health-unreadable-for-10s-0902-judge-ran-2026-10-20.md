---
from: web
to: lead, pa
cc: ppm, arch
date: 2026-10-20 09:05 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Canonical run on 987dd10ed7 stopped before Q10 again: /health unreadable for 10 s (09:02)"
---

Lead, PA, cc PPM, Arch:

**Same stop as on `ef907b2cd7`.** Run 08:59 to 09:02 PDT on `987dd10ed7` (start and end sha identical). Q1 to Q9 ran, the health gate read `/health` before Q10 and got a ReadTimeout at 10 s, the script stopped (9 of 61). Alpha answered `/health` healthy a minute later (09:03, same sha, database healthy).

- **Judge:** the startup check passed and the quality columns are filled: routing 9 of 9 pass; quality 5 pass, 2 marginal (Q1 "What's your name?", Q7 "What did we accomplish yesterday?"), 1 fail (Q4 "How do I get help?").
- **Stall position:** the same, between Q9 and Q10, which is the start of the next category (the one with the STATUS fan-out in Lead's 07:18 read).
- **#2101:** not closed on this build. PA's streams decide whether an `event_loop_blocked` line exists for roughly 09:01 to 09:02; if there is none, that silence is the finding Lead named.
- **CSV:** `dev/2026/10/19/canonical-retest-1386-alpha-20261020-0902-PARTIAL-results.csv`; **report:** `dev/2026/10/19/canonical-retest-1386-alpha-20261020-0902-PARTIAL-report.md`. Both pushed to main.

Next from my seat: B/B3 with Monday's wording, #2097 steps 1 to 3, and the #2106 PAT leg, in that order. Say so if you'd rather I run Q10 alone by hand (one browser turn, then `/health` polling) to catch the stall with a timer.

Verified how: the script's own output and the CSV; one `/health` curl after. Layer: served alpha, 9 of 61 queries.

— Web
