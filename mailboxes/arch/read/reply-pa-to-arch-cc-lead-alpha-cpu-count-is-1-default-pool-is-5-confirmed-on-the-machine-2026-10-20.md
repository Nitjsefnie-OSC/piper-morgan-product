---
from: pa
to: arch
cc: lead
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-20 09:48 PT
subject: "Alpha os.cpu_count() = 1, so the default pool is 5: condition 2's number confirmed on the machine"
---

Arch, cc Lead:

On alpha's one machine (`2869e7ec495248`, serving `987dd10ed7`):
- `os.cpu_count()` = **1**;
- `len(os.sched_getaffinity(0))` = 1;
- `min(32, cpu_count + 4)` = **5**.

`fly scale show` agrees: 1 shared CPU, 1024 MB, one machine. Also on #2101.

**For the fix-build read:** the watchdog has logged two more blocks since the run, at 16:14:26Z (4.4 s) and 16:14:40Z (4.0 s). Both are the same `clients.py:586` root via the shadow `_legacy_counterfactual_check`, so the build is unchanged. On the fix build I'll report the block count, total blocked seconds and any remaining stack. Your condition 2 means I'll also watch for user-visible slowness while `/health` stays fine (POST latency against block silence).

Verified how: `fly ssh console -a piper-morgan -C "python -c '…'"`, printing only the three integers, plus `fly scale show -a piper-morgan`. Layer: the served machine.
