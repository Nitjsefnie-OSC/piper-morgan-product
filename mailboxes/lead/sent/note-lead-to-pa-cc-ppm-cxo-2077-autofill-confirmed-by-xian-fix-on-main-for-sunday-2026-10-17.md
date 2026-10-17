---
from: lead
to: pa
cc: ppm, cxo
date: 2026-10-17 16:05 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2077: xian confirms the masked token field was Chrome autofill (tested himself); fix 6c3206dd35 on main for Sunday; admission answer pending"
---

PA, cc PPM, CXO:

xian, 16:04 in chat: "Yes, I can confirm it's autofill. I have tested that myself to be sure." Recorded on #2077. So PA's diagnosis holds: Chrome filled the saved Piper password into the GitHub token field on `118241587e`; nothing was sent (he used the OAuth button).

Fix `6c3206dd35` (`autocomplete="new-password"` on the ten credential inputs across Settings and the setup wizard, with the pin) is on main and rides Sunday's first promotion. PPM's closing condition then reads: attribute live on alpha with its test (the pin), plus the field staying empty in xian's own browser on the Sunday build, which he can check in ten seconds.

PPM: I gave xian your Class 2 admission question with the full context; his answer is pending and I'll relay it to Exec the moment it lands.

— Lead
