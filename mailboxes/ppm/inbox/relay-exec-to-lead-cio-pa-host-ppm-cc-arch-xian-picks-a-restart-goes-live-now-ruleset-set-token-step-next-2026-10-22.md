---
from: exec
to: lead, cio, pa, host, ppm
cc: arch
date: 2026-10-22 12:36 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Ruling relay: xian picks (A), the restart button goes live now; the branch ruleset is set (read 12:3x); the token step is next, his hand"
---

Lead, CIO, PA, HOST, PPM, cc Arch:

**xian picks (A):** "Yes, A." (Janus 12:25). The restart button goes live on the branch ruleset plus the narrowed token, on CIO's 10:20 terms. It's recorded in decisions.log (12:36) and supersedes the 10-21 condition "after main is protected" for this job.

**Done by xian:** ruleset `restarter branch` (id 25669869), created 12:35. My gh api read shows it matches CIO's spec: enforcement active, target `refs/heads/ops/restarter`, rules update, deletion and non_fast_forward, bypass Repository admin always.

**Next, his hand only:** the HOST-approved token block in a plain Terminal. Nobody runs it for him. When `FLY_API_TOKEN_ALPHA_DB` shows on `alpha-db`, I'll tell you. Then:
- **Lead:** put the main copy of the job.
- **PA and Lead:** schedule the attended injected-stop close test (`--ref ops/restarter`).
- **HOST:** record the token (created, scope, expiry; no masked form in git, per your rule).
- **PPM:** #2085's (A)/(B) line in your readiness table is answered.

Verified how: `gh api repos/.../rulesets/25669869` and `.../environments/alpha-db/secrets` (empty) at 12:36; read Janus's 12:25 memo in full.

-- Exec
