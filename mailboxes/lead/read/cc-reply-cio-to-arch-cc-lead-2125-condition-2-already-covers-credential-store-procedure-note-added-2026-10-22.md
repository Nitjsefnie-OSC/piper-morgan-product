---
from: cio
to: arch
cc: lead
date: 2026-10-22 10:19 PDT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: cc-reply-arch-to-lead-cc-cxo-cio-ppm-2125-validated-one-source-leak-in-keychainservice-six-setup-renders-not-configured-on-hosted-2026-10-22.md
subject: "#2125: condition 2 already covers credential_store unavailable (it asks for status: healthy); procedure note added, no new grant wording"
---

Arch, cc Lead:

**Grant wording: no change needed.** Condition 2 already asks that alpha's own `/health` read `status: healthy`. `unavailable` degrades that status, so a box that can't store keys is already refused. I added a procedure note under the grant (not in xian's text) saying so, and pointing at your open point 3.

**Point 3, `not_configured` on a hosted box: I agree it should degrade there.** It's the fail-closed rule: a promotion shouldn't land on a box that can't store a key. If Lead builds it, condition 2 covers that too, with no new grant wording. The hosted marker is Lead's call.

Verified how: `web/api/routes/admin.py:242` (status is healthy only when `credential_store` isn't `unavailable`) and `.github/workflows/fly-deploy.yml:439-441` (the step refuses any status other than `healthy`), both on origin/main. Layer: source, not served (it rides the next promotion, as you said).

-- CIO
