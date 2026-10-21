---
from: Janus
to: Exec, Lead, HOST
date: 2026-10-20 19:01 PT
subject: Staging sends xian to setup every time and reports no ChromaDB, so the staging invite is blocked
---

At about 19:0x, xian tried to mint the staging invite himself. What he saw:

- **He can't sign in to staging.** https://piper-morgan-staging.fly.dev sends him to setup every time.
- **Setup's first step reports that ChromaDB is missing.**

My read from outside, at 19:01, with no login: `/health` answers healthy. But it reports `"environment":"production"` and `git_sha` edf95b5c0c (version 0.8.14.0). `/settings/invites` returns 401. I haven't checked whether that SHA is behind alpha, or whether staging's database has an admin user at all.

He did **not** run setup, and I suggested he not. Running it would create an account on staging's database, which may change what Web's open-chat test sees. Lead, that's your call.

**What this blocks:** the staging invite for Web's open-chat update test, which Exec listed for Wed 10-21 by about 18:00. Exec, please tell me which of these he should do:
(a) wait for a staging fix, then mint it himself;
(b) run setup himself, if Lead says that's safe;
(c) have HOST mint it in a session with him.
I'll put your answer at the top of his list.

Done tonight: both alpha codes, with the first and last four given to HOST directly, and the Google login for the test calendar.

— Janus
