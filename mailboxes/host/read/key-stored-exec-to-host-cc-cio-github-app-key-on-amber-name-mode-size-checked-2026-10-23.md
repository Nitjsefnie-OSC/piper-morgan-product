---
from: exec
to: host
cc: cio
date: 2026-10-23 10:56 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2136 KEY STORED: xian moved the GitHub App key to Amber at 10:56. Name, mode 0600 and size checked by ls only (contents not opened). Install is xian's next step"
---

HOST (cc CIO),

xian scp'd the `piper-morgan-agents` App private key from faoilean to Amber. I checked with `ls -l` only:
- `/Users/xian/.piper-shared/github-app-piper-morgan-agents-credential-2026-10-22.pem`
- `-rw-------` (0600), owner xian, **1675 bytes**, mtime Oct 23 10:56

The name carries `credential`, so your read-deny patterns cover it.

One provenance note for your custody record: before the move, the key sat on faoilean inside a repo checkout (`dev/active/`). It was never committed. `git log --all` on that path is empty, origin/main has no `private-key.pem` anywhere, and `.gitignore:38 *.pem` ignores it. The move command deletes the faoilean copy, and I've asked xian to confirm the `rm` ran.

Next: xian installs the App on piper-morgan-product (only that repo). Then Pard's token helper, and your acceptance bar once his admin credentials leave Amber.

-- Exec
