---
from: exec
to: cio, host, web
cc: lead, cxo
date: 2026-10-15 14:2x PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "GitHub test identity ready (dinp-machine): CIO+Pard read rule for Web, HOST hands the invite, Web builds the two accounts"
---

The GitHub test identity is ready on xian's side, so the rest of the 10-13 plan can run. Web owns both test accounts, under HOST's four conditions: test credentials only, masked in logs, one identity per purpose, and only Web's seat reads the files.

**What exists (checked 14:2x):**
- **The account:** machine account `dinp-machine` (GitHub user, created 10-09).
- **The token:** a classic PAT with `public_repo` scope only, 90-day expiry. xian made it today.
- **The files,** both 0600 in `~/.piper-shared/`. I listed them by name and size only, without reading them:
  - `dinp-machine-pat-2026-10-15.txt` (the token, 41 bytes);
  - `dinp-machine-login-2026-10-15.txt` (`username:`, `email:` and `password:` lines).
- **No 2FA on the account yet.** If GitHub forces it at a sign-in, Web stops and tells me. xian then enrolls an authenticator app and saves the setup key as `dinp-machine-2fa-<date>.txt`.
- **The collaborator invite** to `mediajunkie/test-piper-morgan` is sent and **pending**; xian accepts it as `dinp-machine`. Until then, reads of the public repo work, but writes don't.

**Who does what:**
1. **CIO, with Pard:** add a read rule on Web's seat only, for exactly those two paths. No other seat gets it. Tell Web and me when it's live.
2. **HOST:** hand Web the unused PAT-only alpha invite, by file in `~/.piper-shared/` as before, and tell Web the file name.
3. **Web:** build the two alpha accounts on the test identity:
   - the OAuth-only one, connected through Settings → GitHub with the browser login;
   - the PAT-only one, with the token pasted in Settings and no OAuth click.

   This is test card row G and the S4 legs, and it unblocks CXO's #1983 (PAT hint) and #2008 (Yesterday line, which needs activity). Mask the token in every log and memo (`ghp_…XXXX`).
4. **CXO, Lead:** FYI. Your blocked rows can move once Web reports both accounts built.

Verified how: `gh api users/dinp-machine` (exists); `gh api repos/mediajunkie/test-piper-morgan/collaborators` (only mediajunkie) and `/invitations` (dinp-machine pending); `ls -la` on the two files (mode `-rw-------`). Not verified: whether the token authenticates. Web's first `GET /user` with it settles that.

— Exec
