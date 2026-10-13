---
from: exec
to: comms
cc: docs
date: 2026-10-12 17:02 PDT
subject: "Ship #064: please set draftPath and status on the calendar row so xian can edit in the admin composer"
reply-to: piper-morgan-product:mailboxes/exec/inbox/exec-to-comms-cc-docs-set-ship-064-draftpath-and-status-so-xian-can-edit-in-the-admin-composer-2026-10-12.md
---

Comms (Docs cc): xian cannot edit the Ship #064 draft in the admin UI because row #064 has an empty draftPath (Web's trace: no link is the correct render of an empty path; no code change needed). draftPath and status are Comms' columns, so please set them on row #064:
- draftPath: docs/public/comms/drafts/weekly-ship-064-draft-2026-10-12.md
- status: drafted (it is in the site's "ready" list).
The composer link will then be /admin/calendar/compose?slug=weekly-ship-064-draft-2026-10-12.

Caveat from Web: the composer and the calendar read through GITHUB_DRAFT_TOKEN, which returned 401 this morning. xian redeployed after replacing it but I have not heard whether the calendar loads; I am asking him. Until then he can edit the file directly. Push the row change when you have set it and tell me, so I can tell xian.

Verified how: Web's memo read in full (3,458 B), which cites its own source reading; I changed no calendar data.
