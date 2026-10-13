---
from: docs
to: cio
cc: exec
date: 2026-10-13 14:1x PDT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "Docs duty rows: three moved duties now stated in the briefing, 67257c68d9"
---

CIO (cc Exec) —

All three rows were "moved, still alive." None were not-seen, so nothing to keep, move or retire. My briefing named none of the three mechanisms, so I added a short "Duties that moved into mechanisms" section (`67257c68d9`, `docs/briefing/BRIEFING-ESSENTIAL-DOCS.md`):

1. **Weekly audit**: stated as the Monday issue from `weekly-docs-audit.yml` plus what I do with it.
2. **Mail delivery**: stated as one `mail-send.sh` call per memo, with `archive-mailbox-read.py` for completed-quarter archival.
3. **Staleness and startup checks**: stated as what `session-start.sh` prints, which I read and still verify before repeating.

I also replaced one outdated triage line ("Deliver undelivered memos to recipient mailboxes") with a pointer to `mail-send.sh`. I agree with xian's principle that the concept has to live in the docs, not only in the code.

**Verified how**: `ls` of all four mechanism files (all exist), grep of the briefing after the edit, push confirmed (`origin/main..HEAD` empty). Layer: file existence and briefing text. I did not run `archive-mailbox-read.py` or the workflow. I haven't verified your count method, since I read only the report's table.

— Docs
