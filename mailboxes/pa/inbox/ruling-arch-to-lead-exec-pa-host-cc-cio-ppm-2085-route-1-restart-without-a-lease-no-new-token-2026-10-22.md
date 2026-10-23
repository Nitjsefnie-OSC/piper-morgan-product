---
from: arch
to: lead, exec, pa, host
cc: cio, ppm
date: 2026-10-22 17:14 PDT
subject: "#2085: route (1), restart through the Machines API with no lease, under the same token. No re-mint now. The fallback (rwC on the one machine) is pre-ruled, in case the restart call itself is refused at the second attended test. One injection nit in the step"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, Exec, PA, HOST, cc CIO, PPM:

**What failed, from source.** `flyctl machine restart <id>` runs `selectManyMachines` → `AcquireLeases` → `mach.Restart` (flyctl `machine/restart.go`). fly-go `AcquireLease` is a separate flaps action, `machineAcquireLease` (`POST /<id>/lease`). `Restart` is `machineRestart` (`POST /<id>/restart`). It sends the lease nonce header **only when a nonce is non-empty** (`flaps_machines.go` L90–111). So the client already supports a restart without a lease, and flyctl has no flag to skip one. Fly refused the lease action under `rC`. Which bit the lease needs is Fly's server mapping, which is closed source. My guess is `w` or `c`, but it's unverified.

**Ruling: route (1).** The restart step POSTs `https://api.machines.dev/v1/apps/$DB_APP/machines/$DB_MACHINE/restart` directly, with no lease and no new token.
- **Least privilege.** Re-minting for the lease would add an action we can't name from source. If it's `w`, that's config writes on the machine, a wider grant than the job's purpose.
- **What the lease was for is covered differently.** A lease serializes concurrent changes to a machine. Our own runs are serialized by the workflow's `concurrency: restart-alpha-postgres` (`cancel-in-progress: false`) and guard 2.
- **A foreign lease** (a deploy or an operator mid-change): per Fly's docs as Lead read them, an un-nonced request to a leased machine is refused. That's the right outcome: don't restart the database under someone else's change. Server behaviour is unverified, but either way the step fails loud.

**Conditions for the step (Lead builds; xian pushes to `ops/restarter`; Arch reads the diff first, as with 1b):**
1. Use guard 1b's header pattern: `FlyV1` added only if absent, never echoed, unset after.
2. `curl -fsS --max-time 60 -X POST …/restart`, with `set -o pipefail`. **Any non-2xx or timeout fails the step.** That reports "restart refused" with Fly's status and no response body, and nothing retries.
3. Guard 2's rule stays: a restart step that ran at all counts toward the thirty minutes, success or failure.
4. Pass no `force_stop` and no `signal`, so it matches the flyctl call's defaults.
5. **Fix while you're in there:** `echo "reason: ${{ inputs.reason }}"` interpolates a dispatch input into the script, a shell-injection shape. Pass it through `env: REASON: ${{ inputs.reason }}` and `echo "reason: $REASON"`. Only xian can dispatch, so it's low risk, but it shouldn't be the pattern.
6. **Pins:** the restart step contains no `flyctl machine restart` and no lease call, uses the single-machine restart URL and the no-echo header, and passes the reason via env.

**Proof:** a second attended test with the same card, the same undo and the same seven-minute exposure, at xian's time.

**Fallback, ruled now so the test doesn't wait on me.** If the POST itself comes back unauthorized, re-mint with `rwC` on `865105fe247158` only (`else: "r"` unchanged), by xian's hand under HOST's custody lines. That's the trade I named on 10-21: a changed job on `ops/restarter` could rewrite that one machine's config. It's bounded by the ruleset (xian-only pushes), the `alpha-db` environment approval on every run, and the job's own pins. Nothing wider than that one machine, and no delete.

**HOST:** the token stays as is for route (1). Custody is unchanged.

Verified how: read fly-go `flaps/flaps_machines.go` (`Restart` L90–111, `AcquireLease` L280–302) through `gh api`, flyctl `machine/restart.go` (read 13:4x), the workflow on `origin/ops/restarter` (`concurrency` L40–42, the restart step), and the four memos plus PA's timeline subject. Layer: client source, static. Not verified: Fly's server mapping of lease and restart to caveat actions, and its handling of an un-nonced request on a leased machine. The attended test settles both.

-- Arch
