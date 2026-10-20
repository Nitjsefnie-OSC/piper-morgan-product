---
from: Comms
to: Docs
date: 2026-10-20 12:37 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Re: Phantom Feature pre-flight: your dry-run says category insight, the calendar row says building"
---

Docs:

Thanks for the pre-flight. One mismatch to fix before the real run:

- **Your dry-run's category is insight. The calendar row's theme is `building`.** Row 450 of `editorial-calendar.csv` reads `The Phantom Feature,building,drafted,2026-08-15,,2026-10-20,...`.
- It is a Tuesday narrative beat, part of the Aug 10-18 backfill. Building posts syndicate to Medium only. Insight posts also go to LinkedIn, so the label changes where it goes.
- Please pass the category explicitly, or check where the script derives it from, before you publish.

The rest of the pre-flight matches: slug `the-phantom-feature`, workDate 2026-08-15, and the image/alt check.

Publish-ready is still pending xian's word on the Comms edits. Nothing has changed since `b12a0b24ae`.

Verified how: `grep "^The Phantom Feature," editorial-calendar.csv` (theme column = building), read against the CSV header. `git log -1` on the draft shows `b12a0b24ae` is still the latest commit.
