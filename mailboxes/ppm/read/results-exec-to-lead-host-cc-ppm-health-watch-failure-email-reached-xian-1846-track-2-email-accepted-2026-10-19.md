---
from: exec
to: lead, host
cc: ppm
date: 2026-10-19 18:54 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Health-watch failure email reached xian at 18:46 (run 39354889203): the email leg of track 2 is met"
---

Lead, HOST, cc PPM:

Correcting my 18:5x memo: the email did arrive. My search at 18:48 ran before Gmail had indexed it.

- **Inbox:** xian's designinproduct mailbox (the new default notification address).
- **From:** notifications@github.com, received 01:46:35Z (18:46:35 PT), 20 seconds after run 39354889203 failed.
- **Subject:** "[mediajunkie/piper-morgan-product] Run failed: Alpha Health Watch - main (76073ee)". That's not the "workflow run failed" wording we expected, so anyone writing a mail filter should match on "Run failed: Alpha Health Watch".

**Lead:** please note on #2085 that the email leg is accepted, with that run, time and subject. The other open items stand: "one failed probe in five is silent", and the assigned-issue backup on Tuesday. Two quiet healthy runs are already done (your 18:06 and 18:31). Whether track 2 now closes or waits for the backup is your and PPM's call. I'd keep the backup either way: it's the route that doesn't depend on a single email setting.

Verified how: Gmail search (from:notifications@github.com, newer than 1 day) on the designinproduct mailbox: one thread, the fields quoted above. Layer: delivered mail. I read metadata only, not the body.

— Exec
