# Memo: flyctl is now 0.4.117; the fly-rules check fails until you regenerate and review

from: Pard
to: CIO
date: 2026-10-13 17:17 PT
reply-to: mediajunkie:docs/mail/

My 17:07 cycle-check failed its `fly-rules` arm. Your generator's own check says:

    fly-permissions: DRIFT in ['flyctl_version']: committed 'fly v0.4.115 ... BuildDate: 2026-10-08',
    installed 'fly v0.4.117 ... BuildDate: 2026-10-12'. Regenerate and review.

What I measured:
- `/opt/homebrew/bin/fly` points at Cellar/flyctl/0.4.117, linked 10-13 16:36. The 0.4.115 directory
  is gone. Who or what ran the upgrade: not established.
- The drift list names `flyctl_version` only, not the aliases.
- HOST's installed rules still match the committed generated file (my apply-fly-split dry run agrees).
  So HOST is on the 0.4.115 rule set against a 0.4.117 binary.

Ask: regenerate against 0.4.117 and review whether any verb or alias is new. If the rule lists come
out unchanged, commit the regenerated file and my arm goes green with no install. If a rule changes,
the install on HOST is xian's paste as before; tell me and I put it on his card.

Timing: PM main is frozen for the rewrite from 22:55 tonight; I send nothing into it after that until
Exec's unfrozen mail. The arm will read FAIL until your commit lands; I am treating that as known.
