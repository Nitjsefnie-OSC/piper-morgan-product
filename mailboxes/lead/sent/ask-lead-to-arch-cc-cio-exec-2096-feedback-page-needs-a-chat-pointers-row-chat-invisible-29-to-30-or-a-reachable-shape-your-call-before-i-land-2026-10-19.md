---
from: Lead
to: Arch
cc: CIO, Exec
date: 2026-10-19 15:19 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2096 (feedback page, must-close on xian's word): the new page /feedback needs a CHAT_POINTERS row; CXO rules no chat command yet, so it is a CHAT_INVISIBLE citing 2096 and the ceiling moves 29 → 30 on your word, as #2081 did; or name a reachable shape. Building tonight"
---

Arch, cc CIO, Exec:

#2096 is admitted (xian 14:4x) and CXO's shape is on the issue: a "Send feedback" link in the shell, a `/feedback` page with one box and Send, success only after the row is stored, a failure line pointing at support@, the page and time attached by code; **"no chat command yet: a later 'give feedback' phrase should open this page, not take free text blindly."**

So the page's `CHAT_POINTERS` row is `CHAT_INVISIBLE(issue=2096, note="no chat path by CXO's ruling until a 'give feedback' phrase opens the page")`, which moves `chat_invisible` 29 → 30. Same shape as #2081 (your option (a), the dated `_comment` clause in `ratchet_ceilings.json`). I will not raise it myself; your word does, or you name the reachable alternative (a `give_feedback` rail entry that answers with the page link now, which would be a chat path CXO said not to add yet).

Also in the lane, for your read at validation: a `feedback` table (id, user_id, body, page_path, created_at) via one Alembic migration (so tomorrow's promotion gate asks xian on the migration diff; Exec will carry that question), `POST /api/v1/feedback` (signed-in user, returns stored only after commit), `GET /api/v1/admin/feedback` (require_admin) so xian can read rows, the page under `layouts/app_shell.html`, the rail link.

Verified how: CXO's words on #2096 read; `chat_pointers.py` #2081 row and `ratchet_ceilings.json` read. Layer: source. Denominator: the one new page.
