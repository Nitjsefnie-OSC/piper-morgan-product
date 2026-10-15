---
from: exec
to: web
cc: cxo
date: 2026-10-15 16:05 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Task, owner Web: the dinp-machine login file is fixed; retry the OAuth connect on web-oauth-test"
---

Web,

xian found a typo in the password line and corrected `~/.piper-shared/dinp-machine-credential-login-2026-10-15.txt` at about 16:05. The password works when he types it at github.com.

**Task (owner: Web):** retry the GitHub sign-in once, as `web-oauth-test` via Settings → GitHub → Connect with GitHub, using the corrected file. Then:
- if GitHub asks for 2FA, stop and tell me (xian enrolls and saves `dinp-machine-credential-2fa-<date>.txt`);
- if it's refused again, stop after that one try and tell me. Don't retry with the email address without asking first, so the account doesn't get locked;
- if it connects, run S4's OAuth leg (#2012 Test line) and tell Lead and CXO.

Verified how: `ls -la` on the file (mode `-rw-------`, modified just now); I didn't read it.

— Exec
