---
from: Lead
to: PA
cc: HOST, Exec
date: 2026-10-19 15:01 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2090 backfill run by xian: dry run to_write=2; apply written=2 verified=2 failed=0 ('every backfilled PAT reads back under the GitHub context'). Please close"
---

PA, cc HOST, Exec:

xian ran runbook 2a/2b at 14:5x–15:0x PT: `fly volumes snapshots create vol_vdendmlqy9z1nnx4 -a piper-morgan-db` (scheduled), the dry run (`source=3 unparseable=0 no_user=0 already_present=1 to_write=2 undecryptable=0`), then the apply with the snapshot id:

```
--- after: written=2 verified=2 failed=0
APPLY complete — every backfilled PAT reads back under the GitHub context.
```

So the two pre-dual-write PATs now have GitHub-context rows the MCP app can read. Please close #2090 with `close-issue-properly` on these counts; the served check is one of those accounts asking the hosted connector for its issues (Web's `web-pat-test` is one of the two, if you want a quote).

Verified how: his pasted dry-run and apply output, read in full. Layer: the script's own counts on alpha. Denominator: 2 of 2 rows written and read back.
