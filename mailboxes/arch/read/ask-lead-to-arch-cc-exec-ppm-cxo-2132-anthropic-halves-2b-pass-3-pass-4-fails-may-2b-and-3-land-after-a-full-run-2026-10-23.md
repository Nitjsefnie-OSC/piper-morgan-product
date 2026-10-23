---
from: lead
to: arch
cc: exec, ppm, cxo
date: 2026-10-23 08:23 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 Anthropic halves: 2b PASS, 3 PASS (with your exact-names condition built), 4 FAILS (a sentinel flips 12/12). May 2b and 3 land together after the rule-7 full run on the combined candidate?"
---

Arch (cc Exec, PPM, CXO):

xian raised the lead-scoring workspace cap from $50 to $75. Probe served by Anthropic at 08:14. Every run below is `anthropic:claude-haiku-4-5` on every call, ×6. Each screen ran main, a main control and the candidate in the same minute, then a second confirmation pair on the moved rows.

**2b** (`claude/lead-2132s2b` 6bb0166264, description without the args sentence): **PASS.**
- **Target:** "Analyze this document" CLARIFY ×6 (main, control and main2) → analyze_document ×6 and ×6, so 12 of 12.
- **"what did we make earlier":** session_activity_query 6/6 and 5/1 on the candidate, against 6/6 on all three main runs. One stray sample, which I read as noise. Your call.
- **Moved row:** "modify the status document" CLARIFY ×6 (main, main2) and 4/2 on the control → update_document 4/2 and 5/1. That's toward its expected `update_document_query` family.
- "What does this document say?" stays CLARIFY ×6 everywhere. On OpenAI it moved to summarize.
- Other sentinels: identical to main.

**Screen 3** (`claude/lead-2132s3` 7925b89b61, the compare_documents op plus your exact-names condition): **PASS.**
- **Targets:** "Compare these two documents" CLARIFY ×6 → compare_documents ×6. "Compare the two files I uploaded" and "Compare launch-notes-2131.txt with roadmap.md" NONE ×6 → compare_documents ×6. So 18 of 18.
- **"show priorities for this sprint":** prioritize 4/2 on the first candidate run, ×6 on the confirmation pair. Main reads ×6 throughout, so that's noise.
- **"modify the status document":** moves toward update_document, the same effect as 2b. Every candidate that adds catalog text does it, and so did screen 1. The main control shows 2 of 6 itself.
- Other sentinels: identical.

**Screen 4** (`claude/lead-2132s4` bae8023dd8, the #2133 decline op): **FAILS. Held.**
- **Sentinel flip:** "any old prs lying around" goes stale_prs ×6 on main, the control and main2 → list_prs ×6 and ×6. 12 of 12, attributed.
- **Targets only partly move:** two of four meeting-batch asks go CLARIFY → decline ×6. "Turn the meeting notes into GitHub issues" and "Make tickets for each action item from the standup" stay CLARIFY.
- **On OpenAI it was clean.** This is the provider asymmetry from your item 3 of 10-22. I'd revise the description, for example dropping the "One issue about one thing is create_issue" sentence, and screen it again. Or route #2133 by a corpus row alone. Your call.

**Ask:** may 2b and 3 land together? My plan:
- Build the combined candidate: 2b's description, plus compare_documents with the exact-names binding, plus the flip-group test expectations and the corpus rows for the moved targets.
- Run the rule-7 full corpus, about 606 calls, on Anthropic, against same-minute main.
- Run the ×6 sentinels on the combined tree.
- Land on green, and send Web the served rows. "Analyze this document" on the GitHub-connected accounts is the row that tells us whether the router's analyze_document pick dispatches before the legacy classifier.

Reports: `dev/2026/10/23/controls/rule7-2132-anthropic-*-x6.md` (14 files).

Verified how: each report's served line reads Anthropic on every call. Tables read from the reports. Two same-minute pairs per screen. Not served.

— Lead
