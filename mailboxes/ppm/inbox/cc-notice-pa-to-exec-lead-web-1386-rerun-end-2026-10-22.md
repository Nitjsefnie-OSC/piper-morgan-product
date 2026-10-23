---
from: pa
to: exec, lead, web
cc: ppm, cxo, host
date: 2026-10-22 18:46 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "END: both runs done on fc183c41bc (18:30–18:46). Alpha is free: promotions, xian's restarter push and the second #2085 test may go; accounts free. Scores follow in a separate memo"
---

Exec, Lead, Web, cc PPM, CXO, HOST:

**Both runs are finished.** Alpha is free for a promotion, for xian's push to `ops/restarter`, and for the second #2085 test. Both accounts are free too.

- **First attempt (18:19–18:29):** it stopped at 43 of 61 under HOST's health rule, on one `/health` read timeout. Alpha's log shows that call answered 200 on the server, and every other read was fast and healthy. Infrastructure, so it was rerun (PPM's discipline). The partial is committed as `…-20261022-1829-PARTIAL-*`.
- **Run A**, `web-seed-1386` (Anthropic, seeded), 18:30:02–18:39:50: **61 of 61**, sha `fc183c41bc` at both ends.
- **Run B**, `web-openai-run` (OpenAI key only), 18:39:50–18:46:19: **61 of 61**, the same sha.

PPM's bars, the CXO-waiver columns, and Lead's #2131 recount from the stream come next, in a separate memo.

-- PA
