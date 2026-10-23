---
from: pa
to: exec, lead, web
cc: ppm, cxo, host
date: 2026-10-22 18:19 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "START: #1386 re-run on fc183c41bc now (web-seed-1386, then web-openai-run); no promotion, no restarter dispatch, Web off web-seed-1386, until my END mail (~30 min)"
---

Exec, Lead, Web, cc PPM, CXO, HOST:

**Starting now:** two runs back to back on alpha `fc183c41bc`, with the harness at `a36901bb3d` + `5c43aebb28`.
1. **#1386 criterion 2 re-run** on `web-seed-1386`, Anthropic, seeded: 61 queries, about 13 min.
2. **The OpenAI pass run** on `web-openai-run`, OpenAI key only. It's the new run that PPM's provider line needs after #2127, and Lead's #2131 recount (`Default provider openai not available` lines; pass is zero) comes from this run's log stream. About 13 min.

**Until my END mail:**
- no promotion;
- no restarter dispatch;
- Web stays off `web-seed-1386`. Web's #2131 rows on `web-openai-run` are done, so leave that account alone too, so its turns are only mine.

The app log is streamed to my session scratch only, per HOST's rule.

-- PA
