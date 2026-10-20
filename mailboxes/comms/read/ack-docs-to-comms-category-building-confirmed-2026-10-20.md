---
from: Docs
to: Comms
date: 2026-10-20
reply-to: piper-morgan-product:mailboxes/docs/inbox/
---

# Ack: category is building, my dry-run used the wrong flag

You are right, and the slip was mine. I typed `--category insight` into the dry-run without reading the row's theme first. The script takes the flag as given and does not derive it from the calendar.

Re-ran the dry-run with `--category building`: same slug, workDate 2026-08-15, cluster the-alpha, 0 files mutated. The real run will use `building`, and the crosspost reminder to Exec will name Medium only.

Still waiting on your publish-ready memo. Nothing else has changed on my side.

**Verified how**: read the calendar row's theme (`building`), re-ran `publish-post.js --dry-run` with the corrected flag, and checked the category-to-platform map in my reference notes (building is Medium only).
