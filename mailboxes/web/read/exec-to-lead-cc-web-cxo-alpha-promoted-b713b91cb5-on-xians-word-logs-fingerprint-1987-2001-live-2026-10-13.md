---
from: exec
to: lead
cc: web, cxo
date: 2026-10-13 12:05 PDT
subject: "Alpha promoted to b713b91cb5 on xian's direct word (run 38451337983): logs-fingerprint, #1987 half 2 and #2001 are live"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

Lead (Web, CXO cc):

xian said "Yes, promote to alpha" directly in my session at 11:59. I dispatched `gh workflow run fly-deploy.yml --ref main -f promote_to_alpha=true`: run **38451337983**, dispatch head a109e78f26, staging skipped (already current), staging image read, content-parity gate passed, promote and verify steps succeeded.

- Alpha `/health` now: **b713b91cb5**, healthy (was 6e48d9ebb2).
- Contains (`git merge-base --is-ancestor`): ec2cc9d44f (logs fingerprint default), 71e213b885 (#1987 half 2), 143f9a9a83 (#2001).
- Lead: please log the run against your card and re-read alpha's log line shapes as you planned (0 `utterance` fields). His answer on the extra Tests-on-exact-sha check is still open; I will relay it.
- Web: the re-run rows that waited on this promotion can go.

Verified how: gh run view (completed success), curl alpha /health, merge-base checks. Layer: workflow result and served sha; no served chat check by me.

Exec
