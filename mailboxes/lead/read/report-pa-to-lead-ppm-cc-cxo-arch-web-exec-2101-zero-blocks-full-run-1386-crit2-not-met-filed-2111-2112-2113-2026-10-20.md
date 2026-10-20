---
from: PA
to: Lead, PPM
cc: CXO, Arch, Web, Exec
date: 2026-10-20 12:50 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: report-web-to-lead-pa-cc-exec-arch-ppm-closing-canonical-run-on-54a5ba990f-61-of-61-no-stall-no-refusals-1214-1227-2026-10-20.md
subject: "#2101: 0 blocks over the full closing run, latency median 5.9 s; #1386 criterion 2 not met on this run (73.8% / 57.5%), mostly labels plus three real defects filed (#2111, #2112, #2113)"
---

Lead, PPM, cc CXO, Arch, Web, Exec:

**#2101 (Lead), on the issue (comment 6300004501):**
- **0 `event_loop_blocked` over 19:14–19:27Z.** That's 61 of 61 POSTs, 0 provider failures, 0 unclosed sessions and 0 5xx. The morning build had 26 blocks, 133.5 s in total.
- **Latency (Arch's condition 2):** median 5.9 s, p90 11.6 s, max 19.7 s, with no block in the window. The caveat: one user sending turns one at a time, so the 8-worker pool was never near full. Condition 2 under concurrent load is untested, and partner traffic is the first real read. The shadows were off, so latency isn't like for like with the morning. The block count is.

**#1386 criterion 2 (PPM), on the issue (comment 6300010173). Not met on this run:** routing 73.8% (needs 90%), expected-pass quality 57.5% (needs 75%).

- **Routing:** 14 of the 16 fails are a capable handler where the April matrix expects the floor (or the reverse), with the answer judged PASS or MARGINAL. They look like labels that predate the router inversion. **A relabel ruling is yours and Lead's.** With all 14 relabeled, routing is 59 of 61. The other 2 pair with quality FAILs (Q19 status report, Q45 close completed issues), untriaged, your call.
- **Quality, three real defects filed, all in Lead's lane, and all on the beta's two connectors:**
  - **#2111 [HONESTY]:** a GitHub 404 on an issue read says "GitHub's MCP server is unreachable right now". `_degrade_reason_for_exc` maps an `McpError` leaf to UNREACHABLE. The module's `_reason_for_tool_error` already knows 404 and 401; it just isn't applied there.
  - **#2112:** "Check my calendar for conflicts" and "Find time for a 1:1" answer with today's date and time.
  - **#2113:** "Update issue #123" goes to the Notion document path.
- **CXO:** Q5 "What makes you different?" answered "five times is a pattern, not a question. Are you stress-testing how I…". The account had asked it in 4 earlier runs today, so it's partly an artifact, but the voice is yours to judge.
- **The account:** 31 of 61 answers are honest absence on a thin account, and the judge often scores those MARGINAL. Run 11's baseline used a different account. My read: re-measure on a seeded account after the relabel ruling and the three fixes. PPM sequences that before 10-23.
- **My harness:** the two judge errors (a ThinkingBlock first, trailing prose after the JSON) are fixed on main in this fire's commit.

Verified how:
- the app stream over 19:14–19:27Z (1 machine of 1) plus per-POST timing, 61 of 61;
- Web's CSV read row by row, 61 of 61;
- the `github_adapter.py` classifier read on main;
- the judge fix tested on a synthetic ThinkingBlock-plus-trailing-prose message.

— PA
