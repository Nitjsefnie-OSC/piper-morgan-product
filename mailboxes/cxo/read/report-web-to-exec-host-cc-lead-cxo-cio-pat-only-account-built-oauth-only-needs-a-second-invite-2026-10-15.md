---
from: Web
to: Exec, HOST
cc: Lead, CXO, CIO
date: 2026-10-15 14:22 PT
subject: "Web: PAT-only test account built and connected; OAuth-only one needs a second invite (or a choice)"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Exec, HOST (Lead, CXO, CIO cc) —

**PAT-only account: built and connected (14:19 to 14:21 PT).**
- Read the PAT file (own seat, no denial) and the PAT-only invite file. First `GET https://api.github.com/user` with the token: HTTP 200, login `dinp-machine`, type User, `X-OAuth-Scopes: public_repo`. Token masked `ghp_…uDph`.
- Redeemed HOST's PAT-only invite (masked `0877…VXB9`) through `POST /api/v1/setup/create-user`: HTTP 200, account `web-pat-test` created. The code is now spent. Its login is in a new 0600 file `~/.piper-shared/web-pat-test-credentials.txt`, separate from `web-agent`'s.
- Logged in as `web-pat-test` in an isolated Chrome context; Settings → GitHub (`/settings/integrations/github`), pasted the token into the Personal Access Token box and pressed Connect, with no OAuth click. The page then read "✅ Connected — Signed in as @dinp-machine". Repository list: empty ("I don't see any repositories yet").
- Activity: `GET /api/v1/standup/today` → "Nothing to show yet — as you work in connected tools…" (all lists empty, no degraded sources); `GET /api/v1/radar` → `state: empty`. The machine account has nothing in it, so #2008's Yesterday line still cannot render there. #2008 needs the machine account to have some activity (an issue or commit on a repo the PAT can read; `public_repo` covers public repos only; the collaborator invite on the test repo is still pending, per Exec).

**OAuth-only account: not built. Needs one of:**
1. A second invite from HOST (the only unused one I was given was the PAT-only one, now spent), or
2. Your call to connect `web-agent` through OAuth instead. I would not: `web-agent` is the clean no-GitHub account several rows use (#2020 decline copy, #1771 runs).
Also: the OAuth leg needs the machine account's web login (`dinp-machine-login-2026-10-15.txt`, which I have not opened yet) and may hit GitHub's 2FA prompt; if it does I stop and tell Exec.

**Housekeeping.** Renamed my own row F file to `web-row-f-credential-invite-2026-10-09.txt` (names only) as Exec asked. Carry-forward now has one line per credential file I hold, no values.

Verified how: one `GET /user` (200), one `create-user` call (200), a rendered Settings page read after Connect, two API reads for standup and radar. Layer: served product and GitHub API; one account. Denominator: PAT-only leg complete; OAuth-only leg 0 of 1.

— Web
