# Alpha promotion hold

- **Held by:** PA (Piper Alpha), from 2026-10-23 10:37 PT.
- **Why:** the #2085 restarter's attended test 3. xian stops alpha's Postgres (B1) and dispatches the lease-free restarter (B2). A promotion during the test would muddle the read of the restart.
- **Clears when:** PA calls test 3 done: the DB machine's pg check reads passing and alpha `/health` reads `database: healthy`, after the restarter run or the undo.
- **Removed by:** PA, with the "done" mail. If it outlives that, Exec or xian.
