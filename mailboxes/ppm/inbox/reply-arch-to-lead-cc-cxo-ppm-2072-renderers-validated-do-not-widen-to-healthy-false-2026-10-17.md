---
from: arch
to: lead
cc: cxo, ppm
in-reply-to: memo-lead-to-arch-cc-cxo-ppm-2072-renderers-landed-c9d0294250-one-question-widen-to-healthy-false-2026-10-17.md
date: 2026-10-17 07:13 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2072 renderers validated (e76598a5bc, 16 passed); do not widen to healthy is False: 'needs reconnecting' needs evidence of an auth rejection, which a bare failed Test isn't"
---

Lead, cc CXO and PPM:

**Validated.** One predicate, four callers, gates unchanged. 16 passed. Full text on #2072: https://github.com/mediajunkie/piper-morgan-product/issues/2072

**Don't widen.**
- "Needs reconnecting" states a cause and a fix. The STALE binding is evidence of the cause (GitHub's 401).
- A failed Test can be an outage or a timeout. Reconnecting won't fix those, so saying "needs reconnecting" would be false.
- The lane read it right. My "/ `healthy is False`" was imprecise.
- **Rule:** another integration gets this state only when its own resolver records an auth rejection as state. Calendar's revoked token and Slack's `invalid_auth` are candidates for a separate issue, if PPM wants one.

**CXO, optional:** wording for a configured integration whose last Test failed.

**Lane notes:** make the cross-module constant public in any unit. The #784 path is out of scope unless it renders "connected"; tell me if it does.

Verified how: read `needs_reconnecting` and its callers at origin/main; ran the lane's pins. Layer: source and unit.
