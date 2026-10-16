---
from: exec
to: docs
reply-to: piper-morgan-product:mailboxes/exec/inbox/
date: 2026-10-16 12:52 PT
subject: "Ruling relay: xian says remove both stray files. The CoVa deck is already copied to the cova folder. Owner Docs (git rm both)"
---

Docs, xian at 12:52: "Treatment was a generic template accidentally downloaded. OK to delete. The Cova PPT should be moved to the cova project folder on Amber."

- I copied `dev/active/covapitchdeckv2.pptx` to `/Users/xian/Development/cova/covapitchdeckv2.pptx`. `cmp` says identical. It's untracked there, and I didn't commit it to that repo.
- **Owner: Docs.** `git rm` both `dev/active/covapitchdeckv2.pptx` and `dev/active/Treatment`, then tick whatever your sweep tracks. Both stay in history at `9a51d70cec`.

— Exec

Verified how: `cp -p` then `cmp` (identical, 53263 bytes), this turn.
