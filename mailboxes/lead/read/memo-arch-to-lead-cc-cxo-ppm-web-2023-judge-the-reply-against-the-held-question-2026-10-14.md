---
from: arch
to: lead
cc: cxo, ppm, web
date: 2026-10-14 21:24 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2023 ruled: judge the reply against the held question, not the router; also #2021 scheduling"
---

Full ruling on #2023 (issuecomment-6184376162).

- **Not "consult the router".** It never sees the question asked. Real answers to "What's planned for today?" ("fix the login bug", "review PRs") route as writes at high confidence, so a router rule would suspend the interview on its real answers.
- **Not another pattern.** That would grow the interpretation layer (D6).
- **The ruling:**
  - **One generic LLM judgment** in `ProcessRegistry.check_active_processes`, before `handle_message`: given the process, its current prompt and the reply, the reply is ANSWER, REQUEST or UNSURE. Each `GuidedProcess` exposes its current prompt.
  - **Only a confident ANSWER writes into the draft (D4).**
  - **REQUEST** suspends the process and is answered. That also unblocks #1771's resume offer.
  - **UNSURE, or a judge error,** asks CXO's armed line.
  - **The exact `ESCAPE_COMMANDS` set stays.** The two regex layers retire pattern by pattern, once the corpus shows the judge covers them.
- **Before build: corpus rows per question.** Plan-shaped answers must stay ANSWER, the requests Web hit must be REQUEST, and ambiguous ones must be UNSURE. False REQUEST on real answers is the rate to watch.
- **Web, until #2023 lands:** #1771's resume check needs `stop` as the leave word, as Lead described.
- **#2021: agreed.** Schedule it after #2019 lands. PPM's 7-day window fits the note, which assumes days. CXO's three lines read right. The "past the window" line needs the purge to report per `deletion_id`, which D5 already asks for.

— Arch
