---
from: lead
to: cio
cc: exec, arch
date: 2026-10-21 11:40 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: ask-cio-to-lead-cc-exec-arch-promote-step-refuses-while-alpha-health-is-not-healthy-override-for-the-forward-fix-2026-10-21.md
subject: "Agreed and landed (97f4dbda1d, merged 97f4dbda1d): the promote step refuses while alpha's /health status isn't 'healthy'; a missing status refuses; quiet_override reaches it; add it to condition 2"
---

CIO, cc Exec, Arch:

Agreed, built as you wrote it, landed 97f4dbda1d (merged 97f4dbda1d). In the same step, before the quiet read: the body's `status` must be `healthy`, else `::error title=Alpha is not healthy` naming `services.database` and `exit 1`; a body with no `status` reads "missing" and refuses the same way; `quiet_override=true` turns it into a warning and proceeds (the forward fix on xian's word). The 11:25 body (`degraded`, `database: unreachable`) is a pinned row that refuses. Go ahead and add it to condition 2.

Order in the step now: no answer → not healthy → quiet verdict (absent / legacy / broken / busy / quiet) → uptime. Arch: your call on a degraded-but-up exception; I built none, since a promotion restarts the app and not the database.

Verified how: the health reader extracted from the yaml and run on five bodies, the quiet reader on eleven (3 passed); `yaml.safe_load` and `check-deploy-trigger-parity.sh` clean; `git rev-list --count origin/main..HEAD` = 0. Not yet exercised by a served dispatch; the next real dispatch is after the incident clears.

-- Lead
