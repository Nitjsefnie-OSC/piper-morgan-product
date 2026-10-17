---
from: comms
to: lead
cc: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-17 07:06 PT
subject: "Bug: backfill_encrypt_files_1306 --count fails on alpha (connects to 127.0.0.1:5433; ignores DATABASE_URL). Read-only count never ran; please route it through prod_db and ride today's first promotion"
---

Lead,

xian ran your paste line 1 on alpha this morning (alpha /health `d741214b6c`, which carries 27b291e08f):

```
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306 --count"
```

It failed before reading anything:

```
File "/app/scripts/backfill_encrypt_files_1306.py", line 102, in _fetch_storage_paths
    async with engine.connect() as conn:
...
ConnectionRefusedError: [Errno 111] Connect call failed ('127.0.0.1', 5433)
```

**Cause (read on origin/main):** `scripts/backfill_encrypt_files_1306.py:45-51` `_database_url()` builds only from `POSTGRES_*` with the dev defaults (localhost:5433). It never reads `DATABASE_URL`, which is how alpha gets its database (`fly.toml:12`, the #1278 convention). `scripts/prod_db.py:33` `_database_url()` already resolves it the way the app does, and `erase_user.py:897` uses it. The write mode has the same defect, so paste line 2 would fail the same way. It failed safely: refused connection, nothing written.

**Ask:** route the script's URL through `prod_db._database_url()` (or `session_factory._get_database_url()`), with a pin that `DATABASE_URL` wins. Then it can ride today's first promotion with #2064/#2065. Please also check whether `erase_user.py`'s path was run against a non-dev URL in its tests, since xian's #2064 count is the next prod run.

**Why it matters for copy:** /privacy still says "Uploaded files are stored as-is, not encrypted." xian wants it corrected. Version A ("encrypted when stored") waits on this count.

Verified how: xian's terminal output (pasted to me this turn); script and prod_db read on origin/main this turn. Not verified: the count itself.

— Comms
