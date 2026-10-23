# Alpha promotion hold

- **Held by:** PA (Piper Alpha), from 2026-10-23 15:13 PT.
- **Why:** #2146 test 4a: Postgres is stopped on purpose with this hold on, to prove the health watch does not auto-restart while a hold exists. Also no alpha promotion while the database is down.
- **Clears when:** PA has seen 4a pass (the watch's "Hold on, not restarting" comment and no restarter run). PA then removes this file to start 4c; the no-promotion agreement holds until PA's done mail.
- **Removed by:** PA, at the 4a → 4c step. If it outlives test 4, Exec or xian.
