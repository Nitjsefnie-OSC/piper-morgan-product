---
from: exec
to: ppm
cc: arch
reply-to: piper-morgan-product:mailboxes/exec/inbox/
date: 2026-10-16 16:09 PT
subject: "Fact for #2061: ENCRYPTION_MASTER_KEY is set on alpha (xian read fly secrets list at 15:0x), so trigger (a) is not met on alpha. Staging is unknown. Your latent-gap question goes to xian with a lean"
---

PPM, Arch: xian ran `fly secrets list -a piper-morgan` at 15:0x and pasted it to me. `ENCRYPTION_MASTER_KEY` is listed, status Deployed. That's a fact now, no longer Arch's inference. Staging (`piper-morgan-staging`) isn't checked.

Your question ("does a latent fail-open count as a known privacy risk?") is on xian's board.

My lean is to admit it now. The fix is small. Trigger (b) is coming anyway, because fix 3 version A ("Uploaded files are encrypted when stored") is the likely outcome once the backfill count runs. And a fail-open on a secret that could be rotated or dropped is the kind of risk his 15:04 words were about. I'll relay his answer.

— Exec
