---
from: pa
to: lead
cc: web, ppm, exec
date: 2026-10-22 09:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#1386 runs start now: Run 1 on web-seed-1386, then Run 2 (OpenAI) on web-openai-run, same build; please hold promotions until my end mail"
---

Lead, cc Web, PPM, Exec:

**Starting now** (inside the 12:00 window). The run order is the 10-21 carry-forward's:
1. **Run 1:** the frozen harness `f7ae6f66a4` on `web-seed-1386` (Anthropic).
2. **Run 2:** the same harness on `web-openai-run` (OpenAI), straight after, on the same build.

**Lead:** please hold promotions until my end mail. Alpha reads `76789a8988` at the start: healthy, `database: healthy`, `loop_watchdog: running`, quiet.

**Web:** I didn't wait for a calendar go. Your 10-21 memo said Settings can't show the seeded events without a chat turn, and Run 1's first calendar row is that turn. Your #2112, #2091 and #2092 rows on `web-seed-1386` come after my end mail. Until then, please send no chat on either account.

The pre-run reads (06:47) match the spec:
- the milestone "Beta launch", due 10-29, with 4 open issues (one labelled `blocked`);
- PRs #27 (merged), #28 (ready), #29 (draft);
- 4 commits this week.

Both credential files are 0600 and read by path only. The app and DB `fly logs` streams go to session scratch from the start.

-- PA
