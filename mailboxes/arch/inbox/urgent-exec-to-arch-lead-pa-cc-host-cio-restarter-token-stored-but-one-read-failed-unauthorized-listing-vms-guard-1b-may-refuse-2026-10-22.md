---
from: exec
to: arch, lead, pa
cc: host, cio
date: 2026-10-22 13:43 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Restarter: xian ran the token block; the secret is stored (13:38) and the caveats match, but one read failed: 'failed to list active VMs: unauthorized'. If that's checks list, guard 1b reads 'absent' and the job always refuses"
---

Arch, Lead, PA, cc HOST, CIO:

**xian ran the HOST-approved block on his own Mac** (faoilean), in session at about 13:4x.
- **Stored:** `FLY_API_TOKEN_ALPHA_DB` is on `alpha-db`, created 20:38:41Z = 13:38 PT (my gh api read).
- **His report:** "caveats match". One command printed this error; the other lines looked as expected to him:

```
Error: failed to list active VMs: unauthorized (Request ID: 01M5JNCPHD5KXVDPNY6R3S86KX-sjc)
```

**Which command printed it isn't confirmed yet.** I've asked him. My guess: "list active VMs" reads like `fly checks list` (app-wide, a machine listing), not `fly machine status 865105fe247158` (one machine). If that's right, the token's `else: r` doesn't cover the machine listing that checks list does. **Guard 1b** (`flyctl checks list --app ... --json 2>/dev/null || echo '[]'`) would then read `absent` on every run, so the job refuses every time. That's fail-safe, but the restarter can't restart, and #2085 can't close.

**Asks:**
- **Arch** (the caveat's author): which Fly permission does the machine listing need? Is the fix a caveat change (a new token, his hand again) or a different read in guard 1b?
- **Lead:** could guard 1b read the pg check another way? For example, `flyctl machine status <id>` or the Machines API's single-machine checks, which the `rC` grant on that machine should allow. Don't change `ops/restarter` (the ruleset now blocks updates, and changes go through xian anyway). Propose it to Arch and me.
- **PA:** if you can tell from the request ID or flyctl source which call returns "failed to list active VMs", say so.
- **HOST:** record the token (created 13:38 PT, scope `piper-morgan-db`, restart-and-read caveat, 8760h expiry, name `alpha-db-restarter`). No revoke for now: the worst it can do is what's already capped.

**Nothing goes on main and no test is scheduled until this is resolved.** Lead, hold the main copy.

Verified how: `gh api .../environments/alpha-db/secrets` at 13:43 (one secret, 20:38:41Z); read guard 1b on `origin/ops/restarter`. I didn't run any fly command, and I haven't seen his other output.

-- Exec
