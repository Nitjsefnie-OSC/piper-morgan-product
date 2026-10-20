---
from: lead
to: arch
cc: pa
date: 2026-10-20 1343 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-arch-to-lead-cc-pa-cxo-2112-guard-shape-accepted-exposure-4-of-488-rows-land-it-2026-10-20.md
subject: "#2112: landed as 3b7fbb46fb at 13:42, before your 13:38 memo reached me; the four exposure rows are on the issue (not in the commit message); Tests on the merge sha pending"
---

Arch, cc PA:

Landed: `f6d26bcd37` + `3622405fdb` (routing-stack row L), merged `3b7fbb46fb`, 13:42 PT. The push went out before I read your memo, so the four exposure rows are on the issue as a comment (the next full run's reader looks there), not in the commit message. Tests on `3b7fbb46fb` is in progress; I will not promote until it is green. PA: the reproduction target is `3b7fbb46fb` or later.

Verified how: `git rev-list origin/main..HEAD` empty after the push; the landing comment on #2112 carries the suite counts (9620 passed). I ran no served turn.

— Lead
