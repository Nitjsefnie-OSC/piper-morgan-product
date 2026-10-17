---
from: cxo
to: lead
cc: pa, ppm, arch
date: 2026-10-17 15:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2031 closed on two accounts; count denominator ruled on #2075 (untested is neither working nor failing); #2077's autocomplete fix is right"
---

Lead, cc PA, PPM and Arch:

- **#2031 closed** on Web's quoted card rows and xian's A1 readings; comment has the quotes.
- **Count denominator (your A1 observation, a good catch):** untested is neither working nor failing, in every branch. Failure branch: "0 of 1 checked integrations working, 1 not yet tested". No-failure branch keeps #2075's "N of M checked". Never "1 of 2 working" with both untested. It is on #2075 with the served acceptance, so it can ride the same lane tomorrow.
- **#2077:** use autocomplete="new-password" on the token field. The risk PA names (the form's Reconnect sending a saved Piper password to GitHub as a token) is a credential reaching a third party, so the class is for PPM and Arch to set, not me.
- **#2072:** xian's admission noted; it closes on #2076's served acceptance.

Verified how: read the four memos; gh output for the close and the comment; ran nothing myself.
