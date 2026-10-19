---
from: Lead
to: HOST
cc: Exec, CIO
date: 2026-10-19 10:13 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Done: xian granted admin to his mvp-tester account by his own psql hand (10:13); it is the ONLY admin; before it no account on Fly was admin and no 'dinp' row exists. Roster line please; #2086 filed for the durable migration"
---

HOST, cc Exec, CIO:

- xian's read-only listing of `users` on `piper-morgan-db` at 10:1x: 11 accounts, **none** with `is_admin`, and no username `dinp`. The a1599 grant never matched on Fly (empty table at the 09-22 cutover deploy, restore afterwards), so every admin route has refused everyone on alpha since then. The listing carries outside testers' details and stays in his terminal.
- Then `UPDATE users SET is_admin = true WHERE username = 'mvp-tester'` → `UPDATE 1`; the is_admin listing shows `mvp-tester` alone. Your one-admin shape holds, on the account he named.
- Roster: the admin account is `mvp-tester` (was "dinp only"). #2081's prerequisite is met; he reads the Invites page in his own browser today.
- #2086 (mine, small): a fail-loud migration keyed on `mvp-tester` so a from-scratch rebuild carries the grant; retires the `dinp` constant. It adds a migration file, so it rides a later promotion after xian's word on the migration-diff check.

Verified how: xian's pasted psql output (rowcount and the one-row admin listing), read in full. Layer: the production users table by his hand. Denominator: all 11 accounts.
