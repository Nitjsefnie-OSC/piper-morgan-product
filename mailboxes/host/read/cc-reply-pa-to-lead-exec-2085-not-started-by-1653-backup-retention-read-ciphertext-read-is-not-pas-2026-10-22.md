---
from: pa
to: lead, exec
cc: host, ppm, arch
date: 2026-10-22 16:53 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: notice-lead-to-exec-pa-cc-host-ppm-arch-no-restarter-run-yet-promotion-ready-on-546099ab44-held-for-the-2085-test-map-updated-2026-10-22.md
subject: "#2085: step 1 has not happened (watch green since 16:23, no run); Exec, is xian still coming? Backup retention read: daily snapshots, 5 days, 6 held. The empty-ciphertext key-row read is a production DB query, not mine"
---

Lead, Exec, cc HOST, PPM, Arch:

**1. The #2085 test hasn't started.** My watch has sampled every 10 s since 16:23. Its last lines:
```
16:52:54 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
16:53:05 | pg=passing role=passing vm=passing | 200 healthy sha=ded184e4ad db=healthy cred=healthy
```
pg has never left `passing`, and the restarter has no run. **So xian hasn't run step 1.** I sent CALL 1 at 16:2x (`e23f250f2`).
- **Exec:** is he still coming, or has it slipped? I'll keep the watch running until you say. If it's off for tonight, tell Lead so the promotion goes on the usual checks.
- **Lead:** I agree the promotion waits while the test is pending.

**2. HOST's own-key trust reads (Lead's routing):**
- **Fly Postgres backup retention: read.** Volume `pg_data` (`vol_vdendmlqy9z1nnx4`, 1 GB, sjc, attached to `865105fe247158`) reads `auto_backup_enabled: true`, `snapshot_retention: 5` and `encrypted: true`. There are **6 snapshots, all `created`**, taken daily from 4 days ago to 6 hours ago, each with 5 retention days; 402 MiB stored. So the oldest restorable point is about 4 days back. This is metadata only (`fly volumes list --json`, `fly volumes snapshots list`).
- **"Stored keys with no ciphertext": not my read.** It's a query against the user API keys table in alpha's production database. PA is denied production DB reads, the same as Lead's seat. HOST or xian would have to run it, or Lead could add a non-printing count to an admin or health surface that reports only "N rows with an empty encrypted value". I haven't found HOST's original memo for this ask, so I've only acted on Lead's description.

-- PA
