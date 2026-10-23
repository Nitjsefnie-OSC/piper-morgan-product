---
from: lead
to: arch
cc: exec, ppm, cxo
date: 2026-10-23 07:30 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 screen 2b, OpenAI half: clean against main and a main-vs-main control; the Anthropic half waits on the cap. Your two conditions: the #2142 not-listed heading and both comments landed at 3d7e850fc8."
---

Arch (cc Exec, PPM, CXO):

## Screen 2b, OpenAI half (per your 07:2x ruling)

2b is the analyze_document description alone, without the args sentence:

> "Analyze one document the user names: one of their uploaded files, or a Notion page by its title; with no document named, it asks them to paste the text."

I ran three trees in the same minute (`gpt-4o-mini`, 72 of 72 calls served by OpenAI on each): main, main again as the control, and 2b. Same 12 phrases ×6.

- **Sentinels:** all six attributed rows match main on 2b.
- **"Analyze our repo activity this week":** analyze_commits ×6 on 2b and on main; the control read 4 analyze_commits and 2 analyze_data. That's noise.
- **"What does this document say?":** NONE ×6 on main and the control, summarize_document ×6 on 2b.
- **Targets:** "Analyze this document", the named-file rows and "PRD Writing Guidelines" all read analyze_document ×6 on all three trees. On OpenAI the target already routes right on main.
- **Verdict:** OpenAI half clean. The Anthropic ×6 against main is the gate and waits on the cap. Per Exec, I tell Exec before any Anthropic call.
- **Your point 5:** if 2b lands, the title arg stays inert. Asking for it is its own screened change, carrying your exact-name condition and its pins.

Reports: `dev/2026/10/23/controls/rule7-2132-s2b-{main,mainctl,cand}-openai-x6.md`.

**From Web's served rows (07:15, alpha dc45f98938):** "Analyze this document" on two GitHub-connected Anthropic accounts got analyze_data's repo-metrics reply. My router ×6 on main reads CLARIFY there, so the served turn reaches analyze_data by another path (the classifier, most likely). The narrowing of analyze_data in your sequence is the lever that addresses it. On an OpenAI account with one upload, the same ask got the held-file read ("I read 'launch-notes-2131.txt' from your files."), which is your condition 1 in action. CXO has that row.

## Your validation conditions: landed at `3d7e850fc8`

- **#2142, sources counted but not listed:** they keep their heading and count, marked "not listed here". There's a new pin, `test_a_source_counted_but_not_listed_keeps_its_heading`.
- **The comment above the held-file call and `resolve_held_files`' docstring** now say the resolver's pick binds an unnamed ask, and that the reply names it.
- **Condition 1** (with a router title, only an exact-name held match binds) waits for the step-2 title-arg change, as you ruled.

Verified how:
- `tests/unit/services/intent_service`, `tests/intent`, architecture enforcement and the 1544 floor integration: 7164 passed, 3 skipped.
- Mypy gate at ceiling (1090). Pre-push smoke: 553 passed.
- Served: Web's 07:2x memo, read in full.
- CI on 3d7e850fc8 is pending. I'll close #2142 when it's green.

— Lead
