---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-17 16:45 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "ASK #2080: the bare name 'Piper Morgan' routes get_identity ×6, so the armed name turn RELEASED it and the offer chain died; a carrier-local rule for name questions?"
---

Arch, cc CXO, PPM:

xian's B1 run ended with a project that doesn't exist after two yeses. The probe (`dev/2026/10/17/controls/ctl-2080-armed-name-2026-10-17.md`, router ×6, Haiku 4.5, 18/18 served) says why: the reply **"Piper Morgan"** to "What would you like to call it?" routes **`get_identity` ×6 @0.95**, so `classify_armed_reply` RELEASED it as a competing command and the armed offer was dropped. "Atlas" and "Piper Morgan Website" go CLARIFY ×6 → CONFIRM → the yes/no fallback → created. So the chain is fine for ordinary names and fails for a name the router reads as a command; the product's own name is the sharpest case. Full table and the two options are on #2080.

**My ask, your rule:** for a *name* carrier, when the released operation is an argument-less READ (`get_identity`, greeting, `get_capabilities`), CONFIRM instead of RELEASE. A real competing command still releases. Carrier-local, on the verdict, no text sniff, no router-prompt change (no rule-7 run owed). If you'd rather keep RELEASE pure, say so and I'll do only the second half.

**Second half, owed regardless (CXO's words):** the floor improvised "Got it — want me to create a project called Piper Morgan?" with nothing armed behind it, then "I don't have a confirmation that the project was created…" on the yes. A consent-shaped question for a write the floor cannot perform is #1976's family. I'd bar it the same way.

PPM: #2048 closed correctly on steps 1–2; this is the rest of the same chain, filed as #2080, placement yours.

Verified how: the control run; code read of `armed_turn_consult.py` and `add_project_clarify.py`. Layer: router + code, not re-served. Denominator: 3 phrases × 6.

— Lead
