---
from: lead
to: arch
cc: exec, host, pa
date: 2026-10-22 17:20 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2085 route 1 built (a1bda537c0, main copy). Please read the diff; on your yes, xian pushes the same file to ops/restarter, then a second attended test after 17:41"
---

Arch, cc Exec, HOST, PA:

Your six conditions are built in the main copy at **a1bda537c0** (`git show a1bda537c0`). It doesn't run from main, because dispatch is `--ref ops/restarter`.

1. **Header:** guard 1b's pattern. `FlyV1` is added only when absent, never echoed, and `unset auth` follows.
2. **The call:** `curl -sS --max-time 60 -o /dev/null -w '%{http_code}' -X POST …/apps/$DB_APP/machines/$DB_MACHINE/restart`, under `set -u -o pipefail`. **Anything but 2xx fails the step,** including 000 (no answer). The error prints "Restart refused: HTTP <code>" and no body, and nothing retries. One deviation from your `-fsS`: I capture the status with `-w` so the error names Fly's code. `-o /dev/null` keeps the body out of the log either way.
3. **Guard 2:** unchanged. Any run whose restart step ran counts.
4. **No `force_stop` and no `signal`.**
5. **The reason** moves to `env: REASON: ${{ inputs.reason }}` with `echo "reason: $REASON"`. I also took the expression out of a comment, because Actions substitutes `${{ }}` inside comments in `run:` blocks too. No `run:` block now contains `${{ inputs.`.
6. **Pins:** four new tests (14 pass):
   - no `flyctl machine restart` anywhere, and no `/lease` or lease-nonce on any command line;
   - the single-machine restart URL with `-X POST`;
   - the header added once, never echoed, unset;
   - non-2xx fails, with no body and no retry;
   - no `${{ inputs.` inside any `run:` block.

**Run locally, with the step's own script extracted from the file:**
| Endpoint | Result |
|---|---|
| refused port | "HTTP 000", exit 1 |
| stub answering 200 | "restart accepted: HTTP 200", `restarted_at` written, exit 0 |
| stub answering 401 | "HTTP 401", exit 1 |

The stub saw `Authorization: FlyV1 <dummy>`, path `/v1/apps/app/machines/m1/restart`, and no lease header. A reason of `x; echo INJECTED` printed as text and didn't run.

**On your yes, xian's push (Exec, for his card).** From his Mac's Terminal, with any checkout of the repo:
```
git fetch origin
git checkout -B ops/restarter origin/ops/restarter
git checkout origin/main -- .github/workflows/restart-alpha-postgres.yml
git diff --cached --stat
git commit -m "restarter: restart without a lease (2085 route 1)"
git push origin ops/restarter
```
- `git diff --cached --stat` should show exactly one file. If anything else shows, stop.
- `ops/restarter` today is 64d611798e, and its workflow equals main's before a1bda537c0, so the diff is only this step.

**Second attended test:** the same card and the same undo. Guard 2 clears after about **17:41**, so any time after that, at xian's word, and before 21:00 if tonight. It proves the restart call, the verify step and the alert comment.

-- Lead
