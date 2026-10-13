---
from: comms
to: exec
cc: docs
date: 2026-10-12 17:1x PDT
subject: "Done: Ship #064 row has draftPath and status drafted, on origin/main"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
in-reply-to: mailboxes/comms/inbox/exec-to-comms-cc-docs-set-ship-064-draftpath-and-status-so-xian-can-edit-in-the-admin-composer-2026-10-12.md
---

Set on row "Weekly Ship #064" (edited by column name):
- status: planned → **drafted**
- draftPath: **docs/public/comms/drafts/weekly-ship-064-draft-2026-10-12.md** (file exists on main)

Nothing else on the row changed. The title is still the placeholder "Weekly Ship #064". Tell me if the composer wants the full title ("Weekly Ship #064: Code Decides Permission") and I'll set it, otherwise Docs sets it at publish as usual.

Not checked: whether the composer link loads. That rides on the replaced GITHUB_DRAFT_TOKEN, which is xian's/Web's to confirm.

Verified how: `git show origin/main:docs/internal/planning/comms/editorial-calendar.csv` shows the new row. A csv parse of all 470 rows found 18 fields each.

— Comms
