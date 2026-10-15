---
from: cio
to: host
date: 2026-10-14 21:18 PDT
subject: "FYI: flyctl updates itself when run; the host-wide off switch writes your fly config, so it's your call"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

HOST, no action needed unless you want it.

- **What happened:** flyctl self-updates when run. Pard traced tonight's 0.4.117 to 0.4.118 at 20:55 to the fly-rules drift check's own `fly` calls. Your fly rules are generated from the installed binary's help, so an update can add a verb no rule names until someone regenerates. Pard's arm catches that within a cycle.
- **Fixed on our side:** the generator and Pard's arm now run flyctl with `FLY_NO_UPDATE_CHECK=1`. Your own attended `fly` calls can still trigger an update.
- **Yours, if you want it:** `fly settings autoupdate disable` stops it host-wide. It writes your fly config, which holds the token, so neither Pard nor I will touch it. If you leave it, an update just means I regenerate; the diff is reviewed.

Record: `docs/internal/operations/prod-command-permissions.md`, section 2026-10-14.

Verified how: Pard's memo (install receipt at 20:55:01, the arm started at 20:54:56, flyctl's binary strings), plus my `--check` after the change, which is OK. Layer: Pard's forensics and the generator. Not tested: whether the variable stops every update.

— CIO
