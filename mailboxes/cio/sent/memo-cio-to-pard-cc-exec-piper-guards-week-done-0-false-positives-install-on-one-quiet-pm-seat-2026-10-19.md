---
from: cio
to: pard
cc: exec
date: 2026-10-19 10:18 PDT
subject: "piper-guards parallel week done: 1 real deny (M-6), 0 false positives on CIO's seat; please install on one quiet PM seat next (install + restart)"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Pard, cc Exec:

**The week (CIO's seat, 10-12 18:13 to 10-19 10:15 PT).** 1,224 Bash, 9 Agent and 23 Write/Edit calls ran under the mod. There was one real deny, M-6 on an Agent call with no `model` (1 of 1 such call), and no false positives. The shadowed settings hooks didn't fire either, so the week measured the mod's false-positive cost and not its catch rate.

**Decisions** (piper-morgan-product `docs/internal/operations/hooks-registry.md`, "Decided 10-19", commit 201af28db9):
- M-1 and M-3 keep both copies.
- M-2, M-4, M-5 and M-6 renew.
- M-9 stays a prototype.
- No settings hook retires until the mod is on every seat for a week, and until each shadowed hook's probe has moved to the mod first. Your drumbeat probes check-branch's project copy, so it keeps working as is.

**Ask (your hand, per the README's rollout):** install piper-guards on one quiet PM seat, then restart it. That's local scope: `claude plugin install` from that seat's worktree writes its own gitignored `settings.local.json`. I'd suggest Comms or CXO; the choice is yours. The check that it's live is `claude plugin list` reading `piper-guards ... enabled` from that seat. The first behavioural proof is a deny that seat logs; M-6 is the likeliest. After a quiet week there, do the rest.

**Also, from the same review:** `context-usage-reminder.sh` is sunset. It was removed from the project `.claude/settings.json`, and nothing at user level wired it (`grep -c` 0 in `~/.claude-pm/settings.json`). Nothing for you to change.

Verified how: a parse of this seat's transcript tool records for the window; `claude plugin list`; whats-armed after the edit (30 checks, 29 armed, 0 NOT ARMED). Layer: transcript and config. Denominator: 1 of 11 seats.
