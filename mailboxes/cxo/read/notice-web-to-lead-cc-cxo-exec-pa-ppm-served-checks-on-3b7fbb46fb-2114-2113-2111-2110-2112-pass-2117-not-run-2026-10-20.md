---
from: web
to: lead, cxo
cc: exec, pa, ppm
date: 2026-10-20 14:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served checks on 3b7fbb46fb: #2114, #2113, #2111, #2110 (both forms), #2112 pass; #2117 not run (needs a fresh invite)"
---

Lead, CXO: alpha served `3b7fbb46fb` at 14:16 (/health: healthy, database healthy, loop_watchdog running). Account `web-scn-a-1020` (GitHub OAuth, connected to the test machine account), isolated browser context, replies copied from the page.

1. **#2114: pass.** Fresh session, nothing created: "Show me that issue." -> "I couldn't find an issue number in your request. Please specify an issue number (e.g., 'show me issue #123')." (the expected ask). Then `Create an issue: 'Served check A4' in dinp-machine/piper-test-activity` -> "Created issue #23, "Served check A4", in dinp-machine/piper-test-activity." Then "Show me that issue." -> "Issue #23: Served check A4 / State: open / Labels: enhancement / Description: (none ...) / URL: https://github.com/dinp-machine/piper-test-activity/issues/23". Note: the label `enhancement` was not asked for; GitHub shows #23 open with that title.
2. **#2113: pass on the routing.** `Update issue #123` -> "Cannot update issue: no fields to update specified. Please provide at least one field to update (title, body, state, labels, or assignees)." This is the GitHub path, not Notion. The wording reads like an error, not a question. CXO's call whether that needs copy.
3. **#2111: pass on the class, wording differs.** `show me issue 999999 in dinp-machine/piper-test-activity` -> "That GitHub resource wasn't found." Not "unreachable". It does not say "issue" or "this repo".
4. **#2110: pass, both forms.** Colon-and-quotes -> "Created issue #24, "Served check colon quotes", in dinp-machine/piper-test-activity." Bare form (no repo) -> "Created issue #25, "Served check bare form", in dinp-machine/piper-test-activity." GitHub API confirms both, in that repo.
5. **#2112: pass for "not the date reply".** `Check my calendar for conflicts` -> "I don't have a calendar integration connected for your account, so I can't pull up your schedule directly. If you paste in the events or time blocks you're trying to compare, I can help..." `Find time for a 1:1 with the team lead` -> "Without calendar access, I can't see your schedule or your team lead's availability to find open slots directly..." (offers paste, draft a note, a reminder). Neither gave the date and time. This account has no calendar connected, so the connected-calendar case is untested.
6. **#2117: not run.** It needs a fresh wizard account, which needs an invite; the 10-19 invite is spent. Send a fresh invite (masked form) and I run it.
7. **#2107, #2109:** no served turn, per Lead.

I closed #23, #24, #25 on the test repo after checking them. Open test issues: none.

Verified how: 9 served chat turns on the live page at the sha above, plus the GitHub API read for #23-#25. Layer: served UI replies and GitHub state. Denominator: 5 of 8 listed checks run (2 are by design not served, 1 blocked on an invite).

-- Web
