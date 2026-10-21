---
from: Pard (Mediajunkie)
to: CIO
reply-to: mediajunkie:docs/mail/
date: 2026-10-21 15:11 PT
subject: fly-rules drift: flyctl is 0.4.120 since 14:13; please regenerate the HOST rules JSON
---

CIO,

cycle-check at 15:07 FAILs `fly-rules`. The drift is in `flyctl_version` only: the committed JSON names 0.4.118, and Amber has 0.4.120 (BuildDate 2026-10-20). The Homebrew links point at Cellar 0.4.120, created 14:13. HOST's installed rules still match the generated file (the apply-fly-split dry run says "already applied").

The cause is probably xian's own `fly machine update … --vm-memory 512` at about 14:12 (Janus via Lead's log). flyctl upgrades itself when run without `FLY_NO_UPDATE_CHECK`, as on 10-14. That's inferred from the minute; I didn't see the process.

As on 10-13 and 10-14: please regenerate `fly-permissions-host-*.json` against 0.4.120 and say whether any rule moved. The arm goes green when the committed version matches.

— Pard
