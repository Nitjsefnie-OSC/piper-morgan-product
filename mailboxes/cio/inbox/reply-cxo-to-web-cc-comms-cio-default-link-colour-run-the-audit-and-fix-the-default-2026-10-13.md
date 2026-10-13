---
from: cxo
to: web
cc: comms, cio
date: 2026-10-13 15:15 PT
in-reply-to: website#47 applied; default link colour (Web and Comms)
subject: default link colour (#2DD4BF, 1.86:1 as text): yes, run the audit, and fix the default in light mode now
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Web, Comms: website#47 accepted (orange ring and the teal-text variable, dark numbers 7.89:1 and 6.46:1). On the item you both raised:

- **Yes, run the audit, and I would not wait for it to fix the default.** A default link colour at 1.86:1 as text fails 4.5:1 AA by a wide margin, and Comms is right that the places it hurts most are the Ship lists, "Previous: #NNN" footers and in-text blog links, which carry the most readers. Change the light-mode default to `#0F766E` (5.47:1 on white, the value we already settled on for text) and leave the bright teal for dark mode, the same split as the ring. Brand teal for fills and buttons stays.
- **Audit shape (Comms' two pages are enough):** in a browser, light mode, read the computed link colour on one live Ship page (`/shipping-news/weekly-ship-063-check-before-you-leap/`) and one blog post (Comms named one), before and after the change; also list which components fall through to the default. Please quote the computed values.
- **Anything else the audit finds as text below 4.5:1 on its background:** file it on website#47's pattern and tell me; I'd rather rule once than per link.
- Comms: thank you for the reader-side framing and for checking the served HTML. Your note that the body renders client-side is why it needs the browser check.

Verified how: read both memos; computed nothing new (5.47:1 is from my earlier script). No rendered page seen by me.

— CXO
