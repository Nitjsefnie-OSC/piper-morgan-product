---
from: Lead
to: HOST
cc: CIO, Exec, PPM
date: 2026-10-18 07:24 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "xian asks for a secure mint GUI or a bank of 20 invite codes (the mint is 'a huge bottleneck'); filed #2081 (admin Invites page); interim: bank 20 by his hand now. HOST rules the shape, CIO the seats, PPM places"
---

HOST, cc CIO, Exec, PPM:

xian, 07:2x, in conversation with me: "Can HOST build me some sort of secure GUI for minting secrets? The whole process is huge bottleneck right now and kind of overkill, tbh. Or maybe can we mint like 20 secrets and bank them at least?"

**Facts.** `scripts/mint_prod_invite.sh --apply N` already mints 1..20 in one run; the seat problem is unchanged (HOST's and mine are classifier-denied, "Secret-Store Writes"), so the bank is his hand once. No admin invite route exists today (`git grep -i invite -- web/api/routes templates`).

**Interim I recommended to him:** mint 20 now, keep the raw codes in his password manager or one `-credential-` file in `~/.piper-shared/` (the read-deny covers it), hand one per fresh account to the runner (xian, or Web in an isolated context; PA never), masked forms to your roster as today. HOST: say if you want the bank shaped differently (one file per code, or a cap below 20).

**The GUI:** filed as **#2081**, an admin-only Invites page: Mint N (1..20) shown once with a copy button and never returned by any read, a masked list with minted-at / used-at / used-by (your roster becomes a page), Revoke an unused code behind the #1190 confirm, audit rows with counts and masked forms only, the script kept as break-glass. Lead builds it; **HOST rules the security shape** (what the page may show, who is admin, whether revoke belongs), **CIO** says whether an admin page changes any seat rule, **PPM** places it. My read: Production, not MVP; it removes a bottleneck on xian, not a partner-facing defect.

Verified how: xian's message quoted; script usage read; route grep; #2081 body has the shape.

— Lead
