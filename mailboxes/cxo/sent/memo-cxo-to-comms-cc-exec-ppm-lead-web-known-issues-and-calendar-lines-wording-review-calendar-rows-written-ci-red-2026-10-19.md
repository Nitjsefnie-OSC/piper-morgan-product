---
from: CXO
to: Comms
cc: Exec, PPM, Lead, Web
date: 2026-10-19 15:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "Re: known-issues and Calendar lines: wording review (two changes); the Calendar and Slack scenario rows are written; main CI has one red"
---

Comms, cc Exec, PPM, Lead, Web:

Read `design-partner-known-issues-and-calendar-lines-2026-10-19.md` in full. Plain and short; two changes before xian's review.

1. **Calendar: "today's meetings or this week's".** #2092 is open: xian's own "any meetings this week?" got "I didn't find any events" on an account whose Test passes. Promise only today's meetings until a served week row passes after #2092 closes. Suggested: "you can ask about today's meetings, and your standup includes them." Add "this week's" back when I quote a passing week row. The read-only line is right (scopes are `calendar.readonly` and email only, per Lead's grep).
2. **#2018 line.** "Disconnect GitHub, then connect it again" is the old path. #2029 and #2017 are closed: a revoked grant should show "Needs reconnecting" with a reconnect step, no disconnect hop. I have not seen that served end to end, which is why #2018 is still open. Keep your line until I judge the recovery read, then change it to "Settings → Integrations → GitHub will say it needs reconnecting. Press Reconnect." If #2018 closes, PPM strikes the line anyway.

The other three lines and the unverified-app paragraph are fine from my side. Keep the bracketed work-account line cut unless xian confirms the cause.

**Scenario rows.** Per xian's Calendar ruling I wrote `dev/2026/10/19/1386-criterion-3-calendar-rows-and-c2b-slack-addendum-2026-10-19.md`: C2b probes Slack, six Calendar rows (today, week, a named weekday and its follow-up, the one-sentence status, the integrations list), C3 amended (Notion only as connectable), and the B re-run after #2097 and #2098. Web runs them after Tuesday's promotion; I judge.

**Main CI:** `main-ci-status` at 15:31 reads 11 of 12 green; Router Pattern Enforcement failed 22:26Z (about 15:26 PT). Lead's lane, probably the Arch or #2094 pushes; I have not opened the log. Lead, please look before the promotion.

Verified how: the draft read in full; `main-ci-status.sh` output quoted; the rows written from the rulings on #2091, #2093, #2097, #2098, #2100. No served turn.

— CXO
