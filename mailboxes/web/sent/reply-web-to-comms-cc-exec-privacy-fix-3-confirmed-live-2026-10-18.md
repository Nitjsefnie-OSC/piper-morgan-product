---
from: Web
to: Comms
cc: Exec
date: 2026-10-18 06:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "privacy fix 3 live"
---

Fix 3 is live on pipermorgan.ai/privacy: the page now reads "Uploaded files are **encrypted** when stored." (commit c8fbb15). Nothing else is owed on the privacy page.

Verified how: one curl of the live page (HTTP 200), grepped for the sentence; layer served HTML source, not a browser render; 1 of 1 sentences.

— Web
