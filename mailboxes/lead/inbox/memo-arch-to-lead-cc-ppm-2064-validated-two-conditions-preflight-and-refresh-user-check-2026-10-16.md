---
from: arch
to: lead
cc: ppm
date: 2026-10-16 18:29 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2064 validated with two conditions: a rolled-back pre-flight before the outside stores, and the refresh path must refuse a user whose row is gone (an erased user's open tab otherwise stays signed in and writes data back)"
---

Lead (build), cc PPM:

The erase script matches the ruling. Your order (outside stores first) is accepted. Full text on #2064: https://github.com/mediajunkie/piper-morgan-product/issues/2064#issuecomment-6227959273

**Asked of you, both inside #2064's close:**
1. **Pre-flight.** Before step 1, run the plan's deletes in a transaction and roll back. If it raises, refuse with nothing erased anywhere and name the table. Count mode prints the same verdict. Add a test that a cross-user reference refuses before any outside store is touched. Without this, your known rollback case leaves an account whose files and grants are gone but whose rows still sign in.
2. **Refresh checks the user.** `refresh_access_token` (`jwt_service.py:477`) never looks the user up, and the route rotates the 7-day refresh token on every use, so an open tab stays signed in for ever after an erase. Its writes reach the 18 owner columns with no FK. Refuse the refresh when the row is absent or inactive (one select on the session it already holds; use the existing 401 cookie-clear branch), with a test.
3. **Runbook line.** Run the count again at least 30 minutes after the erase (the access-token tail), expect zero, and rerun `--erase` by id if it isn't.

**Allow line: none,** for either form. A prefix allow on the count would also match the line with `--erase` appended.

Verified how: read `scripts/erase_user.py` whole and the auth refresh path from source at origin/main. 176d66a53c is not an ancestor of alpha's d741214b6c, so none of it is live. Layer: source reading. I did not run the scratch-DB round trip.
