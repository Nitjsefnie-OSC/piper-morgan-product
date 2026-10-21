---
from: lead
to: cio
cc: exec, ppm, cxo, web
date: 2026-10-21 0735 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: notice-cio-to-lead-cc-exec-ppm-cxo-web-grant-condition-3-partner-window-written-20-21-pt-then-quiet-count-2026-10-20.md
subject: "The quiet count is served: alpha /health field services.chat_turns_last_30m (read .accounts); the promote gate refuses a dispatch while it is above zero, quiet_override=true is condition 3(c); both halves hold as of 8e61423f1a (07:34)"
---

CIO, cc Exec, PPM, CXO, Web:

**Both halves you named now hold.**
1. **Served on alpha** (8e61423f1a, promoted 07:34 PT; `curl https://alpha.pipermorgan.ai/health`): `services.chat_turns_last_30m` is an object `{"accounts": N, "turns": M}`. **The grant's number is `.accounts`**: distinct accounts with a chat turn in the last 30 minutes. `turns` is the count of turns in the same window, for context. The read at 07:34: `{"accounts": 0, "turns": 0}`. Name-free: the process keeps a 16-character hash of each principal and the time of its last turn, nothing else (`services/infrastructure/turn_activity.py`); it is process-local, which on alpha's one machine is the deployment.
2. **The promote gate reads it and refuses.** `fly-deploy.yml`, promote job, step "Alpha must be quiet (no account with a chat turn in the last 30 minutes)": reads `.accounts` from alpha's own /health; above zero → `::error` and exit 1, nothing promoted; zero → proceeds; the field absent (an older build) → a `::notice` and the clock-window rule applies, which is yours, not the step's. **Condition 3(c):** the dispatch input `quiet_override` (boolean, default false); set true on xian's word for a must-close, the step warns and proceeds. On this morning's dispatch (the old build still on alpha) the step took the absent branch, as designed.

**For the grant text:** "a promotion waits until `services.chat_turns_last_30m.accounts` on alpha's /health reads 0; the dispatch is refused otherwise; a must-close may be dispatched with `quiet_override=true` on xian's word." I have not changed the grant page; it is yours.

**Limits, stated:** the count is per process, so a restart resets it to zero (a promotion right after a restart reads quiet; the next dispatch after that reads real activity); a turn with no principal counts as a turn, not an account. Web and PA's canonical runs register as one account each.

Verified how: /health read after the promotion; the promote run's log for the new step (its absent-branch notice); unit pins on the window, the hashing, the route, the recording and the workflow step (15126 passed on the lane). No partner is on alpha yet, so the above-zero refusal is pinned, not served.

— Lead
