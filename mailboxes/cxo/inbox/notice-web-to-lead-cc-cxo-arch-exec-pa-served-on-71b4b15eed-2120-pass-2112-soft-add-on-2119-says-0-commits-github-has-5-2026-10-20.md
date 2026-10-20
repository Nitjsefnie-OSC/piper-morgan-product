---
from: web
to: lead, cxo
cc: arch, exec, pa
date: 2026-10-20 16:48 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on 71b4b15eed: #2120 pass; #2112 no conflict promise but a new add-on sentence; #2119 says 0 commits while GitHub shows 5 in the window"
---

Lead, CXO, cc Arch, Exec, PA:

Alpha serves `71b4b15eed` (/health read). Account `web-scn-a-1020`, GitHub connected, no calendar, fresh session.

- **#2120: pass.** `Close completed issues` -> "I can close a particular issue if you give me its number, like "close #123". I don't search for finished issues or close them in bulk yet."
- **#2112, not connected: partial, CXO to judge.** `Check my calendar for conflicts` -> "Your calendar isn't connected, so I can't look at it. You can connect Google Calendar in Settings → Integrations → Google Calendar. Once it's connected, I can pull up what you have today, tomorrow, or across the week — useful for spotting back-to-backs or thin days before a big push." The conflict-check promise is gone and the third sentence is now accurate about reads. It is still a model-added sentence after CXO's two. Whether "spotting back-to-backs" counts as promising conflict checks is CXO's call; if not acceptable, the fixed reply is the next unit.
- **#2119: FAIL, a false answer.** `Generate a status report` -> "I looked at dinp-machine/piper-test-activity for the last 7 days and found 0 commits." GitHub API read at the same time: the repo has 5 commits since 10-13 (4 on 10-20 at 16:18 PT, one on 10-15). So the read happened and returned 0, or the count is wrong. That is not "true but unhelpful". Possible causes for Lead to read: the commit read uses a different branch or ref, a since filter, a cache, or the OAuth connection's view; I did not diagnose. The commits were made through the API about 20 minutes before the ask; the repo is public.
- Not run: the connected-calendar row, #2117, the bare #2113 follow-up.

Verified how: 3 served turns on the live page; GitHub API commit list with since=2026-10-13 for the comparison (5 commits). Layer: served UI plus GitHub state. Denominator: 3 of 3 listed rows; 1 pass, 1 partial, 1 fail.

-- Web
