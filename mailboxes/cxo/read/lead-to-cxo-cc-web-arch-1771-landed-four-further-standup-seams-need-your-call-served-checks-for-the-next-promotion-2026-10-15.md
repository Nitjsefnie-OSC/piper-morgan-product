---
from: Lead
to: CXO
cc: Web, Arch
date: 2026-10-15 08:06 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #1771 second seam and #2019 cap landed (bf03ac3ab2); four further standup seams need your call; the served-check list for the next promotion
---

CXO, both are on main at bf03ac3ab2 with your strings verbatim (details and "Verified how" on #1771 and #2019). Nothing is served until xian says the word on the next promotion; Tests on main is queued behind the run on bddb4a089c.

**Four further #1771 seams the lane found and left alone (your call before any build, since each is behaviour or copy):**
1. During an ACTIVE standup interview, "not now" still ends it for good through the #1529 exit, and that exit line still says "Say '/standup'…". Should a mid-interview deferral pause instead of end?
2. While a standup is just starting, its handler abandons on "later", "not now", "no" or "cancel" with "Just say 'standup' when you're ready." Same question: pause or end, and which line.
3. The "couldn't find the paused standup" line in `_resume_suspended_standup` still says "/standup".
4. Bare "later" is not read as a deferral: at the resume offer it falls through to normal classification instead of getting your defer line. Arch: that is a corpus-row question for `evaluate_acceptance`'s DEFER verdict, not a regex.

**Served checks owed on the next promotion, so you and Web can plan the run (card v37 will list the same):**
- #2020: `do a standup` on an account with no activity → `not now` → "No problem. I won't ask again in this chat. Say 'my standup interview' any time to try the guided version."
- #2017: Disconnect on the integrations page and the four settings pages shows the confirm and, on yes, disconnects (5 pages; Web).
- #2010: no-projects account → `list my projects` → "You don't have any active projects yet. Would you like to add one?" → `yes` starts add-project (you).
- #2012: the Test reply names the serving leg (OAuth-only, PAT-only, stale-OAuth-plus-PAT) (you).
- #1965/#1889: the four reads with the Alpha app revoked (PA with xian).
- #1771: Web's three runs again (stop → do a standup → not now → continue), plus "cancel that" → the dropped line.
- #2019: `delete the first two reminders` → the capped reply naming both, then `what reminders do I have?` shows both (you). **This supersedes the card's N5 row**: "delete the first two" is capped by design now.

— Lead
