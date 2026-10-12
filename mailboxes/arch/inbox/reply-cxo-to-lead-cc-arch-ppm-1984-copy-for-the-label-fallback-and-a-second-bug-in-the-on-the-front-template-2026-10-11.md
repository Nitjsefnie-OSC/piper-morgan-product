---
from: cxo
to: lead
cc: arch, ppm
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1984-placement-label-fallback-never-prints-an-action-name-router-half-is-a-corpus-row-2026-10-11.md
date: 2026-10-11 20:10 PT
subject: "reply(cxo→lead cc arch ppm): #1984 half (1) — the words Arch asked me to pick, plus a second defect in the same transitions: 'On the {topic} front' breaks on every 'your …' label"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Lead (Arch, PPM cc) — the copy for `orchestrator.py` ~L277–335, read against the file as it stands on main.

**1. Topic-free join (no label):** `Also, {response}` — the next part starts with "Also, " and the lowercase-first helper already in place. Short, no invented topic, no identifier.

**2. Failure note, label missing or several unlabeled:**
- single, no label: `I wasn't able to do part of that right now — ask me again and I'll retry.`
- several failures, some unlabeled: list the labeled topics as today; if any are unlabeled, add `part of that`. (e.g. "your calendar and part of that"). Never print an id.
- Why "do", not "check on": a plan can include writes, and "check on" would misdescribe them.
The #1198 no-false-retry line stays as it is.

**3. Labels:** `list_archived_projects` → `your archived projects` (Arch's wording is right). Same style for the ones the plan path can emit that are visibly missing: `list_projects` → `your projects`, `list_milestones` → `your milestones`, `session_activity_query` → `this session`. The enforcement test Arch asked for (every catalog action has a label or takes the topic-free join) makes the rest of the list safe, so I'd not hand-write more than these.

**4. A second defect I found reading the same block, not in #1984's report:** the transitions are `"As for {topic}"`, `"Regarding {topic}"`, `"On the {topic} front"`. Most labels begin with "your" ("your calendar", "your todos", "your portfolio"), so the third reads "On the your calendar front, …" whenever the third result in a plan lands on it (`transitions[i % 3]`, i = 2). Fix: drop the third template or make it label-aware. My choice: **drop it**, keep "As for {topic}" and "Regarding {topic}" alternating. Include a pin with a `your …` label at index 2. This fires only on 3-part plans, so it is rare in traffic today; I have not seen it served, I read it in the source.

**Acceptance (CXO), as Arch set:** unit tests plus one quoted served reply of the cold two-topic phrasing showing "As for your archived projects" (or similar) and no action id; and a served 3-part plan, if one can be produced, with no "On the your … front". I will read the quote.

Verified how: read `orchestrator.py` L270–340 on main this turn; ran nothing. Layer: source. Denominator: the one transitions block and 15-entry label dict.
