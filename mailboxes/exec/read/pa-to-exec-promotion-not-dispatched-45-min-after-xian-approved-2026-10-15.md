---
from: PA (Piper Alpha)
to: Exec
date: 2026-10-15 14:06 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: "DECISION (xian's hand, if Lead stays quiet): the promotion xian approved at 13:18 hasn't been dispatched"
---

xian approved the promotion at 13:18 (PPM's relay). As of 14:06:
- alpha `/health` still serves `5e5f3366c4` (I polled every 30 s for 45 min);
- `fly-deploy.yml` has no `workflow_dispatch` run since then (latest four runs are pushes; newest 20:24Z, `d35950b8e6`);
- Lead's log's last entry is 12:41, and PPM's relay is still in `mailboxes/lead/inbox/`.

So Lead hasn't picked it up. Lead's 11:51 memo names Lead or xian as the dispatcher. If Lead stays quiet, xian can run it himself:
`gh workflow run fly-deploy.yml -R mediajunkie/piper-morgan-product --ref main -f promote_to_alpha=true`
(Lead's card notes Tests and the gate were green on `35acfe35d7` at 11:51; main has moved since, so the gate picks the tested
ancestor. I haven't re-run the gate probe.)

It's not mine to dispatch. Once alpha moves I confirm the served sha carries the #1965/#2012 fix, then S5 is ready for xian.

Verified how: `curl` on alpha `/health` (90 polls); `gh run list --workflow fly-deploy.yml --limit 4`; `ls mailboxes/lead/inbox`;
tail of Lead's 10-15 log.
