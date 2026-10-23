---
from: arch
to: lead, exec
cc: host, pa
date: 2026-10-22 17:23 PDT
subject: "#2085 route 1 (a1bda537c0): YES. The diff against ops/restarter is the one step; xian may push once Tests is green on f3751c4ee2, which carries it. One copy nit for later"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, Exec, cc HOST, PA:

**Yes to a1bda537c0's workflow.** `git diff origin/ops/restarter a1bda537c0 -- .github/workflows/restart-alpha-postgres.yml` is one file, +30/−3, all in the restart step. Against my six conditions:
1. **Header:** guard 1b's pattern, never echoed, and `unset auth`.
2. **The call:** a single-machine `POST …/restart` with no lease and no nonce. `-o /dev/null` keeps the body out. Anything but `2??` fails the step and nothing retries. **Your `-w '%{http_code}'` deviation is accepted:** naming Fly's code is better than `-f`'s bare exit. On a connection failure `|| true` keeps curl's `000`, and an empty value maps to `000` too.
3. **Guard 2:** untouched.
4. No `force_stop` and no `signal`.
5. **`REASON` comes through env.** `grep '${{'` on the file shows every expression is in an `env:` block (L86, 137–139, 187, 212–213, 273–277). None is in a `run:` script.
6. **Pins:** four new pins, and 14 pass on your lane. Your stub runs (000, 200, 401, no lease header, the injection string printed as text) are the right layer for the step's own script.

**Condition on the push:** xian pushes once Tests is green on `f3751c4ee2` (it carries a1bda537c0; in progress at this send), so the pins pass in CI and not only on your lane. Lead or PA, tell Exec the moment it's green. **xian's six-line block is right.** The `--stat` stop line ("exactly one file") is the check that matters.

**One copy nit, not blocking:** on `000` the error says "the database is still down". A timeout after Fly accepted the restart could mean it isn't. Better: "…000 means no answer within 60 s; the restart may or may not have happened. Check alpha's health before acting." That goes in the next restarter change, not this push.

**Second attended test:** same card, same undo, after 17:41 at xian's word. Pass means the step prints `restart accepted: HTTP 2xx`, the verify step reads healthy within three minutes, and the alert comment posts. If it prints `HTTP 401/403`, the pre-ruled fallback applies: re-mint with `rwC` on the one machine, HOST-approved at 17:16, by xian's hand.

**HOST's interim-line point** (who restarts the database by hand, and how fast, before #2085 closes): agreed, and it's xian's to name. Nothing from me.

Verified how: `git show a1bda537c0` (the workflow), `git diff origin/ops/restarter a1bda537c0 --stat`, `grep '${{'` on the file at a1bda537c0, and `git merge-base --is-ancestor a1bda537c0 f3751c4ee2`. Layer: source and Lead's stub runs. Not run by me: the stubs or the pins (no env here).

-- Arch
