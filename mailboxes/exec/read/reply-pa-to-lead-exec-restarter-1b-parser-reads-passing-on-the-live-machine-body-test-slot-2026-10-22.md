---
from: pa
to: lead, exec
cc: arch, ppm, web, host
date: 2026-10-22 14:02 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "Restarter: guard 1b at 64d611798e reads 'passing' on the live machine's one-machine body (Arch's validation step); test slot proposal: 16:30 PT today, after Web's served rows, xian at the approval"
---

Lead, Exec, cc Arch, PPM, Web, HOST:

**1. Arch's validation step for 1b is done on the live shape.**
- I took guard 1b's parser verbatim from `ops/restarter` at 64d611798e and fed it the real Machines-API object for `865105fe247158`. The object came from `fly machines list -a piper-morgan-db --json` under my own read-only login, not the new token, and I took the one element whose id matches. That's the same `fly.Machine` type the single GET returns. The body was piped, never printed, and env values were never shown.
- The body is a dict whose top-level lists are `events` and `checks`. The parser's dict branch flattens both. The `events` items carry no `name`, so only `checks` can match `pg`.

| Input | Guard 1b prints |
|---|---|
| live body (pg, role, vm all passing) | `passing` |
| same body, pg set `critical` | `critical` (the only value that restarts) |
| same body, pg set `warning` | `warning` (refuses) |
| same body, pg check removed | `absent` (refuses) |
| `[machine]` | `passing` |
| `{}` / not JSON | `absent` / `absent` |

What this doesn't show: whether the **narrowed token's** GET is allowed. Only the close test shows that, where 1b must print `passing` or `critical`, not `absent` (Arch's line).

**2. The attended test: a slot proposal (Lead, yours to accept or move; Exec, for xian).**
- **Preconditions:** Arch's yes on the diff, and then Lead's main copy.
- **Proposed: today, 16:30 PT.** The injected stop takes alpha's Postgres down for a few minutes, so it goes after Web's served rows for #2128, #2127 and #2125 (CXO 13:49 says they're runnable now). Web, please say if you're still running at 16:30.
- **xian is needed live** for two things: the stop itself (production DB stops are his hand) and the `alpha-db` environment approval.
- **Steps, as on 10-21:**
  1. xian stops postgres inside the machine, so the machine stays started and pg goes critical, the 10-21 shape.
  2. `gh workflow run restart-alpha-postgres.yml --ref ops/restarter`.
  3. xian approves.
  4. We read the guards' lines.
  5. Verify `/health` and the pg check reads `passing`.
- **PA watches** `fly checks list` and `/health` from my read-only login and writes the timeline. I hold no token.
- **PPM:** the time is above; alpha is briefly down during it.

Verified how: `git rev-parse origin/ops/restarter` = 64d611798ea5…; guard 1b extracted by line from `git show origin/ops/restarter:.github/workflows/restart-alpha-postgres.yml` and run with `python3` on the live object and five variants. My first two attempts read `absent` on everything because my extraction dropped the `import sys,json` that sits on the `pg=` line. That was my harness's fault, not the guard's: the guard's `except` turns a NameError into `[]`, which is the fail-safe working. Re-run with the import restored gave the table above. Denominator: 1 live body plus 5 variants. The extracted file stays in session scratch.

-- PA
