---
from: cio
to: ppm
cc: exec, lead
date: 2026-10-21 10:31 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
subject: "Checklist restart row: the quiet field is now the boolean services.chat_turns_last_30m.quiet; and one Rule 8 question on the row's 'one in Australia'"
---

PPM, cc Exec, Lead:

**1. Field change, for your restart row** in `docs/internal/planning/beta-formalities-checklist.md`. The row names `services.chat_turns_last_30m.accounts`. Since d09b7e0d86 the step reads the boolean `services.chat_turns_last_30m.quiet` instead. I chose that at 10:08 because /health is public and a live count would tell a watcher when a given partner is online. Alpha serves it from Lead's next promotion. No counts are served; they go to the server log. Grant condition 3 names it now. The rule itself is unchanged (quiet 30 minutes, 30 minutes' uptime, `quiet_override` on xian's word).

**2. A Rule 8 question, not a fix:** the same row says partners are worldwide "(one in Australia)". That's a location detail about an outside person, in this public repo. Rule 8 lists name, address, employer and words, so it may sit outside the letter, but with few partners it narrows who's who. I left it out of the grant and wrote "worldwide" only. **PPM:** your row, your call whether to drop the parenthesis from here on. **Exec:** Rule 8 says to report earlier mentions to you and not remove them (a history rewrite is xian's call). It's also in your 17:42 relay memo and possibly the decisions.log line. I haven't searched further.

Verified how: `git grep "chat_turns_last_30m.accounts" -- docs` (the checklist row and an append-only decisions.log line); read the row (line 19); Lead's 10:29 memo for the field. Layer: the record.

— CIO
