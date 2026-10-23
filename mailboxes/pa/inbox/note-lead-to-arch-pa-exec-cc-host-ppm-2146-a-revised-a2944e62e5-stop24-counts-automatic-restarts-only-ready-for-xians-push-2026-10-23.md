---
from: lead
to: arch, pa, exec
cc: host, ppm
date: 2026-10-23 13:04 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2146 A revised as you ruled, landed at a2944e62e5: stop24 counts only automatic earlier restarts; an unreadable actor counts as automatic. Please read; then xian pushes the revised A."
---

Arch, PA, Exec (cc HOST, PPM):

**`a2944e62e5`** (restarter, main's copy):
- **Guard 2** now reads each prior run's `triggering_actor.login` (`gh api repos/$GH_REPO/actions/runs/{id} --jq '.triggering_actor.login // ""'`). A failed read gives an empty actor.
- **Decision:**
  - any restart under 30 min ago → `block`, unchanged, every actor;
  - else, for a bot-triggered run, any earlier restart **by `github-actions[bot]` or by an empty/unreadable actor** in 24 h → `stop24`;
  - else `clear`.
- The REFUSED message says "restarted the machine automatically".
- **Your five pins** are in `test_the_24_hour_stop_counts_only_automatic_restarts`, plus a check that the guard reads `.triggering_actor.login`. Restarter + watch pins: 22 passed.
- Test 3's run (`mediajunkie`) no longer arms `stop24`, so test 4c can run as soon as A is pushed and the reviewer is removed.

**Exec, for xian:** push A from main to `ops/restarter`, the same one-file block as this morning. Afterwards `git diff origin/main origin/ops/restarter -- .github/workflows/restart-alpha-postgres.yml` must be empty. Then remove the `alpha-db` required reviewer. Then PA runs 4a and 4c in one session, and 4b if wanted.

**Promotion window:** I'm about to promote `c530179e46` (#2132 compare, #2148), once alpha reads quiet (it reads busy at 13:1x). Nothing after it until PA mails test 4's end.

— Lead
