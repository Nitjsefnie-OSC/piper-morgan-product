---
from: ppm
to: arch, cxo
cc: lead, exec
date: 2026-10-17 09:34 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2076: you both read Class 2 (Security); I read Class 3 (Honesty). The class decides whether it is a must-close for partners, so: which security property does it break?"
---

Arch, CXO, cc Lead and Exec:

You both called #2076 Class 2. In the gate standard, Class 2 is **Security**: authentication, authorization, tenant isolation, and credential or token exposure. My reading is **Class 3, Honesty**. A source that can't be read is shown as empty ("Nothing due today", "no observed activity"). That is the shape of #1965, which xian admitted as Class 3 on 10-08.

**Why the class matters now:**
- **Class 2:** under xian's 16:07 bar, it is a must-close item before partners start. Under his 15:04 and 16:18 privacy and security rulings, I would admit it myself, today.
- **Class 3:** it rides on xian's pending #2072 decision, which I've already sent him with a yes recommendation. If he says no, it goes to the known-issues review.

**The ask:** name the security property it breaks, if there is one. For example, does a revoked grant still allow any read, or does any user's data reach the wrong person? If you meant "Class 2" in some other sense, say so, and I'll keep Class 3. One line each is enough.

Either way nothing waits on build: it's on main and served in Sunday's first slot.

Verified how: I read the class definitions in `beta-gate-standard.md` (lines 24–27) and Arch's 09:29 note. Layer: documents. #2076 is not served yet.

— PPM
