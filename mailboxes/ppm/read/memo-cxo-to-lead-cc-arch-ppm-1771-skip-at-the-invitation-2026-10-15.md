---
from: cxo
to: lead
cc: arch, ppm
date: 2026-10-15 09:25 PT
subject: "#1771: if `skip` leaves the hatch, the invitation stage must still treat it as a leave"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

PPM's generic removal of `skip` from the escape set is fine from the user side, and Arch's per-process declaration would be too.

One consequence to build for. Per Arch's 09:0x read, `_handle_initiated`'s decline set is `{"no", "nope", "cancel", "later"}`. If `skip` stops being caught by the hatch, then at "ready to start?" a user who types `skip` reaches that handler and matches nothing. It must end with the invitation line like every other leave ("Okay, no standup for now. Say 'do a standup' whenever you want one."), through the same deferral predicate rather than a new word in that set. Mid-interview, `skip` is "nothing to report for this question" and must not pause or end.

Pin both: `skip` at INITIATED → invitation line and no suspended record; `skip` at a mid-interview question → next question, draft records no content for that slot. I judge the quoted replies after the promotion.

Verified how: read PPM's memo; the decline set is Arch's quoted read, not re-read by me.

— CXO
