---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-12 07:3x PT
subject: ruling(lead): #1984 half (2) — not (a); screen (b) on the named sentence; (c) if it fails
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** **(a) is refused**, and condition (4) stands. **(b) is GO for a screen**, scoped to one sentence I've
read in source. If the screen is clean you get one full run. If (b) fails at either step, **(c)** applies and
CXO decides closure. You were right that read_floor_3 is not a lever (vocabulary 5).

**Why not (a).** The comparison is uneven. The 8 worsened rows got ×6 same-minute attribution against main,
and 4 of them were pinned on the candidate. The 13 improved rows were never attributed. They come from a diff
against the 10-10 report, which was run on a different tree and day, so drift counts as gain there. I can't
trade four losses with a confirmed cause for gains whose cause nobody has checked. One of those losses is an
ANALYSIS survivor that a deletion depends on. A trade like that would need the improvements attributed the same
way first, and it would still need my ruling.

**(b), made concrete.** I read both sources of grammar. The `session_activity_query` registry example
("What did we create this session?", `action_registry.py:339`) is already narrow. The pull comes from the rail
description, `workflow_entries.py:4009–4011`:
"What was created or done in the CURRENT session only — 'what did we create this session', **'what did I work
on today'** — never earlier or previous sessions". That quoted example is the bridge from "my work" to session
activity. Your W3 table shows the same effect: without STATUS's negation, "what am I working on?" falls back to
session_activity 6/6.
- **The edit:** drop the `'what did I work on today'` example. Leave the rest of the sentence, the CURRENT-session
  scope, and the ADR-078 citation unchanged. STATUS text stays main's.
- **A known cost to screen:** the corpus row "what did I work on today" → `action:session_activity_query`
  (`inversion_corpus_phase0.yaml:1371`) licenses a **deleted** TEMPORAL literal (`\bwork on today\b`). Include it
  in the screen. If it moves, that licence is lost, and the result is a NO-GO under rule 10. Don't fix it by
  adding a corpus row.
- **The screen set** (×6 per arm, same minute):
  - main vs (b) on your 11 rows, plus "what did I work on today", plus the session-activity rows.
  - Arm (b) alone is first.
  - If (b) alone doesn't take the #1984 row to the ruled plan at least 5/6, you may screen (b)+W3 as a second
    arm. W3 has no negation, which was the damage lever, and its remaining worsened row, "tasks I'm actively
    working on", is in session_activity's neighbourhood, so (b) may fix it.
  - No third arm. Arms stop there because of the 10-11 lesson: this neighbourhood moves under any edit.
- **To pass the screen:**
  - the #1984 row reaches the ruled plan at least 5/6;
  - the two sentinels hold;
  - no row attributed worse than main, with "worse" meaning a lower count of the expected answer at ×6;
  - "show priorities" must not go from main's split to 6/6 wrong.
- **Then:** one full run. ×6 attribution covers every worsened row, **and** every improved row you cite. Condition
  (4) is unchanged. Re-run the served check on the landing tree with the same four shapes, including the upload
  negative.

**(c) if (b) fails.** The #1984 row is added to the ledger as a measured known miss, with the reading named
(session_activity→list_archived). The served reply stays as it reads today. CXO decides whether #1984 closes on
half (1). No more wordings after that. This neighbourhood has now cost two days of screens.

**Side finding:** I agree that "show me when we shipped the API" (shipped_this_week 6/6 on both trees) is the
COMPLETION_HISTORY ledger's pre-existing miss, not this candidate's.

Verified how: I read `workflow_entries.py:3999–4021` (the session_activity_query rail entry),
`action_registry.py:296/339/437` (the registry examples and STATUS description), and
`inversion_corpus_phase0.yaml:1365–1380` (the "work on today" row and its deleted-literal source), all on main at
07:2x. I read your wordings table in full. I did not re-run any calls, so the counts above are yours.

— Arch
