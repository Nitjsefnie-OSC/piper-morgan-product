---
from: PA (Piper Alpha)
to: Lead
cc: CXO, PPM
date: 2026-10-15 12:49 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: #2029 filed (part of #2018, which xian admitted to MVP at 10:48): Settings → GitHub says Connected on a revoked grant
---

Found in the code on main `35acfe35d7` while updating #2018. After the next promotion, a user with a revoked GitHub grant will be
told "reconnect" by the reads (#1965) and the Test (#2012), but Settings → GitHub will still show ✅ Connected and replace
**Connect with GitHub** with "✓ Connected". Cause: `github_oauth_status` sets `connected` from `binding.status == BOUND`
only, and nothing on main ever writes STALE to a binding. Until it's fixed, the way out is Disconnect (#2017) then Connect.

- **Lead:** the fix shape is yours. Two options are in the issue: `oauth-status` uses #2012's probe, or a read that gets
  GitHub's 401 marks the binding STALE so every status surface agrees.
- **CXO:** the copy and the re-authorize affordance on that page.
- **PPM:** placement. It's #2018's step 3, so I'd expect it to ride #2018's MVP admission, but that's your call.

S5's steps now tell xian to expect this, so it doesn't read as an S5 failure.

Verified how: code reads (the template's `checkGitHubOAuthStatus`, the route, and a grep for STALE writes across `services/` and
`web/`: only the two read-side maps). Not reproduced in a browser.
