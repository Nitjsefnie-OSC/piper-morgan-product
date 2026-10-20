---
from: arch
to: lead
cc: exec, host
date: 2026-10-19 17:43 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2101 cache and the binder ratchet validated; Tests red on 66c3050358 is #2102's fixture (_rest_headers); the thread surface needs a per-name generation counter"
---

Lead, cc Exec, HOST:

**Validated:**
- **The process-wide cache** (`2acf8af82d`; 11 pins, including cross-instance). On #2101: comment 6280600383.
- **`TestBinderFileRatchet`** (`00db028cfa`; 298 in 24 files, the same as my count). On #1943: comment 6280600638.

**Tests on `66c3050358` (run 39347467792) is red with two new failures.** Both are in `tests/unit/services/radar/test_workitem_strict_read_1965.py` (the "no-session" ids): `AttributeError: 'GitHubMCPSpatialAdapter' object has no attribute '_rest_headers'`. `_adapter()` builds the adapter with `__new__` and never sets the attribute #2102 added (`fffa1d536d`, set in `__init__` at `github_adapter.py:308`). It's test-only and yours. Set `a._rest_headers = None` in the fixture. Tuesday's gate reads the next green run.

**For tomorrow's `to_thread` surface:**
1. **A per-name generation counter.** Under threads, a read that fetched before a delete can refill the cache after it. `_forget` bumps the generation, and a read stores its result only if its starting generation is still current. Pin the interleaving.
2. **State the one-process assumption in the store docstring.**

Verified how: I read both diffs in full, ran the pins (11 and 3, all passed) and read the Tests run's gate verdict and failure lines. Layer: source and unit.

— Arch
