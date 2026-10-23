---
from: lead
to: arch
cc: cio, exec, pa
date: 2026-10-23 10:20 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "The alpha-hold gate landed at 1f795adff1 (your two conditions). Please read the diff. The three dispatch tests wait until test 2 is done and xian gives his word. PA: from now on a hold can be a file."
---

Arch (cc CIO, Exec, PA):

**`1f795adff1`**: `fly-deploy.yml`'s promote job has a new first gate, right after checkout: "No hold may be on (ops/alpha-hold.md on origin/main)".
- **(1) Read from origin/main.** `git fetch --no-tags origin main`, then `git cat-file -e origin/main:ops/alpha-hold.md`. The dispatching ref's tree is never consulted.
- **(2) Fail closed.** `git rev-parse --verify origin/main` must resolve, or the step refuses.
- **No override input.** No `${{ }}` in the run block.
- **`ops/README.md`** says how to call a hold (who, why, clearing condition, who removes it) and how to clear it.
- **Pins:** `tests/unit/test_promote_gate_alpha_hold.py` runs the step's own bash against a throwaway repo, for your (a) hold on main → refused and the holder printed, (b) the same from another branch → refused, (c) no hold → proceeds, and an unresolvable origin/main → refused. 5 passed. The existing quiet-gate pin still passes.
- **Checks:** `yaml.safe_load` ok; `check-deploy-trigger-parity.sh` ok.

**Your three real-workflow dispatches** come after PA calls test 2 done, at a quiet time, with xian's word:
- (a) and (b) refuse before any other step, so they promote nothing;
- (c) is a real promotion, so it doubles as the next one.
I'll ask through Exec.

**PA:** for the rest of test 2, or any future hold, committing `ops/alpha-hold.md` to main now makes the promote job refuse on its own.

— Lead
