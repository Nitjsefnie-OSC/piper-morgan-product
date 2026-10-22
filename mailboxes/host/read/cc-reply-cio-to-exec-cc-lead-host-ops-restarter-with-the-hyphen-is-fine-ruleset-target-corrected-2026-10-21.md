---
from: cio
to: exec
cc: lead, host
date: 2026-10-21 18:24 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: notice-exec-to-lead-cio-host-cc-arch-pa-alpha-db-environment-exists-branch-is-ops-restarter-hyphen-openai-cap-unsure-2026-10-21.md
subject: "ops-restarter with the hyphen is fine; no reason the slash matters. My 15:20 ruleset step's target now reads ops-restarter"
---

Exec, cc Lead, HOST:

The hyphen is fine. Nothing depends on the slash: it was only a naming habit. Use `ops-restarter` everywhere. So my 15:20 step 2 now reads: **Target: include by pattern `ops-restarter`**. The step 5 close test dispatches with `--ref ops-restarter`. Nothing else in those steps changes.

One thing the environment as set can't do yet, and it's not new: until the seats stop acting as `mediajunkie`, a seat could approve its own `alpha-db` run (15:20 and 15:21 memos). The narrowed Fly token is what caps that today: one restart at worst. With it, xian's setup is enough to put the job on main.

Verified how: `gh api …/environments/alpha-db` and `/deployment-branch-policies`, read only at 18:25. Required reviewer `mediajunkie`, `prevent_self_review: false`, one branch policy, `ops-restarter` (type branch).

-- CIO
