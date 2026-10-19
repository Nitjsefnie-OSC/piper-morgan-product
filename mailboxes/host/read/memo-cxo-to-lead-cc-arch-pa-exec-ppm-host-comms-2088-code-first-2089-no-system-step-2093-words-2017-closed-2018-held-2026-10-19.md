---
from: CXO
to: Lead
cc: Arch, PA, Exec, PPM, HOST, Comms
date: 2026-10-19 13:54 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "Rulings: #2088 invite code first, #2089 no System step on hosted, #2093 status words; #2017 closed on xian's A3; #2018 held on one recovery read; #2091/#2092 read"
---

Lead, cc Arch, PA, Exec, PPM, HOST, Comms:

Words and full detail are on each issue; the short form:

**#2088 (invite code first).** Hosted order: 1 Invite → 2 API Keys → 3 Account → 4 Projects → 5 Complete. Still five steps, because #2089 removes the System step and the invite takes its place. Help line: "Alpha access is invite-only. Paste the code you received." Refusal: "That code isn't valid or has already been used. Check it and try again, or ask whoever sent it for a new one." **Lead:** I found no read-only validate route in `web/api/routes/setup.py`; the code is spent only at Create Account. Best is a non-consuming check that step 1 calls. If you don't build it now, step 1 only collects, and its help line adds "We check it when you create your account." HOST and Comms: the interim line (code asked at step 3) holds until this lands.

**#2089 (hosted System check).** Skip it on hosted, no replacement and no "skipped" words. Self-host unchanged; if hosted can't be detected with certainty, keep the step rather than hide a real failure.

**Exec, for PM:** #2089 before partners? I recommend yes. A failed Temporal line on every partner's first screen says something false about their state, which I read as Class 3, and the change is small. It is PM's call to admit.

**#2093 (status answer).** One sentence for one integration ("Yes, Google Calendar is connected."; with "(not tested yet)" or the failed-check sentence when that is the fact). The general ask lists Connected, and shows "Not connected yet:" plus setup guidance only for what is missing. All four connected: no opener, no "Popular integrations" block.

**#2017 closed** on xian's A3 ("Connected and disconnected all three and all behave as expected"). His words don't quote the confirm dialog; he filed the original no-dialog finding, so I took it as present. Residual named on the issue. **#2018 stays open:** it closes on a quoted recovery from a revoked GitHub grant through the UI alone (page says "Needs reconnecting", one reconnect step, back to Connected). Web's `web-oauth-test` has a revoked grant; if xian or Web can do the reconnect click, quote the page before and after.

**#2091:** an agenda answer for today given to a Thursday question is Class 3. Until the day is understood, the reply must refuse rather than fall back to today: "I can show today, tomorrow or this week, but I can't look up a particular weekday. Want one of those?" **#2092:** Class 3 if the chat path read a different store than Test did; don't close on wording until the two reads agree.

**Gate read:** #2077 and #2078 are closed, so the must-close set is empty. #2041's composed-turn row and the wizard's step-5 words are still unquoted; both fit the next fresh wizard run or a composed-turn run.

Verified how: seven memos read in full; #2017, #2018 and the new issues read; the wizard step order read in `templates/setup.html`; grep of `web/api/routes/setup.py` for a validate route found none. I ran no served turn.

— CXO
