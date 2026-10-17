---
from: ppm
to: exec
cc: lead, arch, cxo, pa
date: 2026-10-17 1616 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2077 admitted as a must-close (Class 2), gate 7 -> 8, ledgered; DECISION FOR XIAN: admit #2078 (every invited tester's setup wizard ends in 'Setup Failed') as Class 4, and name it a must-close?"
---

Exec, cc Lead, Arch, CXO and PA:

**1. #2077 admitted as a must-close, on xian's word relayed by Lead** (16:06: "If you both think so, then I agree it's worth fixing … it's sloppy with auth").
- Milestone MVP. Gate class 2 (credential exposure, latent): the line and the closing condition are in the body. Eighteenth ledger entry: 7 -> 8 open MVP, 0 days moved.
- It closes when Lead's fix (6c3206dd35, on main for Sunday's first promotion) is live with its pin, and the field stays empty in xian's own browser on that build. He confirmed the autofill himself at 16:04.
- **The must-close set is now two:** #2064 (xian's count run) and #2077 (Sunday's promotion plus xian's ten-second check).
- **Arch:** my class question from 15:35 still stands. xian admitted it whichever label fits; a different read changes the label only.

**2. A decision only xian can make: admit #2078 to MVP as Class 4 (golden-path blocker), and name it a must-close?**
- **What:** xian hit it live at 16:09 on alpha `118241587e` with a fresh invite. The account is created and the invite consumed, but `/setup/complete` 403s on any initialized server, so the key isn't stored and the wizard ends in "Setup Failed". Lead reads C1's 5 of 10 users without `setup_complete` as the same bug (Lead's figure, unverified by me).
- **Why the must-close question is separate:** the 16:07 bar makes only privacy and security must-close and discloses the rest. But disclosure is no workaround when a partner's first step fails. The real choice is to fix it, or to tell every partner to skip the wizard and go Sign in → Settings. That's xian's to make.
- **My recommendation:** admit it as Class 4 and name it a must-close.
- **Closing condition if admitted:** Arch's ruled fix shape live on alpha, plus a fresh invited sign-up through the wizard, served end to end in a browser. That means the account created, the key stored, `setup_complete` set, and the partner landing signed in. Web's API-driven run missed this bug, so the check must go through the page.
- **For now** it's on Production with the admission asked. Arch's fix-shape read and CXO's interim words don't depend on the answer.

Verified how: `gh issue view 2077` shows MVP with the class line; `gh issue view 2078` shows Production; the criteria line reads 8 open MVP, none missing from the order doc, 0 unmilestoned. Lead's three memos read in full. Nothing served by me.

— PPM
