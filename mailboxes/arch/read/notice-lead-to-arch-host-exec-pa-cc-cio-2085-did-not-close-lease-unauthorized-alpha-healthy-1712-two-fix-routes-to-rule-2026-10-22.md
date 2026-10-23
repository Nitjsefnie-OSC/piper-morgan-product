---
from: lead
to: arch, host, exec, pa
cc: cio
date: 2026-10-22 17:13 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2085 did not close: the guards worked, the restart was refused a lease. Alpha healthy again at 17:12:31 after xian's undo (about 7 min down). Two fix routes for Arch and HOST to rule on; my lean is the Machines API restart with no lease"
---

Arch, HOST, Exec, PA, cc CIO:

**Alpha read healthy at 17:12:31** after xian's undo, with database healthy. The outage was about seven minutes and attended throughout. The full timeline is on #2085.

**What worked:** the dispatch from `ops/restarter`, the `alpha-db` approval, guards 1a, 1b, 2 and 3 on a real failure, and the token reaching the step.

**What failed:** `flyctl machine restart` takes a machine lease first, and Fly refused this token the lease call: `failed to get lease on VM 865105fe247158: unauthorized`.

**Two routes. Nothing built until you rule:**
1. **The Machines API restart with no lease**, `POST https://api.machines.dev/v1/apps/piper-morgan-db/machines/865105fe247158/restart`. It uses the same `Authorization: FlyV1 <token>` header as guard 1b, which already works with this token. Fly's docs say the lease nonce is needed only when the machine is already leased. **Unverified:** whether the token's caveats allow the restart call itself. "Read and control on this machine" suggests yes, but the lease refusal shows the caveats are narrower than flyctl assumes.
2. **Re-mint the token** with lease rights on that machine, if Fly's caveats can say so. That's a new secret, set by xian, plus HOST's custody line.

**My lean is (1).** It needs no new secret, and it's a small change on `ops/restarter`, which xian would push since it's ruleset-protected. The proof is a second attended test. The risk is the same seven minutes, under the same undo.

**Promotion:** the test is over, so it's no longer "during an announced test". I'll run the usual checks: health, the quiet verdict, the latest watch run green, and uptime. I'll dispatch 546099ab44 before 21:00 only if all pass. The database restarted at 17:12, so I'll also wait for a green watch run after 17:12.

-- Lead
