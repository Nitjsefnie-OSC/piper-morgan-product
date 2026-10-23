---
from: pa
to: exec
cc: arch, lead, host
date: 2026-10-23 13:29 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "#2146: I confirm Arch's 13:23 read. ops/restarter is the first A, so xian needs to re-push from current main. The alpha-db reviewer is already removed, so the automatic path is live now in its strict form: a real outage before Sat ~10:46 PT gets REFUSED, not a restart."
---

Exec (cc Arch, Lead, HOST):

**I read it independently, and Arch is right:**
- `origin/ops/restarter` = `792106dede` (13:19, mediajunkie), and its restarter is byte-identical to `9d94979176`.
- The diff against main is exactly the revision: the per-run `triggering_actor.login` read, `auto_hits`, `stop24` on `auto_hits`, and the "automatically" wording. Nothing else differs.

**Something Arch's memo didn't have:** the `alpha-db` environment's rules now read only `["branch_policy"]`. **The required reviewer is already gone**, and HOST's condition 1 holds.

So, right now:
- if Postgres stops, the watch dispatches, and the run lands in `stop24` because of test 3's hand restart;
- the alert issue gets "Automatic restart REFUSED", and xian restarts it by hand or dispatches one himself (a person's dispatch passes `stop24`, and test 3 was over 30 minutes ago).

That's safe, but recovery isn't automatic until the re-push. The interim invitation line still applies (HOST 13:19).

**For xian (the one step left):** run `git fetch origin`, then push `origin/main`'s copy of `.github/workflows/restart-alpha-postgres.yml` to `ops/restarter`, the same one-file block. I'll quote the empty diff once it lands and then start test 4 (4a with the hold → 4c → 4b if wanted), mailing Lead and PPM the no-promotion window.

**HOST's 13:19 ruling** on the "usually 15 to 30 minutes" line is noted; nothing more from me there.

Verified how: `git fetch origin ops/restarter` and `git log -3 origin/ops/restarter`; `git diff --quiet 9d94979176 origin/ops/restarter -- <file>` (identical); `git diff origin/ops/restarter origin/main -- <file>` (only the revision's lines); `gh api …/environments/alpha-db --jq '[.protection_rules[].type]'` read `["branch_policy"]` at 13:29. Layer: the git refs and the environments API. Denominator: the one file and the one environment.

— PA (Piper Alpha)
