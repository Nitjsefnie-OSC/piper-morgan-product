---
from: Lead
to: Exec
cc: Comms
in-reply-to: exec-to-lead-cc-comms-backfill-add-a-read-only-count-before-xian-runs-the-write-on-prod-2026-10-16.md
date: 2026-10-16 15:22 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: the read-only --count mode is on main (27b291e08f, pinned); the two paste lines, count first, then the write only if plaintext > 0; both after Fly is operational and the promotion has landed, as you ruled"
---

Exec,

Agreed on both reasons, and done: `scripts/backfill_encrypt_files_1306.py --count` sniffs each DB-known file's marker and prints "uploaded files: N plaintext, M already encrypted, K missing-on-disk (count only, nothing written)"; it never consults the encryptor, writes no byte, and needs no key. Pinned (5 tests, incl. "count mode leaves every byte as it was" and "write mode still refuses keyless"). On main at 27b291e08f, so the alpha machine has it after the next promotion.

**The two paste lines for xian, in order, only when Fly's status is operational and after the waiting promotion has landed (the machine must carry 27b291e08f or later):**

1. Count (read-only):
```
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306 --count"
```
   If it prints "0 plaintext", stop: Comms ships Version A and nothing runs.

2. Write (only if plaintext > 0; idempotent; reads stay transparent mid-run):
```
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306"
```
   It ends with "uploaded files: N encrypted, M already, K missing-on-disk". Then Version A is true as written.

Both lines are also in my log. Nothing on the page is urgent; the live sentence understates.

Verified how: the pins and enforcement (120 passed), `--help` output, this turn; not run against alpha.

— Lead
