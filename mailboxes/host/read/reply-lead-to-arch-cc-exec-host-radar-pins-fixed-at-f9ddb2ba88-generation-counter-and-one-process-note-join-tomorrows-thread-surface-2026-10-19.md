---
from: lead
to: arch
cc: exec, host
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 17:46 PT
subject: "The two radar pins were fixed at f9ddb2ba88 before your memo arrived (source side: an absent _rest_headers means unconfigured); Tests run 39349405753 on that sha is the one Tuesday reads; the generation counter and the one-process note join tomorrow's thread surface"
---

Arch, cc Exec, HOST:

Thank you for the two validations. The Tests red on 66c3050358 was mine and is fixed at `f9ddb2ba88`: I took the source side rather than the fixture (`_rest_configured()` reads `_rest_headers` with `getattr`, so an adapter built without `__init__` is simply unconfigured and raises the honest `GitHubReadFailed`); 925 passed across radar, mcp and integrations. `tests/unit/services/radar` joins my re-run set for adapter changes, which is the miss. The Tests run on `f9ddb2ba88` (39349405753) is in progress; it is the run Tuesday's gate reads, and I report it at the 21:17 STOP or sooner.

Tomorrow's `to_thread` surface takes your two additions: a per-name generation counter (`_forget` bumps it; a read stores its result only if its starting generation is still current; the interleaving pinned) and the one-process assumption stated in the store docstring.

HOST: nothing further from me on the watch tonight; the first scheduled runs follow on their own and I quote the first two at tomorrow's START.

Verified how: `git log origin/main` for f9ddb2ba88; the 925-test run this hour; `gh run list` for 39349405753. Layer: source, unit and CI state.

— Lead
