---
from: Web
to: Exec
cc: HOST, CXO, Lead
date: 2026-10-15 15:54 PT
subject: "Web: OAuth-only account created; the machine account's GitHub login was refused (Incorrect username or password); stopped"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Exec, HOST (CXO, Lead cc) —

**Done:** HOST's OAuth-only invite (masked `X1NZ…WBHA`) redeemed through `POST /api/v1/setup/create-user`: HTTP 200, account `web-oauth-test` created. The invite is spent. Login saved 0600 in `~/.piper-shared/web-oauth-test-credentials.txt` (separate from the other two accounts' files). Carry-forward line to follow.

**Stopped at the GitHub sign-in.** As `web-oauth-test` in its own isolated Chrome context, Settings → GitHub → "Connect with GitHub" took me to `github.com/login` ("to continue to Piper Morgan Alpha"). I entered the username and password from `dinp-machine-credential-login-2026-10-15.txt` once, exactly as written in the file. GitHub answered "Incorrect username or password." There was no 2FA prompt; the password was refused before that step. I did not retry or try the email address, to avoid a lockout, and I am not working around it.

**Ask for xian, via Exec:** check the login file's password against the machine account (a typo when it was saved, or the password was changed), fix the file, and tell me. Then I redo the OAuth step (about two minutes). If GitHub then demands 2FA, he enrolls an authenticator and saves the key as `dinp-machine-credential-2fa-<date>.txt`, as planned. The PAT-only account is unaffected (it used the token, which authenticates).

Also noted: the dinp-machine files were renamed to `dinp-machine-credential-pat-…` and `-login-…` between my reads, so I used the new names for the second read.

Verified how: one `create-user` call (200); one GitHub sign-in attempt with the file's values, refusal read from the rendered page. Layer: served product and github.com sign-in page. Denominator: OAuth-only leg 1 of 2 steps (account created; connection not made).

— Web
