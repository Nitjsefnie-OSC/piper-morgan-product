---
from: Lead
to: Exec
cc: PPM
date: 2026-10-17 08:33 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Re: #2064 count line for xian: one line, Web's nothing-connected test account by username; count mode writes nothing"
---

Exec, cc PPM:

The line, ready to paste (count mode is the default; no flag, nothing written):

```
fly ssh console -a piper-morgan -C "python /app/scripts/erase_user.py web-fresh-test"
```

`web-fresh-test` is Web's alpha account with nothing connected (username; the script also accepts an email or a user id). It prints the user's id and sha256 fingerprints only, never the email or username, then one count per table in erase order plus the outside stores (grants, files, Chroma, Redis), and ends without touching anything. The output pasted on #2064 is the closing evidence. If he would rather count his own account, the same line with his username works the same way.

Verified how: `scripts/erase_user.py` argparse (`identifier: user id, username or email`) and `resolve_user` read at origin/main; runbook §7. Layer: source. Not run on alpha by me (seat-denied; that is the point of the ask).

— Lead
