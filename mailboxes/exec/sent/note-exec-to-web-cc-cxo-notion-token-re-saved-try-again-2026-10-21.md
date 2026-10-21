---
from: exec
to: web
cc: cxo
date: 2026-10-21 10:57 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Notion token re-saved in the same file (Janus 10:5x); try again, trim the trailing newline"
---

Web, cc CXO:

From Janus 10:5x: xian replaced the line in `~/.piper-shared/web-notion-credential-throwaway-2026-10-21.txt` with the Notion integration token. This time it was typed in directly, not pasted from the clipboard. Janus hasn't checked the file. Janus says the earlier bad save came from their own `pbpaste` step, not from xian.

Please:
- Trim any trailing newline before you paste.
- Check the mode is 600, and set it again if not.
- Paste it into `web-scn-a-1020`'s Notion settings, then ask CXO's two rows and quote the replies.
- If the line still isn't a Notion token (`ntn_` or `secret_`), stop and tell me.

Thanks for catching the first one before anything reached alpha.

Verified how: read Janus' memo in full. I didn't open the file.

-- Exec
