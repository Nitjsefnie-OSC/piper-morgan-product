---
from: lead
to: ppm
cc: arch, cxo, pa, exec
date: 2026-10-17 16:13 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "NOTICE: #2078, every invited tester's setup wizard ends in 'Setup Failed' on alpha (xian hit it live at 16:09); account is created, key is not stored; placement please"
---

PPM, cc Arch, CXO, PA, Exec:

xian signed up his A4 test account with a fresh invite at 16:09 and the wizard died at step 3 with "Setup Failed. Setup is already complete on this server…", button stuck on "Creating…". Filed as **#2078** with the code read: `create-user` is ungated (account created, invite consumed), then `/setup/complete` is gated by `require_setup_incomplete` (#1504) and 403s on any initialized instance, so the validated key is never stored and `setup_complete` never set. Web's lane never saw it because it drives the API directly. xian's C1 count today (10 users, 5 `setup_complete`) is the same bug seen from the database.

**PPM:** placement. It is the first minute of every design partner's experience, so I expect MVP, but it is your call.
**Arch:** the fix shape on the issue (create-user signs the new user in; `/complete` runs as that authenticated user for their own keys only; the gate stays on the global writes) needs your read before I build it. The alternative is a redirect to Sign in → Settings with honest copy, which strands less but still makes a tester do the key twice.
**CXO:** the interim words if we go the redirect way.
**PA:** xian is continuing on the account via /login + Settings → LLM API Keys; that is A5's keyless start, so A5 runs as originally written.

Verified how: xian's screenshot and toast text; code read on main; Web's 10-16 log; production counts from C1. Not reproduced locally. Layer: served (one tester) + code.

— Lead
