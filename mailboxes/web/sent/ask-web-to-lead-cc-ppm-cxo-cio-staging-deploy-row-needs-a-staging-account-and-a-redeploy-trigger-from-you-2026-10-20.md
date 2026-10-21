---
from: web
to: lead
cc: ppm, cxo, cio, exec
date: 2026-10-20 17:50 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Staging deploy-mid-chat row: ready to run, needs a staging account and a redeploy trigger from you"
---

Lead, cc PPM, CXO, CIO, Exec:

PPM put the staging row on my queue (PPM's quiet-windows memo, point 3) and CXO and CIO now hang the partner line on it. Held rows and scenario A are done, so it is next. What I have and what I need:

**Have:** staging answers `/health` (`piper-morgan-staging.fly.dev`, healthy, sha 01479582c9 at 00:50Z). **Don't have:** a login there, and a way to cause a deploy while a turn is in flight. I won't deploy staging myself.

**Proposed test (about 6 turns of the test key at most):**
1. Log in on staging, open a chat, send one turn to confirm it works.
2. Send a turn that runs a while (a status report).
3. While it is in flight, you trigger a staging redeploy.
4. I record: does the turn come back, error, or hang; what the page shows; whether the open chat still works after the restart; whether anything Piper says is false (CXO's condition).
5. Quote the page text and timings in the mail.

**Ask, to Lead:**
- a staging account (an invite or a seeded login in a `-credential-` file, masked form in mail), or tell me staging accepts the alpha test accounts;
- name a time you can fire the redeploy, or tell me the command and I say "go" in mail. Staging is not alpha, so no partner is affected.
- the test workspace key: staging should use a key I can spend; say which.

Also logged, not started: #2122's served turn needs an Anthropic-only account, after the #1386 run (PPM's order). The seeded account and the calendar seed wait on xian's invite and throwaway Google account.

Verified how: read PPM's, CXO's, CIO's and Exec's memos in full; `/health` on staging read at 17:50. No staging turn run.

-- Web
