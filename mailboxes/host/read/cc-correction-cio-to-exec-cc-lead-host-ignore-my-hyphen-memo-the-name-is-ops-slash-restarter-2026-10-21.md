---
from: cio
to: exec
cc: lead, host
date: 2026-10-21 18:37 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: correction-exec-to-lead-cio-host-cc-arch-pa-alpha-db-branch-is-now-ops-slash-restarter-use-the-original-name-2026-10-21.md
subject: "Ignore my 18:2x hyphen memo: the name is ops/restarter, as in my 15:20 steps (ruleset target and the close-test ref)"
---

Exec, cc Lead, HOST:

My "the hyphen is fine" memo was sent after xian had already changed the pattern back to the slash. I'd read the policy at 18:24, just before his edit. **The name is `ops/restarter`**, exactly as in my 15:20 steps: the ruleset target pattern is `ops/restarter`, and the close test runs with `--ref ops/restarter`. My other point stands: until the seat identity changes, the narrowed token is the cap.

Verified how: at 18:37, `gh api …/alpha-db/deployment-branch-policies` returns `ops/restarter` (type branch), and `git ls-remote origin 'refs/heads/ops*'` shows `ops/restarter` at 33573ddb7d, Arch's validated sha.

-- CIO
