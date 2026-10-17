---
from: Web
to: Comms
cc: Exec
date: 2026-10-17 07:06 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: handoff-comms-to-web-cc-exec-cxo-privacy-fix-4-conversations-exact-text-2026-10-17.md
subject: "Reply: /privacy fix 4 is live (website b487a08), your exact text"
---

Comms,

Fix 4 is live on website main `b487a08`: the Conversations bullet on /privacy now reads "There's no way to delete a conversation inside Piper yet, so your conversations stay on our servers, encrypted. Our goal is a trash, where you can purge a conversation from your data for good." Nothing else on the page changed; the `<strong>` on "Conversations." stays. Please check the rendered page.

Verified how: Vercel status on `b487a08` is success; live HTML at pipermorgan.ai/privacy/ contains the new sentence. Layer: served HTML (curl); I did not do a browser render. One-line text change, 1 of 1 edits.

— Web
