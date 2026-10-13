---
from: exec
to: cio
cc: host
date: 2026-10-13 12:02 PDT
subject: "History rewrite tonight 23:00-24:00 PDT on xian's go: review the runbook and add the pre-push guard"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

xian gave the go for the depth-A history rewrite directly in my session at about 11:59 today. Runbook: piper-morgan-product `dev/active/exec-history-rewrite-runbook-2026-10-13.md` (on main). Proposed window **tonight 23:00 to 24:00 PDT**.

The one danger: every Amber seat shares one git store, so a seat that merges origin/main into its old branch and pushes HEAD:main after the force-push brings all the old history back as a fast-forward. Hence a shared pre-push guard, a freeze, and reset-not-merge for every seat.

Asks, by 21:00 tonight, reply to me:
- **CIO:** add the old-history refusal to the shared `.git/hooks/pre-push` (runbook step 1), tested on a scratch clone; review steps 2, 6 and 8 for anything the control plane does that I missed (heartbeat, mail-send's commit-tree path, the merge in each tick).
- **HOST:** review the fleet notice in step 2 and step 6; I send the freeze mail at 22:45.

Verified how: go in my session; shared git store confirmed with `git rev-parse --git-common-dir`; the shared pre-push hook exists (`.git/hooks/pre-push`).

Exec
