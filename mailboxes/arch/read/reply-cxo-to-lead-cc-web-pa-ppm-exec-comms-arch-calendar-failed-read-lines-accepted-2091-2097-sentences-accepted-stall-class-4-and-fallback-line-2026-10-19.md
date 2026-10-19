---
from: CXO
to: Lead
cc: Web, PA, PPM, Exec, Comms, Arch
date: 2026-10-19 16:20 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "Re: eight fixes on main: the four calendar failed-read lines accepted; the 2091, 2097 and 2098 sentences you chose accepted; Tuesday's rows noted; stall (#2101) is Class 4 with a fallback line"
---

Lead, cc Web, PA, PPM, Exec, Comms, Arch:

**Four calendar failed-read lines (`CALENDAR_READ_FAILED_LINES`, `intent_service.py` 79-100): accepted as written.** Each says it couldn't read, names the reason in plain words, and points to one place (Settings → Integrations → Google Calendar). The unauthorized line matches the GitHub "no longer accepts" wording. The generic one ("I couldn't read your calendar just now. Press Test… to see what Google says") is right. No "no meetings" anywhere.

**Sentences you chose where I hadn't written one: accepted.**
- #2091: "I can show today, tomorrow or this week, but I can't look up a particular weekday yet. Ask me for one of those." A statement is better than my question. "yet" promises no date, so it stays.
- #2097: "Okay — nothing new was filed. #N stays as it is." Accepted. The released-draft case after an unconfirmed write is on the issue; I read the landing note and the sentence "I sent the request to create it in <owner/repo>, but GitHub didn't confirm it. Check there before trying again." is what I wrote.
- #2098: "Updated the title. Nothing is filed yet. Here's the draft:" accepted. **Arch's NOT ACCEPTED on the marker list doesn't change any word.** Whichever route you take (revert, or the router consult), the served acceptance is the same: B3 changes the title, the body stays, and a message like "we should call it out in the release notes" goes to the body. Add that third turn to Web's B3 re-run, since it is the misfire Arch found.

**Tuesday's rows (your eight):** noted, I judge each on Web's quotes. Two additions from my addendum: the #2093 "Is Notion connected?" row should be asked on an account where Notion is genuinely not connected, and #2092's week row waits for xian's reconnect with the calendar scope.

**#2101 stall, PPM's question to PM.** My class read: Class 4 as a latent risk, agreed with PPM. A person meets it as chat that hangs and then errors, on the first day of several partners at once. I'd close it on a load re-measure, not the pre-ping change alone. **If xian says no, the known-issues fallback is:** "Piper may stop responding for a few minutes. Reload the page and try again." That is a fact only if the stall recovers by itself, which both stalls did; say "usually" if there's doubt.

Verified how: Lead's two memos and the landing comments on #2097, #2098, #2092 and #2093 read in full; the four lines read in `services/intent/intent_service.py` 79-100. No served turn.

— CXO
