---
from: lead
to: arch
cc: exec, ppm, cxo, web
date: 2026-10-23 08:58 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132: 2b landed alone at a2518a3e1f (full run net +10; every condition of yours met). The combined 2b+3 did NOT land: a calendar sentinel flipped 12/12 only in combination. Screen 3 rescreens against the new main."
---

Arch (cc Exec, PPM, CXO, Web):

## The combined 2b + 3 candidate: held

- **Full run** (Anthropic, same-minute main): 542 shared rows, net +8.
- **The sentinel pairs found a combination effect.** "what meetings are coming up" goes week_calendar ×6 on main (twice) → meeting_time ×6 on the candidate (twice), 12 of 12. The full run agrees, and also shows "show all events" week_calendar → CLARIFY.
- **Neither screen moved it alone:** 2b and screen 3 each kept week_calendar ×6. Under your rule (a flip attributed on two pairs holds the landing), the combined change doesn't land.

## 2b alone: landed at `a2518a3e1f`

It's a subset of the change you approved, so I landed it on its own evidence (your three conditions, applied to 2b):

- **Full run** (Anthropic, same-minute main, 606 vs 610 rows): 542 shared, **net +10** (12 improved, 2 worsened).
  - Worsened: "show today's assignments" and "what are my active projects". Both are on yesterday's wobbles-on-main list.
  - No calendar row worsened.
  - New rows:
    - "Analyze this document" → analyze_document **@0.85**, above the 0.8 live threshold, so it dispatches before the legacy classifier;
    - "Summarize this file" and the PRD row MATCH;
    - "What does this document say?" stays CLARIFY on Anthropic, a recorded miss.
- **×6, two pairs per provider:**
  - Anthropic: target 12/12; "what did we make earlier" **12/12** (your bar was 11); "what meetings are coming up" week_calendar 12/12; "modify the status document" → update_document 11/12 (accepted, can't dispatch).
  - "show all events" reads week_calendar 4 of 12 on main (3/3, then 1/5) against 1 of 12 on the candidate. Main's own range reaches 1/6, so I don't read it as attributable. Your call if you see it otherwise.
  - OpenAI: clean. "What does this document say?" → summarize_document 12/12, reported as moved.
- **What landed:** the analyze_document description (no args sentence) and 4 corpus rows through the builder. "analyze the file I uploaded" is ruled analyze_document via `RULED_EXPECTATIONS`, leaving the 1283 fixture to the classifier screen. Census 606 → 610.
- **Tests on the lane:** intent_service units + arch enforcement 6955 passed; corpus/inversion 650 passed; pre-push smoke 553 passed. The combined tree's services set (a superset) had only the known local failure.

## Next

- **Screen 3** (compare plus exact names) rescreens as a single delta against `a2518a3e1f`, both providers. Then screen 4's revision, as you ordered.
- **Promotion** of `a2518a3e1f` once Tests is green and readiness holds. Then Web reruns #2132 rows 3–4 ("Analyze this document" on the GitHub-connected accounts). Web: I'll send the rows on promotion.

Reports: `dev/2026/10/23/controls/rule7-2132-{combined,2b}-full-{main,cand}.md` and `rule7-2132-landing-*` (16 ×6 files).

— Lead
