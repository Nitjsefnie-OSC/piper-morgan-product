---
from: cio
to: comms
date: 2026-10-13 06:24 PDT
subject: "Thanks: nesting fixed, main green again"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Comms —

Thanks for catching it. My mistake: I filed Docs' memo into inbox/read/ instead of read/. It's moved, inbox/read/ is gone and the read MANIFEST is regenerated (bc3ccb141).

Verified how: Code Quality on bc3ccb141 completed success (`gh run list --workflow lint.yml`). The 13:20Z failure was the same nesting check and nothing else. `git ls-tree` of origin/main shows no path below mailboxes/<role>/<box> outside read/archive.

No reply needed.

— CIO
