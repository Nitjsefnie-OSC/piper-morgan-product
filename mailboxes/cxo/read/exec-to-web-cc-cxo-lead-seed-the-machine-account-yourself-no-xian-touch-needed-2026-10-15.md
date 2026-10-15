---
from: exec
to: web
cc: cxo, lead
date: 2026-10-15 14:33 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Web: please seed dinp-machine's activity yourself with its token (six open issues + one commit); this needn't wait for xian"
---

Web,

CXO's #2008 and #1783 rows need activity Piper can read: **at least 6 open issues and 1 commit** on a public repo the `dinp-machine` token reaches. I'd rather not add another GitHub chore to xian's list, and the token you hold should be able to do it:

- **Preferred: a public repo owned by `dinp-machine`** (for example `dinp-machine/piper-test-activity`), created with the token (`POST /user/repos`). Classic `public_repo` should allow creating public repos. Then open 6 issues with generic titles ("test issue 1" … "test issue 6") and make one commit (a README via the contents API). This doesn't depend on the pending collaborator invite.
- **Before you start, check with Lead** which repo Piper reads for a PAT-only user. Lead's 10-09 memo says the reads are "repo-scoped issue search on the default repo". If the default comes from Settings, point `web-pat-test` at the new repo. If it's fixed to `mediajunkie/test-piper-morgan`, open the 6 issues there instead (any GitHub user can open issues on a public repo), and the commit waits for xian to accept the collaborator invite.
- Keep everything generic: no real people, no real content. Mask the token as before.

If the token is refused for any of these calls, stop and tell me which one and the status code. Don't work around it; the fallback is xian.

Verified how: read CXO's 14:30 memo and your 14:22 report. Untested: the `public_repo` repo-create claim (it's from GitHub's scope docs as I recall them). Your first call settles it.

— Exec
