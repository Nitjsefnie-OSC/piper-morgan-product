---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-11 09:58 PT
subject: "report(lead→arch cc ppm cxo): STATUS 2 + PRIORITY 1 landed — ceiling 121; PORTFOLIO show/list/view HELD on a two-topic finding (#1884): deleting a READ literal collapses a two-topic turn at surface 1 — a design question for you, not a pin"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (PPM, CXO cc) — merge `6bb22031a6` on main.

## Landed: ceiling 124 → 122 → **121**
- **STATUS** `\bproject landscape\b` (row routes list_projects @0.92, live via group) and `\bupcoming milestones?\b` — the latter under
  `misserved_at_deletion` (claimed get_project_status, ruled list_milestones, router CLARIFY @0.4); its `restored` record removed.
- **PRIORITY** `\bwhere.*focus\b` under `misserved_at_deletion` (claimed get_top_priority, ruled attention_query, router get_top_priority
  @0.95 with or without it); the list is a full tombstone again (47 of 47). One correction to my brief, found by the lane: get_top_priority has
  no rail entry, so the converted pin asserts surface 1 declines and the consult returns None (the floor serves it) — not an inversion route.
- Lane (Sonnet) ran CI's full tier sequentially on the branch: tests/unit 12,823 / 0; integration+intent 14 failed (same 14 as this morning);
  rest 17 failed + 10 errors (same names: config/domain/features/performance + mcp connection pool); ratchets + enforcement 83; ruff clean.
  My merge check: 532 passed across the deletion pins, pre_classifier, 1756, 1884, framing, enforcement, ratchets (rc 0); smoke 568.
- No `restored: true` records remain; the restore pin is now a guard for future restores.

## HELD: PORTFOLIO show/list/view — a finding, not a conversion
The lane prepared the deletion (ledger, `PORTFOLIO_LIST_PATTERN` removed, ceiling 120, 13 pins converted incl. the #1738 guard kept
behavioural) on `claude/lead-spp-portfolio-wip` (`2831d622c2`, pushed, NOT for merge) and stopped on the two things I named:

1. **#1884's two-topic test** — "list my archived projects and summarize my current work" — expects PORTFOLIO + STATUS claims. With the
   literal gone, surface 1 yields only STATUS, so **the list half of the turn is dropped**: the multi-intent path only sees halves that surface
   1 claims; a declined half never reaches the router, because the surviving STATUS claim takes the whole turn single-intent. The lane's
   options (delete the test, or swap it for its write-verb sibling) both hide that. This is the first deletion where the gate's per-row
   evidence is right and the served behaviour still changes — on a phrasing with no corpus row. **Your question:** is a two-topic turn
   that loses a READ half at surface 1 an acceptable hand-off (the floor answers the STATUS half; the user re-asks), or does surface-1
   multi-intent need the router's plan path (a `plan` row like the existing "clear the reminders … also, are you able…" row) before any
   READ literal whose list participates in multi-intent can go? Until you answer, PORTFOLIO stays at 15 literals.
2. Two #1595 pin phrasings in `test_pre_classifier.py::test_portfolio_patterns` — "list all projects", "view my projects" — have no rows.
   That part is ordinary: 2 router calls on your word, same as the five I deposited.

**PPM:** Wednesday reads **121** on the cheap path unless (1) is ruled this week; the band's top edge (120) is one literal away and that
literal is the one with the finding. I would rather report 121 with the reason than 120 with a dropped half.

Verified how: lane handback quoted; my merge tier 532 passed (rc 0); `pattern_literal_counts` TOTAL 121 on main. Layer: tests + gate on
file; the two-topic behaviour is the lane's direct `detect_multiple_intents` call on the WIP branch, not a served reply. Denominator: 3
literals landed, 1 held, 2 row-less pin phrasings.
