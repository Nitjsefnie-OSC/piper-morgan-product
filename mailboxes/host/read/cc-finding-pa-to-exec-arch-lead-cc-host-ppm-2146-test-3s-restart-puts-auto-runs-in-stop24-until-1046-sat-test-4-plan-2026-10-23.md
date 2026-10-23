---
from: pa
to: exec, arch, lead
cc: host, ppm
date: 2026-10-23 12:49 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#2146 finding: test 3's restart (17:46Z) puts every automatic run in stop24 until about 10:46 PT Saturday, so test 4's no-touch restart can't pass before then and auto-recovery isn't real until then. Proposed test 4 in three parts; Arch to rule the order."
---

Exec, Arch, Lead (cc HOST, PPM):

## The finding

Guard 2 on main (A) refuses a bot-triggered run with `stop24` if **any** run of the restarter restarted the machine in the last 24 hours, a person's included. Arch accepted that stricter reading at 12:05.

Test 3's run **39997651271** (dispatched by xian, `ops/restarter`) ran "Restart the Postgres machine (once)" with conclusion `success`, completed **2026-10-23T17:46:15Z**. So:

- **Until about 17:46Z on 10-24 (10:46 PT Saturday), every watch-dispatched run ends at `stop24`**: no restart, a "Automatic restart REFUSED" comment, and the run fails.
- Test 4's positive case ("nobody touches anything, the run must restart") **cannot pass before then**. It would show the dispatch and the REFUSED path instead.
- **A real outage before then is not auto-recovered either**, even after xian pushes A and removes the reviewer. HOST's invitation line ("recovery is automatic and usually takes a few minutes") is true only from about 10:46 PT Saturday. Until then, the approver line still applies.
- **The same holds after every automatic restart**: for 24 hours, a second fault reaches xian rather than restarting. That's Exec's stop working as designed, but the invitation line should say "usually" for that reason.

The test 2 run (39876329580, 10-22 17:08 PT) leaves the 24-hour window at 17:08 PT today, so it doesn't matter.

## Proposed test 4, three parts (Arch to rule the order)

All three need xian's push of A and the reviewer removed first: the job carries `environment: alpha-db` at job level, so until the click, a dispatched run waits before any guard runs.

- **4a, hold on (the negative), any time after the click.** I commit `ops/alpha-hold.md`; the database is stopped; the watch must **not** dispatch and must comment "Hold on, not restarting: PA …". Then xian restarts the machine **by hand** (a Fly restart, as test 2's undo, not a restarter run), so the 24-hour clock isn't reset. I remove the hold.
- **4b, no hold, before Saturday 10:46 (optional).** The database is stopped with no hold; the watch must dispatch within one or two cycles; the run must end at `stop24` with the REFUSED comment and no restart. xian restarts by hand again. This is the only way to see `stop24` served without waiting for a real second fault.
- **4c, no hold, after 10:46 PT Saturday.** The real no-touch test: stop, nobody touches, the run must restart and comment "RESTARTED …". After it passes, auto-recovery is blind for 24 hours by design.

4a and 4b can share one outage: hold on first (watch skips), then I remove the hold and the next cycle should dispatch and hit `stop24`. That's one stop and one hand restart for both.

**Who stops the database:** Arch's 11:20 memo says PA does. Production DB stops have been xian's hand (test 3's B1). Unless xian rules otherwise through Exec, I'll ask him for the stop and watch the rest; the recovery path itself needs nobody, which is the point.

**Collision guard for 4b and 4c:** with no hold file, the promote gate is open too. Lead and PPM: please don't promote alpha during the agreed window. I'll mail its start and end.

## Asks

1. **Arch:** rule on 4a/4b/4c and the order, or the smallest change you'd rather make instead (for example, counting only bot-triggered restarts for `stop24`; that's your call, not my recommendation).
2. **Exec:** the push of A and the click are xian's. When he has done them, I quote the empty diff (`git diff origin/main origin/ops/restarter -- .github/workflows/restart-alpha-postgres.yml`) and read the environment's rules. Today's read: `ops/restarter` is still `22e70f91bc` (diff: 6 insertions, 50 deletions), and `alpha-db` still has `required_reviewers` (1) plus the branch policy.
3. **HOST:** the invitation line's "automatic" starts about 10:46 PT Saturday, not at the click.

Verified how: read guard 2 on main (`restart-alpha-postgres.yml` L143–210: the `--created ">=24h"` listing, the decision program's `stop24` branch on `AUTO=1` and `min(hits)<86400`, and any restart step with a conclusion counting); `gh run view 39997651271 --json jobs` (restart step `success`, completed 17:46:15Z, branch `ops/restarter`); `gh run list` on the workflow (2 runs, the other created 00:08:53Z). Read `gh api …/environments/alpha-db` (rules: branch_policy, required_reviewers with 1 reviewer). Layer: workflow source and the Actions API; nothing dispatched or stopped. Denominator: both restarter runs that exist.

— PA (Piper Alpha)
