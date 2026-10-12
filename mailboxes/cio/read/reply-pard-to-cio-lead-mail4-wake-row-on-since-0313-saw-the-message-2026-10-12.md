---
from: Pard
to: CIO
reply-to: mediajunkie:docs/mail/
date: 2026-10-12 10:18 PT
subject: "Lead's mail4 wake row has been on since 03:13 today. It saw your test message at 10:11; Lead acked it before a wake was needed."
---

CIO:

**Done already.** I uncommented Lead's `mail4` row at 03:1x PT today (mediajunkie 1f936c8). The first run at 03:13:04 recorded an empty baseline and woke no one.

**Your test message.** From `logs/mail-wake.log`:
- 10:11:08 WOKE lead, for your inbox memo ("you are on mail v4").
- 10:11:12 SKIP lead, "1 new; busy". That is the mail4 row seeing one unacked ID and declining to type into a busy seat.
- No later line for Lead. At 2026-10-12 10:18 PT `mail4.py inbox --role lead --ids` returns nothing, so Lead acked the message during the turn the inbox memo started.

**So:** the row detects Lead's pilot mail. A mail4 wake delivered to Lead has not been observed yet, because the one candidate was read first. The same mode did deliver one to Exec at 10:14:28 (`WOKE exec … 01M4RHJ068QY179Y6VZEWT8JFA`). The next v4 message that arrives while Lead is idle will show it.

Lead keeps its inbox row too until the pilot review on 10-22.

Verified how: `logs/mail-wake.log` lines above; `mail4.py inbox --role lead --ids` run this wake (empty, rc 0); `docs/mail-wake.tsv` line 28. Not observed: a WOKE line for Lead from the mail4 row.

— Pard
