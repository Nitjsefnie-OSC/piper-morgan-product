---
from: Lead
to: HOST
cc: Exec, PA
date: 2026-10-19 13:05 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2081 D5 PASS by xian as mvp-tester (13:01): minted 2, revoked 1; masked forms for the roster: E8EJ…RYSG unused, 80K8…8VTX revoked. One UX gap (list needs a manual reload after mint/revoke), fixing now. Your word closes #2081"
---

HOST, cc Exec, PA:

**D5 on alpha `f9fb8b750b`, xian as `mvp-tester` (the only admin), 13:01–13:03 PT.** The Invites card showed on Settings; `/settings/invites` opened; he minted **2** ("Up to 20 at a time and 20 a day (2 minted today)"); the raw codes showed once on the mint response; the list shows them masked; he revoked one, and its row reads "Revoked 10/19/2026, 1:03:27 PM". Screenshot read by me: the page's words match the build (header "Codes are shown once, right after minting, and never again. This page sends nothing: handing a code to a tester is still your hand.").

**Roster lines:** `E8EJ…RYSG` **unused** (xian's bank, file `xian-invite-bank-credential-20261019.txt`); `80K8…8VTX` **revoked** 13:03 (the D5 check itself). Both minted 10-19 13:01 by his hand.

**The gap he found:** after a mint, and after a revoke, the list below does not refresh; a manual reload shows the new state. Function is right (the writes happened), the page is lazy. I am fixing it in a lane now (re-fetch the list after each write); it rides the second promotion today.

**Your call:** the page met your seven rulings in the code read (your 12:27 yesterday) and now in his hands. Your word closes #2081; I would close it on the function with the refresh fix noted as landed or in flight, your choice.

Verified how: his screenshot and words; the template's handlers read for the gap (`mintCodes` and `revokeInvite` do not call `loadInvites`). Layer: served page in his browser; source for the cause. Denominator: the one page, both writes.
