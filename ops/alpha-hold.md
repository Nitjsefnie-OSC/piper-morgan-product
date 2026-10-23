# Alpha promotion hold

- **Held by:** PA (Piper Alpha), from 2026-10-23 10:22 PT.
- **Why:** the #2085 restarter's attended test 2. xian stopped alpha's Postgres at 09:44 (B1). A promotion during the test would muddle the read of the restart.
- **Clears when:** PA calls test 2 done: the DB machine's pg check reads passing and alpha `/health` reads `database: healthy`, after the restarter run (B2/B3) or the undo (B4).
- **Removed by:** PA, in the same commit window as the "done" mail. If it outlives that, Exec or xian.
